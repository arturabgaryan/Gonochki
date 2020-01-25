import faceControl
import threading


nowFace = None
dict = {"state": None}
datfilename = 'new.dat'

known_face_encodings, known_face_metadata = faceControl.load_known_faces(
    datfilename)
if known_face_encodings == None or known_face_metadata == None:
    raise Exception("Faces data not found")

threading.Thread(target=faceControl.mainloop(known_face_encodings, known_face_metadata, dict)).start()

while True:
    sleep(1)
    print(dict)
