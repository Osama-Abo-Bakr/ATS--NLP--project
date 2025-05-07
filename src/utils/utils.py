import re
import json

def load_json(filepath: str):
    """
    Load and parse a JSON file.

    Args:
        filepath (str): The path to the JSON file to be loaded.

    Returns:
        dict or None: The parsed JSON data, or None if the file was not found or the JSON was invalid.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None
    
def clean_text_Match(text: str):
    """
    Advanced cleaning: remove URLs, mentions, hashtags, non-ASCII, punctuation, and normalize whitespace.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'http\S+\s*', ' ', text) # Remove URLs
    
    # Remove RT and cc (common in social media but sometimes present in pasted CV text)
    text = re.sub(r'\bRT\b|\bcc\b', ' ', text)
    text = re.sub(r'#\S+', '', text) # Remove hashtags
    text = re.sub(r'@\S+', ' ', text)  # Remove mentions (@username)
    
    # Remove end-of-sequence markers (specific to your use case)
    text = text.replace('</s>', '')
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # Remove punctuation
    text = re.sub(r'[^\x00-\x7f]', r' ', text)  # Remove non-ASCII characters (e.g., emojis, foreign symbols)
    text = re.sub(r'\s+', ' ', text).strip().lower() # Normalize whitespace and lowercase
    
    return text

def cleanResume_ML(resumeText):
    """
    Advanced cleaning: remove URLs, mentions, hashtags, non-ASCII, punctuation, and normalize whitespace.

    Args:
        resumeText (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)       # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)         # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)       # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)         # remove extra whitespace
    return resumeText

def extract_cv_content(cv_data, clean_text):
    """
    Extracts and cleans all text sections from a CV.

    This function iterates over each section in the provided CV data, applies 
    a cleaning function to each text entry within the sections, and compiles 
    the cleaned text into a single string.

    Args:
        cv_data (dict): A dictionary representing the CV, containing a 'sections' 
                        key with a list of section dictionaries. Each section 
                        dictionary contains a 'text' key with a list of strings.
        clean_text (function): A function that takes a string as input and returns 
                               a cleaned version of the string.

    Returns:
        str: A single string with all cleaned text entries concatenated together, 
             separated by spaces.
    """
    all_words = []
    
    # Get all text from all sections
    for section in cv_data.get('sections', []):
        for text in section.get('text', []):
            cleaned = clean_text(text)
            if cleaned:
                all_words.append(cleaned)
    
    return ' '.join(all_words)