import time
import feedparser
from notifypy import notify


url = ""  # Put here any github profile link followed by .atom
etag = ""
initial = True


def watch_feed():
    global etag, initial
    f = feedparser.parse(url, etag)
    etag = f.etag
    if (initial):
        initial = False
        print("App started!")
    elif (f.status == 200):
        notify.Notify(
            f.feed.title,
            f.entries[0].title,
            "GitHub Update"
        ).send()


while True:
    watch_feed()
    time.sleep(30)  # Ping time in seconds
