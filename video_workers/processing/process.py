import ffmpeg
from io import BytesIO
import tempfile
import os

def process_mp4(video_bytes, chunk_duration):
    # Create temporary files for input and output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as input_temp_file:
        input_temp_file.write(video_bytes)
        input_temp_file_name = input_temp_file.name

    with tempfile.TemporaryDirectory(delete=False) as output_temp_folder:
        output_temp_folder_name = output_temp_folder.name

    # Calculate the number of chunks needed
    output_files = []
    output_prefix = "chunk"
    output_template = os.path.join(output_temp_folder_name, f"{output_prefix}%03d.ts")

    try:
        ffmpeg.input(input_temp_file_name).output(output_template, format="hls", hls_time=chunk_duration).run()
    except ffmpeg.Error as e:
        print("Error creating HLS chunks:", e)
        return []

    # Generate the HLS playlist file
    playlist_name = os.path.join(output_temp_folder_name, "playlist.m3u8")
    with open(playlist_name, "w") as playlist_file:
        playlist_file.write("#EXTM3U\n")
        playlist_file.write(f"#EXT-X-TARGETDURATION:{chunk_duration}\n")
        playlist_file.write(f"#EXT-X-VERSION:3\n")
        playlist_file.write("#EXT-X-MEDIA-SEQUENCE:0\n")

        for filename in sorted(os.listdir(output_folder)):
            if filename.startswith(output_prefix) and filename.endswith(".ts"):
                chunk_path = os.path.join(output_folder, filename)
                playlist_file.write(f"#EXTINF:{chunk_duration},\n")
                playlist_file.write(f"{filename}\n")
                output_files.append(chunk_path)

    print("Video has been split into HLS format chunks.")
    return output_files, output_temp_folder_name


