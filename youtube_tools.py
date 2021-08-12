import os
import pytube

from noam_utils import general_functions as gf


def print_video_stats(video_url, show_description=False):
    video = pytube.YouTube(video_url)
    vid_title = video.title
    vid_length = video.length
    vid_author = video.author
    vid_publish_date = video.publish_date
    num_views = video.views
    vid_description = video.description
    print(f"\n*** Video Statistics ***\n\n"
          f"Video Title: {vid_title}\n"
          f"Video Author: {vid_author}\n"
          f"Video Length: {int(vid_length / 60)}:{vid_length % 60}\n"
          f"Video Publish Date: {vid_publish_date}\n"
          f"Number of Views: {num_views}\n")
    if show_description:
        print(f"\nVideo Description:\n{vid_description}")


def download_video_from_youtube(video_url, output_dir, save_only_audio=False, show_statistics=False):
    # TODO: Add option to choose which stream to download
    # TODO: Enable more extension control
    if show_statistics:
        print_video_stats(video_url)
    video = pytube.YouTube(video_url)
    # getting relevant stream and converting file to mp3 for audio files
    if save_only_audio:
        stream = video.streams.get_audio_only()
        filename = f"{gf.get_filename(stream.default_filename, with_extension=False)}.mp3"
    else:
        stream = video.streams.get_highest_resolution()
        filename = stream.default_filename
    # downloading stream
    if os.path.isfile(os.path.join(output_dir, filename)):
        print(f"\nThe file ''{filename}'' already exists in {output_dir} directory!")
        return
    print(f"\nDownloading file ''{filename}'' to {output_dir} directory")
    stream.download(output_path=output_dir, filename=filename)
    print("\nDone")
    # TODO: print downloaded video stats (size, fps, format, etc.)