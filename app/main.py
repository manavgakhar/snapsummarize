import time
import os
from watcher import DirectoryWatcher
from ocr import ImageProcessor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Configure paths
    watch_path = os.path.expanduser("~/Desktop/screenshots")
    output_path = os.path.expanduser("~/Desktop/screenshot_notes")
    
    if not os.path.isdir(watch_path):
        logger.error(f"The provided path is not a valid directory: {watch_path}")
    elif not os.path.isdir(output_path):
        logger.error(f"The provided path is not a valid directory: {output_path}")
        
    else:
        processor = ImageProcessor(watch_path, output_path)
        watcher = DirectoryWatcher(watch_path,processor)
        watcher.start()

if __name__ == "__main__":
    main()

