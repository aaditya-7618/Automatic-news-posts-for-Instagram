import { test, chromium } from '@playwright/test';
import path from 'path';
import fs from 'fs';
import { writeFileSync } from 'fs';

(async () => {

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  // Navigate to Google News
  await page.goto('https://news.google.com/', { waitUntil: 'networkidle' });

  // Get the total page height
  const bodyHeight = await page.evaluate(() => document.body.scrollHeight);

  // Scroll down by 40% of the total height
  const scrollAmount = bodyHeight * 0.4;
  await page.evaluate((scrollY) => window.scrollBy(0, scrollY), scrollAmount);

  // Define the screenshot folder
  const screenshotFolder = path.join(process.env.HOME || process.env.USERPROFILE || '.', 'Desktop', 'posts', 'screenshots');

  // Ensure the folder exists
  if (!fs.existsSync(screenshotFolder)) {
    fs.mkdirSync(screenshotFolder, { recursive: true });
  }

  // Take a screenshot of the latest news section
  let screenshotName = `news_${Date.now()}.png`;
  const screenshotPath = path.join(screenshotFolder, screenshotName);
  await page.screenshot({ path: screenshotPath, fullPage: false });

  // Save the name to a file
  writeFileSync('screenshot_name.txt', screenshotName);
  // screenshot path printing
  // console.log(`Screenshot saved at: ${screenshotPath}`);
  // await page.waitForTimeout(10000);
  await browser.close();
})();

