import re
import warnings
from src.utils.lists import keywords_dict
from src.utils.utils import cleanResume_ML, extract_cv_content
warnings.filterwarnings('ignore')


def process_all_cvs(cv_list):
    """
    Process a list of CVs, format their content, and save to a specified file.

    Args:
        cv_list (list): A list of dictionaries, each representing a CV with at least 
                        a 'file-name' key and 'sections' containing text.
        output_file (str, optional): The name of the file to save formatted CV content. 
                                     Defaults to "cv_contexts_clean.txt".

    Returns:
        list: A list of formatted CV strings, each with a header and cleaned content.
    """

    formatted_cvs = []
    for cv in cv_list:
        filename = cv.get('file-name', 'Unknown_CV')
        content = extract_cv_content(cv_data=cv, clean_text=cleanResume_ML) # Extract and clean CV content
        
        if content:
            # Format with header
            formatted_cv = f"===== {filename} =====\n{content}\n\n"
            formatted_cvs.append(formatted_cv)
    
    return formatted_cvs


def load_cv_contexts(content):
    """Load CV contexts from the text file."""
    try:        
        # Split into individual CVs based on delimiter
        cv_contexts = {}
        for section in content:  # Skip first empty split
            parts = section.split('===== ')[1].split('\n', 1)
            if len(parts) == 2:
                cv_name, context = parts
                cv_contexts[cv_name.strip()] = context.strip()
        return cv_contexts
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

def search_keywords_in_cv(domain, cv_contexts):
    """Search for keywords in CVs and generate a report with found percentage."""
    if domain not in keywords_dict:
        print(f"Error: Domain '{domain}' not found in keywords dictionary.")
        return None
    
    keywords = [kw.lower() for kw in keywords_dict[domain]]
    report = []

    for cv_name, context in cv_contexts.items():
        # Find matching and missing keywords
        found_keywords = []
        missing_keywords = []
        
        for keyword in keywords:
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, context, re.IGNORECASE):
                found_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)
        
        # Calculate found percentage
        total_keywords = len(keywords)
        found_percentage = (len(found_keywords) / total_keywords * 100) if total_keywords > 0 else 0
        
        # Add results to report
        report.extend([f'''===== {cv_name} =====\nTotal Keywords: {total_keywords}\nFound Keywords ({len(found_keywords)}): {', '.join(found_keywords) if found_keywords else 'None'}\nFound Percentage is: {found_percentage:.2f}%\nMissing Keywords ({len(missing_keywords)}): {', '.join(missing_keywords) if missing_keywords else 'None'}\n'''])
    
    return report