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
original_template = """
<table style="width: 100%; margin-left: calc(0%);">
	<tbody>
		<tr>
			<td style="width: 15.6939%;">
				<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
			</td>
			<td colspan="3" style="width: 68.9341%;">
				<div style="text-align: center;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>City of Springfield</strong></span></div>

				<p style="text-align: center; padding: 0pt;"><span style="font-family:Arial;color:#000000;font-size:12pt;font-weight:700;font-style:normal;text-decoration:none;">Building Department Inspectional Services</span></p>

				<p style="text-align: center; padding: 0pt;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 14px; font-weight: 400; font-style: normal; text-decoration: none;'>70 Tapley St.<br>Springfield, MA 01104</span>
					<br><span style='font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>(413)787-6031/TTY (413)787-6641<br>FAX (413)787-6641</span></p>

				<p style="text-align: center; padding: 0pt;">
					<br>
				</p>
			</td>
			<td style="width: 15.3022%;">

				<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="width: 37.5709%;">
				<br>
			</td>
			<td style="width: 28.0312%;"><strong><br></strong></td>
			<td style="width: 19.0244%;"><strong><br></strong></td>
			<td style="width: 15.3022%;"><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%;">{{#if FF1028653}}{{FF1028654}}
				<br>{{FF1028655}}{{/if}}
				<br>{{#unless FF1028653}}{{ownerName}}
				<br>{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}}
				<br>{{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/unless}}
				<br>
			</td>
		</tr>
		<tr>
			<td colspan="3" style="width: 65.6062%;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong style="box-sizing: border-box; font-weight: 700;">RE:&nbsp;</strong></span><strong style="box-sizing: border-box; font-weight: 700; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">{{streetNo}} {{streetName}}{{#if FF1028613}}, Unit {{FF1028613}} {{/if}}<br style="box-sizing: border-box;">&nbsp; &nbsp; &nbsp; &nbsp;{{city}}, {{state}} {{zipCode}}</strong> <strong><br></strong></td>
			<td style="width: 19.0244%; text-align: right; vertical-align: top;"><span style="font-family: Arial, Helvetica, sans-serif; font-size: 12px;">Parcel:&nbsp;</span>
				<br><span style="font-family: Arial, Helvetica, sans-serif; font-size: 12px;">Case Number:</span>&nbsp;</td>
			<td style="width: 15.3022%; text-align: left; vertical-align: top;"><span style="font-family: Arial, Helvetica, sans-serif; font-size: 12px;">{{mbl}}</span>
				<br><span style="font-family: Arial, Helvetica, sans-serif; font-size: 12px;">{{recordId}}</span>
				<br>
			</td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: center;">
				<br><span style="font-family:Arial;color:#000000;font-size:16pt;font-weight:700;font-style:normal;text-decoration:underline;">FIRST NOTICE OF VIOLATIONS</span>&nbsp;</td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: left;"><span style="font-family: Arial,Helvetica,sans-serif;">As the result of an inspection that was performed on the above property on {{FF1028748}}, conditions were found that amount to a violation of the Massachusetts State Building Codes.&nbsp;</span><span style="font-family: Arial, Helvetica, sans-serif; color: rgb(0, 0, 0); font-size: 11pt; font-weight: 400; font-style: normal; text-decoration: none;"><br></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>
				<br><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:700;font-style:normal;text-decoration:none;">A full list of the violations may be found on the attached page.<br></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><br></span><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">You are hereby notified in accordance with Massachusetts State Building Code 780 CMR, Ninth edition Chapter 1, (Violations) &nbsp;to immediately discontinue the illegal action and or cause the abatement of the Violations listed on the attached page.&nbsp;</span> <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;"><br><br>Per the Massachusetts State Building Code you are also required to apply for any and all necessary building permits and or if any electrical, plumbing or gas fitting repairs need to be made, you are required to have a Massachusetts State Licensed Electrician or Plumber apply for the necessary permits to correct violations.<br></span>
				<br><span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:700;font-style:normal;text-decoration:none;">A REINSPECTION IS SCHEDULED FOR:</span> {{FF1028777}} {{FF1028778}}</span>
				<br><span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;"><br>Should you have any questions, Please contact {{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}} at <span style="font-family: Arial,Helvetica,sans-serif;"><span style="font-size: 14px;"><span style="color: rgb(255, 0, 0); font-weight: 400; font-style: normal; text-decoration: none;">{{#if FF1028751}}(413) 750-2088 {{/if}}{{#if FF1028753}}(413) 886-5202{{/if}}{{#if FF1028754}}(413) 886-5345{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}(413) 886-5083{{/if}}{{#if FF1027316}}(413) 787 6534{{/if}}</span></span></span> , between the hours of 7:00a.m. and 4:30p.m.</span>
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
			<td style="width: 33.3333%;">{{{OL1028716}}}</td>
			<td style="width: 33.3333%;">{{{OL1028717}}}</td>
			<td style="width: 33.3333%;">{{{OL1028715}}}</td>
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
				<td style="width: 22.6714%;"><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/signature-steve_Tue_Apr_22_2025_06:22:33_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 300px;" class="fr-fic fr-dib"></td>
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
				<td style="width: 22.6714%;">Steven Desilets
					<br>
				</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">{{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}}
					<br>
				</td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">Code Enforcement Commissioner
					<br>
				</td>
				<td style="width: 2.7539%;">
					<br>
				</td>
				<td style="width: 45.401%;">
					<br>
				</td>
				<td style="width: 2.7411%;">
					<br>
				</td>
				<td style="width: 26.3591%;">Building Inspector</td>
			</tr>
			<tr>
				<td style="width: 22.6714%;">
					<br>
				</td>
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

	<table style="width: 100%;">
		<tbody>
			<tr>
				<td style="width: 33.3333%;">Date of Notification:&nbsp;</td>
				<td style="width: 33.3333%;">Will Be Re-Inspected: <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;">{{FF1028777}}</span></td>
				<td style="width: 33.3333%;">File -&nbsp;</td>
			</tr>
			<tr>
				<td style="width: 33.3333%;">Compliance:&nbsp;</td>
				<td style="width: 33.3333%;">Ticket Issue Date:&nbsp;</td>
				<td style="width: 33.3333%;">Docket Number:&nbsp;</td>
			</tr>
		</tbody>
	</table>
</div>
<div>
	<br>
</div>
<div><strong>FROM: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; INSPECTIONAL SERVICES DEPARTMENT / BUILDING DIVISION<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;70 TAPLEY STREET, SPRINGFIELD, MA 01104</strong>
	<br>
	<br>
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
			<td colspan="3" style="width: 99.9432%;"><strong>R</strong>e: <span style="color: rgb(0, 0, 0);">&nbsp;<strong>{{#if FF1027709}}{{FF1028654}} {{FF1028655}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></td>
		</tr>
	</tbody>
</table>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 66.0718%;">
				<br>
			</td>
			<td style="width: 16.7197%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Parcel:</span></strong></td>
			<td style="width: 17.123%;"><strong>{{mbl}}</strong>
				<br>
			</td>
		</tr>
		<tr>
			<td style="width: 66.0718%;"><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:700;font-style:normal;text-decoration:none;">The following violations were found:</span>
				<br>
			</td>
			<td style="width: 16.7197%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Case Number:</span></strong></td>
			<td style="width: 17.123%;"><strong>{{recordId}}</strong>
				<br>
			</td>
		</tr>
	</tbody>
</table>
<div>

	<table style="width: 100%;">
		<thead>
			<tr>
				<td style="width:20%;">
					<br>
				</td>
				<td style="padding:5px; width:8%;"><strong>Unit</strong></td>
				<td style="padding:5px; width:19%;"><strong>Responsibility</strong></td>
				<td style="padding:5px; width:11%;"><strong>Fix By</strong></td>
				<td style="padding:5px; width:10%;"><strong>Status</strong></td>
				<td style="padding:5px; width:32%;"><strong>Violation and Notes</strong></td>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>{{{OL1028705}}}</td>
				<td style="padding:5px;">{{{OL1028703}}}</td>
				<td style="padding:5px;">{{{OL1028702}}}</td>
				<td style="padding:5px;">{{{OL1028706}}}</td>
				<td style="padding:5px;">{{{OL1028704}}}</td>
				<td style="padding:5px;">{{{OL1028700}}}</td>
			</tr>
		</tbody>
	</table>
	<div><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">Please note: &nbsp;You are required to apply for any permits necessary in accordance with applicable zoning requirements or any building permits necessary to gain compliance. &nbsp;</span>&nbsp;</div>
	<div>
		<br>
	</div>
	<div><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">RIGHT OF APPEAL: Receipt of this notice of Violation entitles the recipient to appeal the order to this department. Such petition must be in writing and filed within seven days after the day the order was received. Please refer to&nbsp;</span><span style="font-family:Calibri;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">105 CMR 410.800&nbsp;</span><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">et seq. for all rights and remedies in regard to this Notice.</span>&nbsp;</div>
	<div>
		<br>
	</div>{{#if FF1028656}}

	<p style="page-break-before: always;">
		<br>
	</p>

	<table style="width: 100%; margin-left: calc(0%);">
		<tbody>
			<tr>
				<td style="width: 15.6939%;">
					<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
				</td>
				<td colspan="3" style="width: 67.2141%;">
					<div style="text-align: center;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>City of Springfield</strong></span></div>

					<p style="text-align: center; padding: 0pt;"><span style="font-family:Arial;color:#000000;font-size:12pt;font-weight:700;font-style:normal;text-decoration:none;">Building Department Inspectional Services</span></p>

					<p style="text-align: center; padding: 0pt;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 14px; font-weight: 400; font-style: normal; text-decoration: none;'>70 Tapley St.<br>Springfield, MA 01104</span>
						<br><span style='font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>(413)787-6031/TTY (413)787-6641<br>FAX (413)787-6641</span></p>
				</td>
				<td style="width: 17.0316%;">

					<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
				</td>
			</tr>
			<tr>
				<td colspan="2" style="width: 37.5709%;">
					<br>
				</td>
				<td style="width: 31.27%;"><strong><br></strong></td>
				<td style="width: 14.0501%;"><strong><br></strong></td>
				<td style="width: 17.0316%;"><strong><br></strong></td>
			</tr>
			<tr>
				<td colspan="5" style="width: 99.9433%;"><span style="color: rgb(0, 0, 0);">{{FF1028657}}&nbsp;</span>
					<br><span style="color: rgb(0, 0, 0);">{{{FF1028658}}}</span></td>
			</tr>
			<tr>
				<td colspan="3" style="width: 68.8565%;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>Re:&nbsp;</strong></span><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1028613}}{{/if}}</strong><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>, {{city}}, {{state}} {{zipCode}}</strong></span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
				<td style="width: 14.0501%; text-align: right; vertical-align: top;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Parcel: &nbsp;</span></td>
				<td style="width: 17.0316%; text-align: left; vertical-align: top;">{{mbl}}</td>
			</tr>
			<tr>
				<td style="width: 15.6939%;"><strong><br></strong></td>
				<td style="width: 21.8933%;"><strong><br></strong></td>
				<td style="width: 31.27%;"><strong><br></strong></td>
				<td style="width: 14.0501%; text-align: right;"><span style='font-family: "Times New Roman", Times, serif, -webkit-standard; font-size: 14px;'>Case Number:&nbsp;</span></td>
				<td style="width: 17.0316%;">{{recordId}}<strong><br></strong></td>
			</tr>
			<tr>
				<td colspan="5" style="width: 99.9433%; text-align: center;">
					<br><span style="font-family:Arial;color:#000000;font-size:16pt;font-weight:700;font-style:normal;text-decoration:underline;">FIRST NOTICE OF VIOLATIONS</span>&nbsp;</td>
			</tr>
			<tr>
				<td colspan="5" style="width: 99.9433%; text-align: left;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;">As the result of an inspection that was performed on the above property on {{FF1028748}}, conditions were found that amount to a violation of the Massachusetts State Building Codes.&nbsp;</span><span style="box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: Arial, Helvetica, sans-serif; color: rgb(0, 0, 0); font-size: 11pt;"><br style="box-sizing: border-box;"></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>
					<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700;'>A full list of the violations may be found on the attached page.<br style="box-sizing: border-box;"></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'><br style="box-sizing: border-box;"></span><span style="box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: Arial; color: rgb(0, 0, 0); font-size: 10pt;">You are hereby notified in accordance with Massachusetts State Building Code 780 CMR, Ninth edition Chapter 1, (Violations) &nbsp;to immediately discontinue the illegal action and or cause the abatement of the Violations listed on the attached page.&nbsp;</span><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><br style="box-sizing: border-box;"><br style="box-sizing: border-box;">Per the Massachusetts State Building Code you are also required to apply for any and all necessary building permits and or if any electrical, plumbing or gas fitting repairs need to be made, you are required to have a Massachusetts State Licensed Electrician or Plumber apply for the necessary permits to correct violations.<br style="box-sizing: border-box;"></span>
					<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><span style='box-sizing: border-box; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700; font-style: normal; text-decoration: none;'>A REINSPECTION IS SCHEDULED FOR:</span> {{FF1028777}} {{FF1028778}}</span>
					<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><br style="box-sizing: border-box;">Should you have any questions, Please contact {{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}} at <span style="box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;"><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; color: rgb(255, 0, 0); font-weight: 400; font-style: normal; text-decoration: none;">{{#if FF1028751}}(413) 750-2088 {{/if}}{{#if FF1028753}}(413) 886-5202{{/if}}{{#if FF1028754}}(413) 886-5345{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}(413) 886-5083{{/if}}{{#if FF1027316}}(413) 787 6534{{/if}}</span></span></span> , between the hours of 7:00a.m. and 4:30p.m.</span>
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
				<td style="width: 33.3333%;">{{{OL1028716}}}</td>
				<td style="width: 33.3333%;">{{{OL1028717}}}</td>
				<td style="width: 33.3333%;">{{{OL1028715}}}</td>
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
					<td style="width: 22.6714%;"><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/signature-steve_Tue_Apr_22_2025_06:22:33_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 300px;" class="fr-fic fr-dib"></td>
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
					<td style="width: 22.6714%;">Steven Desilets
						<br>
					</td>
					<td style="width: 2.7539%;">
						<br>
					</td>
					<td style="width: 45.401%;">
						<br>
					</td>
					<td style="width: 2.7411%;">
						<br>
					</td>
					<td style="width: 26.3591%;">{{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}}
						<br>
					</td>
				</tr>
				<tr>
					<td style="width: 22.6714%;">Code Enforcement Commissioner
						<br>
					</td>
					<td style="width: 2.7539%;">
						<br>
					</td>
					<td style="width: 45.401%;">
						<br>
					</td>
					<td style="width: 2.7411%;">
						<br>
					</td>
					<td style="width: 26.3591%;">Building Inspector
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

		<table style="width: 100%;">
			<tbody>
				<tr>
					<td style="width: 33.3333%;">Date of Notification:&nbsp;</td>
					<td style="width: 33.3333%;">Will Be Re-Inspected: <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;">{{FF1028777}}</span></td>
					<td style="width: 33.3333%;">File -&nbsp;</td>
				</tr>
				<tr>
					<td style="width: 33.3333%;">Compliance:&nbsp;</td>
					<td style="width: 33.3333%;">Ticket Issue Date:&nbsp;</td>
					<td style="width: 33.3333%;">Docket Number:&nbsp;</td>
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
				<td colspan="3" style="width: 99.9432%;"><strong>Re:&nbsp;</strong><span style="color: rgb(0, 0, 0);">&nbsp;<span style="color: rgb(0, 0, 0);"><strong>{{#if FF1027709}}{{FF1028654}} {{FF1028655}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></span></td>
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

		<table style="width: 100%;">
			<thead>
				<tr>
					<td style="width:20%;">
						<br>
					</td>
					<td style="padding:5px; width:8%;"><strong>Unit</strong></td>
					<td style="padding:5px; width:19%;"><strong>Responsibility</strong></td>
					<td style="padding:5px; width:11%;"><strong>Fix By</strong></td>
					<td style="padding:5px; width:10%;"><strong>Status</strong></td>
					<td style="padding:5px; width:32%;"><strong>Violation and Notes</strong></td>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>{{{OL1028705}}}</td>
					<td style="padding:5px;">{{{OL1028703}}}</td>
					<td style="padding:5px;">{{{OL1028702}}}</td>
					<td style="padding:5px;">{{{OL1028706}}}</td>
					<td style="padding:5px;">{{{OL1028704}}}</td>
					<td style="padding:5px;">{{{OL1028700}}}</td>
				</tr>
			</tbody>
		</table>
		<div><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">Please note: &nbsp;You are required to apply for any permits necessary in accordance with applicable zoning requirements or any building permits necessary to gain compliance. &nbsp;</span>&nbsp;</div>
		<div>
			<br>
		</div>
		<div><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">RIGHT OF APPEAL: Receipt of this notice of Violation entitles the recipient to appeal the order to this department. Such petition must be in writing and filed within seven days after the day the order was received. Please refer to&nbsp;</span><span style="font-family:Calibri;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">105 CMR 410.800&nbsp;</span><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">et seq. for all rights and remedies in regard to this Notice.</span>&nbsp;</div>
		<div>

			<p style="page-break-before: always;">
				<br>
			</p>{{/if}} {{#if FF1028659}}

			<table style="width: 100%; margin-left: calc(0%);">
				<tbody>
					<tr>
						<td style="width: 15.6939%;">
							<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
						</td>
						<td colspan="3" style="width: 65.4805%;">
							<div style="text-align: center;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>City of Springfield</strong></span></div>

							<p style="text-align: center; padding: 0pt;"><span style="font-family:Arial;color:#000000;font-size:12pt;font-weight:700;font-style:normal;text-decoration:none;">Building Department Inspectional Services</span></p>

							<p style="text-align: center; padding: 0pt;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 14px; font-weight: 400; font-style: normal; text-decoration: none;'>70 Tapley St.<br>Springfield, MA 01104</span>
								<br><span style='font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>(413)787-6031/TTY (413)787-6641<br>FAX (413)787-6641</span></p>
						</td>
						<td style="width: 18.7652%;">

							<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
						</td>
					</tr>
					<tr>
						<td colspan="2" style="width: 37.5709%;">
							<br>
						</td>
						<td style="width: 28.0766%;"><strong><br></strong></td>
						<td style="width: 15.51%;"><strong><br></strong></td>
						<td style="width: 18.7652%;"><strong><br></strong></td>
					</tr>
					<tr>
						<td colspan="5" style="width: 99.9433%;"><span style="color: rgb(0, 0, 0);">{{FF1028660}}&nbsp;</span>
							<br><span style="color: rgb(0, 0, 0);">{{{FF1028661}}}</span></td>
					</tr>
					<tr>
						<td colspan="3" style="width: 65.663%;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>Re:&nbsp;</strong></span><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1028613}}{{/if}}</strong><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>, {{city}}, {{state}} {{zipCode}}</strong></span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
						<td style="width: 15.5101%; text-align: right; vertical-align: top;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Parcel: &nbsp;</span></td>
						<td style="width: 18.7652%; text-align: left; vertical-align: top;">{{mbl}}</td>
					</tr>
					<tr>
						<td style="width: 15.6939%;"><strong><br></strong></td>
						<td style="width: 21.8933%;"><strong><br></strong></td>
						<td style="width: 28.0766%;"><strong><br></strong></td>
						<td style="width: 15.51%; text-align: right;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Case Number:&nbsp;</span></td>
						<td style="width: 18.7652%;">{{recordId}}<strong><br></strong></td>
					</tr>
					<tr>
						<td colspan="5" style="width: 99.9433%; text-align: center;">
							<br><span style="font-family:Arial;color:#000000;font-size:16pt;font-weight:700;font-style:normal;text-decoration:underline;">FIRST NOTICE OF VIOLATIONS</span>&nbsp;</td>
					</tr>
					<tr>
						<td colspan="5" style="width: 99.9433%; text-align: left;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;">As the result of an inspection that was performed on the above property on {{FF1028748}}, conditions were found that amount to a violation of the Massachusetts State Building Codes.&nbsp;</span><span style="box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: Arial, Helvetica, sans-serif; color: rgb(0, 0, 0); font-size: 11pt;"><br style="box-sizing: border-box;"></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>
							<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700;'>A full list of the violations may be found on the attached page.<br style="box-sizing: border-box;"></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt;'><br style="box-sizing: border-box;"></span><span style="box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: Arial; color: rgb(0, 0, 0); font-size: 10pt;">You are hereby notified in accordance with Massachusetts State Building Code 780 CMR, Ninth edition Chapter 1, (Violations) &nbsp;to immediately discontinue the illegal action and or cause the abatement of the Violations listed on the attached page.&nbsp;</span><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><br style="box-sizing: border-box;"><br style="box-sizing: border-box;">Per the Massachusetts State Building Code you are also required to apply for any and all necessary building permits and or if any electrical, plumbing or gas fitting repairs need to be made, you are required to have a Massachusetts State Licensed Electrician or Plumber apply for the necessary permits to correct violations.<br style="box-sizing: border-box;"></span>
							<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><span style='box-sizing: border-box; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700; font-style: normal; text-decoration: none;'>A REINSPECTION IS SCHEDULED FOR:</span> {{FF1028777}} {{FF1028778}}</span>
							<br style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-family: Arial, Helvetica, sans-serif;"><br style="box-sizing: border-box;">Should you have any questions, Please contact {{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}} at&nbsp;<span style="box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;"><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; color: rgb(255, 0, 0); font-weight: 400; font-style: normal; text-decoration: none;">{{#if FF1028751}}(413) 750-2088 {{/if}}{{#if FF1028753}}(413) 886-5202{{/if}}{{#if FF1028754}}(413) 886-5345{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}(413) 886-5083{{/if}}{{#if FF1027316}}(413) 787 6534{{/if}}</span></span></span> , between the hours of 7:00a.m. and 4:30p.m.</span>
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
						<td style="width: 33.3333%;">{{{OL1028716}}}</td>
						<td style="width: 33.3333%;">{{{OL1028717}}}</td>
						<td style="width: 33.3333%;">{{{OL1028715}}}</td>
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
							<td style="width: 22.6714%;"><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/signature-steve_Tue_Apr_22_2025_06:22:33_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 300px;" class="fr-fic fr-dib"></td>
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
							<td style="width: 22.6714%;">Steven Desilets
								<br>
							</td>
							<td style="width: 2.7539%;">
								<br>
							</td>
							<td style="width: 45.401%;">
								<br>
							</td>
							<td style="width: 2.7411%;">
								<br>
							</td>
							<td style="width: 26.3591%;">{{#if FF1028751}}David Markham{{/if}}{{#if FF1028753}}Thomas Kennedy{{/if}}{{#if FF1028754}}Abdul Mohammed{{/if}}{{#if FF1028755}}George Shaw{{/if}}{{#if FF1028757}}Matthew Goodchild{{/if}}{{#if FF1027316}}James Murgolo{{/if}}
								<br>
							</td>
						</tr>
						<tr>
							<td style="width: 22.6714%;">Code Enforcement Commissioner
								<br>
							</td>
							<td style="width: 2.7539%;">
								<br>
							</td>
							<td style="width: 45.401%;">
								<br>
							</td>
							<td style="width: 2.7411%;">
								<br>
							</td>
							<td style="width: 26.3591%;">Building Inspector
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

				<table style="width: 100%;">
					<tbody>
						<tr>
							<td style="width: 33.3333%;">Date of Notification:&nbsp;</td>
							<td style="width: 33.3333%;">Will Be Re-Inspected: <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px;">{{FF1028777}}</span></td>
							<td style="width: 33.3333%;">File -&nbsp;</td>
						</tr>
						<tr>
							<td style="width: 33.3333%;">Compliance:&nbsp;</td>
							<td style="width: 33.3333%;">Ticket Issue Date:&nbsp;</td>
							<td style="width: 33.3333%;">Docket Number:&nbsp;</td>
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
						<td colspan="3" style="width: 99.9432%;"><strong>Re:&nbsp;</strong><span style="color: rgb(0, 0, 0);">&nbsp;<span style="color: rgb(0, 0, 0);"><strong>{{#if FF1027709}}{{FF1028654}} {{FF1028655}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></span></td>
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

				<table style="width: 100%;">
					<thead>
						<tr>
							<td style="width:20%;">
								<br>
							</td>
							<td style="padding:5px; width:8%;"><strong>Unit</strong></td>
							<td style="padding:5px; width:19%;"><strong>Responsibility</strong></td>
							<td style="padding:5px; width:11%;"><strong>Fix By</strong></td>
							<td style="padding:5px; width:10%;"><strong>Status</strong></td>
							<td style="padding:5px; width:32%;"><strong>Violation and Notes</strong></td>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>{{{OL1028705}}}</td>
							<td style="padding:5px;">{{{OL1028703}}}</td>
							<td style="padding:5px;">{{{OL1028702}}}</td>
							<td style="padding:5px;">{{{OL1028706}}}</td>
							<td style="padding:5px;">{{{OL1028704}}}</td>
							<td style="padding:5px;">{{{OL1028700}}}</td>
						</tr>
					</tbody>
				</table>
				<div><span style="font-family:Arial;color:#000000;font-size:10pt;font-weight:400;font-style:normal;text-decoration:none;">Please note: &nbsp;You are required to apply for any permits necessary in accordance with applicable zoning requirements or any building permits necessary to gain compliance. &nbsp;</span>&nbsp;</div>
				<div>
					<br>
				</div>
				<div><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">RIGHT OF APPEAL: Receipt of this notice of Violation entitles the recipient to appeal the order to this department. Such petition must be in writing and filed within seven days after the day the order was received. Please refer to&nbsp;</span><span style="font-family:Calibri;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">105 CMR 410.800&nbsp;</span><span style="font-family:Arial;color:#000000;font-size:9pt;font-weight:400;font-style:normal;text-decoration:none;">et seq. for all rights and remedies in regard to this Notice.</span>&nbsp;</div>
				<div>
					<br>
				</div></div></div></div></div>
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
with open("Multiple Letter Recipients.html", "w", encoding="utf-8") as f:
    for block in output_blocks:
        f.write(block + "\n\n")

print("✅ All variations written to output.html")
