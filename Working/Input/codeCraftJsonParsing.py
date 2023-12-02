import re
import json

def extract_prompt_response_pairs_strict_end(text):
    """
    Extract prompt and response pairs from the provided text,
    ensuring that the response ends strictly at 'End of Response'.
    """
    # Regular expression pattern to match the structure of the provided text
    pattern = re.compile(r"Start of Prompt:\n(.*?)\n\nStart of Response:\n(.*?)\nEnd of Response", re.DOTALL)
    pairs = pattern.findall(text)

    # Cleaning specific phrases like "Copy code"
    cleaned_pairs = []
    for prompt, response in pairs:
        cleaned_response = response.replace("Copy code", "").strip()  # Remove 'Copy code'
        cleaned_pairs.append({"prompt": prompt.strip(), "expectedResponse": cleaned_response})

    return cleaned_pairs

def write_to_json(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Read from a text file with utf-8 encoding
    with open('codeInput.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract dialogues
    dialogues = extract_prompt_response_pairs_strict_end(text)

    # Write to a JSON file
    write_to_json(dialogues, 'codeInput.json')

    # # Process the file with the updated extraction method
    # dialogues_updated_format =
    #
    # # Checking the first few entries of the extracted dialogues for correctness
    # sample_dialogues_updated_format = dialogues_updated_format[:5]  # Displaying the first 5 entries for review
    # sample_dialogues_updated_format


main()

