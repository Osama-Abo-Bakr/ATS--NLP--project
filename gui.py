import streamlit as st
import os
import tempfile
from typing import List
from src.ML.detections import predict
from src.OCR.ocr_detection import loading_data
from src.Matching.matching import process_all_cvs, load_cv_contexts, search_keywords_in_cv
from src.utils.lists import keywords_dict, class_labels

# Page configuration
st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
    }
    .stFileUploader>div>div>div>div {
        color: #4CAF50;
    }
    .report {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .highlight {
        background-color: #e6f7ff;
        padding: 2px 5px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3209/3209266.png", width=100)
    st.title("ATS Resume Analyzer")
    st.write("""
    This tool helps recruiters and job seekers analyze resumes:
    - Predict suitable job categories
    - Check keyword matching for specific domains
    - Get detailed analysis reports
    """)
    st.markdown("---")
    st.markdown("**Developed by:**")
    st.markdown("- Osama Abo Bakr")
    st.markdown("- Ahmed Nos7y")
    st.markdown("- Abdullah Abas")
    st.markdown("- Youseef Hossam")
    st.markdown("- Sherief")

# Main content
st.header("📄 Resume Analysis Dashboard")

# Function to save uploaded files temporarily
def save_uploaded_files(uploaded_files):
    temp_files = []
    for uploaded_file in uploaded_files:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1])
        temp_file.write(uploaded_file.getvalue())
        temp_files.append(temp_file.name)
        temp_file.close()
    return temp_files

# Tab layout
tab1, tab2 = st.tabs(["Job Prediction", "Keyword Matching"])

with tab1:
    st.subheader("Predict Suitable Job Category")
    st.write("Upload resumes to predict the most suitable job category from our 25 predefined classes.")
    
    uploaded_files = st.file_uploader(
        "Upload resumes (PDF or images)",
        type=["pdf", "png", "jpg", "jpeg"],
        accept_multiple_files=True
    )
    
    if uploaded_files and st.button("Predict Job Categories"):
        with st.spinner("Analyzing resumes..."):
            try:
                temp_file_paths = save_uploaded_files(uploaded_files)
                json_data = loading_data(file_paths=temp_file_paths)
                results = [predict(cv_data) for cv_data in json_data]
                
                # Display results
                st.success("Analysis complete!")
                for i, (file, result) in enumerate(zip(uploaded_files, results)):
                    with st.expander(f"Result for {file.name}"):
                        st.markdown(f"""
                        <div class="report">
                            <h3>📌 Predicted Job Category:</h3>
                            <p class="highlight">{result}</p>
                            <h3>ℹ️ All Supported Categories:</h3>
                            <p>{', '.join(class_labels)}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Clean up temp files
                for file_path in temp_file_paths:
                    if os.path.exists(file_path):
                        os.unlink(file_path)
                        
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")

with tab2:
    st.subheader("Check Keyword Matching")
    st.write("Upload resumes and select a job domain to check keyword matching percentage.")
    
    col1, col2 = st.columns(2)
    with col1:
        domain = st.selectbox(
            "Select Job Domain",
            options=list(keywords_dict.keys()),
            index=0
        )
    
    with col2:
        uploaded_files_match = st.file_uploader(
            "Upload resumes for keyword matching",
            type=["pdf", "png", "jpg", "jpeg"],
            accept_multiple_files=True,
            key="match_uploader"
        )
    
    if uploaded_files_match and st.button("Check Keyword Matching"):
        with st.spinner("Analyzing keyword matches..."):
            try:
                temp_file_paths = save_uploaded_files(uploaded_files_match)
                json_data = loading_data(file_paths=temp_file_paths)
                cv_contexts = process_all_cvs(cv_list=json_data)
                cv_contexts = load_cv_contexts(cv_contexts)
                report = search_keywords_in_cv(domain=domain, cv_contexts=cv_contexts)
                
                # Display results
                st.success("Keyword analysis complete!")
                st.markdown(f"### 📊 Domain: {domain}")
                st.markdown(f"**Keywords used for matching:** {', '.join(keywords_dict[domain])}")
                
                for r in report:
                    st.markdown(f"""
                    <div class="report">
                        {r.replace('=====', '###').replace('\n', '<br>')}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Clean up temp files
                for file_path in temp_file_paths:
                    if os.path.exists(file_path):
                        os.unlink(file_path)
                        
            except Exception as e:
                st.error(f"Error during keyword matching: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray;">
        <p>ATS Resume Analyzer - NLP Project © 2023</p>
    </div>
""", unsafe_allow_html=True)