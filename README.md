# SnapSummarize

SnapSummarize is a productivity tool designed to streamline your note-taking workflow. It automatically monitors your MacBook for new screenshots in a specified directory, extracts text from the images using OCR, and summarizes the extracted text using [Ollama](https://github.com/ollama/ollama) `gemma-1b` model. The summarized text is then saved as a text file, making it easier to organize and reference your notes.

Useful when you're researching online, capturing snippets of information, or simply saving time by avoiding manual transcription.

---

## Features

- **Automatic Screenshot Monitoring**: Watches a specified directory for new screenshots in real-time.
- **OCR Text Extraction**: Uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) to extract text from images with high accuracy.
- **AI-Powered Summarization**: Summarizes extracted text using the `gemma-1b` model from Ollama for concise and meaningful notes.
- **Seamless Note Saving**: Saves the summarized text as a `.txt` file in your chosen output directory.
- **Time-Saving Workflow**: Perfect for researchers, students, and professionals who frequently take screenshots for note-taking.

---

## How It Works

1. **Set Up the Watch Directory**: Specify the folder where your screenshots are saved (e.g., `~/Desktop/screenshots`).
2. **Monitor for New Screenshots**: SnapSummarize continuously watches the directory for new files.
3. **Extract Text**: When a new screenshot is detected, the app uses OCR to extract text from the image.
4. **Summarize the Text**: The extracted text is summarized using the `gemma-1b` model. (run ollama pull if you do not have the model)
5. **Save the Summary**: The summarized text is saved as a `.txt` file in your output directory (e.g., `~/Desktop/screenshot_notes`).

---

## To run

1. Clone the repo

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set up Ollama and ensure the gemma-1b model is installed.

4. Run the application:

`python app/main.py`


🖥️ Example Workflow

1. Take a screenshot (e.g., Cmd + Shift + 4 on Mac).
2. SnapSummarize detects the new screenshot in your watch directory.
3. The app extracts text from the image using OCR.
4. The extracted text is summarized using AI.
5. The summary is saved as a .txt file in your output directory.