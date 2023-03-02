import sys
import os
from PIL import Image


# grab args
inbox = sys.argv[1]
outbox = sys.argv[2]

print(inbox)
print(outbox)



# check if folder exists
if not os.path.isdir(outbox):
    os.makedirs(outbox)


#get contents of inbox
image_list = os.listdir(inbox)

#loop images
for file in image_list:

    print('processing file :' + file)
    file_split = split_tup = os.path.splitext(file)
    file_name = file_split[0]
    file_extension = file_split[1]

    img = Image.open('./'+inbox+'/' + file) 
    img.save( './' + outbox + '/' + file_name + '.png', 'png' )



#convert to png

# save to folder