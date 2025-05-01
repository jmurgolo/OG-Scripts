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

//times
//const items = ["7:00 AM","7:15 AM","7:30 AM","7:45 AM","8:00 AM","8:15 AM","8:30 AM","8:45 AM","9:00 AM","9:15 AM","9:30 AM","9:45 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","Actual command not found, wanted to execute git.sync /42311:15 AM","11:30 AM","11:45 AM","12:00 PM","12:15 PM","12:30 PM","12:45 PM","1:00 PM","1:15 PM","1:30 PM","1:45 PM","2:00 PM","2:15 PM","2:30 PM","2:45 PM","3:00 PM","3:15 PM","3:30 PM","3:45 PM","4:00 PM","4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM","6:15 PM","6:30 PM","6:45 PM","7:00 PM","7:15 PM","7:30 PM","7:45 PM","8:00 PM"];

//
//const items = ["50.00 Mass Rental Voucher City Shelter","50.00 LITTER - EXTERIOR 7.16.120 (R/S)","50.00 OVERGROWTH 7.16.120 (V)","50.00 LITTER PUBLIC STREET 7.16.120 (C)","50.00 UNREGISTERED MOTOR VEHICLE 7.16.130","50.00 PLACEMENT OF CONTAINERS 7.16.060","50.00 HOUSING-INTERIOR/EXTERIOR","50.00 OWNER'S INSTALLATION & MAINT","50.00 NUMBERING OF BUILDING 12.16.130","50.00 OWNER NAME/ADDRESS POSTING","50.00 STRUCTURAL ELEMENTS","50.00 MAINTENANCE OF LAND","50.00 DEBRIS - TREEBELT - SIDEWALK","50.00 LITTERING","50.00 MAINT OF SIDEWALKS, GUTTERS","50.00 MAINT OF TREE BELTS","50.00 UNREGISTERED MOTOR VEHICLE ON LOT","75.00 Mass Rental Voucher"];

//Usage Groups
//const items = ['A-1: fixed seating; performing arts, motion pictures','A-2: food or drink consumptions','A-3: worship, recreation or amusement','A-4: indoor sporting','A-5: outdoor activities','B: office, professional services','E: educational','F-1: moderate hazard','F-2: low hazard; non combustibles','H-1: detonation hazard','H-2: deflagration hazard','H-3: physical hazard','H-4: health hazard','H-5: research and development hazard producing','I-1: capable of self-preservation','I-2: not capable of self-preservation','M: sale of merchandise','R-1: hotel, motel','R-2: multi family, dormitories','R-3: 1 or 2 family dwelling','R-4: assisted living between 5-16 occupants','S-1: moderate hazard','S-2: low hazard','U: utility, accessory structures'];

//Ordinance Squad Violations
//const items = ['Alarm: Failure to supply alarm information list','Alarm: Failure to update alarm information list','Blighted property','Building: No numbers on building after notice','Charitable Solicitations without permit','Cigarette, Sale of loose cigarettes(loosies)','Cigarettes, Employee selling to minor','Cigarettes, Failure to post cigarette user sign','Cigarettes, Permit holder allowing sale to minor 1st offense','Cigarettes, Permit holder allowing sale to minor 2nd offense within 15 months','CIgarettes, Permit holder allowing sale to minor 3rd or more offense in 15 months','Curfew: Minor in violation; Permitting minor to violate curfew','Dog / Animal on school grounds during school or athletic event','Dog barking / Nuisance animal 3rd offense','Dog, Failure to remove animal fecal matter','Dog, Unlicensed','Dog, Unlicensed VISCIOUS dog or animal (per day)','Dog, Unrestrained or unsecured vicious dog or animal','Dog, Unspayed or Reproductively whole animal at large','Failure to maintain tree belt | 338-21-C','G.L. CH. 40 SEC 21D: COVID 19/ORDER #31 NO FACE COVERING','Gang Activity 1st | 190-4(.1,.2,.3)','Gang Activity 2nd | 190-4(.1,.2,.3)','Gang Activity 3rd | 190-4(.1,.2,.3)','Graffiti and vandalism violations','Hawkers and Peddlers','HazMat: Violation of alert notification','Littering/trash/overgrowth 1st | 327-13-M.1','Littering/trash/overgrowth 2nd | 327-13-M.2','Littering/trash/overgrowth 3nd | 327-13-M.3','Loitering','Maintenance of Land','Marajuana Use in Public Place | 165-3','Marijuana POSSESION, less than 1 oz.','Motor Scooter 3rd and subsequent','Motor scooter violation 1st','Motor scooter violation 2nd','Motor Vehicle: Abandoned motor vehicle 1st offense','Motor Vehicle: Abandoned motor vehicle 2nd offense','Motor Vehicle: crossing property to avoid traffic signal','Motor Vehicle: Person hanging on or protruding from a Motor Vehicle','No marijuana where smoking is prohibited | General Law - Part I, Title XV, Chapter 94G, Section 13','Noise Ordinance 1st Violation | 259-12(.1,.2,.3)','Noise Ordinance 2nd Violation | 259-12(.1,.2,.3)','Noise Ordinance 3rd Violation | 259-12(.1,.2,.3)','Noise: Landlord allowing repeated noise violations 3rd violation in 12 months','Noise: Landlord allwoing repeated noise violations susequent vilations in 12 months','Noise: Refusing to give true information regarding noise complaint','Nuisance Animal/Barking Dog 1st | 110-6(.1,.2,.3)','Nuisance Animal/Barking Dog 2nd | 110-6(.1,.2,.3)','Open Container of Alcohol in Public | 275-2','Operating a mule, donkey, llama, cow, or other .... without a permit','Operator violations of conduct rules 1st | 390-27.1','Operator violations of conduct rules 2nd | 390-27.2','Other','Overgrowth','Overgrowth Occupied','Overgrowth Vacant Lot','Owner allowing operation w/out a chauffeur lic. 2nd | 390-14.2','Owner allowing operation w/out a chauffeur lic. ist | 390-14.1','Paint Ball / BB gun violations','Panhandling (if non-aggressive check for charitable permit violation)','Parking Motor Vehicle on lawn or landscape area','Parks: Depositing outside waste in Park Department waste receptacles','Parks: Depositing yard waste, leaves on Park Department property','Parks: Littering Park Department maintained property','Refrigerator or Stove stored improperly','Shopping cart on public property after notice','Sidewalk/tree belt/street obstructions | 338','Signs or Handbills, posting in public places','Skateboarding violation 2nd and subsequent offenses','Snow & Ice Removal Violations | 322','Solid Waste: Bulk items left on tree belt','Solid Waste: Leaves and yard waste collection violation','Solid Waste: Materials placed for pickup improperly','Solid Waste: Recycling collection violation','Solid Waste: Removing compostable materials left for pickup','Tag sale without permit','Taxi/Livery operating when Medallion Suspended','Taxi/Livery operation without Medallion','Taxi/Livery Using horn to summon fare','Taxi/Livery Vehicle Appearance Violations','Transient Vendors','Trash pickup violations | 327-7','Trees, Cutting or injuring public tree','Trees, Cutting/removing significant tree over 75 yrs old or 36" diameter','Unregistered motor vehicle on lot 12 days | 327-14','Valet parking rules violations','Viol. of Emergency Parking Ban (snow & ice) | 385.10','Violation of conditions of special permit (bldg. inspectors)','Violation of Parking Rules & Regulations | 1-25-PR','Violation of Permit Parking | 385.39','Zoning Ordinance Violations | 1-25-ZO'];

//Complant Sources
const items = ['Baystate Gas Company','Building Department','Citizen','City Councillor','Civic Group / Council','Department of Children Services','DPW','Electrical Division','Fire Department','Health Department','Housing Department','Internet','Law Department','Mayors Office','MRVP','Other','Owner / Manager','Park Department','Plumbing Division','Police Department','Proactive','Proactive CDBG','Tenant','WMECO','Zoning Division'];

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
