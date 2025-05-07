import pickle
from src.utils.utils import cleanResume_ML, extract_cv_content
from src.utils.lists import class_labels

def predict(resumeText: dict) -> str:
    # Load vectorizer and model
    """
    Predicts the job category of a given resume based on its text content.

    Args:
        resumeText (str): The text content of the resume.

    Returns:
        str: The predicted job category of the resume.
    """
    word_vectorizer = pickle.load(open('./models/ML/vectorizer.pkl', 'rb'))
    model = pickle.load(open('./models/ML/cls_model.pkl', 'rb'))
    resumeText = extract_cv_content(resumeText, cleanResume_ML)
    resumeText = word_vectorizer.transform([resumeText])
    return class_labels[model.predict(resumeText)[0]]