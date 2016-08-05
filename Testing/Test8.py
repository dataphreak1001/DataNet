import pafy
from pprint import pprint
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer


yt = "http://www.youtube.com/watch?v=Ik-RsDGPI5Y"

video = pafy.new(yt)

audiostreams = video.streams

pprint(video.audiostreams)

for s in audiostreams:
    if s.extension == "mp4":
        x = audiostreams.index(s)



fyle = audiostreams[x].download()

print fyle


parent = Widget()
button = Button()


class VideoApp(App):
    def build(self):
        self.v = VideoPlayer(source=fyle, state='play')
        return self.v


if __name__ == '__main__':
    VideoApp().run()


