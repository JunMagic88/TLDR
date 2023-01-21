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
