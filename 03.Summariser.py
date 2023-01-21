# Chunks the text files into GPT-able size, and then summarise each chunk into a folder
import os
from dotenv import load_dotenv
from revChatGPT.ChatGPT import Chatbot
import time

# Load chatGPT session token
load_dotenv()
token =  os.environ.get("CHATGPT_SESSION_TOKEN")

# Create the required folders 
if not os.path.exists("ChunkSummaries"):
    os.makedirs("ChunkSummaries")

# Set the directories for the input and output files
input_directory = "GPTChunks"
output_directory = "ChunkSummaries"

# Look through which chunks have already been summarised and delete them.
is_file_in = "ChunkSummaries"
del_file_in="GPTChunks"

for filename in os.listdir(is_file_in):
    for file in os.listdir(del_file_in):
        if file == filename:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            gpt_chunks_folder = os.path.join(current_directory, "GPTChunks")
            os.system("rm \"" + os.path.join(gpt_chunks_folder, file) + "\"")

# Initiate chatGPT
chatbot = Chatbot({
      "session_token": token
    }, conversation_id=None, parent_id=None) 

# Counter to keep track of chat instances
count =0

# Iterate through the files in the input directory and summarise them
for filename in os.listdir(input_directory):

    with open(os.path.join(input_directory, filename), "r") as file:
        text = file.read()

    # Feel free to experiment with different prompts
    response = chatbot.ask("Write notes about the following text. Use bullet points in complete sentences. \""+text+"\"", conversation_id=None, parent_id=None)
    summary = response['message']

    # Split the summary string into a list of sentences
    sentences = summary.split(". ")

    # Initialize the modified text
    modified_text = ""

    # Add a hyphen at the start and a new line at the end of each sentence
    for sentence in sentences:
        modified_text += sentence + "\n"

    # Save the summary to a text file
    with open(os.path.join(output_directory, filename), "w") as file:
        file.write(modified_text)

    count +=1
    time.sleep(5)
    # reset chat in chatGPT after every 10 chunks to minimise errors
    if (count % 10 == 0):
        chatbot.reset_chat()

# Delete last files that had been summarised in GPTChunks
for filename in os.listdir(is_file_in):
    for file in os.listdir(del_file_in):
        if file == filename:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            gpt_chunks_folder = os.path.join(current_directory, "GPTChunks")
            os.system("rm \"" + os.path.join(gpt_chunks_folder, file) + "\"")
