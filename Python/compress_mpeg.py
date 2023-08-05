import os
from moviepy.editor import VideoFileClip
from PIL import Image

video_file_path = 'Z:/TempFiles/VID_20230804_124743374.mp4'
if os.path.exists(video_file_path):
    print('File found')
else:
    print('File not found!!')


def compress_video(input_file, output_file, target_resolution_percent=50, bitrate='3000k'):
    """
    Compress the video using custom resampling.

    :param input_file: Path to the input video file.
    :param output_file: Path to the output compressed video file.
    :param target_resolution_percent: Percentage of the original video resolution (int), optional. Default is 50%.
    :param bitrate: Target bitrate for the video, optional. Default is '3000k'.
    """
    video_clip = VideoFileClip(input_file)

    original_width, original_height = video_clip.size
    target_width = int(original_width * target_resolution_percent / 100)
    target_height = int(original_height * target_resolution_percent / 100)

    # Create a list to store resized frames
    resized_frames = []
    for frame in video_clip.iter_frames(fps=video_clip.fps):
        # Convert frame to Pillow Image
        image = Image.fromarray(frame)
        # Resize frame using LANCZOS resampling
        resized_frame = image.resize((target_width, target_height), resample=Image.LANCZOS)
        # Convert the resized frame back to numpy array
        resized_frame_np = np.array(resized_frame)
        resized_frames.append(resized_frame_np)

    # Create a new video clip from resized frames
    resized_clip = ImageSequenceClip(resized_frames, fps=video_clip.fps)
    resized_clip.write_videofile(output_file, bitrate=bitrate)

# Example usage
input_video = video_file_path
compression_percentage = 30
output_video = f'{video_file_path}_compressed2{compression_percentage}'
compress_video(input_video, output_video, 
               target_resolution_percent=compression_percentage, 
               bitrate='1000k')
