import re
from collections import defaultdict

# 🔹 Paste your mapping data here
raw_mapping_data = """
{{FF1027847}}​ = Second Tenant Name
{{FF1027848}}​ = Third Tenant name
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
{{FF1026924}}​ = Second Tenant
"""

# 🔹 Paste your original template using First Tenant's codes
original_template = """{{#if FF1027853}}
<table style="width: 100%; margin-left: calc(0%);">
	<tbody>
		<tr>
			<td style="width: 15.6939%;">
				<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
			</td>
			<td colspan="3" style="width: 68.7663%;">
				<div style="text-align: center;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>City of Springfield</strong></span></div>

				<p style="text-align: center; padding: 0pt;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 18px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>Code Enforcement</strong></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>&nbsp;</strong></span></p>

				<p style="text-align: center; padding: 0pt;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">Housing Division<br>70 Tapley St.<br>Springfield, MA 01104<br>Telephone: (413) 787-6730<br>Fax: 413-886-5348</span></p>
			</td>
			<td style="width: 15.4587%;">

				<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="width: 37.5709%;">
				<br>
			</td>
			<td style="width: 33.6719%;"><strong><br></strong></td>
			<td style="width: 13.2022%;"><strong><br></strong></td>
			<td style="width: 15.4588%;"><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%;"><span style="font-size: 12px;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-size: 14px;">{{FF1027852}}<br>&nbsp; &nbsp; &nbsp; &nbsp;{{streetNo}} {{streetName}}{{#if FF1027854}}, Unit {{FF1027854}} {{/if}}<br>&nbsp; &nbsp; &nbsp; &nbsp;{{city}}, {{state}} {{zipCode}}</span><span style="font-size: 12px;">&nbsp;&nbsp;</span> <span style="font-size: 12px; color: rgb(0, 0, 0);">&nbsp; &nbsp;</span><span style="font-size: 14px; color: rgb(0, 0, 0);">&nbsp;</span>
				<br>
				<br>
			</td>
		</tr>
		<tr>
			<td colspan="3" style="width: 71.2533%;"><span style="font-size: 14px;"><span style="font-size: 14px;">&nbsp; &nbsp; &nbsp; &nbsp;</span>Re:&nbsp;{{streetNo}} {{streetName}}{{#if FF1027854}}, Unit {{FF1027854}} {{/if}}
				<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{{city}}, {{state}} {{zipCode}}</span><strong><br></strong></td>
			<td style="width: 13.2022%; text-align: right; vertical-align: top;"><span style="font-size: 12px;">Parcel:&nbsp;</span>&nbsp;</td>
			<td style="width: 15.4588%; text-align: left; vertical-align: top;"><span style="font-size: 12px;">{{mbl}}</span></td>
		</tr>
		<tr>
			<td style="width: 15.6939%;"><strong><br></strong></td>
			<td style="width: 21.8933%;"><strong><br></strong></td>
			<td style="width: 33.6719%;"><strong><br></strong></td>
			<td style="width: 13.2022%; text-align: right;"><span style="font-size: 12px;">Case Number:</span></td>
			<td style="width: 15.4588%;"><span style="font-size: 12px;">{{recordId}}</span><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: center;">
				<br><span style="font-family:Arial;color:#000000;font-size:16pt;font-weight:700;font-style:normal;text-decoration:underline;">FIRST NOTICE OF VIOLATIONS</span>&nbsp;</td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: left;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">As a result of an inspection that was performed on the above property on&nbsp;</span>{{FF1026615}}<span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">, conditions were found to exist that amount to a violation of the Massachusetts State Sanitary Code (105 CMR 410.000 State Sanitary Code Chapter II: Minimum Standards of Fitness for Human Habitation). Property records indicate that you are the party responsible for this premises either by ownership, occupation, or control.<br><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:700;font-style:normal;text-decoration:none;">A full list of the violations may be found on the attached page.<br></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><br>By and through this letter you are hereby ordered to take all steps necessary to correct the attached and bring the property into full compliance with the state code.<br><br></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:700;font-style:normal;text-decoration:none;">A REINSPECTION IS RESCHEDULED FOR:</span> {{FF1027338}}
				<br>
				<br><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:700;font-style:normal;text-decoration:none;">All violations must be cured by this date. If the violations are not cured by this date, the city shall be obligated to take further action.</span>
				<br>
				<br>
			</td>
		</tr>
	</tbody>
</table>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 33.3333%;">Certified Letter Information</td>
			<td style="width: 33.3333%;">
				<br>
			</td>
			<td style="width: 33.3333%;">
				<br>
			</td>
		</tr>
		<tr>
			<td style="width: 33.3333%;">Date Sent</td>
			<td style="width: 33.3333%;">Recipient</td>
			<td style="width: 33.3333%;">Certified Number</td>
		</tr>
		<tr>
			<td style="width: 33.3333%;">{{{OL1026700}}}</td>
			<td style="width: 33.3333%;">{{{OL1026701}}}</td>
			<td style="width: 33.3333%;">{{{OL1026699}}}</td>
		</tr>
	</tbody>
</table>
<div>

	<p>
		<br>
	</p>

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
				<td style="width: 26.3591%;">{{#if FF1027300}}Christopher Bennett{{/if}}{{#if FF1027308}}William Brunton{{/if}}{{#if FF1027309}}Danny Cueto{{/if}}{{#if FF1027310}}Michelle Haska{{/if}}{{#if FF1027311}}Mike Jones{{/if}}{{#if FF1027312}}Jesus Martinez{{/if}}{{#if FF1027313}}Michael McNulty{{/if}}{{#if FF1027314}}Jermain Mitchell{{/if}}{{#if FF1027315}}Michael Whiting{{/if}}{{#if FF1027316}}James Murgolo{{/if}}</td>
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
				<td style="width: 26.3591%;">{{currentDate}}</td>
			</tr>
		</tbody>
	</table>

	<p style="page-break-before: always;">
		<br>
	</p>
</div>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 8.3967%;">
				<br>
			</td>
			<td class="frcustomborder" style="width: 79.0821%; text-align: center;"><span style="font-family: Arial; color: rgb(255, 0, 0); font-size: 24px; font-weight: 700; font-style: normal; text-decoration: none;">VIOLATIONS</span><span style="font-size: 24px;"><br></span></td>
			<td style="width: 12.4639%;">
				<br>
			</td>
		</tr>
		<tr>
			<td colspan="3" style="width: 99.9432%;"><strong>R</strong>e: <span style="color: rgb(0, 0, 0);">&nbsp;<span style="font-size: 14px;"><strong>{{streetNo}} {{streetName}}{{#if FF1027854}}, Unit {{FF1027854}} {{/if}}, &nbsp;{{city}}, {{state}} {{zipCode}}</strong></span></span></td>
		</tr>
	</tbody>
</table>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 73.6149%;">
				<br>
			</td>
			<td style="width: 12.2249%;"><strong>Parcel:</strong></td>
			<td style="width: 14.1057%;"><strong>{{mbl}}</strong>
				<br>
			</td>
		</tr>
		<tr>
			<td style="width: 73.6149%;"><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:700;font-style:normal;text-decoration:none;">The following violations were found:</span>
				<br>
			</td>
			<td style="width: 12.2249%;"><strong>Case Number:</strong></td>
			<td style="width: 14.1057%;"><strong>{{recordId}}</strong>
				<br>
			</td>
		</tr>
	</tbody>
</table>
<div>

	<table style="width: 115%; margin-right: calc(-15%);">
		<tbody>
			<tr>
				<td style="width: 18.2517%; vertical-align: top;"><u>VIOLATIONS:</u></td>
				<td style="width: 81.7483%; display: inline-block; vertical-align: top;">
					<br>
				</td>
			</tr>
			<tr>
				<td style="width: 18.2517%; vertical-align: top;">{{{OL1026635}}}</td>
				<td style="width: 81.7483%; display: inline-block; vertical-align: top;">Responsibility:
					<div style="margin-top:-34px; margin-left:110px;">{{{OL1027836}}}</div>Unit:
					<div style="margin-top:-34px; margin-left:35px;">{{{OL1027832}}}</div>Corrections Required By:
					<div style="margin-top:-34px; margin-left:190px;">{{{OL1027835}}}</div>Status:
					<div style="margin-top:-34px; margin-left:60px;">{{{OL1026634}}}</div>Violation:
					<div style="margin-top:-34px; margin-left:100px;">{{{OL1027831}}}</div>Notes:
					<div style="margin-top:-34px; margin-left:60px;">{{{OL1028592}}}</div>
				</td>
			</tr>
		</tbody>
	</table>
	<div><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">Please note: &nbsp;You are required to apply for any permits necessary in accordance with applicable zoning requirements or any building permits necessary to gain compliance. &nbsp;</span>&nbsp;</div>
	<div>
		<br>
	</div>
	<div><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">RIGHT OF APPEAL: Receipt of this notice of Violation entitles the recipient to appeal the order to this department. Such petition must be in writing and filed within seven days after the day the order was received. Please refer to&nbsp;</span><span style="font-family:Calibri;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">105 CMR 410.800&nbsp;</span><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">et seq. for all rights and remedies in regard to this Notice.</span>&nbsp;</div></div>
{{/if}}
	<p style="page-break-before: always;">
		<br>
	</p>
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

# Step 3: Map the used FF codes to their meaning for the First Tenant
code_meaning_map = {}
for kind in ["Tenant", "Name", "Unit"]:
    first_code = grouped_dict["First"].get(kind)
    if first_code and first_code in used_codes_flat:
        code_meaning_map[first_code] = kind

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
        replacement_code = tenant_data.get(kind)
        if replacement_code:
            block = block.replace(f"{{{{{first_code}}}}}", f"{{{{{replacement_code}}}}}")
            block = block.replace(f"{{{{#if {first_code}}}}}", f"{{{{#if {replacement_code}}}}}")
    output_blocks.append(block)

# Step 5: Write to file
with open("output.html", "w", encoding="utf-8") as f:
    for block in output_blocks:
        f.write(block + "\n\n")

print("✅ All variations written to output.html")
