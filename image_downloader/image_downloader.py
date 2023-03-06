'''
Takes a list of return sep snumbers in a text file(argv1) 
and downloads them to the output folder (argv2)

called lie this...
python3 image_downloader.py snumbers.txt outfolder
'''

import sys
import os
import requests

SNUMBER_FILE = sys.argv[1]
OUT_FOLDER   = sys.argv[2]

REQUEST_TIMEOUT = 300

# check to see if the out_folder is present
if not os.path.isdir('./' + OUT_FOLDER):
    os.makedirs('./' + OUT_FOLDER)

lines = []

with open(SNUMBER_FILE, 'r', encoding="utf-8") as f:
    lines = f.readlines()

print('Starting...')

# print(lines)

for snumber in lines:

    snumber_clean = snumber.strip()

    my_url = 'https://www.staples-3p.com/s7/is/image/Staples/' \
             + snumber_clean + \
             '?wid=2000&hei=2000'

    try:
        img_data = requests.get(my_url, timeout=REQUEST_TIMEOUT).content
        with open('./' + OUT_FOLDER + '/' + snumber_clean + '.jpg', 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print('Error downloading:' + snumber_clean + ' Error: ' + e )
    else:
        print('Downloaded: ' + snumber_clean + '.jpg' )

print('Done!')
