# SnapSummarize

SnapSummarize is a productivity tool designed to streamline your note-taking workflow. It automatically monitors your MacBook for new screenshots in a specified directory, extracts text from the images using OCR, and summarizes the extracted text using [Ollama](https://github.com/ollama/ollama) `gemma-1b` model. The summarized text is then saved as a text file, making it easier to organize and reference your notes.

Useful when you're researching online, capturing snippets of information, or simply saving time by avoiding manual transcription.

---

## How It Works

1. **Set Up the Watch Directory**: Specify the folder where your screenshots are saved (e.g., `~/Desktop/screenshots`).
2. **Monitor for New Screenshots**: SnapSummarize continuously watches the directory for new files.
3. **Extract Text**: When a new screenshot is detected, the app uses OCR to extract text from the image.
4. **Summarize the Text**: The extracted text is summarized using the `gemma-1b` model.
5. **Save the Summary**: The summarized text is saved as a `.txt` file in your output directory (e.g., `~/Desktop/screenshot_notes`).

---

## To run

1. Clone the repo

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set up Ollama and ensure the gemma-1b model is pulled.

4. Run the application:

`python app/main.py`


🖥️ Example Workflow

1. Take a screenshot (e.g., Cmd + Shift + 4 on Mac).
2. SnapSummarize detects the new screenshot in your watch directory.
3. The app extracts text from the image using OCR.
4. The extracted text is summarized using AI.
5. The summary is saved as a .txt file in your output directory.

Folders in Desktop

<img width="100" alt="Screenshot 2025-03-18 at 11 33 33 PM" src="https://github.com/user-attachments/assets/19bc5763-d897-4707-bb4b-34aadfc805d2" />

Logs:

<img width="400" alt="Screenshot 2025-03-18 at 11 34 13 PM" src="https://github.com/user-attachments/assets/9f720dda-ceb0-4ca7-9017-1d4f69e2090f" />

Screenshot:

<img width="400" alt="Screenshot 2025-03-18 at 10 45 36 PM" src="https://github.com/user-attachments/assets/253632fc-45f3-4ca1-98ce-140d6c2c7b24" />

Summary of a screenshot of code from this repo:

<img width="400" alt="Screenshot 2025-03-18 at 11 34 42 PM" src="https://github.com/user-attachments/assets/1d9af167-6881-47b4-96d8-57fad945e5da" />



