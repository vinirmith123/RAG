# PDF Query Application

## Description

A Streamlit application for querying PDF documents using Retrieval-Augmented Generation (RAG) with OpenAI's GPT-3.5.

## Requirements

- Python 3.10
- Install dependencies using requirements.txt

## Setup

1. Clone the repository:
    bash
    git clone <repository-url>
    

2. Navigate to the project directory:
    bash
    cd your_project
    

3. Create a virtual environment:
    bash
    python3 -m venv venv
    

4. Activate the virtual environment:
    - On Windows:
        bash
        venv\Scripts\activate
        
    - On macOS/Linux:
        bash
        source venv/bin/activate
        

5. Install the required packages:
    bash
    pip install -r requirements.txt
    

6. Run the Streamlit application:
    bash
    streamlit run app.py
    

## Environment Variables

Make sure to set your OpenAI API key in a .env file with the following content:
