from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
import re

def parse_news_string(news_string):
    # Extract lines that start with a number followed by a dot and a space
    lines = news_string.strip().split('\n')
    news_list = []
    for line in lines:
        match = re.match(r"\d+\.\s+(.*)", line)
        if match:
            news_list.append(match.group(1).strip())
    return news_list

def create_news_image(news_list, bg_image_path, output_path="/home/aadi/Desktop/posts/news_post.png"):
    # Load background image
    image = Image.open(bg_image_path).convert("RGBA")
    
    # Resize background to fit text properly
    img_width, img_height = 600, 550  # Adjust for better fit
    image = image.resize((img_width, img_height))

    # Reduce background opacity
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 100))  # White with transparency
    image = Image.alpha_composite(image, overlay)

    # Convert back to RGB (for saving as PNG)
    image = image.convert("RGB")

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Load bold font
    try:
        # font = ImageFont.truetype("arialbd.ttf", 22)  # Smaller font size for readability
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    except:
        font = ImageFont.load_default()

    # Text starting position
    x, y = 40, 30
    line_spacing = 25  # Space between wrapped lines

    # Wrap and draw each news headline
    for index, news in enumerate(news_list, start=1):
        wrapped_text = textwrap.fill(f" {news}", width=75)
        draw.text((x, y), wrapped_text, fill=(0, 0, 0), font=font)
        y += line_spacing * (wrapped_text.count("\n") + 1)

    # Save the final image
    image.save(output_path)
    print(f"News image saved as {output_path}")

# Read from file
with open('/home/aadi/Desktop/posts/allNews.txt', 'r') as f:
    allNews = f.read().strip()

# Parse headlines from string
parsed_news = parse_news_string(allNews)

# Background image path
# bg_image_path = "./p1.jpg"  # Update this path as needed
bg_image_path = "/home/aadi/Desktop/posts/generate_image/p1.jpg"

# Generate the news image
create_news_image(parsed_news, bg_image_path)
