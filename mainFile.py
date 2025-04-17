import time
import subprocess

def generate_image_for_posting():
    # this will make the image ready for uploading to the instagram or any platform of your choice
    subprocess.run(["python3", "generate_image/generate_image.py"])

def analyse_screenshot_and_getting_news():
    # this will take the news's screenshot and fetch news from that screenshot and make it ready for uploading
    subprocess.run(["python3", "process_screenshot/getting_and_processing_both.py"])

def take_screenshot_of_news():
    # taking screenshot and fetching news for it
    subprocess.run(["npx", "tsx", "posting_posts/tests/getting_news_screenshot.ts"])

def post_to_instagram():
    # Run your Playwright script for uploading
    subprocess.run(["npx", "tsx", "posting_posts/tests/uploading_posts.ts"])

def main():
    while True:
        print("📸")
        print("Taking screenshot of news from google...")
        take_screenshot_of_news()

        print("Analysing the screenshot and fetching the news from it...")
        analyse_screenshot_and_getting_news()

        print("Generating image to post...")
        generate_image_for_posting()

        print("Uploading post to Instagram...")
        post_to_instagram()

        print("Waiting for half hour before next post...\n")
        time.sleep(1800)  # 1 hour in seconds

if __name__ == "__main__":
    main()
