from sys import argv
from os import system, listdir, getcwd, path
import cv2
import face_recognition
import numpy as np
import pickle

known_face_encodings = []
known_face_metadata = []


def splitvideo(dir_name, video_name):
    cmd = 'mkdir -p {}'.format(dir_name)
    print(cmd)
    if system(cmd) != 0:
        raise Exception("Error creating directory")
    cmd = 'ffmpeg -i "{}" -r "{}" -f image2 {}/images%05d.png'.format(
        video_name, '25', dir_name)
    print(cmd)
    if system(cmd) != 0:
        raise Exception("Error splitting video")


def save_known_faces(dataname):
    with open(dataname, "wb") as face_data_file:
        face_data = [known_face_encodings, known_face_metadata]
        pickle.dump(face_data, face_data_file)
        print("Known faces backed up to disk.")


def load_known_faces(dataname):
    global known_face_encodings, known_face_metadata

    try:
        with open(dataname, "rb") as face_data_file:
            known_face_encodings, known_face_metadata = pickle.load(
                face_data_file)
            print("Known faces loaded from disk.")
    except FileNotFoundError as e:
        print("No previous face data found - starting with a blank known face list.")
        pass


def register_new_face(face_encoding, face_image, name):
    """
    Add a new person to our list of known faces
    """
    # Add the face encoding to the list of known faces
    known_face_encodings.append(face_encoding)
    # Add a matching dictionary entry to our metadata list.
    # We can use this to keep track of how many times a person has visited, when we last saw them, etc.
    known_face_metadata.append({
        "name": name
    })


def rec_faces(dir_name):
    face_encodingL = []
    face_imageL = []
    s = None
    for i, file in enumerate(listdir(getcwd() + '/' + dir_name)):
        photo = getcwd() + '/' + dir_name + '/' + file

        frame = cv2.imread(photo, cv2.IMREAD_UNCHANGED)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_labels = []
        for face_location, face_encoding in zip(face_locations, face_encodings):
            face_encodingL.append(face_encoding)
            top, right, bottom, left = face_location
            face_image = small_frame[top:bottom, left:right]
            face_image = cv2.resize(face_image, (150, 150))
            face_imageL.append(face_image)

        status = int((i/len(listdir(getcwd() + '/' + dir_name)))*100)
        if status % 5 == 0 and s != status:
            s = status
            print(status)

        # print(face_encodings)

    face_encoding = np.mean(face_encodingL, axis=0)
    # print(face_imageL)
    return face_encoding, face_encodingL, face_imageL



if __name__ == "__main__":
    dir_name = 'videoframes'
    dataname = 'new.dat'
    video_name = argv[1]
    name = argv[2]
    splitvideo(dir_name, video_name)
    face_encoding, face_encodings, face_imageL = rec_faces(dir_name)
    load_known_faces(dataname)
    face_distances = face_recognition.face_distance(face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    register_new_face(face_encoding, face_imageL[best_match_index], name)
    save_known_faces(dataname)
    print('ок')
    
