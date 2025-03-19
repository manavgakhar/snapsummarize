import logging
from easyocr import Reader
from summarize import Summarizer
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageProcessor:

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.summarizer = Summarizer()

    def process_image(self, file_path):
        logger.info(f"Processing image: {file_path}")
        
        # Validate file_path
        if not isinstance(file_path, str) or not os.path.isfile(file_path):
            logger.error(f"Invalid file path: {file_path}")
            return
        
        # Initialize EasyOCR Reader
        reader = Reader(['en'], gpu=False)  # Set gpu=True if GPU is available
        
        # Read and extract text from the image
        try:
            result = reader.readtext(file_path, detail=0)  # detail=0 returns only the text
            extracted_text = " ".join(result)
            logger.info(f"Extracted text: {extracted_text}")
            summarized_text = self.summarizer.summarize_text(extracted_text)

            base_name = os.path.basename(file_path)  # Extract the file name
            output_file = os.path.join(self.output_path, f"{os.path.splitext(base_name)[0]}.txt")
            with open(output_file, "w") as f:
                f.write(summarized_text)
            logger.info(f"Summarized text saved to: {output_file}")
            
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            # return None