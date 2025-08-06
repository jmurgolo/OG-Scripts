import re
from collections import defaultdict

def create_grouped_mappings_with_special_conditions(data_string: str) -> str:
    """
    Parses field data and creates grouped, chained mappings, with special
    handling for "next inspection" dates and times.

    Args:
        data_string: A multiline string containing the field data.

    Returns:
        A formatted string with mappings grouped by step.
    """
    # Clean the input of invisible characters
    cleaned_data = data_string.replace('\u200b', '')

    mappings = defaultdict(list)
    line_regex = re.compile(r'\{\{+([A-Z0-9]+)\}\}+\s*=\s*(.*)')
    ordinals_set = {"First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"}

    # --- Data Parsing (handles both ID and plain text formats) ---
    for line in cleaned_data.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        match = line_regex.search(line)
        field_id, description = None, None

        if match:
            field_id = match.group(1)
            description = match.group(2).strip()
        else:
            words = line.split()
            if words and words[0].capitalize() in ordinals_set and not line.endswith(("Inspection", "Details", "ticket")):
                field_id = description = line

        if field_id and description:
            words = description.split()
            normalized_words = [word for word in words if word.capitalize() not in ordinals_set]
            base_description = " ".join(normalized_words)
            mappings[base_description].append(field_id)

    # --- UPDATED LOGIC: Generate Output with Special Conditions ---
    output_lines = []
    ordinals_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    
    # Define the special base descriptions for lookahead handling
    special_keys = {"Date of Inspection", "Time of Inspection"}

    # Loop for each transition step (e.g., first to second)
    for i in range(len(ordinals_list) - 1):
        special_mappings = []
        regular_mappings = []

        # 1. Find the date/time mappings from the *next* step and add them first.
        lookahead_step_index = i + 1
        for key in sorted(special_keys): # Sort for consistent order
            if key in mappings and len(mappings[key]) > lookahead_step_index + 1:
                ids = mappings[key]
                source_id = ids[lookahead_step_index]
                destination_id = ids[lookahead_step_index + 1]
                special_mappings.append(f"{source_id} = {destination_id}")

        # 2. Find all standard mappings for the *current* step, including date/time.
        for base_description in sorted(mappings.keys()):
            ids = mappings[base_description]
            if len(ids) > i + 1:
                source_id = ids[i]
                destination_id = ids[i+1]
                regular_mappings.append(f"{source_id} = {destination_id}")

        # 3. Combine the lists and format the output for this group.
        all_group_mappings = special_mappings + regular_mappings
        if all_group_mappings:
            if output_lines:
                output_lines.append("")
            output_lines.append(f"# {ordinals_list[i]} to {ordinals_list[i+1]}")
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
 {{FF1026392}}​ = Donald Zdunczyk
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
 {{FF1026505}}​ = Tenth Inspection Result
 {{FF1026507}}​ = Time of Tenth Inspection
 {{FF1026520}}​ = Date of Tenth Inspection
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
FIRST NOTICE OF VIOLATIONS
FIRST VIOLATION TICKET
FIRST NOTICE
SECOND NOTICE OF VIOLATIONS
SECOND VIOLATION TICKET
SECOND NOTICE
THIRD NOTICE OF VIOLATIONS
THIRD VIOLATION TICKET
THIRD NOTICE
FOURTH NOTICE OF VIOLATIONS
FOURTH VIOLATION TICKET
FOURTH NOTICE
FIFTH NOTICE OF VIOLATIONS
FIFTH VIOLATION TICKET
FIFTH NOTICE
SIXTH NOTICE OF VIOLATIONS
SIXTH VIOLATION TICKET
SIXTH NOTICE
SEVENTH NOTICE OF VIOLATIONS
SEVENTH VIOLATION TICKET
SEVENTH NOTICE
EIGHTH NOTICE OF VIOLATIONS
EIGHTH VIOLATION TICKET
EIGHTH NOTICE
NINTH NOTICE OF VIOLATIONS
NINTH VIOLATION TICKET
NINTH NOTICE
TENTH NOTICE OF VIOLATIONS
TENTH VIOLATION TICKET
TENTH NOTICE
"""

# --- Run the script and print the output ---
output = create_grouped_mappings_with_special_conditions(input_data)
print(output)