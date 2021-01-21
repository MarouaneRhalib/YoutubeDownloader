from pafy import new
url = input('Enter the url : ')
video = new(url)
print(video.title)

bestQuality = video.getbest()
bestQuality.download()

# download audio
# audio = video.audiostreams
# audio[0].download()

# chose quality
# stream = video.streams
# for i in stream:
#     print(i)
# stream[1].download()

