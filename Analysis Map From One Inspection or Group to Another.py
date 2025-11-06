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

First Inspection
 {{{FF1035769}}}​ = First Inspection Notes For Administrative Staff
 {{FF1035939}}​ = Concentrated
 {{FF1035940}}​ = Condemnation
 {{FF1035941}}​ = Court
 {{FF1035942}}​ = Emergency
 {{FF1035943}}​ = Exterior
 {{FF1035944}}​ = Inspection
 {{FF1035945}}​ = Lead Paint
 {{FF1035946}}​ = MRVP
 {{FF1035947}}​ = Pre-Judgement
 {{FF1035948}}​ = Post Judgment
 {{FF1035949}}​ = Priority
 {{FF1035950}}​ = Christopher Bennett
 {{FF1035951}}​ = William Brunton
 {{FF1035952}}​ = Danny Cueto
 {{FF1035953}}​ = Michelle Haska
 {{FF1035954}}​ = Mike Jones
 {{FF1035955}}​ = Jesus Martinez
 {{FF1035956}}​ = Michael McNulty
 {{FF1035957}}​ = Jermaine Mitchell
 {{FF1035958}}​ = Michael Whiting
 {{FF1035959}}​ = James Murgolo
 {{FF1037963}}​ = Colin Hoppie
 {{FF1036093}}​ = First Inspection Time
 {{FF1036104}}​ = First Inspection Result
 {{FF1036150}}​ = Date of First Inspection
Second Inspection
 {{{FF1035770}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1036059}}​ = Schedule Second Inspection
 {{FF1036060}}​ = Concentrated
 {{FF1036061}}​ = Condemnation
 {{FF1036062}}​ = Court
 {{FF1036063}}​ = Emergency
 {{FF1036064}}​ = Exterior
 {{FF1036065}}​ = Inspection
 {{FF1036066}}​ = Lead Paint
 {{FF1036067}}​ = MRVP
 {{FF1036068}}​ = Pre-Judgement
 {{FF1036069}}​ = Post Judgment
 {{FF1036070}}​ = Priority
 {{FF1036071}}​ = Christopher Bennett
 {{FF1036072}}​ = William Brunton
 {{FF1036073}}​ = Danny Cueto
 {{FF1036074}}​ = Michelle Haska
 {{FF1036075}}​ = Mike Jones
 {{FF1036076}}​ = Jesus Martinez
 {{FF1036077}}​ = Michael McNulty
 {{FF1036078}}​ = Jermaine Mitchell
 {{FF1036079}}​ = Michael Whiting
 {{FF1036080}}​ = James Murgolo
 {{FF1037965}}​ = Colin Hoppie
 {{FF1036092}}​ = Second Inspection Result
 {{FF1036096}}​ = Time of Second Inspection
 {{FF1036151}}​ = Date of Second Inspection
Third Inspection
 {{{FF1035771}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1036027}}​ = Schedule Third Inspection
 {{FF1036028}}​ = Christopher Bennett
 {{FF1036029}}​ = William Brunton
 {{FF1036030}}​ = Danny Cueto
 {{FF1036031}}​ = Michelle Haska
 {{FF1036032}}​ = Mike Jones
 {{FF1036033}}​ = Jesus Martinez
 {{FF1036034}}​ = Michael McNulty
 {{FF1036035}}​ = Jermaine Mitchell
 {{FF1036036}}​ = Michael Whiting
 {{FF1036037}}​ = James Murgolo
 {{FF1036081}}​ = Concentrated
 {{FF1036082}}​ = Court
 {{FF1036083}}​ = Condemnation
 {{FF1036084}}​ = Emergency
 {{FF1036085}}​ = Exterior
 {{FF1036086}}​ = Inspection
 {{FF1036087}}​ = Lead Paint
 {{FF1036088}}​ = MRVP
 {{FF1036089}}​ = Pre-Judgement
 {{FF1036090}}​ = Post Judgment
 {{FF1036091}}​ = Priority
 {{FF1037964}}​ = Colin Hoppie
 {{FF1036095}}​ = Third Inspection Result
 {{FF1036097}}​ = Time of Third Inspection
 {{FF1036148}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1035772}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1036026}}​ = Schedule Fourth Inspection
 {{FF1036038}}​ = Concentrated
 {{FF1036039}}​ = Condemnation
 {{FF1036040}}​ = Court
 {{FF1036041}}​ = Emergency
 {{FF1036042}}​ = Exterior
 {{FF1036043}}​ = Inspection
 {{FF1036044}}​ = Lead Paint
 {{FF1036045}}​ = MRVP
 {{FF1036046}}​ = Pre-Judgement
 {{FF1036047}}​ = Post Judgment
 {{FF1036048}}​ = Priority
 {{FF1036049}}​ = Christopher Bennett
 {{FF1036050}}​ = William Brunton
 {{FF1036051}}​ = Danny Cueto
 {{FF1036052}}​ = Michelle Haska
 {{FF1036053}}​ = Mike Jones
 {{FF1036054}}​ = Jesus Martinez
 {{FF1036055}}​ = Michael McNulty
 {{FF1036056}}​ = Jermaine Mitchell
 {{FF1036057}}​ = Michael Whiting
 {{FF1036058}}​ = James Murgolo
 {{FF1037966}}​ = Colin Hoppie
 {{FF1036094}}​ = Fourth Inspection Result
 {{FF1036100}}​ = Time of Fourth Inspection
 {{FF1036149}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1035773}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1035993}}​ = Schedule Fifth Inspection
 {{FF1035994}}​ = Concentrated
 {{FF1035995}}​ = Condemnation
 {{FF1035996}}​ = Court
 {{FF1035997}}​ = Emergency
 {{FF1035998}}​ = Exterior
 {{FF1035999}}​ = Inspection
 {{FF1036000}}​ = Lead Paint
 {{FF1036001}}​ = MRVP
 {{FF1036002}}​ = Pre-Judgement
 {{FF1036003}}​ = Post Judgment
 {{FF1036004}}​ = Priority
 {{FF1036005}}​ = William Brunton
 {{FF1036006}}​ = Christopher Bennett
 {{FF1036007}}​ = Danny Cueto
 {{FF1036008}}​ = Michelle Haska
 {{FF1036009}}​ = Mike Jones
 {{FF1036010}}​ = Jesus Martinez
 {{FF1036011}}​ = Michael McNulty
 {{FF1036012}}​ = Jermaine Mitchell
 {{FF1036013}}​ = Michael Whiting
 {{FF1036014}}​ = James Murgolo
 {{FF1037961}}​ = Colin Hoppie
 {{FF1036098}}​ = Fifth Inspection Result
 {{FF1036099}}​ = Time of Fifth Inspection
 {{FF1036146}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1035774}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1035961}}​ = Schedule Sixth inspection
 {{FF1035962}}​ = Christopher Bennett
 {{FF1035963}}​ = William Brunton
 {{FF1035964}}​ = Danny Cueto
 {{FF1035965}}​ = Michelle Haska
 {{FF1035966}}​ = Mike Jones
 {{FF1035967}}​ = Jesus Martinez
 {{FF1035968}}​ = Michael McNulty
 {{FF1035969}}​ = Jermaine Mitchell
 {{FF1035970}}​ = Michael Whiting
 {{FF1035971}}​ = James Murgolo
 {{FF1036015}}​ = Concentrated
 {{FF1036016}}​ = Condemnation
 {{FF1036017}}​ = Court
 {{FF1036018}}​ = Emergency
 {{FF1036019}}​ = Exterior
 {{FF1036020}}​ = Inspection
 {{FF1036021}}​ = Lead Paint
 {{FF1036022}}​ = MRVP
 {{FF1036023}}​ = Pre-Judgement
 {{FF1036024}}​ = Post Judgment
 {{FF1036025}}​ = Priority
 {{FF1037962}}​ = Colin Hoppie
 {{FF1036102}}​ = Sixth Inspection Result
 {{FF1036103}}​ = Time of Sixth Inspection
 {{FF1036147}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1035766}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1035960}}​ = Schedule Seventh inspection
 {{FF1035972}}​ = Concentrated
 {{FF1035973}}​ = Condemnation
 {{FF1035974}}​ = Court
 {{FF1035975}}​ = Emergency
 {{FF1035976}}​ = Exterior
 {{FF1035977}}​ = Inspection
 {{FF1035978}}​ = Lead Paint
 {{FF1035979}}​ = MRVP
 {{FF1035980}}​ = Pre-Judgement
 {{FF1035981}}​ = Post Judgment
 {{FF1035982}}​ = Priority
 {{FF1035983}}​ = Christopher Bennett
 {{FF1035984}}​ = William Brunton
 {{FF1035985}}​ = Danny Cueto
 {{FF1035986}}​ = Michelle Haska
 {{FF1035987}}​ = Mike Jones
 {{FF1035988}}​ = Jesus Martinez
 {{FF1035989}}​ = Michael McNulty
 {{FF1035990}}​ = Jermaine Mitchell
 {{FF1035991}}​ = Michael Whiting
 {{FF1035992}}​ = James Murgolo
 {{FF1037968}}​ = Colin Hoppie
 {{FF1036101}}​ = Seventh Inspection Result
 {{FF1036119}}​ = Time of Seventh Inspection
 {{FF1036136}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1035767}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1035868}}​ = Schedule Eighth inspection
 {{FF1035869}}​ = Concentrated
 {{FF1035870}}​ = Condemnation
 {{FF1035871}}​ = Court
 {{FF1035872}}​ = Emergency
 {{FF1035873}}​ = Exterior
 {{FF1035874}}​ = Inspection
 {{FF1035875}}​ = Lead Paint
 {{FF1035876}}​ = MRVP
 {{FF1035877}}​ = Pre-Judgement
 {{FF1035878}}​ = Post Judgment
 {{FF1035879}}​ = Priority
 {{FF1035880}}​ = Christopher Bennett
 {{FF1035881}}​ = William Brunton
 {{FF1035882}}​ = Danny Cueto
 {{FF1035883}}​ = Michelle Haska
 {{FF1035884}}​ = Mike Jones
 {{FF1035885}}​ = Jesus Martinez
 {{FF1035886}}​ = Michael McNulty
 {{FF1035887}}​ = Jermaine Mitchell
 {{FF1035888}}​ = Michael Whiting
 {{FF1035889}}​ = James Murgolo
 {{FF1037969}}​ = Colin Hoppie
 {{FF1036118}}​ = Eighth Inspection Result
 {{FF1036120}}​ = Time of Eighth Inspection
 {{FF1036137}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1035768}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1035836}}​ = Schedule Ninth inspection
 {{FF1035847}}​ = Christopher Bennett
 {{FF1035848}}​ = William Brunton
 {{FF1035849}}​ = Danny Cueto
 {{FF1035850}}​ = Michelle Haska
 {{FF1035851}}​ = Mike Jones
 {{FF1035852}}​ = Jesus Martinez
 {{FF1035853}}​ = Michael McNulty
 {{FF1035854}}​ = Jermaine Mitchell
 {{FF1035855}}​ = Michael Whiting
 {{FF1035856}}​ = James Murgolo
 {{FF1035890}}​ = Concentrated
 {{FF1035891}}​ = Condemnation
 {{FF1035892}}​ = Court
 {{FF1035893}}​ = Emergency
 {{FF1035894}}​ = Exterior
 {{FF1035895}}​ = Inspection
 {{FF1035896}}​ = Lead Paint
 {{FF1035897}}​ = MRVP
 {{FF1035898}}​ = Pre-Judgement
 {{FF1035899}}​ = Post Judgment
 {{FF1035900}}​ = Priority
 {{FF1037967}}​ = Colin Hoppie
 {{FF1036121}}​ = Ninth Inspection Result
 {{FF1036123}}​ = Time of Ninth Inspection
 {{FF1036134}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1035764}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1035835}}​ = Schedule Tenth inspection
 {{FF1035837}}​ = Christopher Bennett
 {{FF1035838}}​ = William Brunton
 {{FF1035839}}​ = Danny Cueto
 {{FF1035840}}​ = Michelle Haska
 {{FF1035841}}​ = Mike Jones
 {{FF1035842}}​ = Jesus Martinez
 {{FF1035843}}​ = Michael McNulty
 {{FF1035844}}​ = Jermaine Mitchell
 {{FF1035845}}​ = Michael Whiting
 {{FF1035846}}​ = James Murgolo
 {{FF1035857}}​ = Concentrated
 {{FF1035858}}​ = Condemnation
 {{FF1035859}}​ = Court
 {{FF1035860}}​ = Emergency
 {{FF1035861}}​ = Exterior
 {{FF1035862}}​ = Inspection
 {{FF1035863}}​ = Lead Paint
 {{FF1035864}}​ = MRVP
 {{FF1035865}}​ = Pre-Judgement
 {{FF1035866}}​ = Post Judgment
 {{FF1035867}}​ = Priority
 {{FF1037970}}​ = New field
 {{FF1036122}}​ = Tenth Inspection Result
 {{FF1036124}}​ = Time of Tenth Inspection
 {{FF1036135}}​ = Date of Tenth Inspection

First Ticket Details
 {{FF1035735}}​ = Person whose name will appear on ticket
 {{{FF1035762}}}​ = First Ticket Notes for Administrative Staff
 {{FF1035803}}​ = First Ticket Total
 {{FF1036138}}​ = First Ticket Due Date
Second Ticket Details
 {{FF1035736}}​ = Person whose name will appear on ticket
 {{{FF1035760}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1035795}}​ = Second Ticket Total
 {{FF1036125}}​ = Second Ticket Due Date
Third Ticket Details
 {{FF1035737}}​ = Person whose name will appear on ticket
 {{{FF1035758}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1035804}}​ = Third Ticket Total
 {{FF1036133}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{FF1035738}}​ = Person whose name will appear on ticket
 {{{FF1035756}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1035796}}​ = Fourth Ticket Total
 {{FF1036132}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{FF1035739}}​ = Person whose name will appear on ticket
 {{{FF1035754}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1035797}}​ = Fifth Ticket Total
 {{FF1036131}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{FF1035740}}​ = Person whose name will appear on ticket
 {{{FF1035752}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1035798}}​ = Sixth Ticket Total
 {{FF1036130}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{FF1035741}}​ = Person whose name will appear on ticket
 {{{FF1035750}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1035799}}​ = Seventh Ticket Total
 {{FF1036129}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{FF1035742}}​ = Person whose name will appear on ticket
 {{{FF1035748}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1035800}}​ = Eighth Ticket Total
 {{FF1036128}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{FF1035743}}​ = Person whose name will appear on ticket
 {{{FF1035746}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1035801}}​ = Ninth Ticket Total
 {{FF1036127}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{FF1035744}}​ = Person whose name will appear on ticket
 {{{FF1035745}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1035802}}​ = Tenth Ticket Total
 {{FF1036126}}​ = Tenth Ticket Due Date

First Ticket
 {{{OL1035765}}}​ = Description
Second Ticket
 {{{OL1035763}}}​ = Second Ticket Description
Third Ticket
 {{{OL1035761}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1035759}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1035757}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1035755}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1035753}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1035751}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1035749}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1035747}}}​ = Tenth Ticket Description

"""

# --- Run the script and print the output ---
output = create_final_mappings(input_data)
print(output)
