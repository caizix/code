import asyncio
import time
@asyncio.coroutine
def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("now playing movie named {}".format(i))
            yield time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("now playing music named {}".format(i))
            yield  time.sleep(2)
        else:
            print("No SUPPORTED")



movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]



loop = asyncio.get_event_loop()
task = [play(movie_list),play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()
