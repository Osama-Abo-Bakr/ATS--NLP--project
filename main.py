import os
from typing import List
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, UploadFile, File
from src.ML.detections import predict
from src.OCR.ocr_detection import loading_data
from src.Matching.matching import process_all_cvs, load_cv_contexts, search_keywords_in_cv

app = FastAPI(
    debug=True,
    title="ATS (NLP) Project.",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict_job(files_data: List[UploadFile] = File(...)):
    """
    Handles file uploads and predicts job categories for the provided resumes.

    Args:
        files_data (List[UploadFile]): A list of uploaded files, each representing
                                       a resume to be processed.

    Returns:
        dict: A dictionary containing a list of predicted job categories for each
              uploaded resume.
    """
    try:
        temp_file_paths = []
        for uploaded_file in files_data:
            temp_file_path = os.path.join(os.getcwd(), uploaded_file.filename)
            temp_file_paths.append(temp_file_path)
            
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(await uploaded_file.read())
            
        json_data = loading_data(file_paths=temp_file_paths)
        result = [predict(cv_data) for cv_data in json_data]
        _ = [os.remove(file_path) for file_path in temp_file_paths]
    
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prediction. {e}")
    
@app.post("/match")
async def match_cv(files_data: List[UploadFile] = File(...), keyword: str = "python"):
    """
    Handles file uploads and searches for keywords in the provided resumes.

    Args:
        files_data (List[UploadFile]): A list of uploaded files, each representing
                                       a resume to be processed.
        keyword (str, optional): The keyword to search for in the CVs. Defaults to "python".

    Returns:
        dict: A dictionary containing a report of found and missing keywords for each
              uploaded resume.
    """
    try:
        temp_file_paths = []
        for uploaded_file in files_data:
            temp_file_path = os.path.join(os.getcwd(), uploaded_file.filename)
            temp_file_paths.append(temp_file_path)
            
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(await uploaded_file.read())
            
        json_data = loading_data(file_paths=temp_file_paths)
        cv_contexts = process_all_cvs(cv_list=json_data)
        cv_contexts = load_cv_contexts(cv_contexts)
        report = search_keywords_in_cv(domain=keyword, cv_contexts=cv_contexts)
        _ = [os.remove(file_path) for file_path in temp_file_paths]
        return {"message": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in matching. {e}")