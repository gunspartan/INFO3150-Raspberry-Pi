# https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
import face_recognition
import cv2
import numpy as np

from DBController import DBController
from Person import Person
from EmailController import EmailController
from GPIOController import GPIOController


gpio = GPIOController()
# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Get users from database
people = []
database = DBController()
users = database.getAllUsers()
for row in users:
    person = Person(row[1], row[2], row[3])
    people.append(person)

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

for person in people:
    image = face_recognition.load_image_file(person.getImage())
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(person.getName())

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
known_face = False
name = "Unknown"

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                known_face = True

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('p'):
        if known_face:
            if name in known_face_names:
                if person.getBlacklisted():
                    print("Blacklisted")
                    gpio.denyEntryLED()
                    break
                else:
                    print("Not Blacklisted")
                    gpio.allowEntryLED()
                    break
        else:
            print("Unrecognized Face Detected")
            if gpio.allowBtn.is_pressed:
                print("Allowing Entry")
                gpio.allowEntryLED()
                name = input()
                image = cv2.imwrite("img/" + name + ".jpg", frame)
                newUser = Person(name, image, False)
                newUser.addToDB()
                break
            if gpio.denyBtn.is_pressed:
                print("Denying Entry")
                gpio.denyEntryLED()
                # Email admin that an unknown face was detected
                email = EmailController()
                email.sendEmail("Unknown Face Detected", "An unknown face was detected at the door")
                email.close()
                break
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        database.close()
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()