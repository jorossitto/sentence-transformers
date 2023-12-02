import json
import logging

def load_json_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        # Handle the file not found situation, e.g., return an empty list or None
        return None
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in the file: {file_path}")
        # Handle invalid JSON format, e.g., return an empty list or None
        return None
    except Exception as e:
        logging.error(f"An error occurred while loading the file: {file_path}, Error: {e}")
        # Handle other potential errors
        return None