import ffmpeg
from io import BytesIO
import tempfile
import os

def convert_to_mp4(video_bytes):
    # Create temporary files for input and output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as input_temp_file:
        input_temp_file.write(video_bytes)
        input_temp_file_name = input_temp_file.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as output_temp_file:
        output_temp_file_name = output_temp_file.name

# Convert the video using FFmpeg
    input_stream = ffmpeg.input(input_temp_file_name)
    output_stream = ffmpeg.output(input_stream, output_temp_file_name, format='mp4', vcodec='libx264', acodec='aac')
    ffmpeg.run(output_stream, overwrite_output=True)

# Read the converted video from the output temporary file
    with open(output_temp_file_name, "rb") as output_temp_file:
        converted_video_bytes = output_temp_file.read()

# You can now use 'converted_video_bytes' for further processing or upload it to S3

# Clean up temporary files
    os.remove(input_temp_file_name)
    os.remove(output_temp_file_name)
    print("Converted video")
    return converted_video_bytes


