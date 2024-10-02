# Sentiment Analysis Project

This project is an original, Python-based sentiment analysis tool that processes reviews from various file formats and provides a summary of sentiments along 
with key positive and negative points. It was developed entirely from scratch, showcasing a unique implementation of sentiment analysis techniques.

## Features

- Supports multiple input formats: CSV, TXT, PDF, JSON, and JSONL
- Analyzes sentiment of reviews using NLTK's VADER sentiment analyzer
- Extracts key positive and negative points from the reviews
- Handles both text input and file input
- Provides a graphical file selection dialog when run interactively
- Implements custom error handling for various scenarios

## Requirements

- Python 3.6+
- pandas
- PyPDF2
- nltk
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```
pip install pandas PyPDF2 nltk
```

3. Run the script once to download the necessary NLTK data:

```
python c.py
```

## Usage

You can run the script in two ways:

1. From the command line with arguments:

```
python c.py --input_type file --input_data path/to/your/file.csv
```

or

```
python c.py --input_type text --input_data "Your review text here"
```

2. Without arguments, which will prompt you for the input type and open a file dialog if needed:

```
python c.py
```

## Input Formats

- CSV: Must contain a 'review' column
- TXT: Each line is treated as a separate review
- PDF: Each page is treated as a separate review
- JSON: Must contain a 'review' key for each review
- JSONL: Each line must be a JSON object with a 'review' key

## Error Handling

The script includes error handling for various scenarios:

- Empty files
- Files with no valid reviews
- Unsupported file types
- General exceptions during processing

When an error occurs, an appropriate error message will be displayed.

### Libraries Used
This project makes use of the following Python libraries:

NLTK (Natural Language Toolkit)
pandas
PyPDF2

While these libraries are used, the implementation of the sentiment analysis logic, file processing, and overall structure of the project is entirely original work.

## License
This project is open source and available under the [MIT License](LICENSE).

### Disclaimer
This project was developed as an original work, with every line of code written from scratch. The specific implementation, algorithms, error handling,
and features are unique to this project and were not copied from any existing sources. If you use this project or parts of it in your own work,
please provide appropriate attribution to the original author.

### Contributing
Feel free to fork this project and submit pull requests with improvements or bug fixes.
All contributions will be thoroughly reviewed to maintain the originality and integrity of the project.

## Samples
I have provided sample files of different types to test if you want to after setup.
