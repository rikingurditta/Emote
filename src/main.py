import cognitive_face as CF
from api_keys import *

CF.Key.set(API_KEY1)

BASE_URL = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

# example image
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url, attributes=['emotion'])
print(faces)
