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

First Court Inspection
 {{FF1022517}}​ = Next Court Appearance
 {{FF1022518}}​ = Record ID
 {{FF1022520}}​ = Time of Reinspection
 {{{FF1022527}}}​ = Purpose
 {{{FF1022532}}}​ = Inspector Findings
 {{{FF1022533}}}​ = Images
 {{FF1022528}}​ = Photographs
 {{FF1022529}}​ = Narrative
 {{FF1022530}}​ = Formal Report
 {{FF1022531}}​ = Court Attendance Necessary
 {{FF1022521}}​ = Record Type
 {{FF1022522}}​ = Building Inspector
 {{FF1022523}}​ = Electrical Inspector
 {{FF1022524}}​ = Housing Inspector
 {{FF1022525}}​ = Plumbing Gas Inspector
 {{FF1022526}}​ = Zoning Inspector
 {{FF1022519}}​ = Date of Inspection
Second Court Inspection
 {{FF1022535}}​ = Next Court Appearance
 {{FF1022536}}​ = Record ID
 {{FF1022538}}​ = Time of Inspection
 {{{FF1022545}}}​ = Purpose
 {{{FF1022550}}}​ = Inspector Findings
 {{{FF1022551}}}​ = Images
 {{FF1022534}}​ = Schedule Second Court Inspection
 {{FF1022546}}​ = Photographs
 {{FF1022547}}​ = Narrative
 {{FF1022548}}​ = Formal Report
 {{FF1022549}}​ = Court Attendance Necessary
 {{FF1022539}}​ = Record Type
 {{FF1022540}}​ = Building Inspectors
 {{FF1022541}}​ = Electrical Inspectors
 {{FF1022542}}​ = Housing Inspector
 {{FF1022543}}​ = Plumbing Gas Inspectors
 {{FF1022544}}​ = Zoning Inspectors
 {{FF1022537}}​ = Date of Inspection
Third Court Inspection
 {{FF1022553}}​ = Next Court Appearance
 {{FF1022554}}​ = Record ID
 {{FF1022556}}​ = Time of Inspection
 {{{FF1022563}}}​ = Purpose
 {{{FF1022568}}}​ = Inspector Findings
 {{FF1022552}}​ = Schedule Third Court Inspection
 {{FF1022564}}​ = Photographs
 {{FF1022565}}​ = Narrative
 {{FF1022566}}​ = Formal Report
 {{FF1022567}}​ = Court Attendance Necessary
 {{FF1022557}}​ = Record Type
 {{FF1022558}}​ = Building Inspectors
 {{FF1022559}}​ = Electrical Inspectors
 {{FF1022560}}​ = Housing Inspectors
 {{FF1022561}}​ = Plumbing Gas Inspectors
 {{FF1022562}}​ = Zoning Inspectors
 {{FF1022555}}​ = Date of Inspection
Fourth Court Inspection
 {{FF1022570}}​ = Next Court Appearance
 {{FF1022571}}​ = Record ID
 {{FF1022573}}​ = Time of Inspection
 {{{FF1022580}}}​ = Purpose
 {{{FF1022585}}}​ = Inspector Findings
 {{FF1022569}}​ = Schedule Fourth Court Inspection
 {{FF1022581}}​ = Photographs
 {{FF1022582}}​ = Narrative
 {{FF1022583}}​ = Formal Report
 {{FF1022584}}​ = Court Attendance Necessary
 {{FF1022574}}​ = Record Type
 {{FF1022575}}​ = Building Inspectors
 {{FF1022576}}​ = Electrical Inspectors
 {{FF1022577}}​ = Housing Inspectors
 {{FF1022578}}​ = Plumbing Gas Inspectors
 {{FF1022579}}​ = Zoning Inspectors
 {{FF1022572}}​ = Date of Inspection
Fifth Court Inspection
 {{FF1022589}}​ = Next Court Appearance
 {{FF1022590}}​ = Record ID
 {{FF1022592}}​ = Time of Inspection
 {{{FF1022599}}}​ = Purpose
 {{{FF1022604}}}​ = Inspector Findings
 {{FF1022588}}​ = Schedule Fifth Court Inspection
 {{FF1022600}}​ = Photographs
 {{FF1022601}}​ = Narrative
 {{FF1022602}}​ = Formal Report
 {{FF1022603}}​ = Court Attendance Necessary
 {{FF1022593}}​ = Record Type
 {{FF1022594}}​ = Building Inspectors
 {{FF1022595}}​ = Electrical Inspectors
 {{FF1022596}}​ = Housing Inspectors
 {{FF1022597}}​ = Plumbing Gas Inspectors
 {{FF1022598}}​ = Zoning Inspectors
 {{FF1022591}}​ = Date of Inspection
Sixth Court Inspection
 {{FF1038238}}​ = Next Court Appearance
 {{FF1038239}}​ = Time of Inspection
 {{FF1038245}}​ = Record ID
 {{{FF1038247}}}​ = Purpose
 {{{FF1038251}}}​ = Inspector Findings
 {{FF1038237}}​ = Schedule Sixth Court Inspection
 {{FF1038240}}​ = Photographs
 {{FF1038246}}​ = Court Attendance Necessary
 {{FF1038252}}​ = Narrative
 {{FF1038253}}​ = Formal Report
 {{FF1038241}}​ = Plumbing Gas Inspectors
 {{FF1038242}}​ = Record Type
 {{FF1038243}}​ = Housing Inspectors
 {{FF1038244}}​ = Zoning Inspectors
 {{FF1038248}}​ = Building Inspectors
 {{FF1038249}}​ = Electrical Inspectors
 {{FF1038250}}​ = Date of Inspection
Seventh Court Inspection
 {{FF1038254}}​ = Record ID
 {{FF1038258}}​ = Time of Inspection
 {{FF1038261}}​ = Next Court Appearance
 {{{FF1038268}}}​ = Purpose
 {{{FF1038270}}}​ = Inspector Findings
 {{FF1038259}}​ = Schedule Seventh Court Inspection
 {{FF1038262}}​ = Formal Report
 {{FF1038263}}​ = Narrative
 {{FF1038265}}​ = Court Attendance Necessary
 {{FF1038269}}​ = Photographs
 {{FF1038255}}​ = Record Type
 {{FF1038256}}​ = Housing Inspectors
 {{FF1038257}}​ = Building Inspectors
 {{FF1038264}}​ = Plumbing Gas Inspectors
 {{FF1038266}}​ = Electrical Inspectors
 {{FF1038267}}​ = Zoning Inspectors
 {{FF1038260}}​ = Date of Inspection
Eighth Court Inspection
 {{FF1038272}}​ = Time of Inspection
 {{FF1038273}}​ = Date of Inspection
 {{FF1038277}}​ = Record ID
 {{FF1038283}}​ = Next Court Appearance
 {{{FF1038275}}}​ = Purpose
 {{{FF1038278}}}​ = Inspector Findings
 {{FF1038279}}​ = Schedule Eighth Court Inspection
 {{FF1038281}}​ = Narrative
 {{FF1038285}}​ = Photographs
 {{FF1038286}}​ = Formal Report
 {{FF1038287}}​ = Court Attendance Necessary
 {{FF1038271}}​ = Housing Inspectors
 {{FF1038274}}​ = Record Type
 {{FF1038276}}​ = Plumbing Gas Inspectors
 {{FF1038280}}​ = Electrical Inspectors
 {{FF1038282}}​ = Building Inspectors
 {{FF1038284}}​ = Zoning Inspectors
Ninth Court Inspection
 {{FF1038294}}​ = Record ID
 {{FF1038298}}​ = Date of Inspection
 {{FF1038301}}​ = Time of Inspection
 {{FF1038302}}​ = Next Court Appearance
 {{{FF1038290}}}​ = Inspector Findings
 {{{FF1038303}}}​ = Purpose
 {{FF1038288}}​ = Court Attendance Necessary
 {{FF1038289}}​ = Photographs
 {{FF1038292}}​ = Narrative
 {{FF1038297}}​ = Schedule Ninth Court Inspection
 {{FF1038304}}​ = Formal Report
 {{FF1038291}}​ = Electrical Inspectors
 {{FF1038293}}​ = Plumbing Gas Inspectors
 {{FF1038295}}​ = Record Type
 {{FF1038296}}​ = Zoning Inspectors
 {{FF1038299}}​ = Housing Inspectors
 {{FF1038300}}​ = Building Inspectors
Tenth Court Inspection
 {{FF1038316}}​ = Time of Inspection
 {{FF1038318}}​ = Date of Inspection
 {{FF1038322}}​ = Record ID
 {{FF1038327}}​ = Next Court Appearance
 {{{FF1038329}}}​ = Inspector Findings
 {{{FF1038330}}}​ = Purpose
 {{FF1038320}}​ = Photographs
 {{FF1038324}}​ = Narrative
 {{FF1038325}}​ = Schedule Tenth Court Inspection
 {{FF1038328}}​ = Formal Report
 {{FF1038331}}​ = Court Attendance Necessary
 {{FF1038315}}​ = Record Type
 {{FF1038317}}​ = Electrical Inspectors
 {{FF1038319}}​ = Zoning Inspectors
 {{FF1038321}}​ = Building Inspectors
 {{FF1038323}}​ = Plumbing Gas Inspectors
 {{FF1038326}}​ = Housing Inspectors
Eleventh Court Inspection
 {{FF1038337}}​ = Record ID
 {{FF1038340}}​ = Time of Inspection
 {{FF1038341}}​ = Date of Inspection
 {{FF1038342}}​ = Next Court Appearance
 {{{FF1038335}}}​ = Purpose
 {{{FF1038346}}}​ = Inspector Findings
 {{FF1038334}}​ = Photographs
 {{FF1038336}}​ = Schedule Eleventh Court Inspection
 {{FF1038345}}​ = Formal Report
 {{FF1038347}}​ = Court Attendance Necessary
 {{FF1038348}}​ = Narrative
 {{FF1038332}}​ = Housing Inspectors
 {{FF1038333}}​ = Record Type
 {{FF1038338}}​ = Building Inspectors
 {{FF1038339}}​ = Electrical Inspectors
 {{FF1038343}}​ = Plumbing Gas Inspectors
 {{FF1038344}}​ = Zoning Inspectors
Twelfth Court Inspection
 {{FF1038353}}​ = Next Court Appearance
 {{FF1038358}}​ = Time of Inspection
 {{FF1038359}}​ = Date of Inspection
 {{FF1038362}}​ = Record ID
 {{{FF1038350}}}​ = Purpose
 {{{FF1038356}}}​ = Inspector Findings
 {{FF1038349}}​ = Photographs
 {{FF1038351}}​ = Schedule Twelfth Court Inspection
 {{FF1038360}}​ = Formal Report
 {{FF1038364}}​ = Narrative
 {{FF1038365}}​ = Court Attendance Necessary
 {{FF1038352}}​ = Building Inspectors
 {{FF1038354}}​ = Plumbing Gas Inspectors
 {{FF1038355}}​ = Record Type
 {{FF1038357}}​ = Electrical Inspectors
 {{FF1038361}}​ = Housing Inspectors
 {{FF1038363}}​ = Zoning Inspectors
Thirteenth Court Inspection
 {{FF1038367}}​ = Record ID
 {{FF1038373}}​ = Date of Inspection
 {{FF1038376}}​ = Next Court Appearance
 {{FF1038380}}​ = Time of Inspection
 {{{FF1038370}}}​ = Inspector Findings
 {{{FF1038378}}}​ = Purpose
 {{FF1038366}}​ = Court Attendance Necessary
 {{FF1038369}}​ = Photographs
 {{FF1038371}}​ = Formal Report
 {{FF1038377}}​ = Narrative
 {{FF1038379}}​ = Schedule Thirteenth Court Inspection
 {{FF1038368}}​ = Building Inspectors
 {{FF1038372}}​ = Record Type
 {{FF1038374}}​ = Housing Inspectors
 {{FF1038375}}​ = Plumbing Gas Inspectors
 {{FF1038381}}​ = Electrical Inspectors
 {{FF1038382}}​ = Zoning Inspectors
Fourteenth Court Inspection
 {{FF1038385}}​ = Date of Inspection
 {{FF1038388}}​ = Next Court Appearance
 {{FF1038389}}​ = Record ID
 {{FF1038390}}​ = Time of Inspection
 {{{FF1038383}}}​ = Purpose
 {{{FF1038384}}}​ = Inspector Findings
 {{FF1038387}}​ = Schedule Fourteenth Court Inspection
 {{FF1038393}}​ = Court Attendance Necessary
 {{FF1038394}}​ = Photographs
 {{FF1038395}}​ = Narrative
 {{FF1038399}}​ = Formal Report
 {{FF1038386}}​ = Electrical Inspectors
 {{FF1038391}}​ = Housing Inspectors
 {{FF1038392}}​ = Zoning Inspectors
 {{FF1038396}}​ = Plumbing Gas Inspectors
 {{FF1038397}}​ = Building Inspectors
 {{FF1038398}}​ = Record Type
Fifteenth Court Inspection
 {{FF1038404}}​ = Record ID
 {{FF1038406}}​ = Time of Inspection
 {{FF1038407}}​ = Date of Inspection
 {{FF1038415}}​ = Next Court Appearance
 {{{FF1038411}}}​ = Inspector Findings
 {{{FF1038423}}}​ = Purpose
 {{FF1038401}}​ = Schedule Fifteenth Court Inspection
 {{FF1038408}}​ = Formal Report
 {{FF1038409}}​ = Court Attendance Necessary
 {{FF1038410}}​ = Photographs
 {{FF1038422}}​ = Narrative
 {{FF1038400}}​ = Plumbing Gas Inspectors
 {{FF1038402}}​ = Housing Inspectors
 {{FF1038403}}​ = Electrical Inspectors
 {{FF1038405}}​ = Building Inspectors
 {{FF1038416}}​ = Zoning Inspectors
 {{FF1038421}}​ = Record Type
Sixteenth Court Inspection
 {{FF1038412}}​ = Next Court Appearance
 {{FF1038418}}​ = Record ID
 {{FF1038428}}​ = Time of Inspection
 {{FF1038430}}​ = Date of Inspection
 {{{FF1038413}}}​ = Inspector Findings
 {{{FF1038432}}}​ = Purpose
 {{FF1038414}}​ = Court Attendance Necessary
 {{FF1038417}}​ = Schedule Sixteenth Court Inspection
 {{FF1038419}}​ = Formal Report
 {{FF1038420}}​ = Narrative
 {{FF1038433}}​ = Photographs
 {{FF1038424}}​ = Record Type
 {{FF1038425}}​ = Building Inspectors
 {{FF1038426}}​ = Plumbing Gas Inspectors
 {{FF1038427}}​ = Electrical Inspectors
 {{FF1038429}}​ = Housing Inspectors
 {{FF1038431}}​ = Zoning Inspectors
Seventeenth Court Inspection
 {{FF1038436}}​ = Time of Inspection
 {{FF1038438}}​ = Next Court Appearance
 {{FF1038440}}​ = Record ID
 {{FF1038442}}​ = Date of Inspection
 {{{FF1038444}}}​ = Inspector Findings
 {{{FF1038446}}}​ = Purpose
 {{FF1038437}}​ = Schedule Seventeenth Court Inspection
 {{FF1038447}}​ = Photographs
 {{FF1038448}}​ = Formal Report
 {{FF1038449}}​ = Court Attendance Necessary
 {{FF1038450}}​ = Narrative
 {{FF1038434}}​ = Plumbing Gas Inspectors
 {{FF1038435}}​ = Housing Inspectors
 {{FF1038439}}​ = Electrical Inspectors
 {{FF1038441}}​ = Building Inspectors
 {{FF1038443}}​ = Record Type
 {{FF1038445}}​ = Zoning Inspectors
Eighteenth Court Inspection
 {{FF1038452}}​ = Time of Inspection
 {{FF1038456}}​ = Next Court Appearance
 {{FF1038464}}​ = Record ID
 {{FF1038467}}​ = Date of Inspection
 {{{FF1038460}}}​ = Purpose
 {{{FF1038466}}}​ = Inspector Findings
 {{FF1038451}}​ = Schedule Eighteenth Court Inspection
 {{FF1038453}}​ = Court Attendance Necessary
 {{FF1038454}}​ = Narrative
 {{FF1038455}}​ = Photographs
 {{FF1038465}}​ = Formal Report
 {{FF1038457}}​ = Record Type
 {{FF1038458}}​ = Electrical Inspectors
 {{FF1038459}}​ = Zoning Inspectors
 {{FF1038461}}​ = Housing Inspectors
 {{FF1038462}}​ = Plumbing Gas Inspectors
 {{FF1038463}}​ = Building Inspectors
Nineteenth Court Inspection
 {{FF1038471}}​ = Time of Inspection
 {{FF1038477}}​ = Record ID
 {{FF1038480}}​ = Date of Inspection
 {{FF1038481}}​ = Next Court Appearance
 {{{FF1038468}}}​ = Purpose
 {{{FF1038470}}}​ = Inspector Findings
 {{FF1038469}}​ = Formal Report
 {{FF1038475}}​ = Schedule Nineteenth Court Inspection
 {{FF1038478}}​ = Photographs
 {{FF1038483}}​ = Narrative
 {{FF1038484}}​ = Court Attendance Necessary
 {{FF1038472}}​ = Housing Inspectors
 {{FF1038473}}​ = Electrical Inspectors
 {{FF1038474}}​ = Building Inspectors
 {{FF1038476}}​ = Record Type
 {{FF1038479}}​ = Plumbing Gas Inspectors
 {{FF1038482}}​ = Zoning Inspectors
Twentieth Court Inspection
 {{FF1038490}}​ = Time of Inspection
 {{FF1038492}}​ = Record ID
 {{FF1038493}}​ = Next Court Appearance
 {{FF1038494}}​ = Date of Inspection
 {{{FF1038498}}}​ = Inspector Findings
 {{{FF1038500}}}​ = Purpose
 {{FF1038488}}​ = Court Attendance Necessary
 {{FF1038489}}​ = Schedule Twentieth Court Inspection
 {{FF1038497}}​ = Photographs
 {{FF1038499}}​ = Narrative
 {{FF1038501}}​ = Formal Report
 {{FF1038485}}​ = Housing Inspectors
 {{FF1038486}}​ = Building Inspectors
 {{FF1038487}}​ = Record Type
 {{FF1038491}}​ = Electrical Inspectors
 {{FF1038495}}​ = Plumbing Gas Inspectors
 {{FF1038496}}​ = Zoning Inspectors
Twenty First Court Inspection
 {{FF1038504}}​ = Next Court Appearance
 {{FF1038506}}​ = Record ID
 {{FF1038508}}​ = Time of Inspection
 {{FF1038509}}​ = Date of Inspection
 {{{FF1038502}}}​ = Purpose
 {{{FF1038512}}}​ = Inspector Findings
 {{FF1038503}}​ = Photographs
 {{FF1038511}}​ = Court Attendance Necessary
 {{FF1038513}}​ = Formal Report
 {{FF1038514}}​ = Schedule Twenty First Court Inspection
 {{FF1038517}}​ = Narrative
 {{FF1038505}}​ = Building Inspectors
 {{FF1038507}}​ = Electrical Inspectors
 {{FF1038510}}​ = Record Type
 {{FF1038515}}​ = Housing Inspectors
 {{FF1038516}}​ = Plumbing Gas Inspectors
 {{FF1038518}}​ = Zoning Inspectors

"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
