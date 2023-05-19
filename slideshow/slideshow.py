'''
MoviePy
https://zulko.github.io/moviepy/index.html

Create a sub-folder relative to this script named:
/slideshow_stills

Update the name value (line 23) before running

TODO have this script accept an argument, so you can name the video when running

'''


from moviepy.editor import *
from os import listdir

img_clips = []
path_list = []


# Use this for the name portion of the filename
name = "hand_bug"


# accessing path of each image
for image in os.listdir('slideshow_stills/'):
    if image.endswith(".png"):
        path_list.append(os.path.join('slideshow_stills/', image))

# creating slide for each image
for img_path in path_list:
    slide = ImageClip(img_path, duration=.25)
    img_clips.append(slide)

# concatenating slides
video_slides = concatenate_videoclips(img_clips, method='compose')

# export as final video
video_slides.write_videofile(name + ".mp4", fps=4)

# export as animated .gif
video_slides.write_gif(name + ".gif", fps=4, program='ffmpeg')
