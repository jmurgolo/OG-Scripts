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
General Info
 {{FF1035688}}​ = Inspection Access Contact Name
 {{FF1035689}}​ = Inspection Access Contact Phone
 {{FF1035690}}​ = Inspection Access Contact Title
 {{FF1035691}}​ = Other Source
 {{FF1035692}}​ = When & how did you contact them
 {{FF1035693}}​ = Who did you contact
 {{FF1035694}}​ = Unit Number - to be printed on the inspection report
 {{FF1035695}}​ = First Tenant Name
 {{FF1035696}}​ = First Tenant Unit
 {{FF1035697}}​ = First Tenant Phone Number
 {{FF1035698}}​ = Second Tenant Name
 {{FF1035699}}​ = Second Tenant Unit
 {{FF1035700}}​ = Third Tenant Name
 {{FF1035701}}​ = Third Tenant Unit
 {{FF1035702}}​ = Fourth Tenant Name
 {{FF1035703}}​ = Fourth Tenant Unit
 {{FF1035704}}​ = Fifth Tenant Name
 {{FF1035705}}​ = Fifth Tenant Unit
 {{FF1035706}}​ = Sixth Tenant Name
 {{FF1035707}}​ = Sixth Tenant Unit
 {{FF1035708}}​ = Seventh Tenant Name
 {{FF1035709}}​ = Seventh Tenant Unit
 {{FF1035710}}​ = Eighth Tenant Name
 {{FF1035711}}​ = Eighth Tenant Unit
 {{FF1035712}}​ = Ninth Tenant Name
 {{FF1035713}}​ = Ninth Tenant Unit
 {{FF1035714}}​ = Tenth Tenant Name
 {{FF1035715}}​ = Tenth Tenant Unit
 {{FF1035716}}​ = Eleventh Tenant Name
 {{FF1035717}}​ = Eleventh Tenant Unit
 {{FF1035718}}​ = Twelfth Tenant Name
 {{FF1035719}}​ = Twelfth Tenant Unit
 {{FF1035720}}​ = Alternative Owner Name
 {{FF1035721}}​ = Second Owner Name
 {{FF1035722}}​ = Third Owner Name
 {{FF1036863}}​ = If Condemnation it Applies to
 {{FF1036866}}​ = Condemnation Unit
 {{FF1036867}}​ = Condemnation Address
 {{{FF1035778}}}​ = Refer to Office of Housing Details
 {{{FF1035779}}}​ = Refer to Zoning Details
 {{{FF1035780}}}​ = Refer to Court Details
 {{{FF1035781}}}​ = Refer to Building Details
 {{{FF1035782}}}​ = Refer to Electrical Details
 {{{FF1035783}}}​ = Refer to Plumbing Details
 {{{FF1035784}}}​ = Refer to Fire Details
 {{{FF1035785}}}​ = Refer to Police Ordinance Details
 {{{FF1035786}}}​ = Refer to Health Department Details
 {{{FF1035787}}}​ = Refer to Elderly Affairs Details
 {{{FF1035788}}}​ = Refer to Animal Control Details
 {{{FF1035789}}}​ = Third Owner Address
 {{{FF1035790}}}​ = Second Owner Address
 {{{FF1035791}}}​ = Alternative Owner Address (Shift Enter for only one space between lines)
 {{{FF1035792}}}​ = What was the response
 {{{FF1035793}}}​ = 311 Description
 {{{FF1035794}}}​ = General Notes (Internal)
 {{FF1035901}}​ = Interior
 {{FF1035902}}​ = Exterior
 {{FF1035903}}​ = 311
 {{FF1035904}}​ = Sixth Tenant
 {{FF1035905}}​ = Fifth Tenant
 {{FF1035906}}​ = Fourth Tenant
 {{FF1035907}}​ = Third Tenant
 {{FF1035908}}​ = Second Tenant
 {{FF1035909}}​ = Have you contacted the owner
 {{FF1035910}}​ = First Tenant
 {{FF1035911}}​ = Add Second Additional Owner
 {{FF1035912}}​ = Twelfth Tenant
 {{FF1035913}}​ = Eleventh Tenant
 {{FF1035914}}​ = Tenth Tenant
 {{FF1035915}}​ = Ninth Tenant
 {{FF1035916}}​ = Eighth Tenant
 {{FF1035917}}​ = Seventh Tenant
 {{FF1035918}}​ = Add Third Additional Owner
 {{FF1035919}}​ = Order to Vacant Owner
 {{FF1035920}}​ = Order To Vacate Tenant
 {{FF1035921}}​ = Posting of Name of Owner
 {{FF1035922}}​ = GSSSI and/or DPPC Referral
 {{FF1035923}}​ = Condemnation Owner
 {{FF1035924}}​ = Condemnation Tenant
 {{FF1035925}}​ = Owner Different than GIS
 {{FF1035926}}​ = Refer to Court
 {{FF1035927}}​ = Refer to Office of Housing
 {{FF1035928}}​ = Refer to Animal Control
 {{FF1035929}}​ = Refer to Elderly Affairs
 {{FF1035930}}​ = Refer to Health Department
 {{FF1035931}}​ = Refer to Police Ordinance
 {{FF1035932}}​ = Refer to Fire Department
 {{FF1035933}}​ = Refer to Electrical Enforcement
 {{FF1035934}}​ = Refer to Plumbing Enforcement
 {{FF1035935}}​ = Refer to Building Enforcement
 {{FF1035937}}​ = Refer to Zoning
 {{FF1036864}}​ = Adjust Unit for Condemnation
 {{FF1036865}}​ = Adjust Entire Address for Condemnation
 {{FF1037926}}​ = Emergency
 {{FF1036113}}​ = Violation Observed/Demand Access?
 {{FF1036114}}​ = Emergency Violations Observed
 {{FF1036115}}​ = Unregistered Motor Vehicles Observed
 {{FF1036116}}​ = Lead Inspection Required
 {{FF1036117}}​ = Complaint Source
 {{FF1036139}}​ = When did the problem first occur
 {{FF1036140}}​ = Condemnation Inspection Date for Letter
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
 {{FF1036122}}​ = Tenth Inspection Result
 {{FF1036124}}​ = Time of Tenth Inspection
 {{FF1036135}}​ = Date of Tenth Inspection
Letters
 {{FF1035805}}​ = Send First Access Demand
 {{FF1035806}}​ = Send Second Access Demand
 {{FF1035807}}​ = Send Third Access Demand
 {{FF1035808}}​ = Send Fourth Access Demand
 {{FF1035809}}​ = Send Fifth Access Demand
 {{FF1035810}}​ = Send Sixth Access Demand
 {{FF1035811}}​ = Send Seventh Access Demand
 {{FF1035812}}​ = Send Eighth Access Demand
 {{FF1035813}}​ = Send Ninth Access Demand
 {{FF1035814}}​ = Send Tenth Access Demand
 {{FF1035815}}​ = Send First Violation Letters
 {{FF1035816}}​ = Send Second Violation Letters
 {{FF1035817}}​ = Send Third Violation Letters
 {{FF1035818}}​ = Send Fourth Violation Letters
 {{FF1035819}}​ = Send Fifth Violation Letters
 {{FF1035820}}​ = Send Sixth Violation Letters
 {{FF1035821}}​ = Send Seventh Violation Letters
 {{FF1035822}}​ = Send Eighth Violation Letters
 {{FF1035823}}​ = Send Ninth Violation Letters
 {{FF1035824}}​ = Send Tenth Violation Letters
 {{FF1035825}}​ = Send First Emergency Letters
 {{FF1035826}}​ = Send Second Emergency Letters
 {{FF1035827}}​ = Send Third Emergency Letters
 {{FF1035828}}​ = Send Fourth Emergency Letters
 {{FF1035829}}​ = Send Fifth Emergency Letters
 {{FF1035830}}​ = Send Sixth Emergency Letters
 {{FF1035831}}​ = Send Seventh Emergency Letters
 {{FF1035832}}​ = Send Eighth Emergency Letters
 {{FF1035833}}​ = Send Ninth Emergency Letters
 {{FF1035834}}​ = Send Tenth Emergency Letters
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

Multi Entry Section Entries:
Please note that object list entries are marked with three curly brackets, not two.


Code Case Violations
 {{{OL1035723}}}​ = Unit(s)
 {{{OL1035777}}}​ = Code / Description
 {{{OL1036107}}}​ = Responsible Party
 {{{OL1036108}}}​ = Status
 {{{OL1036141}}}​ = Correction Required By:
 {{{OL1036196}}}​ = Picture
Unregistered Motor Vehicles
 {{{OL1035724}}}​ = License Plate #
 {{{OL1035725}}}​ = VIN #
 {{{OL1035776}}}​ = Comments
 {{{OL1036109}}}​ = Status
 {{{OL1036110}}}​ = Make
 {{{OL1036111}}}​ = Model
 {{{OL1036112}}}​ = Color
 {{{OL1036142}}}​ = Correction Required By:
 {{{OL1036195}}}​ = Picture
Certified Letters
 {{{OL1035726}}}​ = Recipient
 {{{OL1035727}}}​ = Cc
 {{{OL1035732}}}​ = Certified Number
 {{{OL1036144}}}​ = Date sent
Family Breakdown Adult
 {{{OL1035728}}}​ = First Name
 {{{OL1035729}}}​ = Middle Name
 {{{OL1035730}}}​ = Last Name
 {{{OL1035731}}}​ = First Child Name
 {{{OL1035938}}}​ = First Child Six and Under
 {{{OL1036145}}}​ = First Child Date of Birth
Emergency Violations
 {{{OL1035733}}}​ = Unit
 {{{OL1035775}}}​ = Code / Description
 {{{OL1036105}}}​ = Responsible Party
 {{{OL1036106}}}​ = Status
 {{{OL1036143}}}​ = Correction Required By:
 {{{OL1036194}}}​ = Picture
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

Multi Entry Sections:
Please note that multiEntry sections are marked with three curly brackets, not two.


 {{{MES1013214}}}​ = Code Case Violations
 {{{MES1013215}}}​ = Unregistered Motor Vehicles
 {{{MES1013216}}}​ = Certified Letters
 {{{MES1013217}}}​ = Family Breakdown Adult
 {{{MES1013218}}}​ = Emergency Violations
 {{{MES1013230}}}​ = First Ticket
 {{{MES1013233}}}​ = Second Ticket
 {{{MES1013235}}}​ = Third Ticket
 {{{MES1013237}}}​ = Fourth Ticket
 {{{MES1013239}}}​ = Fifth Ticket
 {{{MES1013241}}}​ = Sixth Ticket
 {{{MES1013243}}}​ = Seventh Ticket
 {{{MES1013245}}}​ = Eighth Ticket
 {{{MES1013247}}}​ = Ninth Ticket
 {{{MES1013249}}}​ = Tenth Ticket

Fees:
 {{FEE514}}​ = Violation Fee
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
 {{assignedToTS2163}}​ = 311
 {{assignedToTS2111}}​ = Send Out Record Letters
 {{assignedToTS2058}}​ = Order to Vacate Owner Letter
 {{assignedToTS2059}}​ = Order to Vacate Tenant Letter
 {{assignedToTS2054}}​ = Condemnation Owner Letter
 {{assignedToTS2179}}​ = Condemnation Placard Owner
 {{assignedToTS2114}}​ = Condemnation Tenant Letter
 {{assignedToTS2180}}​ = Condemnation Placard Tenant
 {{assignedToTS2060}}​ = Posting of Name of Owner Letter
 {{assignedToTS2047}}​ = Housing Inspection Letter - No Violations
 {{assignedToTS2115}}​ = GSSSI and/or DPPC Referral
 {{assignedToTS2112}}​ = Send Out First Inspection Letters
 {{assignedToTS2037}}​ = First Violation Letter Owner
 {{assignedToTS2143}}​ = First Violation Letter Tenant
 {{assignedToTS2057}}​ = First Emergency Letter Owner
 {{assignedToTS2153}}​ = First Emergency Letter Tenant
 {{assignedToTS2110}}​ = First Access Demand Letter
 {{assignedToTS2113}}​ = Approve First Ticket
 {{assignedToTS2053}}​ = First Ticket
 {{assignedToTS2116}}​ = Send Out Second Inspection Letters
 {{assignedToTS2038}}​ = Second Violation Letter Owner
 {{assignedToTS2144}}​ = Second Violation Letter Tenant
 {{assignedToTS2073}}​ = Second Emergency Letter Owner
 {{assignedToTS2154}}​ = Second Emergency Letter Tenant
 {{assignedToTS2134}}​ = Second Access Demand Letter
 {{assignedToTS2117}}​ = Approve Second Ticket
 {{assignedToTS2072}}​ = Second Ticket
 {{assignedToTS2118}}​ = Send Out Third Inspection Letters
 {{assignedToTS2039}}​ = Third Violation Letter Owner
 {{assignedToTS2145}}​ = Third Violation Letter Tenant
 {{assignedToTS2080}}​ = Third Emergency Letter Owner
 {{assignedToTS2155}}​ = Third Emergency Letter Tenant
 {{assignedToTS2056}}​ = Third Last and Final
 {{assignedToTS2135}}​ = Third Access Demand Letter
 {{assignedToTS2126}}​ = Approve Third Ticket
 {{assignedToTS2081}}​ = Third Ticket
 {{assignedToTS2119}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS2040}}​ = Fourth Violation Letter Owner
 {{assignedToTS2146}}​ = Fourth Violation Letter Tenant
 {{assignedToTS2083}}​ = Fourth Emergency Letter Owner
 {{assignedToTS2156}}​ = Fourth Emergency Letter Tenant
 {{assignedToTS2084}}​ = Fourth Last and Final
 {{assignedToTS2136}}​ = Fourth Access Demand Letter
 {{assignedToTS2127}}​ = Approve Fourth Ticket
 {{assignedToTS2085}}​ = Fourth Ticket
 {{assignedToTS2120}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS2041}}​ = Fifth Violation Letter Owner
 {{assignedToTS2147}}​ = Fifth Violation Letter Tenant
 {{assignedToTS2087}}​ = Fifth Emergency Letter Owner
 {{assignedToTS2157}}​ = Fifth Emergency Letter Tenant
 {{assignedToTS2088}}​ = Fifth Last and Final
 {{assignedToTS2137}}​ = Fifth Access Demand Letter
 {{assignedToTS2128}}​ = Approve Fifth Ticket
 {{assignedToTS2089}}​ = Fifth Ticket
 {{assignedToTS2121}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS2042}}​ = Sixth Violation Letter Owner
 {{assignedToTS2148}}​ = Sixth Violation Letter Tenant
 {{assignedToTS2091}}​ = Sixth Emergency Letter Owner
 {{assignedToTS2158}}​ = Sixth Emergency Letter Tenant
 {{assignedToTS2092}}​ = Sixth Last and Final
 {{assignedToTS2138}}​ = Sixth Access Demand Letter
 {{assignedToTS2129}}​ = Approve Sixth Ticket
 {{assignedToTS2093}}​ = Sixth Ticket
 {{assignedToTS2122}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS2043}}​ = Seventh Violation Letter Owner
 {{assignedToTS2149}}​ = Seventh Violation Letter Tenant
 {{assignedToTS2096}}​ = Seventh Emergency Letter Owner
 {{assignedToTS2159}}​ = Seventh Emergency Letter Tenant
 {{assignedToTS2095}}​ = Seventh Last and Final
 {{assignedToTS2139}}​ = Seventh Access Demand Letter
 {{assignedToTS2130}}​ = Approve Seventh Ticket
 {{assignedToTS2097}}​ = Seventh Ticket
 {{assignedToTS2123}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS2044}}​ = Eighth Violation Letter Owner
 {{assignedToTS2150}}​ = Eighth Violation Letter Tenant
 {{assignedToTS2103}}​ = Eighth Emergency Letter Owner
 {{assignedToTS2160}}​ = Eighth Emergency Letter Tenant
 {{assignedToTS2104}}​ = Eight Last and Final
 {{assignedToTS2140}}​ = Eighth Access Demand Letter
 {{assignedToTS2131}}​ = Approve Eighth Ticket
 {{assignedToTS2101}}​ = Eighth Ticket
 {{assignedToTS2124}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS2045}}​ = Ninth Violation Letter Owner
 {{assignedToTS2151}}​ = Ninth Violation Letter Tenant
 {{assignedToTS2099}}​ = Ninth Emergency Letter Owner
 {{assignedToTS2161}}​ = Ninth Emergency Letter Tenant
 {{assignedToTS2100}}​ = Ninth Last and Final
 {{assignedToTS2141}}​ = Ninth Access Demand Letter
 {{assignedToTS2132}}​ = Approve Ninth Ticket
 {{assignedToTS2105}}​ = Ninth Ticket
 {{assignedToTS2125}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS2046}}​ = Tenth Violation Letter Owner
 {{assignedToTS2152}}​ = Tenth Violation Letter Tenant
 {{assignedToTS2107}}​ = Tenth Emergency Letter Owner
 {{assignedToTS2162}}​ = Tenth Emergency Letter Tenant
 {{assignedToTS2142}}​ = Tenth Access Demand Letter
 {{assignedToTS2133}}​ = Approve Tenth Ticket
 {{assignedToTS2108}}​ = Tenth Ticket
 {{assignedToTS2070}}​ = Tenth Inspection Date and Time
 {{assignedToTS2069}}​ = Ninth Inspection Date and Time
 {{assignedToTS2068}}​ = Eighth Inspection Date and Time
 {{assignedToTS2067}}​ = Seventh Inspection Date and Time
 {{assignedToTS2066}}​ = Sixth Inspection Date and Time
 {{assignedToTS2065}}​ = Fifth Inspection Date and Time
 {{assignedToTS2064}}​ = Fourth Inspection Date and Time
 {{assignedToTS2063}}​ = Third Inspection Date and Time
 {{assignedToTS2062}}​ = Second Inspection Date and Time
 {{assignedToTS2061}}​ = First Inspection Date and Time
 {{assignedToTS2109}}​ = Tenth Violation Fee
 {{assignedToTS2106}}​ = Ninth Violation Fee
 {{assignedToTS2102}}​ = Eighth Violation Fee
 {{assignedToTS2098}}​ = Seventh Violation Fee
 {{assignedToTS2094}}​ = Sixth Violation Fee
 {{assignedToTS2090}}​ = Fifth Violation Fee
 {{assignedToTS2086}}​ = Fourth Violation Fee
 {{assignedToTS2082}}​ = Third Violation Fee
 {{assignedToTS2071}}​ = Second Violation Fee
 {{assignedToTS2048}}​ = First Violation Fee
 {{assignedToTS2049}}​ = Refer to Court
 {{assignedToTS2052}}​ = Refer to Plumbing Enforcement
 {{assignedToTS2074}}​ = Refer to Animal Control
 {{assignedToTS2051}}​ = Refer to Electrical Enforcement
 {{assignedToTS2075}}​ = Refer to Police Ordinance
 {{assignedToTS2076}}​ = Refer to Health Department
 {{assignedToTS2050}}​ = Refer to Building Enforcement
 {{assignedToTS2079}}​ = Refer to Zoning
 {{assignedToTS2078}}​ = Refer to Office of Housing
 {{assignedToTS2077}}​ = Refer to Elderly Affairs
 {{assignedToTS2055}}​ = Refer to Fire
"""

# --- Run the script and print the output ---
output = create_grouped_mappings_with_special_conditions(input_data)
print(output)