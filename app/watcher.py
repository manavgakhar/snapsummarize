import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from pathlib import Path

import logging
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ScreenshotHandler(FileSystemEventHandler):
    def __init__(self, processor):
        self.processor = processor
        
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        file_parts = list(file_path.parts)
        file_parts[-1] = file_parts[-1][1:]
        file_path = "/".join(file_parts)

        logger.info(f"New screenshot detected: {file_path}")
        self.processor.process_image(file_path)

class DirectoryWatcher:
    def __init__(self, directory, processor):
        self.directory = directory
        self.processor = processor
        self.observer = Observer()

    def start(self):
        event_handler = ScreenshotHandler(self.processor)
        self.observer.schedule(event_handler, self.directory, recursive=False)
        logger.info(f"Watching directory: {self.directory}")
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()

