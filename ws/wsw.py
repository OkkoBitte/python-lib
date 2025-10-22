# WEB SNIFF WORM 1.0 [MBG]

import requests as     net
import re as           t_parse
import html.parser as  ht_parse
from .nwf import       nwf
import sys as          system
from .ww import        main
def vanih(CELEM,VAH):
    if CELEM == "TEXT":
        main(VAH,want=['link'],pathss=['/dev/null','/dev/null','links.html'])
    elif CELEM == "IMG":
        main(VAH,want=['photo'],pathss=['photo.html','/dev/null','/dev/null'])
    elif CELEM == "VIDEO":
        main(VAH,want=['video'],pathss=['/dev/null','video.html','/dev/null'])
    else:
        main(VAH,ss='1',want=['photo','video','link'])
        
    

