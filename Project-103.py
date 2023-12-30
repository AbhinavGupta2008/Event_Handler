import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/Hariom/Downloads"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self,event):
        print(f"Hey, {event.src_path} has been deleted!")
    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been moved!")
    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been modified!")
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()
try:
     while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    Observer.stop()
