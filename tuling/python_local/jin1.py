import _thread as thread
import time

movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("你现在收看的是：{}".format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("你现在收听的是：{}".format(i))
            time.sleep(2)
        else:
            print("没有能能播放的格式")


def thread_run():
    thread.start_new_thread(play, (movie_list,))
    thread.start_new_thread(play, (music_list,))
    while True:
        time.sleep(10)


if __name__ == "__main__":
    thread_run()