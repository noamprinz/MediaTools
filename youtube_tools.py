import yt_dlp
import os


def download_from_youtube(video_url, output_path, format_type='mp4'):
    """
    Download content from YouTube as either MP4 video or MP3 audio.

    Args:
        video_url (str): URL of the YouTube video
        output_path (str): Directory path where the file will be saved
        format_type (str): Either 'mp4' or 'mp3' (default: 'mp4')
    """
    if format_type not in ['mp4', 'mp3']:
        raise ValueError("format_type must be either 'mp4' or 'mp3'")

    # Configure options based on format type
    if format_type == 'mp4':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
    else:  # mp3
        ydl_opts = {
            'format': 'bestaudio/best',
            'extract_audio': True,
            'audio_format': 'mp3',
            'audio_quality': 0,  # 0 is the best quality
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"{'Video' if format_type == 'mp4' else 'Audio'} downloaded successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    output_path = r"C:\Users\Noam Prinz\Desktop\songs"

    paths = ['https://www.youtube.com/watch?v=1_mBUXFNrCc',
             'https://www.youtube.com/watch?v=p1Nhx-Dn3yw',
             'https://www.youtube.com/watch?v=0xSmcYGHMHE',
             'https://www.youtube.com/watch?v=WXLPWP3bduU',
             'https://www.youtube.com/watch?v=YCp2bQ_KOgg',
             'https://www.youtube.com/watch?v=sN3hDWjiGb0',
             'https://www.youtube.com/watch?v=I_lDQkxe5xw',
             'https://www.youtube.com/watch?v=jSvbsndk4Jk',
             'https://www.youtube.com/watch?v=ujap-AZz860',
             'https://www.youtube.com/watch?v=Rf2dlAbWOew',
             'https://www.youtube.com/watch?v=f3tiN2ZVTAA',
             'https://www.youtube.com/watch?v=zMJ1qZqWS_8',
             'https://www.youtube.com/watch?v=YevXvvoZ7oI',
             'https://www.youtube.com/watch?v=upLuP1SCvJA',
             'https://www.youtube.com/watch?v=0ktmt8bZ_ek',
             'https://www.youtube.com/watch?v=-0QZMHsDxtY']
    for path in paths:
        download_from_youtube(path, output_path, format_type='mp3')