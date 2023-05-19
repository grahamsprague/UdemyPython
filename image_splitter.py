import os
from PIL import Image

# Get the path to the image folder
image_folder = "./image_splitter/in"

# Create a new folder to store the quadrant images
quadrant_images_folder = "./image_splitter/out"
if not os.path.exists(quadrant_images_folder):
    os.mkdir(quadrant_images_folder)

# Iterate over the images in the image folder
for image_name in os.listdir(image_folder):
    
    # ignore invisible files
    if not image_name.startswith('.'):

        # Get the path to the image
        image_path = os.path.join(image_folder, image_name)

        # Open the image
        image = Image.open(image_path)

        # Get the width and height of the image
        width, height = image.size

        # Calculate the size of each quadrant
        quadrant_width = width // 2
        quadrant_height = height // 2

        # Iterate over the quadrants
        for i in range(0, 4):
            # Get the top-left corner of the quadrant
            if i == 0:
                left = (0)
                top = (0)
                bottom = top + quadrant_height
                right = left + quadrant_width

            if i == 1:
                left = (quadrant_width)
                top = (0)
                bottom = top + quadrant_height
                right = left + quadrant_width
            
            if i == 2:
                left = (0)
                top = (quadrant_height)
                bottom = top + quadrant_height
                right = quadrant_width

            if i == 3:
                left = (quadrant_width)
                top = (quadrant_height)
                bottom = top + quadrant_height
                right = left + quadrant_width

    

            # Crop the image to the quadrant
            print('CURRENT: ' + str(i) )
            
            

            mytuple = (left, top, right, bottom)

            quadrant = image.crop(mytuple)

            # Save the quadrant to a file
            quadrant.save(os.path.join(quadrant_images_folder, "quadrant_" + str(i) + "_" + image_name + ".png"))

print("Done!")