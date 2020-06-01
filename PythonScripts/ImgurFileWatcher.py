import time 
 
from Imgur import UploadtoImgur
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler
import pyperclip

#http://thepythoncorner.com/dev/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/
#https://github.com/gorakhargosh/watchdog

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    Upload(event)

def on_deleted(event):
    print(f" deleted {event.src_path}!")


def on_modified(event):
    print(f"{event.src_path} has been modified")
    Upload(event)


def on_moved(event):
    print(f"moved {event.src_path} to {event.dest_path}")

#create handlers
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

linksDone =[]

# upload function
def Upload(event):
    time.sleep(1)
    link = event.src_path
    #print(f"found, {link} has been created!")
    print("uploading")
   # print(link.lower())
    if (link.endswith('.jpg') | link.endswith('.gif') | link.lower().endswith('.png')):
        linksDone.append(link)
        if(linksDone.count(link) > 1): return
        imglink = UploadtoImgur(link)
        #Write to clipboard.
        print(f"Uploaded.....:{imglink}")
        print("Paste to clipboard.")
        pyperclip.copy(imglink) 
        clearlist()

def clearlist():
    time.sleep(4)
    linksDone.clear()

#create an observer
path = "C:\\Users\\richa\\Pictures\\Captures"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
      time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

