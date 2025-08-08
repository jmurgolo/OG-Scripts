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
General Info
 {{FF1022992}}​ = Inspection Access Contact Name
 {{FF1022993}}​ = Inspection Access Contact Phone
 {{FF1022994}}​ = Inspection Access Contact Title
 {{FF1022996}}​ = Other Source
 {{FF1023004}}​ = When & how did you contact them
 {{FF1023005}}​ = Who did you contact
 {{FF1023007}}​ = Unit Number - to be printed on the inspection report
 {{FF1023010}}​ = Alternative Owner Name
 {{FF1023013}}​ = Second Owner Name
 {{FF1023016}}​ = Third Owner Name
 {{FF1023046}}​ = First Tenant Name
 {{FF1023047}}​ = First Tenant Unit
 {{FF1023049}}​ = Second Tenant Name
 {{FF1023050}}​ = Second Tenant Unit
 {{FF1023052}}​ = Third Tenant Name
 {{FF1023053}}​ = Third Tenant Unit
 {{FF1023055}}​ = Fourth Tenant Name
 {{FF1023056}}​ = Fourth Tenant Unit
 {{FF1023058}}​ = Fifth Tenant Name
 {{FF1023059}}​ = Fifth Tenant Unit
 {{FF1023061}}​ = Sixth Tenant Name
 {{FF1023062}}​ = Sixth Tenant Unit
 {{{FF1022990}}}​ = General Notes
 {{{FF1023006}}}​ = What was the response
 {{{FF1023011}}}​ = Alternative Owner Address
 {{{FF1023014}}}​ = Second Owner Address
 {{{FF1023017}}}​ = Third Owner Address
 {{{FF1023022}}}​ = Refer to Court Details
 {{{FF1023024}}}​ = Refer to Housing Enforcement Details
 {{{FF1023026}}}​ = Refer to Electrical Details
 {{{FF1023028}}}​ = Refer to Plumbing Details
 {{{FF1023030}}}​ = Refer to Fire Details
 {{{FF1023032}}}​ = Refer to Police Ordinance Details
 {{{FF1023034}}}​ = Refer to Health Department Details
 {{{FF1023036}}}​ = Refer to Elderly Affairs Details
 {{{FF1023038}}}​ = Refer to Animal Control Details
 {{{FF1023040}}}​ = Refer to Office of Housing Details
 {{{FF1023042}}}​ = Refer to Zoning Details
 {{FF1022997}}​ = Interior
 {{FF1022998}}​ = Exterior
 {{FF1022999}}​ = Referral
 {{FF1023003}}​ = Have you contacted the owner
 {{FF1023009}}​ = Owner Different than GIS
 {{FF1023012}}​ = Add Second Additional Owner
 {{FF1023015}}​ = Add Third Additional Owner
 {{FF1023019}}​ = Section 105 Required
 {{FF1023021}}​ = Refer to Court
 {{FF1023023}}​ = Refer to Housing Enforcement
 {{FF1023025}}​ = Refer to Electrical Enforcement
 {{FF1023027}}​ = Refer to Plumbing Enforcement
 {{FF1023029}}​ = Refer to Fire Department
 {{FF1023031}}​ = Refer to Police Ordinance
 {{FF1023033}}​ = Refer to Health Department
 {{FF1023035}}​ = Refer to Elderly Affairs
 {{FF1023037}}​ = Refer to Animal Control
 {{FF1023039}}​ = Refer to Office of Housing
 {{FF1023041}}​ = Refer to Zoning
 {{FF1023043}}​ = Add Parties Responsible for Payment
 {{FF1023045}}​ = First Tenant
 {{FF1023048}}​ = Second Tenant
 {{FF1023051}}​ = Third Tenant
 {{FF1023054}}​ = Fourth Tenant
 {{FF1023057}}​ = Fifth Tenant
 {{FF1023060}}​ = Sixth Tenant
 {{FF1022995}}​ = Complaint Source
 {{FF1023000}}​ = Usage Group
 {{FF1023001}}​ = When did the problem first occur
First Inspection
 {{{FF1023093}}}​ = First Inspection Notes For Administrative Staff
 {{FF1023081}}​ = Court
 {{FF1023082}}​ = Emergency
 {{FF1023083}}​ = Inspection
 {{FF1023088}}​ = Riccardo Bedinotti
 {{FF1023089}}​ = Aaron Cole
 {{FF1023090}}​ = Joseph Desmond
 {{FF1023091}}​ = Peter Nham
 {{FF1023086}}​ = First Inspection Time
 {{FF1023092}}​ = First Inspection Result
 {{FF1023085}}​ = Date of First Inspection
Second Inspection
 {{{FF1023108}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1023094}}​ = Schedule Second Inspection
 {{FF1023096}}​ = Court
 {{FF1023097}}​ = Emergency
 {{FF1023098}}​ = Inspection
 {{FF1023103}}​ = Riccardo Bedinotti
 {{FF1023104}}​ = Aaron Cole
 {{FF1023105}}​ = Joseph Desmond
 {{FF1023106}}​ = Peter Nham
 {{FF1023101}}​ = Time of Second Inspection
 {{FF1023107}}​ = Second Inspection Result
 {{FF1023100}}​ = Date of Second Inspection
Third Inspection
 {{{FF1023123}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1023109}}​ = Schedule Third Inspection
 {{FF1023111}}​ = Court
 {{FF1023112}}​ = Emergency
 {{FF1023113}}​ = Inspection
 {{FF1023118}}​ = Riccardo Bedinotti
 {{FF1023119}}​ = Aaron Cole
 {{FF1023120}}​ = Joseph Desmond
 {{FF1023121}}​ = Peter Nham
 {{FF1023116}}​ = Time of Third Inspection
 {{FF1023122}}​ = Third Inspection Result
 {{FF1023115}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1023138}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1023124}}​ = Schedule Fourth Inspection
 {{FF1023126}}​ = Court
 {{FF1023127}}​ = Emergency
 {{FF1023128}}​ = Inspection
 {{FF1023133}}​ = Riccardo Bedinotti
 {{FF1023134}}​ = Aaron Cole
 {{FF1023135}}​ = Joseph Desmond
 {{FF1023136}}​ = Peter Nham
 {{FF1023131}}​ = Time of Fourth Inspection
 {{FF1023137}}​ = Fourth Inspection Result
 {{FF1023130}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1023153}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1023139}}​ = Schedule Fifth Inspection
 {{FF1023141}}​ = Court
 {{FF1023142}}​ = Emergency
 {{FF1023143}}​ = Inspection
 {{FF1023148}}​ = Riccardo Bedinotti
 {{FF1023149}}​ = Aaron Cole
 {{FF1023150}}​ = Joseph Desmond
 {{FF1023151}}​ = Peter Nham
 {{FF1023146}}​ = Time of Fifth Inspection
 {{FF1023152}}​ = Fifth Inspection Result
 {{FF1023145}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1023168}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1023154}}​ = Schedule Sixth inspection
 {{FF1023156}}​ = Court
 {{FF1023157}}​ = Emergency
 {{FF1023158}}​ = Inspection
 {{FF1023163}}​ = Riccardo Bedinotti
 {{FF1023164}}​ = Aaron Cole
 {{FF1023165}}​ = Joseph Desmond
 {{FF1023166}}​ = Peter Nham
 {{FF1023161}}​ = Time of Sixth Inspection
 {{FF1023167}}​ = Sixth Inspection Result
 {{FF1023160}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1023183}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1023169}}​ = Schedule Seventh inspection
 {{FF1023171}}​ = Court
 {{FF1023172}}​ = Emergency
 {{FF1023173}}​ = Inspection
 {{FF1023178}}​ = Riccardo Bedinotti
 {{FF1023179}}​ = Aaron Cole
 {{FF1023180}}​ = Joseph Desmond
 {{FF1023181}}​ = Peter Nham
 {{FF1023176}}​ = Time of Seventh Inspection
 {{FF1023182}}​ = Seventh Inspection Result
 {{FF1023175}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1023198}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1023184}}​ = Schedule Eighth inspection
 {{FF1023186}}​ = Court
 {{FF1023187}}​ = Emergency
 {{FF1023188}}​ = Inspection
 {{FF1023193}}​ = Riccardo Bedinotti
 {{FF1023194}}​ = Aaron Cole
 {{FF1023195}}​ = Joseph Desmond
 {{FF1023196}}​ = Peter Nham
 {{FF1023191}}​ = Time of Eighth Inspection
 {{FF1023197}}​ = Eighth Inspection Result
 {{FF1023190}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1023213}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1023199}}​ = Schedule Ninth inspection
 {{FF1023201}}​ = Court
 {{FF1023202}}​ = Emergency
 {{FF1023203}}​ = Inspection
 {{FF1023208}}​ = Riccardo Bedinotti
 {{FF1023209}}​ = Aaron Cole
 {{FF1023210}}​ = Joseph Desmond
 {{FF1023211}}​ = Peter Nham
 {{FF1023206}}​ = Time of Ninth Inspection
 {{FF1023212}}​ = Ninth Inspection Result
 {{FF1023205}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1023228}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1023214}}​ = Schedule Tenth inspection
 {{FF1023216}}​ = Court
 {{FF1023217}}​ = Emergency
 {{FF1023218}}​ = Inspection
 {{FF1023223}}​ = Riccardo Bedinotti
 {{FF1023224}}​ = Aaron Cole
 {{FF1023225}}​ = Joseph Desmond
 {{FF1023226}}​ = Peter Nham
 {{FF1023221}}​ = Time of Tenth Inspection
 {{FF1023227}}​ = Tenth Inspection Result
 {{FF1023220}}​ = Date of Tenth Inspection
Letters
 {{FF1023231}}​ = Send First Violation Letters
 {{FF1023232}}​ = Send Second Violation Letters
 {{FF1023233}}​ = Send Third Violation Letters
 {{FF1023234}}​ = Send Fourth Violation Letters
 {{FF1023235}}​ = Send Fifth Violation Letters
 {{FF1023236}}​ = Send Sixth Violation Letters
 {{FF1023237}}​ = Send Seventh Violation Letters
 {{FF1023238}}​ = Send Eighth Violation Letters
 {{FF1023239}}​ = Send Ninth Violation Letters
 {{FF1023240}}​ = Send Tenth Violation Letters
 {{FF1023242}}​ = First Stop Work Letter
 {{FF1023243}}​ = Second Stop Work Letter
 {{FF1023244}}​ = Third Stop Work Letter
 {{FF1023245}}​ = Fourth Stop Work Letter
 {{FF1023246}}​ = Fifth Stop Work Letter
 {{FF1023247}}​ = Sixth Stop Work Letter
 {{FF1023248}}​ = Seventh Stop Work Letter
 {{FF1023249}}​ = Eighth Stop Work Letter
 {{FF1023250}}​ = Ninth Stop Work Letter
 {{FF1023251}}​ = Tenth Stop Work Letter
First Ticket Details
 {{FF1023254}}​ = Person whose name will appear on ticket
 {{{FF1023255}}}​ = First Ticket Notes for Administrative Staff
 {{FF1023252}}​ = First Ticket Total
 {{FF1023253}}​ = First Ticket Due Date
Second Ticket Details
 {{FF1023259}}​ = Person whose name will appear on ticket
 {{{FF1023260}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1023257}}​ = Second Ticket Total
 {{FF1023258}}​ = Second Ticket Due Date
Third Ticket Details
 {{FF1023264}}​ = Person whose name will appear on ticket
 {{{FF1023265}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1023263}}​ = Third Ticket Total
 {{FF1023262}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{FF1023269}}​ = Person whose name will appear on ticket
 {{{FF1023270}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1023267}}​ = Fourth Ticket Total
 {{FF1023268}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{FF1023274}}​ = Person whose name will appear on ticket
 {{{FF1023275}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1023272}}​ = Fifth Ticket Total
 {{FF1023273}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{FF1023279}}​ = Person whose name will appear on ticket
 {{{FF1023280}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1023277}}​ = Sixth Ticket Total
 {{FF1023278}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{FF1023284}}​ = Person whose name will appear on ticket
 {{{FF1023285}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1023282}}​ = Seventh Ticket Total
 {{FF1023283}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{FF1023289}}​ = Person whose name will appear on ticket
 {{{FF1023290}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1023287}}​ = Eighth Ticket Total
 {{FF1023288}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{FF1023294}}​ = Person whose name will appear on ticket
 {{{FF1023295}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1023292}}​ = Ninth Ticket Total
 {{FF1023293}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{FF1023299}}​ = Person whose name will appear on ticket
 {{{FF1023300}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1023297}}​ = Tenth Ticket Total
 {{FF1023298}}​ = Tenth Ticket Due Date

Multi Entry Section Entries:
Please note that object list entries are marked with three curly brackets, not two.


Electrical Violations
 {{{OL1023065}}}​ = Unit(s)
 {{{OL1023063}}}​ = Code / Description
 {{{OL1023064}}}​ = Responsible Party
 {{{OL1023066}}}​ = Status
 {{{OL1023068}}}​ = Correction Required By:
 {{{OL1023067}}}​ = Picture
Certified Letters
 {{{OL1023069}}}​ = Certified Number
 {{{OL1023071}}}​ = Recipient
 {{{OL1023072}}}​ = Cc
 {{{OL1023070}}}​ = Date sent
Emergency Violations
 {{{OL1023075}}}​ = Unit
 {{{OL1023073}}}​ = Code / Description
 {{{OL1023074}}}​ = Responsible Party
 {{{OL1023077}}}​ = Status
 {{{OL1023076}}}​ = Correction Required By:
 {{{OL1023078}}}​ = Picture
Parties Responsible for Online Payment
 {{{OL1023079}}}​ = Email Address
First Ticket
 {{{OL1023229}}}​ = First Ticket Description
Second Ticket
 {{{OL1023256}}}​ = Second Ticket Description
Third Ticket
 {{{OL1023261}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1023266}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1023271}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1023276}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1023281}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1023286}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1023291}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1023296}}}​ = Tenth Ticket Description

Multi Entry Sections:
Please note that multiEntry sections are marked with three curly brackets, not two.


 {{{MES1012169}}}​ = Electrical Violations
 {{{MES1012170}}}​ = Certified Letters
 {{{MES1012171}}}​ = Emergency Violations
 {{{MES1012172}}}​ = Parties Responsible for Online Payment
 {{{MES1012183}}}​ = First Ticket
 {{{MES1012186}}}​ = Second Ticket
 {{{MES1012188}}}​ = Third Ticket
 {{{MES1012190}}}​ = Fourth Ticket
 {{{MES1012192}}}​ = Fifth Ticket
 {{{MES1012194}}}​ = Sixth Ticket
 {{{MES1012196}}}​ = Seventh Ticket
 {{{MES1012198}}}​ = Eighth Ticket
 {{{MES1012200}}}​ = Ninth Ticket
 {{{MES1012202}}}​ = Tenth Ticket

Fees:
 {{FEE502}}​ = Violation Fee
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
 {{assignedToTS1158}}​ = Send Out Record Letters
 {{assignedToTS1211}}​ = Section 105 Letter
 {{assignedToTS1159}}​ = Send Out First Inspection Letters
 {{assignedToTS1183}}​ = First Stop Work Letter
 {{assignedToTS1185}}​ = First Violation Letter
 {{assignedToTS1160}}​ = Approve First Ticket
 {{assignedToTS1184}}​ = First Ticket
 {{assignedToTS1140}}​ = Send Out Second Inspection Letters
 {{assignedToTS1186}}​ = Second Violation Letter
 {{assignedToTS1210}}​ = Second Stop Work Letter
 {{assignedToTS1141}}​ = Approve Second Ticket
 {{assignedToTS1209}}​ = Second Ticket
 {{assignedToTS1142}}​ = Send Out Third Inspection Letters
 {{assignedToTS1187}}​ = Third Violation Letter Owner
 {{assignedToTS1181}}​ = Third Stop Work Letter
 {{assignedToTS1150}}​ = Approve Third Ticket
 {{assignedToTS1182}}​ = Third Ticket
 {{assignedToTS1143}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS1188}}​ = Fourth Violation Letter Owner
 {{assignedToTS1207}}​ = Fourth Stop Work Letter
 {{assignedToTS1151}}​ = Approve Fourth Ticket
 {{assignedToTS1208}}​ = Fourth Ticket
 {{assignedToTS1144}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS1189}}​ = Fifth Violation Letter Owner
 {{assignedToTS1205}}​ = Fifth Stop Work Letter
 {{assignedToTS1152}}​ = Approve Fifth Ticket
 {{assignedToTS1206}}​ = Fifth Ticket
 {{assignedToTS1145}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS1190}}​ = Sixth Violation Letter Owner
 {{assignedToTS1203}}​ = Sixth Stop Work Letter
 {{assignedToTS1153}}​ = Approve Sixth Ticket
 {{assignedToTS1204}}​ = Sixth Ticket
 {{assignedToTS1146}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS1191}}​ = Seventh Violation Letter Owner
 {{assignedToTS1201}}​ = Seventh Stop Work Letter
 {{assignedToTS1154}}​ = Approve Seventh Ticket
 {{assignedToTS1202}}​ = Seventh Ticket
 {{assignedToTS1147}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS1192}}​ = Eighth Violation Letter Owner
 {{assignedToTS1197}}​ = Eighth Stop Work Letter
 {{assignedToTS1155}}​ = Approve Eighth Ticket
 {{assignedToTS1200}}​ = Eighth Ticket
 {{assignedToTS1148}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS1193}}​ = Ninth Violation Letter Owner
 {{assignedToTS1199}}​ = Ninth Stop Work Letter
 {{assignedToTS1156}}​ = Approve Ninth Ticket
 {{assignedToTS1198}}​ = Ninth Ticket
 {{assignedToTS1149}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS1194}}​ = Tenth Violation Letter Owner
 {{assignedToTS1195}}​ = Tenth Stop Work Letter
 {{assignedToTS1157}}​ = Approve Tenth Ticket
 {{assignedToTS1196}}​ = Tenth Ticket
 {{assignedToTS1180}}​ = Tenth Inspection Date and Time
 {{assignedToTS1179}}​ = Ninth Inspection Date and Time
 {{assignedToTS1178}}​ = Eighth Inspection Date and Time
 {{assignedToTS1177}}​ = Seventh Inspection Date and Time
 {{assignedToTS1176}}​ = Sixth Inspection Date and Time
 {{assignedToTS1175}}​ = Fifth Inspection Date and Time
 {{assignedToTS1174}}​ = Fourth Inspection Date and Time
 {{assignedToTS1173}}​ = Third Inspection Date and Time
 {{assignedToTS1172}}​ = Second Inspection Date and Time
 {{assignedToTS1171}}​ = First Inspection Date and Time
 {{assignedToTS1161}}​ = Tenth Violation Fee
 {{assignedToTS1170}}​ = Ninth Violation Fee
 {{assignedToTS1169}}​ = Eighth Violation Fee
 {{assignedToTS1168}}​ = Seventh Violation Fee
 {{assignedToTS1167}}​ = Sixth Violation Fee
 {{assignedToTS1166}}​ = Fifth Violation Fee
 {{assignedToTS1165}}​ = Fourth Violation Fee
 {{assignedToTS1164}}​ = Third Violation Fee
 {{assignedToTS1163}}​ = Second Violation Fee
 {{assignedToTS1162}}​ = First Violation Fee
 {{assignedToTS1129}}​ = Refer to Court
 {{assignedToTS1132}}​ = Refer to Plumbing Enforcement
 {{assignedToTS1134}}​ = Refer to Animal Control
 {{assignedToTS1131}}​ = Refer to Electrical Enforcement
 {{assignedToTS1135}}​ = Refer to Police Ordinance
 {{assignedToTS1136}}​ = Refer to Health Department
 {{assignedToTS1130}}​ = Refer to Housing Enforcement
 {{assignedToTS1139}}​ = Refer to Zoning
 {{assignedToTS1138}}​ = Refer to Office of Housing
 {{assignedToTS1137}}​ = Refer to Elderly Affairs
 {{assignedToTS1133}}​ = Refer to Fire
"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
