import cognitive_face as CF
from api_keys import *
import os.path
import mss
import time


CF.Key.set(API_KEY1)

BASE_URL = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

# example image
# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
# faces = CF.face.detect(img_url, attributes=['emotion'])
# print(f'not wasif: {faces}')
# print()
# print()

# The simplest use, save a screen shot of the 1st monitor


def on_exists(file_path: str) -> None:
    """What to do when the image file exists.
    """

    if os.path.isfile(file_path):
        cur_face = CF.face.detect(f'./{file_path}', attributes=['emotion'])
        print(file_path)
        print(f'lily: {cur_face}')


def graphics_show(face_data) -> None:
    print(face_data)


while True:
    with mss.mss() as sct:
        file_name = 'temp.png'
        out_file = sct.shot(output=file_name)
        cur_face = CF.face.detect(f'./{file_name}', attributes=['emotion'])
        if len(cur_face) > 0:
            graphics_show(cur_face[0]['faceAttributes']['emotion'])
        else:
            print('nothing')
    time.sleep(3)
