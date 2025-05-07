import os
import fitz
import json
import numpy as np
from PIL import Image
from ultralytics import YOLO
from typing import List, Dict, Optional
from vision_agent.tools.tools import florence2_ocr

os.environ["VISION_AGENT_API_KEY"]="dm53ZnI0dW56cmp3dXg1cXk4OWM3Omw1WGhSa0xPZHg1NkMwdGhZRnRYQVJ2TmFpNlFiT3dF"
YOLO_MODEL = YOLO("./models/OD/yolo11_OD.pt")
classes = YOLO_MODEL.names
    
def pdf_to_images(temp_file_path: str, dpi: int = 100) -> Optional[List[np.array]]: 
    """
    Converts a PDF file into a list of images, with each page of the PDF
    represented as a separate image.

    Args:
        temp_file_path (str): The file path of the PDF to be converted.

    Returns:
        Optional[List[np.array]]: A list of images represented as numpy arrays, 
        with each array corresponding to a page in the PDF. Returns None if an 
        error occurs during processing.
    """
    images = []
    pdf_document = None
    try:
        # Open the PDF using PyMuPDF(fitz)
        pdf_document = fitz.open(temp_file_path)
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            pix = page.get_pixmap(dpi=dpi)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(np.array(img))
            
    except Exception as e:
        print(f"Error processing PDF {temp_file_path}: {str(e)}")
        
    finally:
        # Ensure the PDF document is closed properly
        if pdf_document:
            pdf_document.close()

    return images


def detect_section_in_resumes(image: np.array) -> List[Dict[str, np.array]]:
    """
    Detects sections in a given resume image, and returns the detected sections
    as a list of dictionaries, where each dictionary contains the section name
    and the corresponding image as a numpy array.

    Args:
        image (np.array): The input image to detect sections in.

    Returns:
        List[Dict[str, np.array]]: The detected sections as a list of dictionaries,
        where each dictionary contains the section name and the corresponding
        image as a numpy array.
    """
    results = YOLO_MODEL.predict(image)[0]
    
    new_data = []
    for result in results:
        xyxy = result.boxes.xyxy[0]
        cls = classes[result.boxes.cls.cpu().numpy().astype(int)[0]]
        if cls == "resume": cls = "description"
        elif cls == "image": continue
        else: pass
        
        new_data.append({"section": cls, "image": image[int(xyxy[1]):int(xyxy[3]), int(xyxy[0]):int(xyxy[2])]})

    return new_data


def apply_ocr(image: np.ndarray) -> List[str]:
    """
    Applies OCR to a given image and returns the extracted text data.

    Args:
        image (np.ndarray): The image to apply OCR to.

    Returns:
        List[str]: The extracted text data.
    """
    data = florence2_ocr(image=image)
    text_data = [txt['label'] for txt in data]
    return text_data

def saving_data(data):
    """
    Saves the extracted data to two files: a JSON file and a text file.

    Args:
        data (List[Dict]): The extracted data, where each dictionary contains
            information about a single file, including the file name, and
            a list of sections, each containing the section name and text.

    Output:
        Two files in the "./output" directory: "outputs.json" containing the
        data in JSON format containing the data in a
        human-readable format.
    """
    ## Save the data to a JSON file
    os.makedirs("./output", exist_ok=True)
    output_path_json = "./output/outputs.json"
    with open(output_path_json, "w") as f:
        all_data = json.dumps(data, indent=4)
        f.write(str(all_data))
    print(f"✅ Finished processing. Output saved to Json: {output_path_json}")
    
    
def loading_data(file_paths: List[str], save: bool = False) -> List[Dict[str, List[Dict[str, List[str]]]]]:   
    all_data = []
    print(f"🚀 Start Loading {len(file_paths)} files")
    for file_path in file_paths:
        ext = file_path.split(".")[-1]
        filename = os.path.basename(file_path)
        filename_data = {"file-name": filename, "sections": []}
        print(f"📂 Processing: {filename}")
        
        
        if ext == "pdf":
            print("📄 Converting PDF to images...")
            images = pdf_to_images(file_path)
                    
        elif ext in ["png", "jpg", "jpeg"]:
            print("🖼️ Reading image file...")
            images = [np.array(Image.open(file_path))]
        else:
            print(f"[⚠️] Unsupported file type: {ext}")  
            continue
        
        for i, img in enumerate(images):
            print(f"\n🔍 Detecting sections on image {i + 1}...")
            sections = detect_section_in_resumes(img)
            for section in sections:
                print(f"🔡 Applying OCR to section: {section['section']}")
                text = apply_ocr(section["image"])
                filename_data["sections"].append({"section": section["section"], "text": text})
              
        all_data.append(filename_data)
        print("✅ Finish Loading file: ", file_path)
        
        
    print("🚀 Saving Data into JSON Fromat.\n")
    if save:
        saving_data(all_data)
    print("✅ Finish Saving Data into JSON Fromat.\n")
    return all_data