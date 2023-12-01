import pytube
from pytube import YouTube
from pathlib import Path


desktop_dir_win_from_wsl = Path("/mnt/c/Users/chris/Desktop")

def get_target():
    """get url of video to download from user terminal input"""
    video_url = input("Enter URL you want to download: ")

    return video_url


def get_streams_available(video_url):
    video = YouTube(video_url)
    video_streams = video.streams
    for item in video_streams:
        print(item)

    return video_streams


def get_itag_of_video():
    """user reads itag of the video format they want, and enters it as user input from terminal"""
    print("\nReview list above and pick the itag of the video you want (resolution,  codec, etc")
    itag_num = input("Enter itag number as an integer: ")

    return itag_num


def download_video(video_url, itag):
    """download the video to current directory"""
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    print(f"downloading video with itag {itag}")
    try:
        video.download(desktop_dir_win_from_wsl)   # path to save video to; currently same directory
    except Exception:
        print(Exception)

    return True


if __name__ == "__main__":

    print("Desktop is seen as directory: ", Path.is_dir(desktop_dir_win_from_wsl))

    url = get_target()

    get_streams_available(url)

    itag = get_itag_of_video()

    download_video(url, itag)
