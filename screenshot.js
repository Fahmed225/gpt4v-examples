const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const url = process.argv[2];
const full_page = !!process.argv[3];
const timeout = 8000;

(async () => {
    const browser = await puppeteer.launch( {
        headless: "new",
    } );

    const page = await browser.newPage();

    await page.setViewport({
        width: 1200,
        height: 1200,
        deviceScaleFactor: 1,
    });

    console.log("Navigating to URL:", url);
    await page.goto(url, {
        waitUntil: "networkidle0",
        timeout: timeout,
    });

    console.log("Taking screenshot after page load");
    await page.screenshot({
        path: "screenshot.jpg",
        fullPage: full_page,
    });

    await browser.close();
})();