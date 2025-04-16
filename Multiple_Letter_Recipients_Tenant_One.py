import re
from collections import defaultdict

# First Housing Letter
raw_mapping_data = """ {{FF1027847}}​ = Second Tenant Name
 {{FF1027848}}​ = Third Tenant Name
 {{FF1027849}}​ = Fourth Tenant Name
 {{FF1027850}}​ = Fifth Tenant Name
 {{FF1027852}}​ = First Tenant Name
 {{FF1027854}}​ = First Tenant Unit
 {{FF1027855}}​ = Second Tenant Unit
 {{FF1027856}}​ = Third Tenant Unit
 {{FF1027859}}​ = Fourth Tenant Unit
 {{FF1027860}}​ = Fifth Tenant Unit
 {{FF1027862}}​ = Sixth Tenant Name
 {{FF1027863}}​ = Sixth Tenant Unit
 {{FF1027865}}​ = Seventh Tenant Name
 {{FF1027866}}​ = Seventh Tenant Unit
 {{FF1027868}}​ = Eighth Tenant Name
 {{FF1027869}}​ = Eighth Tenant Unit
 {{FF1027871}}​ = Ninth Tenant Name
 {{FF1027872}}​ = Ninth Tenant Unit
 {{FF1027874}}​ = Tenth Tenant Name
 {{FF1027875}}​ = Tenth Tenant Unit
 {{FF1028294}}​ = Eleventh Tenant Name
 {{FF1028295}}​ = Eleventh Tenant Unit
 {{FF1028297}}​ = Twelfth Tenant Name
 {{FF1028298}}​ = Twelfth Tenant Unit
 {{FF1026924}}​ = Second Tenant
 {{FF1027844}}​ = Third Tenant
 {{FF1027845}}​ = Fourth Tenant
 {{FF1027846}}​ = Fifth Tenant
 {{FF1027853}}​ = First Tenant
 {{FF1027861}}​ = Sixth Tenant
 {{FF1027864}}​ = Seventh Tenant
 {{FF1027867}}​ = Eighth Tenant
 {{FF1027870}}​ = Ninth Tenant
 {{FF1027873}}​ = Tenth Tenant
 {{FF1028293}}​ = Eleventh Tenant
 {{FF1028296}}​ = Twelfth Tenant
 {{FF1026620}}​ = First Tenant Phone Number
  """

# Second Housing Letter
# raw_mapping_data = """
# {{FF1027847}}​ = Second Tenant Name
# {{FF1027848}}​ = Third Tenant name
# {{FF1027849}}​ = Fourth Tenant Name
# {{FF1027850}}​ = Fifth Tenant Name
# {{FF1027852}}​ = First Tenant Name
# {{FF1027854}}​ = First Tenant Unit
# {{FF1027855}}​ = Second Tenant Unit
# {{FF1027856}}​ = Third Tenant Unit
# {{FF1027859}}​ = Fourth Tenant Unit
# {{FF1027860}}​ = Fifth Tenant Unit
# {{FF1027862}}​ = Sixth Tenant Name
# {{FF1027863}}​ = Sixth Tenant Unit
# {{FF1027865}}​ = Seventh Tenant Name
# {{FF1027866}}​ = Seventh Tenant Unit
# {{FF1027868}}​ = Eighth Tenant Name
# {{FF1027869}}​ = Eighth Tenant Unit
# {{FF1027871}}​ = Ninth Tenant Name
# {{FF1027872}}​ = Ninth Tenant Unit
# {{FF1027874}}​ = Tenth Tenant Name
# {{FF1027875}}​ = Tenth Tenant Unit
# {{FF1028294}}​ = Eleventh Tenant Name
# {{FF1028295}}​ = Eleventh Tenant Unit
# {{FF1028297}}​ = Twelfth Tenant Name
# {{FF1028298}}​ = Twelfth Tenant Unit
# {{FF1027844}}​ = Third Tenant
# {{FF1027845}}​ = Fourth Tenant
# {{FF1027846}}​ = Fifth Tenant
# {{FF1027853}}​ = First Tenant
# {{FF1027861}}​ = Sixth Tenant
# {{FF1027864}}​ = Seventh Tenant
# {{FF1027867}}​ = Eighth Tenant
# {{FF1027870}}​ = Ninth Tenant
# {{FF1027873}}​ = Tenth Tenant
# {{FF1028293}}​ = Eleventh Tenant
# {{FF1028296}}​ = Twelfth Tenant
# {{FF1026924}}​ = Second Tenant
# """

# 🔹 Paste your original template using First Tenant's codes
original_template = """
<div>{{#if FF1027853}}</div>

<table style="width: 100%; margin-left: calc(0%); margin-right: calc(0%);">
	<tbody>
		<tr>
			<td colspan="5" style="width: 99.9432%;">
				<div style="text-align: center;"><span style="font-family:Arial;color:#000000;font-size:8pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>ESTE ES UN IMPORTANTE DOCUMENTO LEGAL EL CUAL LE PUEDE AFECTAR SUS DERECHOS. DEBE TENERLO TRADUCIDO.</strong></span><strong>&nbsp;</strong></div>
			</td>
		</tr>
		<tr>
			<td style="width: 15.6939%;">
				<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
			</td>
			<td colspan="3" style="width: 68.9494%;">
				<div style="text-align: center;"><span style="font-family:Times New Roman;color:#000000;font-size:16pt;font-weight:400;font-style:italic;text-decoration:none;"><strong>THE COMMONWEALTH OF MASSACHUSETTS</strong></span>
					<br><span style="font-family:Times New Roman;color:#000000;font-size:16pt;font-weight:400;font-style:italic;text-decoration:none;"><strong><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:italic;text-decoration:none;">To the Sheriff&#39;s of our several Counties, or their Deputies, or any <br>Constable of any City or Town within our said Commonwealth:</span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><br>DEPARTMENT OF CODE ENFORCEMENT, HOUSING DIVISION, GREETING.<br>We Command you to serve the below described person or legal entity:</span>&nbsp;</strong></span><strong>&nbsp;</strong><strong><br></strong></div>
			</td>
			<td style="width: 15.2955%;">

				<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="width: 37.5709%;">
				<br>
			</td>
			<td style="width: 38.58%;"><strong><br></strong></td>
			<td style="width: 8.4761%;"><strong><br></strong></td>
			<td style="width: 15.2955%;"><strong><br></strong></td>
		</tr>
	</tbody>
</table>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 19.4039%;">
				<br>
			</td>
			<td style="width: 80.5353%;"><span style='color: rgb(0, 0, 0); font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>{{FF1027852}}<br></span><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="color: rgb(0, 0, 0); font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">{{#if FF1027854}}, Unit&nbsp;</span><span style="color: rgb(0, 0, 0); font-size: 14px;color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">{{FF1027854}}</span><span style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">&nbsp;{{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1026624}}{{/if}}</strong></span></span></span></span></span></span>
				<br>
				</span><span style="color: rgb(0, 0, 0); font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{city}}, {{state}} {{zipCode}}</span></strong></span></span></span></span></span></span></span></span></span></span></span><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">&nbsp;<br><span style="font-size: 14px;">Parcel:&nbsp;{{mbl}}</span></span>
				<br>
			</td>
		</tr>
	</tbody>
</table>

<table style="width: 100%; margin-left: calc(0%); margin-right: calc(0%);">
	<tbody>
		<tr>
			<td style="width: 76.1689%;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 14px; font-weight: 400; font-style: normal; text-decoration: none;'>Owner, occupant, tenant, or agent of property located in the City of Springfield at:</span></td>
			<td style="width: 8.4761%;"><strong><br></strong></td>
			<td style="width: 15.2955%;"><strong><span style="font-size: 14px;"><br></span></strong></td>
		</tr>
		<tr>
			<td colspan="3" style="width: 99.9392%; text-align: center;"><span style="font-size: 14px;"><span style='font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>&nbsp; &nbsp; &nbsp;&nbsp;</span></span><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">&nbsp;</span>
				<br><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>&nbsp;{{streetNo}} {{streetName}}{{#if unit}}, Unit {{unit}} {{/if}} {{#if FF39670}}, {{FF1026624}}{{/if}}, {{city}}, {{state}} {{zipCode}}</strong><strong><br></strong></span></td>
		</tr>
	</tbody>
</table>
<div>
	<hr style="border: none; height: 3px; background-color: #000;">
</div>
<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">That the Deputy Director, Department of Code Enforcement - Housing Division, City of Springfield, has adjudged certain private property which you own, manage or occupy is in violation of the State Sanitary Code Chapter II: Minimum Standards of Fitness for Human Habitation - 105 CMR 410.000 authorized under Chapter 111 Section 127A of the Massachusetts General Laws to wit:</span></div>
<div>
	<br>
</div>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 61.2699%;"><strong><u><span style='font-family: "Times New Roman", Times, serif, -webkit-standard; font-size: 14px;'>EMERGENCY VIOLATIONS</span></u></strong>
				<br>
			</td>
			<td style="width: 38.6696%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">DATE: {{currentDate}}</span></strong>
				<br>
			</td>
		</tr>
	</tbody>
</table>
<div>
	<br>

	<table style="width: 100%;">
		<thead>
			<tr>
				<td style="width: 19.7689%;">
					<br>
				</td>
				<td style="padding: 5px; width: 9.0337%;"><span style='font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>Unit</span></td>
				<td style="padding: 5px; width: 18.4801%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Responsibility</span></td>
				<td style="padding: 5px; width: 10.947%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Fix By</span></td>
				<td style="padding:5px; width:10%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Status</span></td>
				<td style="padding:5px; width:32%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Violation and Notes</span></td>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td style="width: 19.7689%;">{{{OL1026795}}}</td>
				<td style="padding: 5px; width: 9.0337%;"><span style="font-size: 12px;">{{{OL1027833}}}</span></td>
				<td style="padding: 5px; width: 18.4801%;"><span style="font-size: 12px;">{{{OL1027837}}}</span></td>
				<td style="padding: 5px; width: 10.947%;"><span style="font-size: 12px;">{{{OL1026794}}}</span></td>
				<td style="padding:5px;"><span style="font-size: 12px;">{{{OL1026796}}}</span></td>
				<td style="padding:5px;"><span style="font-size: 12px;">{{{OL1027834}}}</span></td>
			</tr>
		</tbody>
	</table>

	<p>
		<br>
	</p>

	<p><strong><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">HEREOF FAIL NOT, under penalty of law to comply with said Sanitary Code, within FORTHWITH. &nbsp;Please see other side regarding your Right to a Hearing.</span></strong></p>

	<p><strong><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">CERTIFIED LETTERS</span></strong></p>

	<table style="width: 100%;">
		<tbody>
			<tr>
				<td class="frcustomborder" style="width: 33.3333%;">Date Sent</td>
				<td class="frcustomborder" style="width: 33.3333%;">Recipient</td>
				<td class="frcustomborder" style="width: 33.3333%;">Certified Number</td>
			</tr>
			<tr>
				<td class="frcustomborder" style="width: 33.3333%;">{{{OL1026700}}}
					<br>
				</td>
				<td class="frcustomborder" style="width: 33.3333%;">{{{OL1026701}}}
					<br>
				</td>
				<td class="frcustomborder" style="width: 33.3333%;">{{{OL1026699}}}
					<br>
				</td>
			</tr>
		</tbody>
	</table>

	<table style="width: 100%; margin-right: calc(0%);">
		<tbody>
			<tr>
				<td style="width: 22.6714%;"><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/housing_director_signature_Tue_Mar_18_2025_16:36:22_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 300px;" class="fr-fic fr-dib"></td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">
					<br>
				</td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">Keith D. O&#39;Connor</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">{{#if FF1027300}}Christopher Bennett{{/if}}{{#if FF1027308}}William Brunton{{/if}}{{#if FF1027309}}Danny Cueto{{/if}}{{#if FF1027310}}Michelle Haska{{/if}}{{#if FF1027311}}Mike Jones{{/if}}{{#if FF1027312}}Jesus Martinez{{/if}}{{#if FF1027313}}Michael McNulty{{/if}}{{#if FF1027314}}Jermain Mitchell{{/if}}{{#if FF1027315}}Michael Whiting{{/if}}{{#if FF1027316}}James Murgolo{{/if}}
					<br>
				</td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">Deputy Director of Code Enforcement</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">Code Enforcement Inspector</td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">Housing Division</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">
					<br>
				</td>
			</tr>
			<tr>
				<td colspan="5" style="width: 99.9433%; text-align: center;"><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">Compensation Will Not Be Allowed Unless Officer&#39;s<br>Return Contains A Bill of Item, Together with Affidavit</span></td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">
					<br>
				</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%; text-align: center;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">{{currentDate}}
					<br>
				</td>
			</tr>
		</tbody>
	</table>
	<br>
	<br>

	<p style="page-break-before: always;"><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">By virtue of this Writ, I this day served the before described person or entity by:<br>(CROSS OUT THOSE THAT DO NOT APPLY)<br><br>1. Personally.<br><br>2. By leaving a copy of the order at this last and usual place of adobe.<br><br>3. The premises are unoccupied and the residence of the owner or agent is unknown or is without the Commonwealth, therefore, I posted the order in a conspicuous place on the premises.<br><br>&nbsp; &nbsp; A true copy. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Attest: ___________________________________________________________<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (Constable)<br><br>Fees, ________________________<br>Service, ______________________<br>Travel, _______________________<br><br>(If served other than personally please state reason)<br><br>______________________________________________________________________________________<br><br>______________________________________________________________________________________<br><br>______________________________________________________________________________________<br><br>______________________________________________________________________________________<br><br>NOTICE IN COMPLIANCE WITH SANITARY CODE</span></p>

	<p style="page-break-before: always;">
		<br>
	</p>
</div>
<div>{{/if}}</div>

"""

# Step 1: Parse mapping into structured dictionary
cleaned_data = (
    raw_mapping_data
    .encode("ascii", "ignore")        # strip non-ASCII characters
    .decode("ascii")
    .replace("\u200b", "")            # zero-width space
    .replace("\u00a0", " ")           # non-breaking space
    .replace("’", "'")                # curly apostrophe
    .replace("“", '"').replace("”", '"')  # curly quotes
)
grouped_dict = defaultdict(dict)

pattern = re.compile(r"\{\{(FF\d+)\}}\s*=\s*(.+?)\s*$", re.IGNORECASE)

for line in cleaned_data.strip().splitlines():
    match = pattern.search(line.strip())
    if match:
        code, label = match.groups()
        label = label.strip()
        label_lower = label.lower()

        ordinal_match = re.match(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth)", label_lower)
        if ordinal_match:
            ordinal = ordinal_match.group(1).capitalize()
            if "name" in label_lower:
                grouped_dict[ordinal]["Name"] = code
            elif "unit" in label_lower:
                grouped_dict[ordinal]["Unit"] = code
            elif re.search(r"^\w+ tenant$", label_lower):  # e.g., "first tenant"
                grouped_dict[ordinal]["Tenant"] = code

# Step 2: Detect which specific codes are used in the template
used_codes = re.findall(r"\{\{#?if\s*(FF\d+)\}\}|\{\{(FF\d+)\}\}", original_template)
used_codes_flat = set(filter(None, [item for pair in used_codes for item in pair]))  # flatten and remove None

# Step 3: Create full reverse mapping from code → kind
code_meaning_map = {}
for kind in ["Tenant", "Name", "Unit"]:
    for ordinal, data in grouped_dict.items():
        code = data.get(kind)
        if code:
            code_meaning_map[code] = kind

# 🔹 Debug: Print out the grouped code map
print("🔍 Tenant Code Map:")
for ordinal in grouped_dict:
    print(f"{ordinal}: {grouped_dict[ordinal]}")
print("-" * 50)

# Step 4: Generate blocks for each tenant
order = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
output_blocks = []

for ordinal in order:
    tenant_data = grouped_dict.get(ordinal)
    if not tenant_data:
        continue

    block = original_template

    for first_code, kind in code_meaning_map.items():
        first_tenant_code = grouped_dict["First"].get(kind)
        if not first_tenant_code:
            continue
        replacement_code = tenant_data.get(kind)
        if not replacement_code:
            continue

        pattern = re.compile(
            rf"(\{{{{#if )({re.escape(first_tenant_code)})(_[\w\d]+)?\}}}}|\{{{{({re.escape(first_tenant_code)})(_[\w\d]+)?\}}}}"
        )

        def repl(match):
            if match.group(1):  # it's a {{#if ...}}
                suffix = match.group(3) or ""
                return f"{{{{#if {replacement_code}{suffix}}}}}"
            else:  # it's a normal {{...}}
                suffix = match.group(5) or ""
                return f"{{{{{replacement_code}{suffix}}}}}"

        block = pattern.sub(repl, block)

    output_blocks.append(block)

# Step 5: Write to file
print("✅ Output blocks generated:", len(output_blocks))

with open("Results.html", "w", encoding="utf-8") as f:
    for block in output_blocks:
        f.write(block + "\n\n")

print("✅ All variations written to output.html")
