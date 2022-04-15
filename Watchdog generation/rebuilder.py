# This is some testing code for playing around with automated preview rebuilding on file changes in ezcv https://github.com/Descent098/ezcv

from os.path import abspath
import sys     # Used to read input arguments
import time    # used to create artificial delays
import logging # Used to help log in the logging example
import webbrowser # Used to open the preview in the browser
from ezcv.core import generate_site


# Watchdog is used to "watch" folders and do things when changes happen (create, update, delete files)
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

output_folder = "site"

class MyHandler(FileSystemEventHandler):
    # Custom fileSystem handler for watching files on the local system
    def on_any_event(self, event):
        """Overriding the method on watchdog.events.FileSystemEventHandler that is called on any file system event"""
        print(f"File {event.src_path} was {event.event_type}, rebuilding")
        generate_site(output_folder)
        open_in_browser(abspath(output_folder))
        print("Please refresh browser to see changes")


def open_in_browser(output_folder:str):
    browser_types = ["chromium-browser", "chromium", "chrome", "google-chrome", "firefox", "mozilla", "opera", "safari"] # A list of all the types of browsers to try
    for browser_name in browser_types:
        try:
            webbrowser.get(browser_name) # Search for browser
            break # Browser has been found
        except webbrowser.Error:
            continue
    webbrowser.open(f"file:///{abspath(output_folder)}/index.html", new=2) # Open the preview in the browser

if __name__ == "__main__": # Call method on change example
    content_path = "content/"

    event_handler = MyHandler() # Instantiate an event handler
    content_observer = Observer() # Instantiate an observer to "watch" the event hendler
    content_observer.schedule(event_handler, content_path, recursive=True) # Schedule the observer to watch the event handler on the provided path (and include recursive changes to sub-paths)
    content_observer.start() # Start the watching

    generate_site("site")
    open_in_browser(output_folder)
    # Wait one second between polling the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        content_observer.stop()
    content_observer.join() # Keep program running until termination
