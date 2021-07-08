import os
import pytube


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


def download_vid_from_youtube(video_url, video_output_path, show_statistics=False):
    # TODO: Add test for file/folder existence
    if show_statistics:
        print_video_stats(video_url)
    video = pytube.YouTube(video_url)
    vid_best_stream = video.streams.get_highest_resolution()
    # TODO: Add option to choose which stream to download
    vid_best_stream.download(video_output_path)
    print(f"Saved {video.title} to {video_output_path} directory")
    # TODO: pring downloaded video stats (size, fps, format, etc.)