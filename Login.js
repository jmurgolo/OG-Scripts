const puppeteer = require('puppeteer');
const url = "https://www.eversource.com/security/account/login"

function run () {
    return new Promise(async (resolve, reject) => {
        try {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            await page.goto(url);
            const getDimensions = await page.evaluate(() => {
            return {
                item: document.getElementById('Email/Username').clientWidth                           
                };
            });            
            console.log(getDimensions);               
            await browser.close();
        } catch (e) {
            return reject(e);
        }
    })
}

run().then(console.log).catch(console.error);