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
    ordinals_set = {'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth', 'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth', 'Nineteenth', 'Twentieth', 'Twenty-first'}

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
    ordinals_list_lower = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty-first']
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
 {{FF1038148}}​ = Third Inspection Date
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
 {{FF1038069}}​ = Fourth Inspection Date
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
 {{FF1038077}}​ = Fifth Inspection Date
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
 {{FF1038161}}​ = Sixth Inspection Date
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
 {{FF1038097}}​ = Seventh Inspection Date
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
 {{FF1038101}}​ = Eighth Inspection Date
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
 {{FF1038121}}​ = Ninth Inspection Date
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
 {{FF1038113}}​ = Tenth Inspection Date
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

"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
