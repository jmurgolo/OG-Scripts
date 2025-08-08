const puppeteer = require('puppeteer');
const path = require('path');
const fs = require("fs");
const fsp = require('fs/promises');

const url = "https://springfieldma-migration.workflow.opengov.com/#/settings/system/record-types/1006584/form";

async function run () {
    try {
        //read the text file with the accounts we will be logging into
        var accountsfile = fs.readFileSync(__dirname + '//times.txt', 'utf8'); 
        
        //put the accounts into an array 
        var accountsarray = accountsfile.toString().replace(/(?:\r\n|\r|\n)/g,'\t').split("\t");
        let x;

        //console.log(accountsarray);
        
        //var userid = 'jmurgolo@springfieldcityhall.com';
        //var pword = '$SFhhGtfq344KDmT';
  
        //launch the browser in head mode
        const browser = await puppeteer.launch({
            headless: false,
            executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
            userDataDir: './myUserDataDir'
        });
        
        //create a new page
        const page = await browser.newPage();
        await page.setBypassCSP(true);
        await page.setViewport({ width: 1024, height: 768 });
        page.setDefaultNavigationTimeout(50000);
        page.setDefaultTimeout(50000);

        //go to the url
        await page.goto(url);
        await page.waitForTimeout(30000);

        for(x=0;x<accountsarray.length;x=x+1){
        
            // Wait for the element with the specific class to appear
            //const element = await page.$('#element-id'); 
            //const addselector = 'currentDropdownItemName'; // Use the specific class combination
            //await page.waitForSelector(addselector);

            //Click the span element
            //await page.click(addselector);

            // Wait for the input element to appear
            const firsttextinput = 'input#currentDropdownItemName'; // Targeting by ID
            //await page.waitForSelector(firsttextinput);
           
            // Type text into the input field
            await page.type(firsttextinput, accountsarray[0+x]);
           
            await page.keyboard.press('Enter');
            await page.waitForTimeout(3000);

            //const secondtextinput = 'input#new_checklist_item_itemText'; // Targeting by ID
            //await page.waitForSelector(secondtextinput);
        
            // Type text into the input field
            //await page.type(secondtextinput,  accountsarray[0+x+1]);        
            
            //const submitselector = 'button.btn.btn-primary'; // Targeting by class
            //await page.waitForSelector(submitselector);
        
            // Click the button
            //await page.click(submitselector);

            console.log('Adding: ' + firsttextinput);

            await page.waitForTimeout(1000);

        }

        process.exit(1);

    } catch (e) {
        console.log("error 0: " + e);  
        process.exit(1);
    }
}

run();