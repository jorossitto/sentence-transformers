import re
import json

def extract_dialogues_updated_format(text):
    """
    Extract dialogues from the text in the updated format.
    """
    # Splitting the text into segments based on 'prompt' and 'response' labels
    segments = text.split("prompt\n-----------\n")
    dialogues = []

    for segment in segments[1:]:  # Skipping the first empty segment
        if "\nresponse\n-----------\n" in segment:
            prompt, response = segment.split("\nresponse\n-----------\n", 1)
            dialogues.append({"prompt": prompt.strip(), "expectedResponse": response.strip()})

    return dialogues

def write_to_json(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Read from a text file with utf-8 encoding
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract dialogues
    dialogues = extract_dialogues_updated_format(text)

    # Write to a JSON file
    write_to_json(dialogues, 'output.json')

    # # Process the file with the updated extraction method
    # dialogues_updated_format =
    #
    # # Checking the first few entries of the extracted dialogues for correctness
    # sample_dialogues_updated_format = dialogues_updated_format[:5]  # Displaying the first 5 entries for review
    # sample_dialogues_updated_format


main()

