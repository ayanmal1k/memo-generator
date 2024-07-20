# Memo Generator

A simple GUI application to generate memos based on user inputs. The application uses `tkinter` for the GUI, `datetime` for the current date, `ollama` for generating the memo content, and `python-docx` along with `docx2pdf` for creating and converting the document.

## Features

- Generates memos based on user input
- Uses a template to create a Word document
- Converts the Word document to PDF

## Requirements

- Python 3.x
- tkinter
- datetime
- ollama
- python-docx
- docx2pdf

-tinyllama from ollama 

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/memo-generator.git
    cd memo-generator
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python memo_generator.py
    ```

2. Fill in the fields in the GUI and click "Generate Memo".

## Files

- `memo_generator.py`: Main Python script.
- `requirements.txt`: List of required Python packages.
- `memotemplate_template.docx`: Template for the memo : edit as you may like.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
