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

//Record Type
// const items = ['Building','Electrical','Housing','Plumbing','Zoning' ];

//Housing Inspectiors
//const items = ["Jermaine Mitchell","Michael McNulty","Jesus Martinez","Mike Jones","Michelle Haska","Danny Cueto","William Brunton","Christopher Bennett"];
// const items = ['Anthony Bedinelli','William Catellier','Keith Fleming','Tommie Hart','Jason Laviolette','Matthew Lee','Giselle Made','Andrew Normand','Joel Rosemond','Julio Vazquez'];

//Building Inspectors
//const items = ['David Markham','Paul Brodeur','Matthew Goodchild','Abdul Mohammed','Donald Zdunczyk','Mark Hebert','Thomas Kennedy','George Shaw'];
  
//Electrical Inspectors
// const items = ['Aaron Cole','Riccardo Bedinotti','Joseph Desmond','Peter Nham'];

//Plumbing Inspectors
//const items = ['Thomas Witkop','Sam Santaniello','Roderick Cruz','Paul Brodeur'];

//Type of proposed business
//const items = ['Apartment','Auto Body','Auto Dealer','Auto Rental','Auto Repair','Auto Sales','Bakery','Bar','Barber Shop','Beauty Parlor','Billards','Bookstore','Business','Church','Cleaners','Clothing','Club','Day Care','Distribution','Florest','Garage','Gas Station','Grocery Store','Gym','Hair Salon','Laundromat','Lounge','Machine Shop','Manufacturing','Massage Parlor','Medical Office','Multi Family Facility','Multi Family Residence','Nail Salon','Office','Pizza Shop','Printing','Real Estate','Repairs','Residence','Restaurant','Retail','Retail Store','Sales','Salon','School','Service Station','Shoe Repair','Shop','Storage','Store','Studio','Take-Out Only','Track','Upholstering','Use Car Lot','Warehouse'];

//Usage Groups
//const items = ['A-1: fixed seating; performing arts, motion pictures','A-2: food or drink consumptions','A-3: worship, recreation or amusement','A-4: indoor sporting','A-5: outdoor activities','B: office, professional services','E: educational','F-1: moderate hazard','F-2: low hazard; non combustibles','H-1: detonation hazard','H-2: deflagration hazard','H-3: physical hazard','H-4: health hazard','H-5: research and development hazard producing','I-1: capable of self-preservation','I-2: not capable of self-preservation','M: sale of merchandise','R-1: hotel, motel','R-2: multi family, dormitories','R-3: 1 or 2 family dwelling','R-4: assisted living between 5-16 occupants','S-1: moderate hazard','S-2: low hazard','U: utility, accessory structures'];

//Ordinance Squad Violations
//const items = ['Alarm: Failure to supply alarm information list','Alarm: Failure to update alarm information list','Blighted property','Building: No numbers on building after notice','Charitable Solicitations without permit','Cigarette, Sale of loose cigarettes(loosies)','Cigarettes, Employee selling to minor','Cigarettes, Failure to post cigarette user sign','Cigarettes, Permit holder allowing sale to minor 1st offense','Cigarettes, Permit holder allowing sale to minor 2nd offense within 15 months','CIgarettes, Permit holder allowing sale to minor 3rd or more offense in 15 months','Curfew: Minor in violation; Permitting minor to violate curfew','Dog / Animal on school grounds during school or athletic event','Dog barking / Nuisance animal 3rd offense','Dog, Failure to remove animal fecal matter','Dog, Unlicensed','Dog, Unlicensed VISCIOUS dog or animal (per day)','Dog, Unrestrained or unsecured vicious dog or animal','Dog, Unspayed or Reproductively whole animal at large','Failure to maintain tree belt | 338-21-C','G.L. CH. 40 SEC 21D: COVID 19/ORDER #31 NO FACE COVERING','Gang Activity 1st | 190-4(.1,.2,.3)','Gang Activity 2nd | 190-4(.1,.2,.3)','Gang Activity 3rd | 190-4(.1,.2,.3)','Graffiti and vandalism violations','Hawkers and Peddlers','HazMat: Violation of alert notification','Littering/trash/overgrowth 1st | 327-13-M.1','Littering/trash/overgrowth 2nd | 327-13-M.2','Littering/trash/overgrowth 3nd | 327-13-M.3','Loitering','Maintenance of Land','Marajuana Use in Public Place | 165-3','Marijuana POSSESION, less than 1 oz.','Motor Scooter 3rd and subsequent','Motor scooter violation 1st','Motor scooter violation 2nd','Motor Vehicle: Abandoned motor vehicle 1st offense','Motor Vehicle: Abandoned motor vehicle 2nd offense','Motor Vehicle: crossing property to avoid traffic signal','Motor Vehicle: Person hanging on or protruding from a Motor Vehicle','No marijuana where smoking is prohibited | General Law - Part I, Title XV, Chapter 94G, Section 13','Noise Ordinance 1st Violation | 259-12(.1,.2,.3)','Noise Ordinance 2nd Violation | 259-12(.1,.2,.3)','Noise Ordinance 3rd Violation | 259-12(.1,.2,.3)','Noise: Landlord allowing repeated noise violations 3rd violation in 12 months','Noise: Landlord allwoing repeated noise violations susequent vilations in 12 months','Noise: Refusing to give true information regarding noise complaint','Nuisance Animal/Barking Dog 1st | 110-6(.1,.2,.3)','Nuisance Animal/Barking Dog 2nd | 110-6(.1,.2,.3)','Open Container of Alcohol in Public | 275-2','Operating a mule, donkey, llama, cow, or other .... without a permit','Operator violations of conduct rules 1st | 390-27.1','Operator violations of conduct rules 2nd | 390-27.2','Other','Overgrowth','Overgrowth Occupied','Overgrowth Vacant Lot','Owner allowing operation w/out a chauffeur lic. 2nd | 390-14.2','Owner allowing operation w/out a chauffeur lic. ist | 390-14.1','Paint Ball / BB gun violations','Panhandling (if non-aggressive check for charitable permit violation)','Parking Motor Vehicle on lawn or landscape area','Parks: Depositing outside waste in Park Department waste receptacles','Parks: Depositing yard waste, leaves on Park Department property','Parks: Littering Park Department maintained property','Refrigerator or Stove stored improperly','Shopping cart on public property after notice','Sidewalk/tree belt/street obstructions | 338','Signs or Handbills, posting in public places','Skateboarding violation 2nd and subsequent offenses','Snow & Ice Removal Violations | 322','Solid Waste: Bulk items left on tree belt','Solid Waste: Leaves and yard waste collection violation','Solid Waste: Materials placed for pickup improperly','Solid Waste: Recycling collection violation','Solid Waste: Removing compostable materials left for pickup','Tag sale without permit','Taxi/Livery operating when Medallion Suspended','Taxi/Livery operation without Medallion','Taxi/Livery Using horn to summon fare','Taxi/Livery Vehicle Appearance Violations','Transient Vendors','Trash pickup violations | 327-7','Trees, Cutting or injuring public tree','Trees, Cutting/removing significant tree over 75 yrs old or 36" diameter','Unregistered motor vehicle on lot 12 days | 327-14','Valet parking rules violations','Viol. of Emergency Parking Ban (snow & ice) | 385.10','Violation of conditions of special permit (bldg. inspectors)','Violation of Parking Rules & Regulations | 1-25-PR','Violation of Permit Parking | 385.39','Zoning Ordinance Violations | 1-25-ZO'];

//Complant Sources
//const items = ['Baystate Gas Company','Building Department','Citizen','City Councillor','Civic Group / Council','Department of Children Services','DPW','Electrical Division','Fire Department','Health Department','Housing Department','Internet','Law Department','Mayors Office','MRVP','Other','Owner / Manager','Park Department','Plumbing Division','Police Department','Proactive','Proactive CDBG','Tenant','WMECO','Zoning Division'];

//car brands
const items = ['Acura','Alfa Romeo','Aston Martin','Audi','Bentley','BMW','Bugatti','Buick','BYD','Cadillac','Chevrolet','Chrysler','Dodge','Ferrari','Fiat','Ford','Genesis','GMC','Honda','Hummer','Hyundai','Infiniti','Jaguar','Jeep','Kia','Lamborghini','Land Rover','Lexus','Lincoln','Lucid','Maserati','Mazda','McLaren','Mercedes-Benz','MINI','Mitsubishi','Nissan','Polestar','Porsche','RAM','Rivian','Rolls-Royce','Subaru','Tesla','Toyota','Volkswagen','Volvo','Zeekr'];

//car models
//const items = ['Accord','Altima','Armada','Ascent','Atlas','A4','A6','Avalon','Aviator','Blazer','Bolt','Bronco','Camry','Canyon','Challenger','Charger','Cherokee','Civic','Colorado','Compass','Corolla','Corvette','CR-V','Crosstrek','CX-30','CX-5','CX-50','Defender','Durango','Edge','Elantra','Enclave','Encore','Envision','Equinox','Escalade','Escape','Expedition','Explorer','F-150','Forester','Forte','Frontier','Fusion','Gladiator','Golf','Grand Cherokee','Grand Wagoneer','Highlander','HR-V','Impala','Impreza','Jetta','Journey','K5','Kona','Malibu','Maverick','MDX','Model 3','Model S','Model X','Model Y','Murano','Mustang','Odyssey','Outback','Pacifica','Palisade','Passport','Pathfinder','Pilot','Q3','Q5','Q7','QX50','QX60','RAV4','Renegade','Ridgeline','Rogue','RX','Santa Cruz','Santa Fe','Seltos','Sentra','Sequoia','Sierra','Silverado','Sonata','Sorento','Soul','Sportage','Suburban','Tacoma','Tahoe','Telluride','Terrain','Tiguan','Titan','Trailblazer','Traverse','Tundra','Tucson','UX','Veloster','Venue','Versa','Wagoneer','Wrangler','XT4','XT5','XT6','Yukon'];

// //car colors
//const items = ['Beige','Black','Blue','Bronze','Brown','Burgundy','Charcoal','Copper','Cream','Gold','Gray','Green','Maroon','Orange','Pink','Purple','Red','Silver','Tan','Teal','White','Yellow'];

//Plumbing Gas Enforcment
//const items = ["248CMR 10.07(8)(d)(f)  Illegal connection, PVC, ABS, cast iron","248 CMR 10.02(3)  No hot water","248 CMR 10.04(2)(a)2  Failing to call for inspection","1st offense-Non corrected violation","2nd offense-Non corrected violation","3rd offense-Non corrected violation","Serious life safety issue","Other","248 CMR 10.02(20) Structural integrity compromised","248 CMR 10.05(2) Improper pitch, drainage piping","248 CMR 10.05(3) Improper change of direction, drainage piping","248 CMR 10.05(17) Poor workmanship","248 CMR 10.08(2)(g) Running trap","248 CMR 10.08(3)(n) Connections to cleanouts prohibited","248 CMR 3.04(1) Materials/fixtures not product accepted","248 CMR 10.10(1)(c) Plumbing fixture installation not code compliant","248 CMR 10.10(8)(a)(b)(c) Clothes washing machine connection not code compliant","248 CMR 10.02(6) Minimum fixture requirement not met","248 CMR 1013(1)(a) No condensate neutralizer","248 CMR 10.14(2)(b) Pressure absorbing devices not installed","248 CMR 10.14(5)(f) no/improper runoff tube on water heater relief valve","248 CMR 10.17(2)(6)(7) Ground water pump discharging into sanatary drainage system","248CMR 10.07(8)(d)(f)  Illegal connection, PVC, ABS, cast iron","248 CMR 10.02(3)  No hot water","248 CMR 10.04(2)(a)2  Failing to call for inspection","1st offense-Non corrected violation","2nd offense-Non corrected violation","3rd offense-Non corrected violation","Serious life safety issue","Other","248 CMR 10.02(20) Structural integrity compromised","248 CMR 10.05(2) Improper pitch, drainage piping","248 CMR 10.05(3) Improper change of direction, drainage piping","248 CMR 10.05(17) Poor workmanship","248 CMR 10.08(2)(g) Running trap","248 CMR 10.08(3)(n) Connections to cleanouts prohibited","248 CMR 3.04(1) Materials/fixtures not product accepted","248 CMR 10.10(1)(c) Plumbing fixture installation not code compliant","248 CMR 10.10(8)(a)(b)(c) Clothes washing machine connection not code compliant","248 CMR 10.02(6) Minimum fixture requirement not met","248 CMR 1013(1)(a) No condensate neutralizer","248 CMR 10.14(2)(b) Pressure absorbing devices not installed","248 CMR 10.14(5)(f) no/improper runoff tube on water heater relief valve","248 CMR 10.17(2)(6)(7) Ground water pump discharging into sanatary drainage system"];



const input = document.getElementById(":r1o9:");


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