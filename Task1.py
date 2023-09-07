from pytube import YouTube
link = input('link to video\n')
video = YouTube(link)
quality = int(input('High(1)/Low(2)\n'))
if quality == 1:
    out = video.streams.get_highest_resolution()
elif quality == 2:
    out = video.streams.get_lowest_resolution()
out.download()