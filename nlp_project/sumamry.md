# Text Analysis Project

This project is a Django-based web application for text analysis, utilizing spaCy to perform various natural language processing (NLP) operations. The application allows users to input text and receive several analyses, including tokenization, stopword filtering, frequency distribution, named entity recognition (NER), part-of-speech (POS) tagging, and lemmatization.

## `views.py`

The `views.py` file contains the backend logic for text analysis. Here is an overview of its main functionalities:

- **Loading the spaCy Model**: The pre-trained `en_core_web_sm` model from spaCy is loaded.
- **`analyze_text` Function**: Handles POST requests and performs the following operations:
  - **Tokenization**
  - **Stopword Filtering**
  - **Frequency Distribution**
  - **Named Entity Recognition (NER)**
  - **Part-of-Speech (POS) Tagging**
  - **Lemmatization**
  - **Context**: Creates a context dictionary with the analysis results.

## `analyze.html`

The `analyze.html` file is the HTML template that displays the text analysis results. Here is an overview of its main functionalities:

- **Input Form**: Allows users to input the text to be analyzed.
- **Results Sections**: Displays the analysis results:
  - **Original Text**
  - **Tokens**
  - **Filtered Tokens**
  - **Frequency Distribution**
  - **Named Entities**
  - **POS Tags**
  - **Lemmas**
- **Error Handling**: Displays an error message if something goes wrong.

## How to Download and Run the Project

### Prerequisites

- Python 3.x
- pip
- Git

### Steps

1. **Clone the Repository**

git clone https://github.com/Mike014/Django.git cd Django

2. **Create a Virtual Environment**

python -m venv venv source venv/bin/activate  # On Windows use venv\Scripts\activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run Database Migrations**

python manage.py makemigrations python manage.py migrate

5. **Start the Django Server**

python manage.py runserver

6. **Access the Application**

Open your browser and navigate to `http://127.0.0.1:8000/nlp_app/analyze/`.

7. **Input Text**

Enter some text in the form and press "Analyze".

8. **View Results**

The analysis results will be displayed in the various sections of the page.

## Conclusion

This project provides a simple yet powerful platform for text analysis using the advanced capabilities of spaCy. It is an excellent starting point for anyone interested in exploring natural language processing and its practical applications.


   

   

   

   

   