import cv2
import pytesseract
import ollama
import sys
import os

PROMPT2 = """
I will provide you text extracted from news websites and you have to fetch news from it here is the text {newsText}. Paraphase the lines.
Do not include count of news and date of news.
Take the first 10 news only.
Provide me just news no other opening or closing phrases.
"""

def getALlNews(text):
    response = ollama.chat(model='llama3.2:3b', messages=[{'role': 'user', 'content': PROMPT2.format(newsText=text)}])
    return response['message']['content']


def getAllNewsFromScreenshot(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return None

    # Convert to grayscale (improves OCR accuracy)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR
    text = pytesseract.image_to_string(gray)

    # Process the extracted text using LLM
    return getALlNews(text)

if __name__ == '__main__':
    with open('/home/aadi/Desktop/posts/screenshot_name.txt', 'r') as f:
        screenshot_name = f.read().strip()

    image_path = os.path.join('/home/aadi/Desktop/posts/screenshots/', screenshot_name)
    allNews = getAllNewsFromScreenshot(image_path)

    if allNews:
        with open('allNews.txt', 'w') as f:
            f.write(allNews)
        # print(allNews)
