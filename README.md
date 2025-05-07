# ATS (Applicant Tracking System) - NLP Project

## Overview

This project is an Applicant Tracking System (ATS) that uses Natural Language Processing (NLP) and Computer Vision techniques to analyze resumes. It can predict job categories based on resume content and match resumes against specific job domains by checking for relevant keywords.
![Project Flow](img/NLP%20-%20Task.jpg)

## Project Team

This project was developed by:
- **Osama Abo-Bakr**
- **Ahmed Nos7y**
- **Abdullah Abas**
- **Yousef Hossam**
- **Sherif**

## Features

- **Resume Parsing**: Extracts text from PDF and image-based resumes using OCR
- **Job Category Prediction**: Predicts the most suitable job category from 25 predefined classes
- **Keyword Matching**: Checks resumes for domain-specific keywords and provides a matching percentage
- **Section Detection**: Identifies different sections in resumes (e.g., education, experience)
- **API Endpoints**: Provides RESTful APIs for easy integration

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### Running the Frontend

Start Streamlit GUI:
```bash
streamlit run gui.py
```

The API will be available at `http://127.0.0.1:8000`

### API Endpoints

1. **Job Prediction**:
   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/predict' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'files_data=@your_resume.pdf;type=application/pdf'
   ```

2. **Keyword Matching**:
   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/match?keyword=Data%20Science' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'files_data=@your_resume.pdf;type=application/pdf'
   ```

### Supported Job Categories

The system supports 25 job categories including:
- Data Science
- HR
- Advocate
- Arts
- Health and fitness
- Civil Engineer
- Java Developer
- And more...

## Project Structure

```
project/
├── src/
│   ├── ML/
│   │   └── __init__.py
│   │   └── detections.py          # ML model for job prediction
│   ├── OCR/
│   │   └── __init__.py
│   │   └── ocr_detection.py       # OCR processing and section detection
│   ├── Matching/
│   │   └── __init__.py
│   │   └── matching.py            # Keyword matching functionality
│   └── utils/
│       ├── utils.py               # Utility functions
│       └── lists.py               # Keyword dictionaries and class labels
├── main.py                        # FastAPI application
├── gui.py                         # GUI application using Streamlit
├── requirements.txt               # Dependencies
└── test.ipynb                     # API documentation examples
```

## Dependencies

- Python 3.11+
- FastAPI (for API endpoints)
- Ultralytics (for object detection)
- Vision Agent (for OCR)
- PyMuPDF (for PDF processing)
- NLTK (for NLP processing)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.