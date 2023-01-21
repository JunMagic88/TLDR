# Break the text files to GPT-able chunks

import os

# Create the "GPTChunks" folder if it does not already exist
if not os.path.exists("GPTChunks"):
    os.makedirs("GPTChunks")

# Set the directories for the input and output files
input_directory = "Texts"
output_directory = "GPTChunks"

# Set the maximum number of words per file
max_words_per_file = 1200

# Iterate through the files in the input directory
for filename in os.listdir(input_directory):
    # Open the file and read its contents
    with open(os.path.join(input_directory, filename), "r") as file:
        text = file.read()

    # Split the text into a list of words
    words = text.split()

    # If the number of words is less than the maximum, save the entire file to the output directory
    if len(words) <= max_words_per_file:
        output_filename = filename
        with open(os.path.join(output_directory, output_filename), "w") as file:
            file.write(text)
    # If the number of words is greater than the maximum, split the text into multiple files
    else:
        # Initialize the current word count and file index
        current_word_count = 0
        file_index = 1

        # Initialize the current output text and filename
        current_output_text = ""
        current_output_filename = filename.rsplit(".", 1)[0] + ":::" + str(file_index).zfill(2) + ".txt"

        # Iterate through the words in the input text
        for word in words:
            # Add the word to the current output text
            current_output_text += word + " "

            # Increment the current word count
            current_word_count += 1

            # If the current word count is equal to the maximum, save the current output text to a file
            # and reset the current output text and word count
            if current_word_count == max_words_per_file:
                with open(os.path.join(output_directory, current_output_filename), "w") as file:
                    file.write(current_output_text)
                current_output_text = ""
                current_word_count = 0
                file_index += 1
                current_output_filename = filename.rsplit(".", 1)[0] + ":::" + str(file_index).zfill(2) + ".txt"

        # Save any remaining text to a file
        if current_output_text.strip():
            with open(os.path.join(output_directory, current_output_filename), "w") as file:
                file.write(current_output_text)

