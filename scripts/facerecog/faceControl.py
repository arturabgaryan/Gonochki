import cv2
import numpy as np
import pickle
import face_recognition
from time import sleep


def load_known_faces(filename):
    global known_face_encodings, known_face_metadata

    try:
        with open(filename, "rb") as face_data_file:
            known_face_encodings, known_face_metadata = pickle.load(
                face_data_file)
            return known_face_encodings, known_face_metadata
            print("Known faces loaded from disk.")
    except FileNotFoundError as e:
        print("No previous face data found - starting with a blank known face list.")
        return None, None


def lookup_known_face(face_encoding, known_face_encodings, known_face_metadata):
    """
    See if this is a face we already have in our face list
    """
    metadata = None

    if len(known_face_encodings) == 0:
        return metadata

    face_distances = face_recognition.face_distance(
        known_face_encodings, face_encoding)

    # Get the known face that had the lowest distance (i.e. most similar) from the unknown face.
    best_match_index = np.argmin(face_distances)

    if face_distances[best_match_index] < 0.65:
        # If we have a match, look up the metadata we've saved for it (like the first time we saw it, etc)
        metadata = known_face_metadata[best_match_index]

    return metadata


def mainloop(known_face_encodings, known_face_metadata, d):
    video_capture = cv2.VideoCapture(0)

    while True:
        # print(_image)
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the face locations and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # print(face_locations)
        if len(face_locations) > 0:
            face_encoding = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            # print(face_encoding)
            metadata = lookup_known_face(
                face_encoding, np.array(known_face_encodings), known_face_metadata)

            if metadata != None:
                d["state"] = metadata['name']
                print(metadata['name'])
            else:
                d["state"] = None
                print('There is no known face')

        else:
            d["state"] = None
            print('There is no face')
        open_cv_image = frame[:, :, ::-1]
        cv2.imshow('Video', open_cv_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            save_known_faces()
            break
        sleep(1)
