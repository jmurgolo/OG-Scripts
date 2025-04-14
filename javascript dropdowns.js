/**
 * Script to automate dropdown item entry.
 * 
 * Instructions:
 * - Paste this script into the browser console.
 * - Ensure the input field has the ID "currentDropdownItemName".
 * - Modify the `items` array as needed.
 * 
 * Author: [Your Name]
 * Date: [Date]
 */

/**
 * Open your browser (I use chrome) and right click on the dropdown element on the right where you enter values.  Select inspect.  
 * In the inspection window open the console and paste the code into there and hit enter.  The first time it will ask you to type something
 * to allow pasting.  Change the array values as needed.  
 * 
 * Usage:
 * - This script simulates entering dropdown items into an input field.
 * - Ensure the input field has the ID "currentDropdownItemName".
 * - Modify the `items` array to include the desired dropdown items.
 * 
 * Notes:
 * - The script uses promises and async/await for sequential execution.
 * - Includes a timeout mechanism to handle cases where the input does not clear.
 * 
 */

//const items = ["7:00 AM","7:15 AM","7:30 AM","7:45 AM","8:00 AM","8:15 AM","8:30 AM","8:45 AM","9:00 AM","9:15 AM","9:30 AM","9:45 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","11:15 AM","11:30 AM","11:45 AM","12:00 PM","12:15 PM","12:30 PM","12:45 PM","1:00 PM","1:15 PM","1:30 PM","1:45 PM","2:00 PM","2:15 PM","2:30 PM","2:45 PM","3:00 PM","3:15 PM","3:30 PM","3:45 PM","4:00 PM","4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM","6:15 PM","6:30 PM","6:45 PM","7:00 PM","7:15 PM","7:30 PM","7:45 PM","8:00 PM"];
//const items = ["50.00 Mass Rental Voucher City Shelter","50.00 LITTER - EXTERIOR 7.16.120 (R/S)","50.00 OVERGROWTH 7.16.120 (V)","50.00 LITTER PUBLIC STREET 7.16.120 (C)","50.00 UNREGISTERED MOTOR VEHICLE 7.16.130","50.00 PLACEMENT OF CONTAINERS 7.16.060","50.00 HOUSING-INTERIOR/EXTERIOR","50.00 OWNER'S INSTALLATION & MAINT","50.00 NUMBERING OF BUILDING 12.16.130","50.00 OWNER NAME/ADDRESS POSTING","50.00 STRUCTURAL ELEMENTS","50.00 MAINTENANCE OF LAND","50.00 DEBRIS - TREEBELT - SIDEWALK","50.00 LITTERING","50.00 MAINT OF SIDEWALKS, GUTTERS","50.00 MAINT OF TREE BELTS","50.00 UNREGISTERED MOTOR VEHICLE ON LOT","75.00 Mass Rental Voucher"];

const items = ['A-1: fixed seating; performing arts, motion pictures','A-2: food or drink consumptions','A-3: worship, recreation or amusement','A-4: indoor sporting','A-5: outdoor activities','B: office, professional services','E: educational','F-1: moderate hazard','F-2: low hazard; non combustibles','H-1: detonation hazard','H-2: deflagration hazard','H-3: physical hazard','H-4: health hazard','H-5: research and development hazard producing','I-1: capable of self-preservation','I-2: not capable of self-preservation','M: sale of merchandise','R-1: hotel, motel','R-2: multi family, dormitories','R-3: 1 or 2 family dwelling','R-4: assisted living between 5-16 occupants','S-1: moderate hazard','S-2: low hazard','U: utility, accessory structures'];
const input = document.getElementById("currentDropdownItemName");

function waitForInputClear(timeout = 5000) {
    return new Promise((resolve, reject) => {
        const start = Date.now();
        const interval = setInterval(() => {
            if (input.value === "") {
                clearInterval(interval);
                resolve();
            } else if (Date.now() - start > timeout) {
                clearInterval(interval);
                reject("⏰ Timed out waiting for input to clear.");
            }
        }, 100); // check every 100ms
    });
}

async function simulateEntry(item) {
    input.focus();
    input.value = item;
    input.dispatchEvent(new Event("input", { bubbles: true }));

    await new Promise(r => setTimeout(r, 200)); // Small delay before firing keys

    // Simulate full Enter key sequence
    ["keydown", "keypress", "keyup"].forEach(eventType => {
        input.dispatchEvent(new KeyboardEvent(eventType, {
            bubbles: true,
            cancelable: true,
            key: "Enter",
            code: "Enter",
            keyCode: 13,
            which: 13
        }));
    });

    // Old-school fallback
    document.execCommand("insertText", false, "\n");

    console.log("✅ Entered:", item);

    // ⏳ Wait for input to clear before continuing
    await waitForInputClear().catch(err => console.warn(err));
}

async function runAll() {
    for (const item of items) {
        await simulateEntry(item);
    }

    console.log("🎉 Done entering all items.");
}

runAll();
