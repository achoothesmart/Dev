# Importing the module
from moviepy.editor import *

# uploading the video we want to edit
video_file_path = 'Z:/TempFiles/VID_20230804_124743374.mp4'
video = VideoFileClip(video_file_path)


# getting width and height of video 1
width_of_video1 = video.w
height_of_video1 = video.h

print("Width and Height of original video : ", end = " ")
print(str(width_of_video1) + " x ", str(height_of_video1))

print("#################################")

# resizing....
video_resized = video.resize(0.7)

# getting width and height of video 2 which is resized
width_of_video2 = video_resized.w
height_of_video2 = video_resized.h

print("Width and Height of resized video : ", end = " ")
print(str(width_of_video2) + " x ", str(width_of_video2))

print("###################################")


# displaying final clip
# video_resized.ipython_display()
out_file = video_file_path.replace('.', '_compresed.')
video_resized.write_videofile(filename=out_file)


