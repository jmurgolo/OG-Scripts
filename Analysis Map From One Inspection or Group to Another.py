import re
from collections import defaultdict

def create_final_mappings(data_string: str) -> str:
    """
    Parses field data and creates grouped, chained mappings.

    This script:
    1. Handles {{ID}}-based fields from the input.
    2. Automatically generates sequential mappings for predefined text templates
       (e.g., "FIRST NOTICE" = "SECOND NOTICE").
    3. Applies special lookahead logic to place "next inspection" dates
       and times at the top of each group.

    Args:
        data_string: A multiline string containing the field data.

    Returns:
        A formatted string with all mappings grouped by sequential step.
    """
    # Clean the input of invisible characters
    cleaned_data = data_string.replace('\u200b', '')

    # This dictionary will only be populated from the input file
    mappings_from_file = defaultdict(list)
    line_regex = re.compile(r'\{\{+([A-Z0-9]+)\}\}+\s*=\s*(.*)')
    ordinals_set = {"First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"}

    # --- Data Parsing (processes only {{ID}} lines from the file) ---
    for line in cleaned_data.strip().split('\n'):
        match = line_regex.search(line.strip())
        if match:
            field_id = match.group(1)
            description = match.group(2).strip()
            words = description.split()
            normalized_words = [word for word in words if word.capitalize() not in ordinals_set]
            base_description = " ".join(normalized_words)
            mappings_from_file[base_description].append(field_id)

    # --- Define templates for automatic generation ---
    generated_templates = [
        "NOTICE OF VIOLATIONS",
        "VIOLATION TICKET",
        "NOTICE"
    ]

    # --- Generate the final grouped output ---
    output_lines = []
    ordinals_list_lower = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    ordinals_list_upper = [o.upper() for o in ordinals_list_lower]

    # Define the special base descriptions for the lookahead handling
    special_keys = {"Date of Inspection", "Time of Inspection"}

    # Loop for each transition step (e.g., first to second)
    for i in range(len(ordinals_list_lower) - 1):
        special_mappings = []
        regular_mappings = []
        generated_mappings = []

        # 1. Find date/time mappings from the *next* step to place at the top.
        lookahead_step_index = i + 1
        for key in sorted(special_keys):
            if key in mappings_from_file and len(mappings_from_file[key]) > lookahead_step_index + 1:
                ids = mappings_from_file[key]
                source_id = ids[lookahead_step_index]
                destination_id = ids[lookahead_step_index + 1]
                special_mappings.append(f"{source_id} = {destination_id}")

        # 2. Find all standard mappings for the *current* step from the input file.
        for base_description in sorted(mappings_from_file.keys()):
            ids = mappings_from_file[base_description]
            if len(ids) > i + 1:
                source_id = ids[i]
                destination_id = ids[i+1]
                regular_mappings.append(f"{source_id} = {destination_id}")

        # 3. Generate the plain text mappings from the templates.
        source_ordinal = ordinals_list_upper[i]
        dest_ordinal = ordinals_list_upper[i+1]
        for template in generated_templates:
            source_line = f"{source_ordinal} {template}"
            dest_line = f"{dest_ordinal} {template}"
            generated_mappings.append(f"{source_line} = {dest_line}")

        # 4. Combine all mappings for this group.
        all_group_mappings = special_mappings + regular_mappings + generated_mappings
        if all_group_mappings:
            if output_lines:
                output_lines.append("")
            output_lines.append(f"# {ordinals_list_lower[i]} to {ordinals_list_lower[i+1]}")
            output_lines.extend(all_group_mappings)

    return "\n".join(output_lines)

input_data = """
Form Details:
Usage
 {{FF1036837}}​ = Issued to Name
 {{FF1036838}}​ = Issued to Address
 {{FF1022400}}​ = Send to Court
 {{FF1022419}}​ = Usage Group
 {{FF1022420}}​ = Type of Construction
 {{FF1022421}}​ = Inspection Status
 {{FF1022422}}​ = Liquor License
 {{FF1033100}}​ = Residency Type
 {{FF1034630}}​ = Inspector
 {{FF1022425}}​ = Expiration Date
 {{FF1034628}}​ = Issue Date
 {{FF1034629}}​ = Inspection Date
Capacities
 {{{FF1022361}}}​ = Comments
 {{FF1022367}}​ = Number of Beds in Building
 {{FF1022368}}​ = Number of Units
 {{FF1022369}}​ = Total Persons
 {{FF1022370}}​ = Tables and Chairs
 {{FF1022371}}​ = Loose Chairs
 {{FF1022372}}​ = Standing
 {{FF1022373}}​ = Fixed Seating
 {{FF1022418}}​ = Bleachers Present
Additional Information
 {{FF1022410}}​ = Building Has Fire Escape(s)
 {{FF1022411}}​ = Building Has Ansel System
 {{FF1022412}}​ = Building Has Pressurized Stairways
 {{FF1022413}}​ = Building Has Generator
 {{FF1022414}}​ = Building Has Smoke Evac System
First Violations Inspection
 {{{FF1022363}}}​ = First Inspection Notes for Administrative Staff
 {{FF1022394}}​ = Matthew Goodchild
 {{FF1022395}}​ = Thomas Kennedy
 {{FF1022396}}​ = David Markham
 {{FF1022397}}​ = Abdul Mohammed
 {{FF1022398}}​ = George Shaw
 {{FF1038194}}​ = Chris Nunez
 {{FF1022417}}​ = First Inspection Result
 {{FF1022423}}​ = First Inspection Time
 {{FF1022430}}​ = First Inspection Date
Letters
 {{FF1022388}}​ = First Order to Repair
 {{FF1022389}}​ = Second Order to Repair
 {{FF1022390}}​ = First Violation Letter
 {{FF1022391}}​ = Second Violation Letter
 {{FF1022392}}​ = First Cease and Desist
 {{FF1022393}}​ = Second Cease and Desist
 {{FF1038198}}​ = Fourth Violation Letter
 {{FF1038199}}​ = Seventh Cease and Desist
 {{FF1038200}}​ = Fourth Cease and Desist
 {{FF1038201}}​ = Sixth Cease and Desist
 {{FF1038202}}​ = Tenth Cease and Desist
 {{FF1038203}}​ = Eighth Order to Repair
 {{FF1038204}}​ = Third Order to Repair
 {{FF1038205}}​ = Fifth Violation Letter
 {{FF1038206}}​ = Sixth Violation Letter
 {{FF1038207}}​ = Fifth Order to Repair
 {{FF1038208}}​ = Tenth Order to Repair
 {{FF1038209}}​ = Ninth Violation Letter
 {{FF1038210}}​ = Tenth Violation Letter
 {{FF1038211}}​ = Ninth Cease and Desist
 {{FF1038212}}​ = Fourth Order to Repair
 {{FF1038213}}​ = Sixth Order to Repair
 {{FF1038214}}​ = Seventh Order to Repair
 {{FF1038215}}​ = Third Violation Letter
 {{FF1038216}}​ = Ninth Order to Repair
 {{FF1038217}}​ = Seventh Violation Letter
 {{FF1038218}}​ = Eighth Violation Letter
 {{FF1038219}}​ = Third Cease and Desist
 {{FF1038220}}​ = Fifth Cease and Desist
 {{FF1038221}}​ = Eighth Cease and Desist
First Ticket Details
 {{{FF1022365}}}​ = First Ticket Notes for Administrative Staff
 {{FF1022366}}​ = First Ticket Total
 {{FF1022424}}​ = First Ticket Due Date
Second Violations Section
 {{{FF1038057}}}​ = Second Inspection Notes for Administrative Staff
 {{FF1038050}}​ = David Markham
 {{FF1038053}}​ = Thomas Kennedy
 {{FF1038055}}​ = Abdul Mohammed
 {{FF1038056}}​ = Chris Nunez
 {{FF1038060}}​ = Matthew Goodchild
 {{FF1038061}}​ = George Shaw
 {{FF1038063}}​ = Schedule Second Inspection
 {{FF1038058}}​ = Second Inspection Time
 {{FF1038062}}​ = Second Inspection Result
 {{FF1038059}}​ = Second Inspection Date
Third Violations Section
 {{{FF1038066}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1038068}}​ = Schedule Third Inspection
 {{FF1038133}}​ = David Markham
 {{FF1038134}}​ = George Shaw
 {{FF1038140}}​ = Thomas Kennedy
 {{FF1038141}}​ = Chris Nunez
 {{FF1038143}}​ = Matthew Goodchild
 {{FF1038145}}​ = Abdul Mohammed
 {{FF1038065}}​ = Third Inspection Result
 {{FF1038146}}​ = Third Inspection Time
 {{FF1038148}}​ = Date of Third Inspection
Fourth Violations Section
 {{{FF1038051}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1038067}}​ = Schedule Fourth Inspection
 {{FF1038070}}​ = Chris Nunez
 {{FF1038072}}​ = Matthew Goodchild
 {{FF1038073}}​ = Thomas Kennedy
 {{FF1038074}}​ = David Markham
 {{FF1038075}}​ = Abdul Mohammed
 {{FF1038149}}​ = George Shaw
 {{FF1038071}}​ = Fourth Inspection Result
 {{FF1038150}}​ = Time of Fourth Inspection
 {{FF1038069}}​ = Date of Fourth Inspection
Fifth Violations Section
 {{{FF1038086}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1038076}}​ = Schedule Fifth Inspection
 {{FF1038079}}​ = David Markham
 {{FF1038080}}​ = Abdul Mohammed
 {{FF1038082}}​ = Thomas Kennedy
 {{FF1038083}}​ = George Shaw
 {{FF1038084}}​ = Chris Nunez
 {{FF1038155}}​ = Matthew Goodchild
 {{FF1038078}}​ = Time of Fifth Inspection
 {{FF1038085}}​ = Fifth Inspection Result
 {{FF1038077}}​ = Date of Fifth Inspection
Sixth Violations Section
 {{{FF1038156}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1038091}}​ = Schedule Sixth Inspection
 {{FF1038092}}​ = George Shaw
 {{FF1038093}}​ = Abdul Mohammed
 {{FF1038094}}​ = Thomas Kennedy
 {{FF1038095}}​ = Chris Nunez
 {{FF1038151}}​ = David Markham
 {{FF1038162}}​ = Matthew Goodchild
 {{FF1038081}}​ = Time of Sixth Inspection
 {{FF1038096}}​ = Sixth Inspection Result
 {{FF1038161}}​ = Date of Sixth Inspection
Seventh Violations Section
 {{{FF1038107}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1038088}}​ = David Markham
 {{FF1038098}}​ = Chris Nunez
 {{FF1038099}}​ = George Shaw
 {{FF1038103}}​ = Abdul Mohammed
 {{FF1038105}}​ = Time of Seventh Inspection
 {{FF1038106}}​ = Thomas Kennedy
 {{FF1038183}}​ = Schedule Seventh Inspection
 {{FF1038102}}​ = Time of Seventh Inspection
 {{FF1038104}}​ = Seventh Inspection Result
 {{FF1038097}}​ = Date of Seventh Inspection
Eighth Violations Section
 {{{FF1038087}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1038090}}​ = Abdul Mohammed
 {{FF1038108}}​ = Schedule Eighth Inspection
 {{FF1038109}}​ = George Shaw
 {{FF1038110}}​ = Thomas Kennedy
 {{FF1038111}}​ = Chris Nunez
 {{FF1038153}}​ = David Markham
 {{FF1038163}}​ = Matthew Goodchild
 {{FF1038100}}​ = Time of Eighth Inspection
 {{FF1038157}}​ = Eighth Inspection Result
 {{FF1038101}}​ = Date of Eighth Inspection
Ninth Violations Section
 {{{FF1038124}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1038112}}​ = Schedule Ninth Inspection
 {{FF1038118}}​ = Matthew Goodchild
 {{FF1038122}}​ = Thomas Kennedy
 {{FF1038123}}​ = Abdul Mohammed
 {{FF1038154}}​ = David Markham
 {{FF1038158}}​ = Chris Nunez
 {{FF1038159}}​ = George Shaw
 {{FF1038119}}​ = Ninth Inspection Result
 {{FF1038121}}​ = Date of Ninth Inspection
 {{FF1038117}}​ = Time of Ninth Inspection
Tenth Violations Section
 {{{FF1038128}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1038114}}​ = David Markham
 {{FF1038115}}​ = Abdul Mohammed
 {{FF1038120}}​ = Schedule Tenth Inspection
 {{FF1038126}}​ = Matthew Goodchild
 {{FF1038127}}​ = Thomas Kennedy
 {{FF1038129}}​ = Chris Nunez
 {{FF1038130}}​ = George Shaw
 {{FF1038116}}​ = Tenth Inspection Result
 {{FF1038164}}​ = Time of Tenth Inspection
 {{FF1038113}}​ = Date of Tenth Inspection
Second Ticket Details
 {{{FF1038166}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1038131}}​ = Second Ticket Total
 {{FF1038132}}​ = Second Ticket Due Date
Third Ticket Details
 {{{FF1038144}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1038139}}​ = Third Ticket Total
 {{FF1038142}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{{FF1038168}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1038167}}​ = Fourth Ticket Total
 {{FF1038165}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{{FF1038172}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1038171}}​ = Fifth Ticket Total
 {{FF1038173}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{{FF1038176}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1038174}}​ = Sixth Ticket Total
 {{FF1038175}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{{FF1038177}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1038170}}​ = Seventh Ticket Total
 {{FF1038179}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{{FF1038178}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1038181}}​ = Eighth Ticket Total
 {{FF1038169}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{{FF1038182}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1038180}}​ = Ninth Ticket Total
 {{FF1038136}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{{FF1038138}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1038137}}​ = Tenth Ticket Total
 {{FF1038135}}​ = Tenth Ticket Due Date


Occupancy
 {{{OL1022352}}}​ = Floor Number
 {{{OL1022353}}}​ = Number of Rooms Per Floor
 {{{OL1022354}}}​ = Number of Units Per Floor
 {{{OL1022355}}}​ = Number of Beds Per Floor
 {{{OL1022356}}}​ = Number of Persons Per Floor
 {{{OL1022432}}}​ = Date
Fire Detection
 {{{OL1022357}}}​ = Floor Number
 {{{OL1022381}}}​ = Current Test
 {{{OL1022382}}}​ = Monitored
 {{{OL1022383}}}​ = Smoke
 {{{OL1022384}}}​ = Pulls
 {{{OL1022385}}}​ = Carbon Monoxide
 {{{OL1022386}}}​ = Heat
 {{{OL1022387}}}​ = Horn-Strobe
 {{{OL1022426}}}​ = Date
Fire Suppression
 {{{OL1022358}}}​ = Floor Number
 {{{OL1022374}}}​ = Current Test
 {{{OL1022375}}}​ = Monitored
 {{{OL1022376}}}​ = Sprinkler Wet
 {{{OL1022377}}}​ = Sprinkler Dry
 {{{OL1022378}}}​ = Chemical
 {{{OL1022379}}}​ = Kitchen Hood
 {{{OL1022380}}}​ = Fire Extinguishers
 {{{OL1022427}}}​ = Date
Means of Egress
 {{{OL1022359}}}​ = Floor Number
 {{{OL1022360}}}​ = Number of Exits
 {{{OL1022399}}}​ = Illuminated Exit Signs
 {{{OL1022401}}}​ = Emergency Lighting
 {{{OL1022402}}}​ = Front
 {{{OL1022403}}}​ = Rear
 {{{OL1022404}}}​ = Side
 {{{OL1022405}}}​ = Fire Escapes
 {{{OL1022415}}}​ = Type Lighting
 {{{OL1022428}}}​ = Date
 {{{OL1022433}}}​ = Certification Date
Handicap Access
 {{{OL1022406}}}​ = Building
 {{{OL1022407}}}​ = Bathrooms
 {{{OL1022408}}}​ = Elevators
 {{{OL1022409}}}​ = Signage
 {{{OL1022431}}}​ = Date
Violations
 {{{OL1022362}}}​ = Description
 {{{OL1022416}}}​ = Status
 {{{OL1022429}}}​ = Corrections Required By
 {{{OL1022435}}}​ = Picture
First Ticket
 {{{OL1022364}}}​ = First Ticket Description
Second Ticket
 {{{OL1038185}}}​ = Second Ticket Description
Third Ticket
 {{{OL1038186}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1038187}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1038188}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1038189}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1038190}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1038191}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1038192}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1038193}}}​ = Tenth Ticket Description

 {{{MES1012108}}}​ = Occupancy
 {{{MES1012109}}}​ = Fire Detection
 {{{MES1012110}}}​ = Fire Suppression
 {{{MES1012111}}}​ = Means of Egress
 {{{MES1012112}}}​ = Handicap Access
 {{{MES1012114}}}​ = Violations
 {{{MES1012117}}}​ = First Ticket
 {{{MES1013523}}}​ = Second Ticket
 {{{MES1013525}}}​ = Third Ticket
 {{{MES1013527}}}​ = Fourth Ticket
 {{{MES1013529}}}​ = Fifth Ticket
 {{{MES1013531}}}​ = Sixth Ticket
 {{{MES1013533}}}​ = Seventh Ticket
 {{{MES1013535}}}​ = Eighth Ticket
 {{{MES1013537}}}​ = Ninth Ticket
 {{{MES1013539}}}​ = Tenth Ticket

Fees:
 {{FEE473}}​ = Assembly - Theaters Capacity 400 or greater
 {{FEE474}}​ = Assembly - Theaters Capacity 400 or fewer: Stage & Scenery
 {{FEE475}}​ = Assembly - Theaters Capacity 400 or fewer: Movie
 {{FEE476}}​ = Assembly - Night Clubs or Similar >400
 {{FEE477}}​ = Assembly - Night Clubs or Similar <400
 {{FEE478}}​ = Assembly - Lecture Hall, Rec.Center Terminal >400
 {{FEE479}}​ = Assembly - Lecture Hall, Rec.Center Terminal <400
 {{FEE480}}​ = Assembly - Stadiums, Bleachers
 {{FEE481}}​ = Educational
 {{FEE482}}​ = Day Care
 {{FEE483}}​ = Institutional - Hospital Care
 {{FEE484}}​ = Institutional - Restrained
 {{FEE485}}​ = Institutional - Residential
 {{FEE486}}​ = Residential - Multi-family
 {{FEE487}}​ = Residential Special - Detox
 {{FEE488}}​ = Residential Special - Summer Camp
 {{FEE489}}​ = Residential Special - Group
 {{FEE490}}​ = Residential Special - Limited
 {{FEE491}}​ = Re-Insepction After Third Inspection
 {{FEE492}}​ = Assembly- Place of Religious Assembly
 {{totalPaid}}​ = Total of all payments for the Record

Organization/Document Details:
 {{orgName}}​ = Organization Name
 {{orgLogoURL}}​ = Logo URL
 {{docTitle}}​ = Document's Title
 {{issuedByUserName}}​ = Issuing User’s Name

Record Details:
 {{recordId}}​ = Record's ID number
 {{recordType}}​ = Type of Record
 {{renewalNo}}​ = Record's renewal number
 {{dateSubmitted}}​ = Date the Record was submitted
 {{permitLicenseIssuedDate}}​ = Date the record's first permit or license was issued

Project Details:
 {{projectId}}​ = Project ID
 {{projectName}}​ = Project Name

Applicant Details:
 {{applicantFirstName}}​ = Applicant's First Name
 {{applicantLastName}}​ = Applicant's Last Name
 {{applicantEmail}}​ = Applicant's Email Address
 {{applicantPhoneNo}}​ = Applicant's Phone Number
 {{applicantStreet}}​ = Applicant's Street Address
 {{applicantCity}}​ = Applicant's City
 {{applicantState}}​ = Applicant's State
 {{applicantZip}}​ = Applicant's Zip Code
 {{applicantAddress2}}​ = Applicant's Address 2

Address Details:
 {{streetNo}}​ = streetNo
 {{streetName}}​ = streetName
 {{unit}}​ = unit
 {{city}}​ = city
 {{state}}​ = state
 {{zipCode}}​ = zip code

Owner Details:
 {{ownerName}}​ = Owner's Name
 {{ownerStreetNo}}​ = Owner's Street No.
 {{ownerStreetName}}​ = Owner's Street Name
 {{ownerCity}}​ = Owner's City
 {{ownerState}}​ = Owner's State
 {{ownerZipCode}}​ = Owner's Zip Code
 {{ownerUnit}}​ = Owner's Address Unit
 {{ownerPhoneNo}}​ = Owner's Phone Number
 {{ownerEmail}}​ = Owner's Email Address

Property Details:
 {{bookPage}}​ = Book Page
 {{yearBuilt}}​ = Year Built
 {{mbl}}​ = MBL
 {{zoning}}​ = Zoning
 {{lotArea}}​ = Lot Area
 {{propertyUse}}​ = Property Use
 {{occupancy}}​ = Occupancy
 {{buildingType}}​ = Building Type
 {{water}}​ = Water
 {{sewage}}​ = Sewage
 {{subdivision}}​ = subdivision

Today's Date:
 {{currentDay}}​ = day
 {{currentMonth}}​ = month
 {{currentYear}}​ = year
 {{currentYY}}​ = year (2 digits. E.g. 15)
 {{currentDate}}​ = full date (MMMM DD, YYYY)

Expiration Date:
 {{expirationDate}}​ = Document's Expiration Date

Segment Location Details:
 {{latitude}}​ = Segment Start Point Latitude
 {{longitude}}​ = Segment Start Point Longitude
 {{secondaryLatitude}}​ = Segment End Point Latitude
 {{secondaryLongitude}}​ = Segment End Point Longitude
 {{segmentPrimaryLabel}}​ = Segment Starting Location (Geocoded Location)
 {{segmentSecondaryLabel}}​ = Segment Ending Location (Geocoded Location)
 {{segmentLabel}}​ = Segment Label (Start Street - End Street)

Primary Location:
 {{primaryLocation}}​ = Record Primary Location

Additional Location:
 {{additionalLocations}}​ = Record Additional Locations

Template Step Assignments Details:
 {{assignedToTS964}}​ = 30 Day Notice to Schedule Inspection
 {{assignedToTS963}}​ = Send 30 Day Notice
 {{assignedToTS954}}​ = Notice to Schedule Inspection 14 Day Notice
 {{assignedToTS956}}​ = Inspection
 {{assignedToTS966}}​ = 14 Day Notice to Schedule Inspection
 {{assignedToTS957}}​ = Certificate of Inspection Issued
 {{assignedToTS965}}​ = Send 14 Day Notice
 {{assignedToTS969}}​ = First Order to Repair Letter
 {{assignedToTS973}}​ = Cease and Desist
 {{assignedToTS967}}​ = First Order to Repair
 {{assignedToTS2000}}​ = First Violation Letter
 {{assignedToTS970}}​ = Approve First Ticket
 {{assignedToTS971}}​ = First Ticket
 {{assignedToTS972}}​ = Send to Court
 {{assignedToTS1997}}​ = Owes Fees
 {{assignedToTS1999}}​ = Approve Fees
 {{assignedToTS959}}​ = Add Fees
 {{assignedToTS953}}​ = Inspections
 {{assignedToTS1998}}​ = Draft Certificate of Inspection
 {{assignedToTS2003}}​ = Draft Certificate of Inspection
 {{assignedToTS960}}​ = Send Certificates of Inspection
 {{assignedToTS955}}​ = Certificate of Inspection Multifamily Issued
 {{assignedToTS961}}​ = Certificate of Inspection Other than Multifamily Issued
 {{assignedToTS958}}​ = Fire Approval
 {{assignedToTS2004}}​ = Draft Certificate of Inspection for Liquor License
 {{assignedToTS2005}}​ = Draft Certificate of Inspection for Liquor License Issued
 {{assignedToTS2006}}​ = Certificate of Inspection for Liquor License
 {{assignedToTS962}}​ = Certificate of Inspection for Liquor License Issued
"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
