# Sentiment Analysis Project

This project is a Python-based sentiment analysis tool that processes reviews from various file formats and provides a summary of sentiments along with key positive and negative points.

## Features

- Supports multiple input formats: CSV, TXT, PDF, JSON, and JSONL
- Analyzes sentiment of reviews using NLTK's VADER sentiment analyzer
- Extracts key positive and negative points from the reviews
- Handles both text input and file input
- Provides a graphical file selection dialog when run interactively

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

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).
