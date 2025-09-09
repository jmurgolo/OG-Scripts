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
General Info
 {{FF1023307}}​ = Inspection Access Contact Name
 {{FF1023308}}​ = Inspection Access Contact Phone
 {{FF1023309}}​ = Inspection Access Contact Title
 {{FF1023311}}​ = Other Source
 {{FF1023319}}​ = When & how did you contact them
 {{FF1023320}}​ = Who did you contact
 {{FF1023322}}​ = Unit Number - to be printed on the inspection report
 {{FF1023325}}​ = Alternative Owner Name
 {{FF1023328}}​ = Second Owner Name
 {{FF1023331}}​ = Third Owner Name
 {{{FF1023305}}}​ = General Notes
 {{{FF1023321}}}​ = What was the response
 {{{FF1023326}}}​ = Alternative Owner Address
 {{{FF1023329}}}​ = Second Owner Address
 {{{FF1023332}}}​ = Third Owner Address
 {{{FF1023337}}}​ = Refer to Court Details
 {{{FF1023339}}}​ = Refer to Housing Enforcement Details
 {{{FF1023341}}}​ = Refer to Electrical Details
 {{{FF1023343}}}​ = Refer to Building Details
 {{{FF1023345}}}​ = Refer to Fire Details
 {{{FF1023347}}}​ = Refer to Police Ordinance Details
 {{{FF1023349}}}​ = Refer to Health Department Details
 {{{FF1023351}}}​ = Refer to Elderly Affairs Details
 {{{FF1023353}}}​ = Refer to Animal Control Details
 {{{FF1023355}}}​ = Refer to Office of Housing Details
 {{{FF1023357}}}​ = Refer to Zoning Details
 {{FF1023312}}​ = Interior
 {{FF1023313}}​ = Exterior
 {{FF1023314}}​ = Referral
 {{FF1023318}}​ = Have you contacted the owner
 {{FF1023324}}​ = Owner Different than GIS
 {{FF1023327}}​ = Add Second Additional Owner
 {{FF1023330}}​ = Add Third Additional Owner
 {{FF1023334}}​ = Section 105 Required
 {{FF1023336}}​ = Refer to Court
 {{FF1023338}}​ = Refer to Housing Enforcement
 {{FF1023340}}​ = Refer to Electrical Enforcement
 {{FF1023342}}​ = Refer to Building Enforcement
 {{FF1023344}}​ = Refer to Fire Department
 {{FF1023346}}​ = Refer to Police Ordinance
 {{FF1023348}}​ = Refer to Health Department
 {{FF1023350}}​ = Refer to Elderly Affairs
 {{FF1023352}}​ = Refer to Animal Control
 {{FF1023354}}​ = Refer to Office of Housing
 {{FF1023356}}​ = Refer to Zoning
 {{FF1023358}}​ = Add Parties Responsible for Payment
 {{FF1023310}}​ = Complaint Source
 {{FF1023315}}​ = Usage Group
 {{FF1023316}}​ = When did the problem first occur
First Inspection
 {{{FF1023391}}}​ = First Inspection Notes For Administrative Staff
 {{FF1023378}}​ = Court
 {{FF1023379}}​ = Emergency
 {{FF1023380}}​ = Inspection
 {{FF1023385}}​ = Paul Brodeur
 {{FF1023386}}​ = Roderick Cruz
 {{FF1023387}}​ = Sam Santaniello
 {{FF1023388}}​ = Thomas Witkop
 {{FF1038231}}​ = Marc Turgeon
 {{FF1023383}}​ = First Inspection Time
 {{FF1023390}}​ = First Inspection Result
 {{FF1023382}}​ = Date of First Inspection
Second Inspection
 {{{FF1023407}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1023392}}​ = Schedule Second Inspection
 {{FF1023394}}​ = Court
 {{FF1023395}}​ = Emergency
 {{FF1023396}}​ = Inspection
 {{FF1023401}}​ = Paul Brodeur
 {{FF1023402}}​ = Roderick Cruz
 {{FF1023403}}​ = Sam Santaniello
 {{FF1023404}}​ = Thomas Witkop
 {{FF1038228}}​ = Marc Turgeon
 {{FF1023399}}​ = Time of Second Inspection
 {{FF1023406}}​ = Second Inspection Result
 {{FF1023398}}​ = Date of Second Inspection
Third Inspection
 {{{FF1023423}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1023408}}​ = Schedule Third Inspection
 {{FF1023410}}​ = Court
 {{FF1023411}}​ = Emergency
 {{FF1023412}}​ = Inspection
 {{FF1023417}}​ = Paul Brodeur
 {{FF1023418}}​ = Roderick Cruz
 {{FF1023419}}​ = Sam Santaniello
 {{FF1023420}}​ = Thomas Witkop
 {{FF1038230}}​ = Marc Turgeon
 {{FF1023415}}​ = Time of Third Inspection
 {{FF1023422}}​ = Third Inspection Result
 {{FF1023414}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1023439}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1023424}}​ = Schedule Fourth Inspection
 {{FF1023426}}​ = Court
 {{FF1023427}}​ = Emergency
 {{FF1023428}}​ = Inspection
 {{FF1023433}}​ = Paul Brodeur
 {{FF1023434}}​ = Roderick Cruz
 {{FF1023435}}​ = Sam Santaniello
 {{FF1023436}}​ = Thomas Witkop
 {{FF1038232}}​ = Marc Turgeon
 {{FF1023431}}​ = Time of Fourth Inspection
 {{FF1023438}}​ = Fourth Inspection Result
 {{FF1023430}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1023455}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1023440}}​ = Schedule Fifth Inspection
 {{FF1023442}}​ = Court
 {{FF1023443}}​ = Emergency
 {{FF1023444}}​ = Inspection
 {{FF1023449}}​ = Paul Brodeur
 {{FF1023450}}​ = Roderick Cruz
 {{FF1023451}}​ = Sam Santaniello
 {{FF1023452}}​ = Thomas Witkop
 {{FF1038229}}​ = Marc Turgeon
 {{FF1023447}}​ = Time of Fifth Inspection
 {{FF1023454}}​ = Fifth Inspection Result
 {{FF1023446}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1023471}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1023456}}​ = Schedule Sixth inspection
 {{FF1023458}}​ = Court
 {{FF1023459}}​ = Emergency
 {{FF1023460}}​ = Inspection
 {{FF1023465}}​ = Paul Brodeur
 {{FF1023466}}​ = Roderick Cruz
 {{FF1023467}}​ = Sam Santaniello
 {{FF1023468}}​ = Thomas Witkop
 {{FF1038233}}​ = Marc Turgeon
 {{FF1023463}}​ = Time of Sixth Inspection
 {{FF1023470}}​ = Sixth Inspection Result
 {{FF1023462}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1023487}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1023472}}​ = Schedule Seventh inspection
 {{FF1023474}}​ = Court
 {{FF1023475}}​ = Emergency
 {{FF1023476}}​ = Inspection
 {{FF1023481}}​ = Paul Brodeur
 {{FF1023482}}​ = Roderick Cruz
 {{FF1023483}}​ = Sam Santaniello
 {{FF1023484}}​ = Thomas Witkop
 {{FF1038234}}​ = Marc Turgeon
 {{FF1023479}}​ = Time of Seventh Inspection
 {{FF1023486}}​ = Seventh Inspection Result
 {{FF1023478}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1023503}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1023488}}​ = Schedule Eighth inspection
 {{FF1023490}}​ = Court
 {{FF1023491}}​ = Emergency
 {{FF1023492}}​ = Inspection
 {{FF1023497}}​ = Paul Brodeur
 {{FF1023498}}​ = Roderick Cruz
 {{FF1023499}}​ = Sam Santaniello
 {{FF1023500}}​ = Thomas Witkop
 {{FF1038235}}​ = Marc Turgeon
 {{FF1023495}}​ = Time of Eighth Inspection
 {{FF1023502}}​ = Eighth Inspection Result
 {{FF1023494}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1023519}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1023504}}​ = Schedule Ninth inspection
 {{FF1023506}}​ = Court
 {{FF1023507}}​ = Emergency
 {{FF1023508}}​ = Inspection
 {{FF1023513}}​ = Paul Brodeur
 {{FF1023514}}​ = Roderick Cruz
 {{FF1023515}}​ = Sam Santaniello
 {{FF1023516}}​ = Thomas Witkop
 {{FF1038236}}​ = Marc Turgeon
 {{FF1023511}}​ = Time of Ninth Inspection
 {{FF1023518}}​ = Ninth Inspection Result
 {{FF1023510}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1023535}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1023520}}​ = Schedule Tenth inspection
 {{FF1023522}}​ = Court
 {{FF1023523}}​ = Emergency
 {{FF1023524}}​ = Inspection
 {{FF1023529}}​ = Paul Brodeur
 {{FF1023530}}​ = Roderick Cruz
 {{FF1023531}}​ = Sam Santaniello
 {{FF1023532}}​ = Thomas Witkop
 {{FF1038227}}​ = Marc Turgeon
 {{FF1023527}}​ = Time of Tenth Inspection
 {{FF1023534}}​ = Tenth Inspection Result
 {{FF1023526}}​ = Date of Tenth Inspection
Letters
 {{FF1023538}}​ = Send First Violation Letters
 {{FF1023539}}​ = Send Second Violation Letters
 {{FF1023540}}​ = Send Third Violation Letters
 {{FF1023541}}​ = Send Fourth Violation Letters
 {{FF1023542}}​ = Send Fifth Violation Letters
 {{FF1023543}}​ = Send Sixth Violation Letters
 {{FF1023544}}​ = Send Seventh Violation Letters
 {{FF1023545}}​ = Send Eighth Violation Letters
 {{FF1023546}}​ = Send Ninth Violation Letters
 {{FF1023547}}​ = Send Tenth Violation Letters
 {{FF1023549}}​ = First Stop Work Letter
 {{FF1023550}}​ = Second Stop Work Letter
 {{FF1023551}}​ = Third Stop Work Letter
 {{FF1023552}}​ = Fourth Stop Work Letter
 {{FF1023553}}​ = Fifth Stop Work Letter
 {{FF1023554}}​ = Sixth Stop Work Letter
 {{FF1023555}}​ = Seventh Stop Work Letter
 {{FF1023556}}​ = Eighth Stop Work Letter
 {{FF1023557}}​ = Ninth Stop Work Letter
 {{FF1023558}}​ = Tenth Stop Work Letter
First Ticket Details
 {{{FF1023561}}}​ = First Ticket Notes for Administrative Staff
 {{FF1023559}}​ = First Ticket Total
 {{FF1023560}}​ = First Ticket Due Date
Second Ticket Details
 {{{FF1023565}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1023563}}​ = Second Ticket Total
 {{FF1023564}}​ = Second Ticket Due Date
Third Ticket Details
 {{{FF1023569}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1023568}}​ = Third Ticket Total
 {{FF1023567}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{{FF1023573}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1023571}}​ = Fourth Ticket Total
 {{FF1023572}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{{FF1023577}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1023575}}​ = Fifth Ticket Total
 {{FF1023576}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{{FF1023581}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1023579}}​ = Sixth Ticket Total
 {{FF1023580}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{{FF1023585}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1023583}}​ = Seventh Ticket Total
 {{FF1023584}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{{FF1023589}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1023587}}​ = Eighth Ticket Total
 {{FF1023588}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{{FF1023593}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1023591}}​ = Ninth Ticket Total
 {{FF1023592}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{{FF1023597}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1023595}}​ = Tenth Ticket Total
 {{FF1023596}}​ = Tenth Ticket Due Date



Parties Responsible for Online Payment
 {{{OL1023376}}}​ = Email Address
First Ticket
 {{{OL1023536}}}​ = First Ticket Description
Second Ticket
 {{{OL1023562}}}​ = Second Ticket Description
Third Ticket
 {{{OL1023566}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1023570}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1023574}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1023578}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1023582}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1023586}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1023590}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1023594}}}​ = Tenth Ticket Description

 {{{MES1012206}}}​ = Plumbing and Gas Violations
 {{{MES1012207}}}​ = Certified Letters
 {{{MES1012208}}}​ = Emergency Violations
 {{{MES1012209}}}​ = Parties Responsible for Online Payment
 {{{MES1012220}}}​ = First Ticket
 {{{MES1012223}}}​ = Second Ticket
 {{{MES1012225}}}​ = Third Ticket
 {{{MES1012227}}}​ = Fourth Ticket
 {{{MES1012229}}}​ = Fifth Ticket
 {{{MES1012231}}}​ = Sixth Ticket
 {{{MES1012233}}}​ = Seventh Ticket
 {{{MES1012235}}}​ = Eighth Ticket
 {{{MES1012237}}}​ = Ninth Ticket
 {{{MES1012239}}}​ = Tenth Ticket

Fees:
 {{FEE504}}​ = Violation Fee
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
 {{assignedToTS1243}}​ = Send Out Record Letters
 {{assignedToTS1296}}​ = Section 105 Letter
 {{assignedToTS1244}}​ = Send Out First Inspection Letters
 {{assignedToTS1268}}​ = First Stop Work Letter
 {{assignedToTS1270}}​ = First Violation Letter
 {{assignedToTS1245}}​ = Approve First Ticket
 {{assignedToTS1269}}​ = First Ticket
 {{assignedToTS1225}}​ = Send Out Second Inspection Letters
 {{assignedToTS1271}}​ = Second Violation Letter
 {{assignedToTS1295}}​ = Second Stop Work Letter
 {{assignedToTS1226}}​ = Approve Second Ticket
 {{assignedToTS1294}}​ = Second Ticket
 {{assignedToTS1227}}​ = Send Out Third Inspection Letters
 {{assignedToTS1272}}​ = Third Violation Letter Owner
 {{assignedToTS1266}}​ = Third Stop Work Letter
 {{assignedToTS1235}}​ = Approve Third Ticket
 {{assignedToTS1267}}​ = Third Ticket
 {{assignedToTS1228}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS1273}}​ = Fourth Violation Letter Owner
 {{assignedToTS1292}}​ = Fourth Stop Work Letter
 {{assignedToTS1236}}​ = Approve Fourth Ticket
 {{assignedToTS1293}}​ = Fourth Ticket
 {{assignedToTS1229}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS1274}}​ = Fifth Violation Letter Owner
 {{assignedToTS1290}}​ = Fifth Stop Work Letter
 {{assignedToTS1237}}​ = Approve Fifth Ticket
 {{assignedToTS1291}}​ = Fifth Ticket
 {{assignedToTS1230}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS1275}}​ = Sixth Violation Letter Owner
 {{assignedToTS1288}}​ = Sixth Stop Work Letter
 {{assignedToTS1238}}​ = Approve Sixth Ticket
 {{assignedToTS1289}}​ = Sixth Ticket
 {{assignedToTS1231}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS1276}}​ = Seventh Violation Letter Owner
 {{assignedToTS1286}}​ = Seventh Stop Work Letter
 {{assignedToTS1239}}​ = Approve Seventh Ticket
 {{assignedToTS1287}}​ = Seventh Ticket
 {{assignedToTS1232}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS1277}}​ = Eighth Violation Letter Owner
 {{assignedToTS1282}}​ = Eighth Stop Work Letter
 {{assignedToTS1240}}​ = Approve Eighth Ticket
 {{assignedToTS1285}}​ = Eighth Ticket
 {{assignedToTS1233}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS1278}}​ = Ninth Violation Letter Owner
 {{assignedToTS1284}}​ = Ninth Stop Work Letter
 {{assignedToTS1241}}​ = Approve Ninth Ticket
 {{assignedToTS1283}}​ = Ninth Ticket
 {{assignedToTS1234}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS1279}}​ = Tenth Violation Letter Owner
 {{assignedToTS1280}}​ = Tenth Stop Work Letter
 {{assignedToTS1242}}​ = Approve Tenth Ticket
 {{assignedToTS1281}}​ = Tenth Ticket
 {{assignedToTS1265}}​ = Tenth Inspection Date and Time
 {{assignedToTS1264}}​ = Ninth Inspection Date and Time
 {{assignedToTS1263}}​ = Eighth Inspection Date and Time
 {{assignedToTS1262}}​ = Seventh Inspection Date and Time
 {{assignedToTS1261}}​ = Sixth Inspection Date and Time
 {{assignedToTS1260}}​ = Fifth Inspection Date and Time
 {{assignedToTS1259}}​ = Fourth Inspection Date and Time
 {{assignedToTS1258}}​ = Third Inspection Date and Time
 {{assignedToTS1257}}​ = Second Inspection Date and Time
 {{assignedToTS1256}}​ = First Inspection Date and Time
 {{assignedToTS1246}}​ = Tenth Violation Fee
 {{assignedToTS1255}}​ = Ninth Violation Fee
 {{assignedToTS1254}}​ = Eighth Violation Fee
 {{assignedToTS1253}}​ = Seventh Violation Fee
 {{assignedToTS1252}}​ = Sixth Violation Fee
 {{assignedToTS1251}}​ = Fifth Violation Fee
 {{assignedToTS1250}}​ = Fourth Violation Fee
 {{assignedToTS1249}}​ = Third Violation Fee
 {{assignedToTS1248}}​ = Second Violation Fee
 {{assignedToTS1247}}​ = First Violation Fee
 {{assignedToTS1214}}​ = Refer to Court
 {{assignedToTS1217}}​ = Refer to Building Enforcement
 {{assignedToTS1219}}​ = Refer to Animal Control
 {{assignedToTS1216}}​ = Refer to Electrical Enforcement
 {{assignedToTS1220}}​ = Refer to Police Ordinance
 {{assignedToTS1221}}​ = Refer to Health Department
 {{assignedToTS1215}}​ = Refer to Housing Enforcement
 {{assignedToTS1224}}​ = Refer to Zoning
 {{assignedToTS1223}}​ = Refer to Office of Housing
 {{assignedToTS1222}}​ = Refer to Elderly Affairs
 {{assignedToTS1218}}​ = Refer to Fire
"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
