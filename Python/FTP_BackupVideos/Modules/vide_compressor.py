# Importing the module
from moviepy.editor import VideoFileClip
import os

class VideoCompressor:

    def __init__(self) -> None:
        pass

    def debugInfo(self, VideoFilePath: str):
        clip = VideoFileClip(VideoFilePath)
        print(f'Height: {clip.h}, Width: {clip.w}')
        with open('video_file_sizes_log.csv', 'a') as f:
            f.write(f'{VideoFilePath},{clip.h},{clip.w}\n')

    def CompressVideo(self, InFilePath: str, OutFilePath: str, CompressionPercentage: float = 50.0):
        # Sample VideoFilePath = 'Z:/TempFiles/VID_20230804_124743374.mp4'
        clip = VideoFileClip(InFilePath)
        resize_value = CompressionPercentage / 100
        video_resized = clip.resize(resize_value)
        out_file_path = OutFilePath.replace('.', f'_comp_{CompressionPercentage}.')
        out_file_name = os.path.basename(out_file_path)
        temp_out_file_path = os.path.join(os.path.dirname(out_file_path), f'~{out_file_name}')
        video_resized.write_videofile(filename=temp_out_file_path)
        os.rename(temp_out_file_path, out_file_path)
        print(f' ** Video Compressed and saved to {out_file_path} **')

        # # getting width and height of video 1
        # width_of_video1 = video.w
        # height_of_video1 = video.h

        # print("Width and Height of original video : ", end = " ")
        # print(str(width_of_video1) + " x ", str(height_of_video1))

        # print("#################################")

        # # resizing....

        # # getting width and height of video 2 which is resized
        # width_of_video2 = video_resized.w
        # height_of_video2 = video_resized.h

        # print("Width and Height of resized video : ", end = " ")
        # print(str(width_of_video2) + " x ", str(width_of_video2))

        # print("###################################")


        # displaying final clip
        # video_resized.ipython_display()
        

    def CompressVideosFromFolder(self, SourceFolderPath: str, DestinationFolderPath: str,
                                 CompressionPercentage: float = 50.0, FilterInExtensions: list = ['mp4']):
        video_files = [file for file in os.listdir(SourceFolderPath) if file.split('.')[1].lower() in 
                       [ext.lower() for ext in FilterInExtensions]]
        if len(video_files) > 0:
            print(f'Compression started | Source Folder: "{SourceFolderPath}" | Destination Folder: "{DestinationFolderPath}"')
            for idx, video_file in enumerate(video_files):
                print(f'Processing {idx+1}/{len(video_files)} | {video_file}')
                # self.CompressVideo(
                #     InFilePath=os.path.join(SourceFolderPath, video_file), 
                #     OutFilePath=os.path.join(DestinationFolderPath, video_file),
                #     CompressionPercentage=CompressionPercentage)

                self.debugInfo(VideoFilePath=os.path.join(SourceFolderPath, video_file))
        else:
            print(f' !! No video files to compress in "{SourceFolderPath}" path !!')
        print(' $$ All Done $$ ')
        

