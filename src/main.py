import cognitive_face as CF
from api_keys import *
import mss
import time
from typing import List, Dict, Tuple


CF.Key.set(API_KEY1)
BASE_URL = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)


def graphics_show(face_data) -> None:
    print(face_data)


def dict_sorted_list(input_dict: Dict[str, float]) -> List[Tuple[str, float]]:
    """Convert a dict to a sorted list of tuples of key-value pairs.
    The dict's values must be numerical.

    >>> d = {'a': 3, 'b': 1, 'c': 2.6}
    >>> dict_sorted_list(d)
    [('a', 3), ('c', 2.6), ('b', 1)]
    """

    output_list = []
    for k in input_dict:
        output_list.append((k, input_dict[k]))
    output_list.sort(key=(lambda x: x[1]), reverse=True)
    return output_list


def filter_zero_emotions(emotions: List[Tuple[str, float]]) -> None:
    """Return emotions from list whose values are >0.
    """

    output = []
    for pair in emotions:
        if pair[1] > 0:
            output.append(pair)
        else:
            break
    return output


def start_screen_watch_loop() -> None:
    while True:
        with mss.mss() as sct:
            file_name = 'temp.png'
            sct.shot(output=file_name)
            cur_face = CF.face.detect(f'./{file_name}', attributes=['emotion'])
            if len(cur_face) > 0:
                emotions_dict = cur_face[0]['faceAttributes']['emotion']
                graphics_show(filter_zero_emotions(dict_sorted_list(emotions_dict)))
            else:
                print('nothing')
        time.sleep(3)


if __name__ == '__main__':
    start_screen_watch_loop()
