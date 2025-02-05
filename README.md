


# RAG-QA-using-DeepSeek-R1

**RAG-QA-using-DeepSeek-R1** is a document-based question-answering system that leverages retrieval-augmented generation (RAG) powered by DeepSeek R1. It extracts and processes content from documents—via URLs or PDFs—to generate accurate, context-aware answers.

## Overview

This project comprises three primary components:

- **Data Ingestion:**  
  - **URL Ingestion:** Scrapes and parses text from web pages.  
  - **PDF Ingestion:** Uses the `PDFPlumberLoader` from `langchain_community.document_loaders` to extract text from PDF files.

- **Model Integration:**  
  Simulates integration with DeepSeek R1 to process extracted document content and generate answers using retrieval-augmented generation (RAG).

- **User Interface:**  
  An interactive Streamlit UI where users can upload a document (or input a URL), submit a question, and receive a context-aware answer.

<!-- ## Demo Video

Watch the demo video below to see **RAG-QA-using-DeepSeek-R1** in action:

[![Demo Video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) -->

## Project Structure

```plaintext
RAG-QA-using-DeepSeek-R1/
├── data_ingestion.py         # Module for extracting text from URLs and PDFs using PDFPlumberLoader
├── model_integration.py      # Module simulating DeepSeek R1 integration for Q/A
├── app.py                    # Streamlit-based user interface for document-based Q/A
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amangupta05/RAG-QA-using-DeepSeek-R1.git
   cd RAG-QA-using-DeepSeek-R1
   ```

2. **Install the required dependencies:**

   Ensure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Launch the Streamlit application by executing:

```bash
streamlit run app.py
```

This command will open a new browser window or tab displaying the UI. From the interface, you can:

- **Provide Document Input:**  
  - **URL:** Enter the URL of a document to fetch and parse its content.
  - **PDF Upload:** Upload a PDF file from which text is extracted using `PDFPlumberLoader`.

- **Pose a Question:**  
  Enter your question in the provided input box.

- **View the Answer:**  
  Click the button to generate and display an answer based on the document content.

## Customization

- **Data Ingestion:**  
  Modify `data_ingestion.py` to refine text extraction methods. You can adjust the URL scraping logic or customize the PDF extraction process using `PDFPlumberLoader`.

- **Model Integration:**  
  Replace the dummy implementation in `model_integration.py` with actual DeepSeek R1 API calls or integration logic as needed.

- **UI Modifications:**  
  Customize `app.py` to enhance the interface layout, add new features, or adjust the styling.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Acknowledgements

- **DeepSeek R1:** For providing advanced retrieval-augmented generation capabilities.
- **Streamlit:** For the intuitive UI framework.
- **LangChain Community:** For the `PDFPlumberLoader` and other helpful document processing tools.
- **Community Libraries:** Including tools for web scraping and document parsing.
```

---

Feel free to modify any section to better match your project's specifics. Replace the demo video placeholder with your actual video link, and adjust the license section if needed.
