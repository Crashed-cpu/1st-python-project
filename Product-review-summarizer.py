import argparse
import pandas as pd
import PyPDF2
import json
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
import re
import sys
import tkinter as tk
from tkinter import filedialog

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

def analyze_sentiment(review):
    try:
        sentiment = sia.polarity_scores(review)
        if sentiment["compound"] >= 0.05:
            return 'Positive'
        elif sentiment["compound"] <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'Neutral'

def summarize_reviews(reviews):
    sentiments = [analyze_sentiment(review) for review in reviews]
    summary = Counter(sentiments)
    return summary

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

def extract_key_points(reviews):
    positive_reviews = [review for review in reviews if analyze_sentiment(review) == 'Positive']
    negative_reviews = [review for review in reviews if analyze_sentiment(review) == 'Negative']
    
    positive_text = ' '.join([preprocess_text(review) for review in positive_reviews])
    negative_text = ' '.join([preprocess_text(review) for review in negative_reviews])
    
    positive_words = word_tokenize(positive_text)
    negative_words = word_tokenize(negative_text)
    
    positive_freq = Counter(positive_words)
    negative_freq = Counter(negative_words)
    
    return positive_freq.most_common(10), negative_freq.most_common(10)

def read_file(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        if 'review' not in df.columns:
            raise ValueError("CSV file must contain a 'review' column")
        reviews = df['review'].tolist()
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            reviews = file.readlines()
    elif file_path.endswith('.pdf'):
        reviews = []
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                reviews.append(page.extract_text())
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                reviews = [item['review'] for item in data if 'review' in item]
            elif isinstance(data, dict):
                reviews = [data['review']] if 'review' in data else []
    elif file_path.endswith('.jsonl'):
        reviews = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = json.loads(line)
                if 'review' in data:
                    reviews.append(data['review'])
    else:
        raise ValueError("Unsupported file type. Please upload a CSV, TXT, PDF, JSON, or JSONL file.")
    
    # Check if the file is empty or contains only whitespace
    reviews = [review.strip() for review in reviews if review.strip()]
    if not reviews:
        raise ValueError("The file is empty or contains no valid reviews.")
    
    return reviews

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(
            ("CSV files", "*.csv"),
            ("Text files", "*.txt"),
            ("PDF files", "*.pdf"),
            ("JSON files", "*.json"),
            ("JSONL files", "*.jsonl"),
            ("All files", "*.*")
        )
    )
    return file_path

def get_multiline_input():
    print("Enter your review text (press Ctrl+D on Unix/Linux or Ctrl+Z on Windows and then Enter to finish):")
    return sys.stdin.read().strip()

def process_input(input_type, input_data):
    try:
        if input_type == 'text':
            if not input_data:
                 input_data = get_multiline_input()
            reviews = input_data.split('\n')
        elif input_type == 'file':
            if not input_data:
                input_data = select_file()
                if not input_data:
                    return "No file selected", None, None
            reviews = read_file(input_data)
        else: 
            return "Please specify how you want to summarize (text or file)", None, None
        
        reviews = [review.strip() for review in reviews if review.strip()]
        
        if not reviews:
            return "No valid reviews found", None, None
        
        summary = summarize_reviews(reviews)
        positive_points, negative_points = extract_key_points(reviews)
        
        return summary, positive_points, negative_points
    except ValueError as e:
        return str(e), None, None
    except Exception as e:
        print(f"Error processing input: {e}")
        return None, None, None

def main(input_type, input_data):
    summary, positive_points, negative_points = process_input(input_type, input_data)
    
    if isinstance(summary, str):
        print(summary)
        return
    
    print("Summary of Sentiments:")
    for sentiment, count in summary.items():
        print(f"{sentiment}: {count}")
    
    print("\nTop Positive Key Points:")
    for word, count in positive_points:
        print(f"{word}: {count}")
    
    print("\nTop Negative Key Points:")
    for word, count in negative_points:
        print(f"{word}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and analyze reviews for sentiment.")
    parser.add_argument('--input_type', choices=['text', 'file'], help='Type of input: text or file')
    parser.add_argument('--input_data', help='The actual input data or file path')
    
    args = parser.parse_args()

    if not args.input_type:
        args.input_type = input("Enter input type (text/file): ")
    if args.input_type == 'file' and not args.input_data:
        args.input_data = None  # This will trigger the file dialog

    main(args.input_type, args.input_data)