import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 

from_dir="C:/Users/rajla/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
       print(event)


event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

while True:
    time.sleep(2)
    print("running....")


 


 
 
 

