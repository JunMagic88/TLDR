# TLDR.app
Summarise longer texts (eBooks, Youtube, PDFs, etc.) with chatGPT

## Setup
1. Install Python: https://www.python.org/
2. Download chromedriver https://chromedriver.chromium.org/downloads - NOTE: make sure you download the version that matches your Google Chrome version (check in *About Chrome*)
3. Put the chromedriver executable file in a location and add that location to the **PATH** - follow guide [here](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) for Windows:  and [here](https://www.swtestacademy.com/install-chrome-driver-on-mac/) for Mac: 
4. Create a chatGPT account: https://chat.openai.com/chat and log in using Google Chrome
5. Press **F12** to open console in Chrome. Go to Application > Cookies and Copy the session token value in **__Secure-next-auth.session-token**
6. Download or git clone this repository to a local folder of your choice
```python
git clone https://github.com/JunMagic88/TLDR.git
```
8. Using a text editor, create and save a file named **.env** (no file extension) with a single line in its content: **CHATGPT_SESSION_TOKEN=XXXXXXX** replace XXXXXXX with the session token you got from step 5
9. Navigate to the TLDR folder in **Terminal (Mac)** or **Command Prompt (Windows)** and run: 
```python
pip install -r requirements
```

## Adding texts to summarise
1. Add any **.txt** files in the **/Texts** folder 
2. Add any **.epub** or **.pdf** files in the **/00.EPUBs+PDFs** folder
3. Add any **YouTube links** (can be video or public playlist URLs) to the Youtube

## Let's TLDR!
1. Run this to download the **transcripts** of the YouTube videos to the **/Texts** folder
```python
python 01.GetTranscripts.py
```
2. Run this to convert the epub and PDF files into **.txt** and save them in the **/Texts** folder
```python
python 01.ParseToTxt.py
```
3. Run this to break the files in /Texts into **chunks** that would fit into single chatGPT windows
```python
python 02.Chunkify.py
```
4. Run this to start the summarisation. This should start a Chrome window. Do not try to login and allow it to close automatically. The summarised chunks are saved in **/ChunkSummaries** folder
```python
python 03.Summarise.py
```
5. Run this after all the chunks have been summarised. This will combine all chunk summaries back into a final summary for for each text in the **FinalSummaries** folder. 
```python
python 04.CombineSummaries.py
```
## Common issues & workarounds
03.Summarise.py may fail and exit from time to time. This is typically due to: 
* The number of chats in chatGPT has filled up - FIX: log into chatGPT and clear your chats via the left panel
* The session token is out of date - FIX: get a new token - see step 5 above. 
* Too many requests in 1 minute - FIX: Run the script again or change the x in **time.sleep(x)** within the code to a higher number so that the script pauses for x seconds before trying again
* Too many requests in 1 hour - FIX: chatGPT rate limit. create an additional account + get session token to run another instance of the script.
