import { test, chromium } from '@playwright/test';
import path from 'path';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    // create auth.json file using skip login yt video, it will give you session and cookies which help us to skip multiple logins
    // this can be done using codegen and using some syntax, refer video for it
    storageState: '/home/aadi/Desktop/posts/posting_posts/auth.json',
    viewport: { width: 1280, height: 900 }
  });
  const page = await context.newPage();
  
  // opening instagram website with context saved 
  await page.goto('https://www.instagram.com');

  // Path to the news image (modify the path accordingly)
  const imagePath = path.join(process.env.HOME || process.env.USERPROFILE || '.', 'Desktop', 'posts', 'news_post.png');
  // console.log(imagePath)

  // Navigate to new post page
  await page.getByRole('link', { name: 'New post Create' }).click();
  await page.getByRole('link', { name: 'Post Post' }).click();

  // uploading photo
  const input = await page.locator('input[type="file"]');
  await input.setInputFiles(imagePath);
  await page.getByRole('button', { name: 'Next' }).click();
  await page.getByRole('button', { name: 'Next' }).click();

  // writing a caption for post
  await page.getByRole('textbox', { name: 'Write a caption...' }).click();
  const caption = "📢 Latest News Update! 📰\n\n#BreakingNews #LatestUpdates #TrendingNews";
  await page.getByRole('textbox', { name: 'Write a caption...' }).fill(caption);

  // Click share button
  await page.getByRole('button', { name: 'Share' }).click();
  // ✅ Wait for confirmation that post is uploaded
  await page.waitForSelector('h3:text("Your post has been shared.")');

  console.log('Post uploaded successfully!');
  // await page.waitForTimeout(30000);
  await browser.close();
})();
