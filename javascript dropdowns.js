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
const items = ["7:00 AM","7:15 AM","7:30 AM","7:45 AM","8:00 AM","8:15 AM","8:30 AM","8:45 AM","9:00 AM","9:15 AM","9:30 AM","9:45 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","Actual command not found, wanted to execute git.sync /42311:15 AM","11:30 AM","11:45 AM","12:00 PM","12:15 PM","12:30 PM","12:45 PM","1:00 PM","1:15 PM","1:30 PM","1:45 PM","2:00 PM","2:15 PM","2:30 PM","2:45 PM","3:00 PM","3:15 PM","3:30 PM","3:45 PM","4:00 PM","4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM","6:15 PM","6:30 PM","6:45 PM","7:00 PM","7:15 PM","7:30 PM","7:45 PM","8:00 PM"];

//Usage Groups
//const items = ['A-1: fixed seating; performing arts, motion pictures','A-2: food or drink consumptions','A-3: worship, recreation or amusement','A-4: indoor sporting','A-5: outdoor activities','B: office, professional services','E: educational','F-1: moderate hazard','F-2: low hazard; non combustibles','H-1: detonation hazard','H-2: deflagration hazard','H-3: physical hazard','H-4: health hazard','H-5: research and development hazard producing','I-1: capable of self-preservation','I-2: not capable of self-preservation','M: sale of merchandise','R-1: hotel, motel','R-2: multi family, dormitories','R-3: 1 or 2 family dwelling','R-4: assisted living between 5-16 occupants','S-1: moderate hazard','S-2: low hazard','U: utility, accessory structures'];

//Complant Sources
//const items = ['Baystate Gas Company','Building Department','Citizen','City Councillor','Civic Group / Council','Department of Children Services','DPW','Electrical Division','Fire Department','Health Department','Housing Department','Internet','Law Department','Mayors Office','MRVP','Other','Owner / Manager','Park Department','Plumbing Division','Police Department','Proactive','Proactive CDBG','Tenant','WMECO','Zoning Division'];

//car brands
//const items = ['Acura','Alfa Romeo','Aston Martin','Audi','Bentley','BMW','Bugatti','Buick','BYD','Cadillac','Chevrolet','Chrysler','Dodge','Ferrari','Fiat','Ford','Genesis','GMC','Honda','Hummer','Hyundai','Infiniti','Jaguar','Jeep','Kia','Lamborghini','Land Rover','Lexus','Lincoln','Lucid','Maserati','Mazda','McLaren','Mercedes-Benz','MINI','Mitsubishi','Nissan','Polestar','Porsche','RAM','Rivian','Rolls-Royce','Subaru','Tesla','Toyota','Volkswagen','Volvo','Zeekr'];

//car models
//const items = ['Accord','Altima','Armada','Ascent','Atlas','A4','A6','Avalon','Aviator','Blazer','Bolt','Bronco','Camry','Canyon','Challenger','Charger','Cherokee','Civic','Colorado','Compass','Corolla','Corvette','CR-V','Crosstrek','CX-30','CX-5','CX-50','Defender','Durango','Edge','Elantra','Enclave','Encore','Envision','Equinox','Escalade','Escape','Expedition','Explorer','F-150','Forester','Forte','Frontier','Fusion','Gladiator','Golf','Grand Cherokee','Grand Wagoneer','Highlander','HR-V','Impala','Impreza','Jetta','Journey','K5','Kona','Malibu','Maverick','MDX','Model 3','Model S','Model X','Model Y','Murano','Mustang','Odyssey','Outback','Pacifica','Palisade','Passport','Pathfinder','Pilot','Q3','Q5','Q7','QX50','QX60','RAV4','Renegade','Ridgeline','Rogue','RX','Santa Cruz','Santa Fe','Seltos','Sentra','Sequoia','Sierra','Silverado','Sonata','Sorento','Soul','Sportage','Suburban','Tacoma','Tahoe','Telluride','Terrain','Tiguan','Titan','Trailblazer','Traverse','Tundra','Tucson','UX','Veloster','Venue','Versa','Wagoneer','Wrangler','XT4','XT5','XT6','Yukon'];

//car colors
//const items = ['Beige','Black','Blue','Bronze','Brown','Burgundy','Charcoal','Copper','Cream','Gold','Gray','Green','Maroon','Orange','Pink','Purple','Red','Silver','Tan','Teal','White','Yellow'];





const input = document.getElementById(":ra5q:");


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async function simulateEntry() {
    await sleep(1000);
    for (const item of items) {
      try {
        input.focus();
        input.value = item;
        input.dispatchEvent(new Event("input", { bubbles: true }));
        await sleep(1000); // let React or the form notice the change
        input.value = item;
        document.execCommand("insertText", false, "\n");

        //Simulate full Enter key sequence
        for (const type of ["keydown", "keypress", "keyup"]) {
          input.dispatchEvent(new KeyboardEvent(type, {
            bubbles: true,
            cancelable: true,
            key: "Enter",
            code: "Enter",
            keyCode: 13,
            which: 13
          }));
        }
  
      } catch (err) {
        console.warn(`❌ Error entering "${item}":`, err);
      }
    }
  
    console.log("🎉 Done entering all items.");
  }
  
  simulateEntry();