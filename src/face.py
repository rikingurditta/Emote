import cognitive_face as CF
from api_keys import *
import mss
import time
from typing import List, Dict, Tuple

CF.Key.set(API_KEY1)
BASE_URL = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)


def dict_sorted_list(input_dict: Dict[str, float]) -> List[Tuple[str, float]]:
    """Convert a dict to a sorted list of tuples of key-value pairs.
    The dict's values must be numerical.
    turn key-value pair into a list of tuples (like a list), then sort the list
    >>> d = {'a': 3, 'b': 1, 'c': 2.6}
    >>> dict_sorted_list(d)
    [('a', 3), ('c', 2.6), ('b', 1)]
    """

    output_list = []  # variable for output
    for key in input_dict:  # for going through every value
        output_list.append((key, input_dict[key]))
        # every time you find a key, add a tuple which is key and value
    output_list.sort(key=(lambda x: x[1]),
                     reverse=True)  # calls a special sort function
    return output_list


def filter_zero_emotions(emotions: List[Tuple[str, float]]) -> None: #filters zero emotion
    """Return emotions from list whose values are >0.
    (filters zero emotion)
    """

    output = []
    for pair in emotions:  # goes through every pair of emotions and values
        # in list
        if pair[1] > 0:  # remember pair[1] is the value, pair [0] would be the
            # name of emotion
            output.append(pair)  # add the emotion and value to the output
            # list if value is greater than 0
    return output


def start_screen_watch_loop() -> None:  # screenshot loop to scan images
    while True:  # repeat infinitely because true will be true
        screenshot()
        time.sleep(3)  # screenshots every 3 seconds


def screenshot() -> List[Tuple[str, float]]:
    file_name = 'temp.png'  # name of file we are outputting to
    # takes a screenshot, and then outputs to temp.png
    mss.mss().shot(output=file_name)

    # call the API and get the emotional attribute
    cur_face = CF.face.detect(f'./{file_name}', attributes=['emotion'])

    if len(cur_face) > 0:  # checks if there is a face, len = # of faces
        emotions_dict = cur_face[0]['faceAttributes']['emotion']
        output = filter_zero_emotions(dict_sorted_list(emotions_dict))
        # filters out emotions that are zero
        # noinspection PyTypeChecker
        return output
    else:
        return cur_face


def top_3_emotions(emotions_list: List[Tuple[str, int]]) -> List[str]:
    return ([e[0] for e in emotions_list] + ['', '', ''])[:3]


if __name__ == '__main__':
    start_screen_watch_loop()  # starts the program
