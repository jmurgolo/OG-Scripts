#change alternative owner name and address to first owner name and address
#remove multienty violation sections

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
        "NOTICE",
        "STOP WORK NOTICE"
    ]

    # --- Generate the final grouped output ---
    output_lines = []
    ordinals_list_lower = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    ordinals_list_upper = [o.upper() for o in ordinals_list_lower]

    # Define the special base descriptions for the lookahead handling
    special_keys = {"Date of Inspection", "Time of Inspection","Inspection Date","Inspection Time"}

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

First Inspection
 {{{FF1026255}}}​ = First Inspection Notes For Administrative Staff
 {{FF1026471}}​ = Matthew Goodchild
 {{FF1026472}}​ = Thomas Kennedy
 {{FF1026473}}​ = David Markham
 {{FF1026474}}​ = Abdul Mohammed
 {{FF1026475}}​ = George Shaw
 {{FF1026476}}​ = Donald Zdunczyk
 {{FF1026477}}​ = Condemnation
 {{FF1026478}}​ = Court
 {{FF1026479}}​ = Emergency
 {{FF1026480}}​ = Inspection
 {{FF1037943}}​ = Chris Nunez
 {{FF1026482}}​ = First Inspection Result
 {{FF1026488}}​ = First Inspection Time
 {{FF1026540}}​ = Date of First Inspection
Second Inspection
 {{{FF1026256}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1026443}}​ = Matthew Goodchild
 {{FF1026444}}​ = Thomas Kennedy
 {{FF1026445}}​ = David Markham
 {{FF1026446}}​ = Abdul Mohammed
 {{FF1026447}}​ = George Shaw
 {{FF1026448}}​ = Donald Zdunczyk
 {{FF1026449}}​ = Schedule Second Inspection
 {{FF1026450}}​ = Condemnation
 {{FF1026451}}​ = Court
 {{FF1026452}}​ = Emergency
 {{FF1026453}}​ = Inspection
 {{FF1037944}}​ = Chris Nunez
 {{FF1026489}}​ = Second Inspection Result
 {{FF1026490}}​ = Time of Second Inspection
 {{FF1026536}}​ = Date of Second Inspection
Third Inspection
 {{{FF1026274}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1026442}}​ = Schedule Third Inspection
 {{FF1026454}}​ = Court
 {{FF1026455}}​ = Condemnation
 {{FF1026456}}​ = Emergency
 {{FF1026457}}​ = Inspection
 {{FF1026458}}​ = Matthew Goodchild
 {{FF1026459}}​ = Thomas Kennedy
 {{FF1026460}}​ = David Markham
 {{FF1026461}}​ = Abdul Mohammed
 {{FF1026462}}​ = George Shaw
 {{FF1026463}}​ = Donald Zdunczyk
 {{FF1037942}}​ = Chris Nunez
 {{FF1026486}}​ = Third Inspection Result
 {{FF1026487}}​ = Time of Third Inspection
 {{FF1026537}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1026275}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1026408}}​ = Schedule Fourth Inspection
 {{FF1026409}}​ = Matthew Goodchild
 {{FF1026410}}​ = Thomas Kennedy
 {{FF1026411}}​ = David Markham
 {{FF1026412}}​ = Abdul Mohammed
 {{FF1026413}}​ = George Shaw
 {{FF1026414}}​ = Donald Zdunczyk
 {{FF1026464}}​ = Condemnation
 {{FF1026465}}​ = Court
 {{FF1026466}}​ = Emergency
 {{FF1026467}}​ = Inspection
 {{FF1037945}}​ = Chris Nunez
 {{FF1026493}}​ = Fourth Inspection Result
 {{FF1026494}}​ = Time of Fourth Inspection
 {{FF1026532}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1026276}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1026387}}​ = Matthew Goodchild
 {{FF1026388}}​ = Thomas Kennedy
 {{FF1026389}}​ = David Markham
 {{FF1026390}}​ = Abdul Mohammed
 {{FF1026391}}​ = George Shaw
 {{FF1026392}}​ = Chris Nunez
 {{FF1026403}}​ = Schedule Fifth Inspection
 {{FF1026404}}​ = Condemnation
 {{FF1026405}}​ = Court
 {{FF1026406}}​ = Emergency
 {{FF1026407}}​ = Inspection
 {{FF1026496}}​ = Fifth Inspection Result
 {{FF1026497}}​ = Time of Fifth Inspection
 {{FF1026533}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1026277}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1026386}}​ = Schedule Sixth inspection
 {{FF1026393}}​ = Condemnation
 {{FF1026394}}​ = Court
 {{FF1026395}}​ = Emergency
 {{FF1026396}}​ = Inspection
 {{FF1026397}}​ = David Markham
 {{FF1026398}}​ = Matthew Goodchild
 {{FF1026399}}​ = Thomas Kennedy
 {{FF1026400}}​ = Abdul Mohammed
 {{FF1026401}}​ = George Shaw
 {{FF1026402}}​ = Donald Zdunczyk
 {{FF1037946}}​ = Chris Nunez
 {{FF1026495}}​ = Sixth Inspection Result
 {{FF1026500}}​ = Time of Sixth Inspection
 {{FF1026530}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1026278}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1026375}}​ = Schedule Seventh inspection
 {{FF1026376}}​ = Condemnation
 {{FF1026377}}​ = Court
 {{FF1026378}}​ = Emergency
 {{FF1026379}}​ = Inspection
 {{FF1026380}}​ = Matthew Goodchild
 {{FF1026381}}​ = Thomas Kennedy
 {{FF1026382}}​ = David Markham
 {{FF1026383}}​ = Abdul Mohammed
 {{FF1026384}}​ = George Shaw
 {{FF1026385}}​ = Donald Zdunczyk
 {{FF1037949}}​ = Chris Nunez
 {{FF1026498}}​ = Seventh Inspection Result
 {{FF1026499}}​ = Time of Seventh Inspection
 {{FF1026531}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1026279}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1026360}}​ = Schedule Eighth inspection
 {{FF1026361}}​ = Condemnation
 {{FF1026362}}​ = Court
 {{FF1026363}}​ = Emergency
 {{FF1026364}}​ = Inspection
 {{FF1026365}}​ = Matthew Goodchild
 {{FF1026366}}​ = Thomas Kennedy
 {{FF1026367}}​ = David Markham
 {{FF1026368}}​ = Abdul Mohammed
 {{FF1026369}}​ = George Shaw
 {{FF1037947}}​ = Chris Nunez
 {{FF1026501}}​ = Eighth Inspection Result
 {{FF1026502}}​ = Time of Eighth Inspection
 {{FF1026528}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1026280}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1026313}}​ = Schedule Ninth inspection
 {{FF1026314}}​ = Matthew Goodchild
 {{FF1026315}}​ = Thomas Kennedy
 {{FF1026316}}​ = David Markham
 {{FF1026317}}​ = Abdul Mohammed
 {{FF1026318}}​ = George Shaw
 {{FF1026371}}​ = Condemnation
 {{FF1026372}}​ = Court
 {{FF1026373}}​ = Emergency
 {{FF1026374}}​ = Inspection
 {{FF1037950}}​ = Chris Nunez
 {{FF1026503}}​ = Ninth Inspection Result
 {{FF1026504}}​ = Time of Ninth Inspection
 {{FF1026529}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1026281}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1026292}}​ = Matthew Goodchild
 {{FF1026293}}​ = Thomas Kennedy
 {{FF1026294}}​ = David Markham
 {{FF1026295}}​ = Abdul Mohammed
 {{FF1026296}}​ = George Shaw
 {{FF1026308}}​ = Schedule Tenth inspection
 {{FF1026309}}​ = Condemnation
 {{FF1026310}}​ = Court
 {{FF1026311}}​ = Emergency
 {{FF1026312}}​ = Inspection
 {{FF1037948}}​ = Chris Nunez
 {{FF1026505}}​ = Tenth Inspection Result
 {{FF1026507}}​ = Time of Tenth Inspection
 {{FF1026520}}​ = Date of Tenth Inspection
Letters
 {{FF1026298}}​ = Send First Violation Letters
 {{FF1026299}}​ = Send Second Violation Letters
 {{FF1026300}}​ = Send Third Violation Letters
 {{FF1026301}}​ = Send Fourth Violation Letters
 {{FF1026302}}​ = Send Fifth Violation Letters
 {{FF1026303}}​ = Send Sixth Violation Letters
 {{FF1026304}}​ = Send Seventh Violation Letters
 {{FF1026305}}​ = Send Eighth Violation Letters
 {{FF1026306}}​ = Send Ninth Violation Letters
 {{FF1026307}}​ = Send Tenth Violation Letters
 {{FF1026320}}​ = Send First Cease and Desist Letter
 {{FF1026321}}​ = Send Second Cease and Desist Letter
 {{FF1026322}}​ = Send Third Cease and Desist Letter
 {{FF1026323}}​ = Send Fourth Cease and Desist Letter
 {{FF1026324}}​ = Send Fifth Cease and Desist Letter
 {{FF1026325}}​ = Send Sixth Cease and Desist Letter
 {{FF1026326}}​ = Send Seventh Cease and Desist Letter
 {{FF1026327}}​ = Send Eighth Cease and Desist Letter
 {{FF1026328}}​ = Send Ninth Cease and Desist Letter
 {{FF1026329}}​ = Send Tenth Cease and Desist Letter
 {{FF1026330}}​ = Send First Access Demand
 {{FF1026331}}​ = Send Second Access Demand
 {{FF1026332}}​ = Send Third Access Demand
 {{FF1026333}}​ = Send Fourth Access Demand
 {{FF1026334}}​ = Send Fifth Access Demand
 {{FF1026335}}​ = Send Sixth Access Demand
 {{FF1026336}}​ = Send Seventh Access Demand
 {{FF1026337}}​ = Send Eighth Access Demand
 {{FF1026338}}​ = Send Ninth Access Demand
 {{FF1026339}}​ = Send Tenth Access Demand
 {{FF1026340}}​ = First Stop Work Letter
 {{FF1026341}}​ = Second Stop Work Letter
 {{FF1026342}}​ = Third Stop Work Letter
 {{FF1026343}}​ = Fourth Stop Work Letter
 {{FF1026344}}​ = Fifth Stop Work Letter
 {{FF1026345}}​ = Sixth Stop Work Letter
 {{FF1026346}}​ = Seventh Stop Work Letter
 {{FF1026347}}​ = Eighth Stop Work Letter
 {{FF1026348}}​ = Ninth Stop Work Letter
 {{FF1026349}}​ = Tenth Stop Work Letter
 {{FF1026350}}​ = First Order to Vacate Letter
 {{FF1026351}}​ = Second Order to Vacate Letter
 {{FF1026352}}​ = Third Order to Vacate Letter
 {{FF1026353}}​ = Fourth Order to Vacate Letter
 {{FF1026354}}​ = Fifth Order to Vacate Letter
 {{FF1026355}}​ = Sixth Order to Vacate Letter
 {{FF1026356}}​ = Seventh Order to Vacate Letter
 {{FF1026357}}​ = Eighth Order to Vacate Letter
 {{FF1026358}}​ = Ninth Order to Vacate Letter
 {{FF1026359}}​ = Tenth Order to Vacate Letter
First Ticket Details
 {{FF1026233}}​ = Person whose name will appear on ticket
 {{{FF1026252}}}​ = First Ticket Notes for Administrative Staff
 {{FF1026282}}​ = First Ticket Total
 {{FF1026518}}​ = First Ticket Due Date
Second Ticket Details
 {{FF1026234}}​ = Person whose name will appear on ticket
 {{{FF1026251}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1026284}}​ = Second Ticket Total
 {{FF1026521}}​ = Second Ticket Due Date
Third Ticket Details
 {{FF1026235}}​ = Person whose name will appear on ticket
 {{{FF1026250}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1026285}}​ = Third Ticket Total
 {{FF1026517}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{FF1026236}}​ = Person whose name will appear on ticket
 {{{FF1026249}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1026283}}​ = Fourth Ticket Total
 {{FF1026519}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{FF1026237}}​ = Person whose name will appear on ticket
 {{{FF1026248}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1026286}}​ = Fifth Ticket Total
 {{FF1026522}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{FF1026238}}​ = Person whose name will appear on ticket
 {{{FF1026247}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1026287}}​ = Sixth Ticket Total
 {{FF1026523}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{FF1026239}}​ = Person whose name will appear on ticket
 {{{FF1026246}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1026288}}​ = Seventh Ticket Total
 {{FF1026524}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{FF1026240}}​ = Person whose name will appear on ticket
 {{{FF1026245}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1026289}}​ = Eighth Ticket Total
 {{FF1026525}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{FF1026241}}​ = Person whose name will appear on ticket
 {{{FF1026244}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1026290}}​ = Ninth Ticket Total
 {{FF1026526}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{FF1026242}}​ = Person whose name will appear on ticket
 {{{FF1026243}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1026291}}​ = Tenth Ticket Total
 {{FF1026527}}​ = Tenth Ticket Due Date

Parties Responsible for Online Payment
 {{{OL1026232}}}​ = Email Address
First Ticket
 {{{OL1026506}}}​ = First Ticket Description
Second Ticket
 {{{OL1026515}}}​ = Second Ticket Description
Third Ticket
 {{{OL1026516}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1026514}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1026513}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1026512}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1026511}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1026510}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1026509}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1026508}}}​ = Tenth Ticket Description

Multi Entry Sections:
Please note that multiEntry sections are marked with three curly brackets, not two.


 {{{MES1012465}}}​ = Building Violations
 {{{MES1012466}}}​ = Certified Letters
 {{{MES1012467}}}​ = Emergency Violations
 {{{MES1012468}}}​ = Parties Responsible for Online Payment
 {{{MES1012479}}}​ = First Ticket
 {{{MES1012482}}}​ = Second Ticket
 {{{MES1012484}}}​ = Third Ticket
 {{{MES1012486}}}​ = Fourth Ticket
 {{{MES1012488}}}​ = Fifth Ticket
 {{{MES1012490}}}​ = Sixth Ticket
 {{{MES1012492}}}​ = Seventh Ticket
 {{{MES1012494}}}​ = Eighth Ticket
 {{{MES1012496}}}​ = Ninth Ticket
 {{{MES1012498}}}​ = Tenth Ticket

Fees:
 {{FEE509}}​ = Violation Fee
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
 {{assignedToTS1641}}​ = Send Out Record Letters
 {{assignedToTS1667}}​ = Condemnation Placard
 {{assignedToTS1668}}​ = 139B Letter
 {{assignedToTS1670}}​ = 186C Letter
 {{assignedToTS1642}}​ = Send Out First Inspection Letters
 {{assignedToTS1697}}​ = First Access Demand Letter
 {{assignedToTS1707}}​ = First Cease and Desist Letter
 {{assignedToTS1717}}​ = First Order to Vacate Letter
 {{assignedToTS1666}}​ = First Stop Work Letter
 {{assignedToTS1671}}​ = First Violation Letter
 {{assignedToTS1643}}​ = Approve First Ticket
 {{assignedToTS1669}}​ = First Ticket
 {{assignedToTS1623}}​ = Send Out Second Inspection Letters
 {{assignedToTS1672}}​ = Second Violation Letter
 {{assignedToTS1708}}​ = Second Cease and Desist Letter
 {{assignedToTS1696}}​ = Second Stop Work Letter
 {{assignedToTS1718}}​ = Second Order to Vacate Letter
 {{assignedToTS1698}}​ = Second Access Demand Letter
 {{assignedToTS1624}}​ = Approve Second Ticket
 {{assignedToTS1695}}​ = Second Ticket
 {{assignedToTS1625}}​ = Send Out Third Inspection Letters
 {{assignedToTS1673}}​ = Third Violation Letter Owner
 {{assignedToTS1709}}​ = Third Cease and Desist Letter
 {{assignedToTS1664}}​ = Third Stop Work Letter
 {{assignedToTS1719}}​ = Third Order to Vacate Letter
 {{assignedToTS1699}}​ = Third Access Demand Letter
 {{assignedToTS1633}}​ = Approve Third Ticket
 {{assignedToTS1665}}​ = Third Ticket
 {{assignedToTS1626}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS1674}}​ = Fourth Violation Letter Owner
 {{assignedToTS1710}}​ = Fourth Cease and Desist Letter
 {{assignedToTS1693}}​ = Fourth Stop Work Letter
 {{assignedToTS1720}}​ = Fourth Order to Vacate Letter
 {{assignedToTS1700}}​ = Fourth Access Demand Letter
 {{assignedToTS1634}}​ = Approve Fourth Ticket
 {{assignedToTS1694}}​ = Fourth Ticket
 {{assignedToTS1627}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS1675}}​ = Fifth Violation Letter Owner
 {{assignedToTS1711}}​ = Fifth Cease and Desist Letter
 {{assignedToTS1691}}​ = Fifth Stop Work Letter
 {{assignedToTS1721}}​ = Fifth Order to Vacate Letter
 {{assignedToTS1701}}​ = Fifth Access Demand Letter
 {{assignedToTS1635}}​ = Approve Fifth Ticket
 {{assignedToTS1692}}​ = Fifth Ticket
 {{assignedToTS1628}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS1676}}​ = Sixth Violation Letter Owner
 {{assignedToTS1712}}​ = Sixth Cease and Desist Letter
 {{assignedToTS1689}}​ = Sixth Stop Work Letter
 {{assignedToTS1722}}​ = Sixth Order to Vacate Letter
 {{assignedToTS1702}}​ = Sixth Access Demand Letter
 {{assignedToTS1636}}​ = Approve Sixth Ticket
 {{assignedToTS1690}}​ = Sixth Ticket
 {{assignedToTS1629}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS1677}}​ = Seventh Violation Letter Owner
 {{assignedToTS1713}}​ = Seventh Cease and Desist Letter
 {{assignedToTS1687}}​ = Seventh Stop Work Letter
 {{assignedToTS1723}}​ = Seventh Order to Vacate Letter
 {{assignedToTS1703}}​ = Seventh Access Demand Letter
 {{assignedToTS1637}}​ = Approve Seventh Ticket
 {{assignedToTS1688}}​ = Seventh Ticket
 {{assignedToTS1630}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS1678}}​ = Eighth Violation Letter Owner
 {{assignedToTS1714}}​ = Eighth Cease and Desist Letter
 {{assignedToTS1683}}​ = Eighth Stop Work Letter
 {{assignedToTS1724}}​ = Eighth Order to Vacate Letter
 {{assignedToTS1704}}​ = Eighth Access Demand Letter
 {{assignedToTS1638}}​ = Approve Eighth Ticket
 {{assignedToTS1686}}​ = Eighth Ticket
 {{assignedToTS1631}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS1679}}​ = Ninth Violation Letter Owner
 {{assignedToTS1715}}​ = Ninth Cease and Desist Letter
 {{assignedToTS1685}}​ = Ninth Stop Work Letter
 {{assignedToTS1725}}​ = Ninth Order to Vacate Letter
 {{assignedToTS1705}}​ = Ninth Access Demand Letter
 {{assignedToTS1639}}​ = Approve Ninth Ticket
 {{assignedToTS1684}}​ = Ninth Ticket
 {{assignedToTS1632}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS1680}}​ = Tenth Violation Letter Owner
 {{assignedToTS1716}}​ = Tenth Cease and Desist Letter
 {{assignedToTS1681}}​ = Tenth Stop Work Letter
 {{assignedToTS1726}}​ = Tenth Order to Vacate Letter
 {{assignedToTS1706}}​ = Tenth Access Demand Letter
 {{assignedToTS1640}}​ = Approve Tenth Ticket
 {{assignedToTS1682}}​ = Tenth Ticket
 {{assignedToTS1663}}​ = Tenth Inspection Date and Time
 {{assignedToTS1662}}​ = Ninth Inspection Date and Time
 {{assignedToTS1661}}​ = Eighth Inspection Date and Time
 {{assignedToTS1660}}​ = Seventh Inspection Date and Time
 {{assignedToTS1659}}​ = Sixth Inspection Date and Time
 {{assignedToTS1658}}​ = Fifth Inspection Date and Time
 {{assignedToTS1657}}​ = Fourth Inspection Date and Time
 {{assignedToTS1656}}​ = Third Inspection Date and Time
 {{assignedToTS1655}}​ = Second Inspection Date and Time
 {{assignedToTS1654}}​ = First Inspection Date and Time
 {{assignedToTS1644}}​ = Tenth Violation Fee
 {{assignedToTS1653}}​ = Ninth Violation Fee
 {{assignedToTS1652}}​ = Eighth Violation Fee
 {{assignedToTS1651}}​ = Seventh Violation Fee
 {{assignedToTS1650}}​ = Sixth Violation Fee
 {{assignedToTS1649}}​ = Fifth Violation Fee
 {{assignedToTS1648}}​ = Fourth Violation Fee
 {{assignedToTS1647}}​ = Third Violation Fee
 {{assignedToTS1646}}​ = Second Violation Fee
 {{assignedToTS1645}}​ = First Violation Fee
 {{assignedToTS1612}}​ = Refer to Court
 {{assignedToTS1615}}​ = Refer to Plumbing Enforcement
 {{assignedToTS1617}}​ = Refer to Animal Control
 {{assignedToTS1614}}​ = Refer to Electrical Enforcement
 {{assignedToTS1618}}​ = Refer to Police Ordinance
 {{assignedToTS1619}}​ = Refer to Health Department
 {{assignedToTS1613}}​ = Refer to Housing Enforcement
 {{assignedToTS1622}}​ = Refer to Zoning
 {{assignedToTS1621}}​ = Refer to Office of Housing
 {{assignedToTS1620}}​ = Refer to Elderly Affairs
 {{assignedToTS1616}}​ = Refer to Fire
"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
