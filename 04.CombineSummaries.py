import os

# Create the "TubesFinal" folder if it does not already exist
if not os.path.exists("FinalSummaries"):
    os.makedirs("FinalSummaries")

# Set the input and output directories
input_directory = "ChunkSummaries"
output_directory = "FinalSummaries"

# Initialize a dictionary to store the text for each file
file_texts = {}

# Sort the files alphabetically first
sorted_file_paths = sorted(os.listdir(input_directory))

# Iterate through the files in the input directory
for file_path in sorted_file_paths:
    # Use the os.path.splitext() function to split the file path into a tuple
    file_name, file_extension = os.path.splitext(file_path)
    
    if ":::" not in file_name:
        base_name = file_name
    else:
        # Split the file name into a base name and a suffix
        base_name, file_suffix = file_name.split(":::")

    # If the base name is not in the dictionary, initialize an empty string for it
    if base_name not in file_texts:
        file_texts[base_name] = ""

    # Open the file and read its contents
    with open(os.path.join(input_directory, file_path), "r") as file:
        text = file.read()

    # Add the text to the dictionary entry for the base name
    file_texts[base_name] += text

# Iterate through the base names in the dictionary
for base_name in file_texts:
    # Save the text for the base name to a file in the output directory
    with open(os.path.join(output_directory, base_name + ".txt"), "w") as file:
        file.write(file_texts[base_name])

