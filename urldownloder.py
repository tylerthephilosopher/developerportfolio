from pytube import YouTube

video = YouTube("https://youtu.be/NkK0krAQKRo")
save_video = video.streams.get_lowest_resolution()
save_video.download()