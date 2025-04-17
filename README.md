# 📰 Auto-News Poster for Instagram

This project is a fully automated system that fetches the latest news from Google, paraphrases it using an LLM, and posts it on Instagram every 30 minutes — all without any manual intervention.

## ⚙️ Features
- ⏱️ Automatically runs every 30 minutes
- 📸 Takes screenshots of the latest news using Playwright
- 🧾 Extracts text from images using Python OCR## 📦 Requirements

- Python 3.8+
- Node.js 18+
- Playwright
- Tesseract (for OCR, or any OCR library)
- Access to a local or API-based LLM
- Instagram credentials (stored securely in `auth.json`)
- 🧠 Uses an LLM to understand and paraphrase the news
- 🖼️ Generates a visually appealing image with the paraphrased news
- 📤 Posts the generated image to Instagram using Playwright automation
- 🎯 All components are orchestrated by a single `mainFile.py` controller
  

## 🗂️ Project Structure
├── generate_image/ 
  ── generate_image.py # Creates image with background and news text 
├── posting_posts/
  ├── tests/ 
    ── getting_news_screenshot.ts # Playwright script to capture news screenshot
    ── uploading_posts.ts # Playwright script to post to Instagram 
  ── playwright.config.ts 
├── process_screenshot/ 
  ── getting_and_processing_both.py # OCR and LLM-based text extraction + paraphrasing
├── screenshots/ # Stores raw news screenshots 
├── mainFile.py # Master script that runs everything periodically 
├── allNews.txt # Stores all paraphrased news for record-keeping 
├── news_post.png # Latest generated image to be posted 
├── screenshot_name.txt # Tracks the latest screenshot name 
|── .gitignore # Git ignore rules


## 🚀 How It Works
1. `mainFile.py` is executed (either manually or via a scheduler).
2. It triggers Playwright to capture a Google News screenshot.
3. OCR processes the screenshot to extract text.
4. An LLM paraphrases the news content.
5. The paraphrased text is passed to an image generation script.
6. Playwright uploads the image to Instagram.
7. The loop repeats every 30 minutes.


## 📦 Requirements
- Python 3.8+
- Node.js 18+
- Playwright
- Tesseract (for OCR, or any OCR library)
- Access to a local or API-based LLM
- Instagram credentials (stored securely in `auth.json`)
  
