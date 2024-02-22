from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import json
import time

folder_to_track = "C:\Users\Justin Rivera\MyFolder"
folder_destination = "C:\Users\Justin Rivera\MyFolder"

class FHandler (FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

event_handler = FHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()