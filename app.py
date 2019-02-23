import urllib.request
from sys import argv
import random

_link = argv[1]

def extract_video_id(string):

    # print(string[0:4])
    
    if string[0:4] == 'http':
        return string[32:]

    elif string[0:4] == 'watc':
        return string[8:]


urllib.request.urlretrieve("http://img.youtube.com/vi/" + extract_video_id(_link) + "/maxresdefault.jpg", str(random.randint(0,10000)) + ".jpg")