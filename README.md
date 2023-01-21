# TLDR.app
Summarise your texts (eBooks, Youtube, PDFs, etc.) with chatGPT

## Setup
1. Install Python: https://www.python.org/
2. Download chromedriver https://chromedriver.chromium.org/downloads - NOTE: make sure you download the version that matches your Google Chrome version (check in *About Chrome*)
3. Put the chromedriver executable file in a location and add that location to the **PATH** - follow guide [here](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) for Windows:  and [here](https://www.swtestacademy.com/install-chrome-driver-on-mac/) for Mac: 
4. Create a chatGPT account: https://chat.openai.com/chat and log in using Google Chrome
5. Press **F12** to open console in Chrome. Go to Application > Cookies and Copy the session token value in **__Secure-next-auth.session-token**
6. Download or git clone this repository (git clone https://github.com/JunMagic88/TLDR.git) to a local folder of your choice
7. Using a text editor, create and save a file named **.env** (no file extension) in the same folder with a single line: **CHATGPT_SESSION_TOKEN=XXXXXXX** replace XXXXXXX with the session token you got from step 5
8. Navigate to the folder in **Terminal (Mac)** or **Command Prompt (Windows)** and run: 
```python
pip install -r requirements
```

## Adding the Texts you want to Summarise
1. Add any **.txt** files in the **/Texts** folder 
2. Add any **.epub** or **.pdf** files in the **/00.EPUBs+PDFs** folder
3. Add any **YouTube links** (can be video or public playlist URLs) to the Youtube

## Now the Fun begins
1. Run this to download the **transcripts** for the YouTube videos and save them to the **/Texts** folder
2. Run this to convert the epub and PDF files into **.txt** and save them to the **/Texts** folder
3. Run this to break the files in /Texts into **chunks** that would fit into single chatGPT window
4. Run this to start the summarisation 
5. Run this after all the chunks have been summarised to combine all the chunk summaries back into a single summary for each text. 
