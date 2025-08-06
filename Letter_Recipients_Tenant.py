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
<div>{{#if FF1027853_checked}}</div>

<table style="width: 100%; margin-left: calc(0%);">
	<tbody>
		<tr>
			<td style="width: 15.6939%;">
				<div style="text-align: center;"><strong><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/city_seal_LG_blue-vector_Mon_Mar_17_2025_20:44:12_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 126px;" class="fr-fic fr-dib"></strong></div>
			</td>
			<td colspan="3" style="width: 68.9518%;">
				<div style="text-align: center;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>City of Springfield</strong></span></div>

				<p style="text-align: center; padding: 0pt;"><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 18px; font-weight: 400; font-style: normal; text-decoration: none;'><strong>Code Enforcement</strong></span><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>&nbsp;</strong></span></p>

				<p style="text-align: center; padding: 0pt;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">Housing Division<br>70 Tapley St.<br>Springfield, MA 01104<br>Telephone: (413) 787-6730<br>Fax: 413-886-5348</span></p>
			</td>
			<td style="width: 15.2973%;">

				<p><strong><img alt="barcode" class="fr-fir fr-dii" src="/assets/images/qrcode.jpg" title="Barcode" style="width: 151px;"></strong></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="width: 37.5709%;">
				<br>
			</td>
			<td style="width: 27.4198%;"><strong><br></strong></td>
			<td style="width: 19.6348%;"><strong><br></strong></td>
			<td style="width: 15.2973%;"><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%;"><span style='color: rgb(0, 0, 0); font-size: 14px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>{{FF1027852}}<br></span><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="color: rgb(0, 0, 0); font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">{{#if FF1027854}}, Unit&nbsp;</span><span style="color: rgb(0, 0, 0); font-size: 14px;color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">{{FF1027854}}</span><span style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">&nbsp;{{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1026624}}{{/if}}</strong></span></span></span></span></span></span>
				<br>
				</span><span style="color: rgb(0, 0, 0); font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{city}}, {{state}} {{zipCode}}</span></strong></span></span></span></span></span></span></span></span></span></span>
				<br>
				<br>
				</span></td>
		</tr>
		<tr>
			<td colspan="3" style="width: 65.0062%;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;"><strong>Re:&nbsp;</strong></span><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1026624}}{{/if}}</strong><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>, {{city}}, {{state}} {{zipCode}}</strong></span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
			<td style="width: 19.6348%; text-align: right; vertical-align: top;"><span style='font-size: 12px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>Parcel: &nbsp;</span></td>
			<td style="width: 15.2973%; text-align: left; vertical-align: top;"><span style='font-size: 12px; font-family: "Times New Roman", Times, serif, -webkit-standard;'>{{mbl}}</span></td>
		</tr>
		<tr>
			<td style="width: 15.6939%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><br></strong></span></td>
			<td style="width: 21.8933%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><br></strong></span></td>
			<td style="width: 27.4198%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><br></strong></span></td>
			<td style="width: 19.6348%; text-align: right;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="font-size: 12px;">Case Number:&nbsp;</span></span></td>
			<td style="width: 15.2973%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="font-size: 12px;">{{recordId}}</span><strong><br></strong></span></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: center;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br><span style="color: rgb(0, 0, 0); font-size: 16pt; font-weight: 700; font-style: normal; text-decoration: underline;">FIRST NOTICE OF VIOLATIONS</span>&nbsp;</span></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: left;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 400; font-style: normal; text-decoration: none;">As a result of an inspection that was performed on the above property on&nbsp;</span>{{FF1026615}}<span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 400; font-style: normal; text-decoration: none;">, conditions were found to exist that amount to a violation of the Massachusetts State Sanitary Code (105 CMR 410.000 State Sanitary Code Chapter II: Minimum Standards of Fitness for Human Habitation). Property records indicate that you are the party responsible for this premises either by ownership, occupation, or control.<br><br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700; font-style: normal; text-decoration: none;">A full list of the violations may be found on the attached page.<br></span><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 400; font-style: normal; text-decoration: none;"><br>By and through this letter you are hereby ordered to take all steps necessary to correct the attached and bring the property into full compliance with the state code.<br><br></span><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700; font-style: normal; text-decoration: none;">A REINSPECTION IS SCHEDULED FOR:</span> {{FF1027338}}
				<br>
				<br><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 700; font-style: normal; text-decoration: none;">All violations must be cured by this date. If the violations are not cured by this date, the city shall be obligated to take further action.</span>
				<br>
				<br>
				</span></td>
		</tr>
	</tbody>
</table>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Certified Letter Information</span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
		</tr>
		<tr>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Date Sent</span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Recipient</span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Certified Number</span></td>
		</tr>
		<tr>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026700}}}</span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026701}}}</span></td>
			<td style="width: 33.3333%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026699}}}</span></td>
		</tr>
	</tbody>
</table>
<div>

	<p><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></p>

	<table style="width: 100%; margin-right: calc(0%);">
		<tbody>
			<tr>
				<td style="width: 22.6714%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><img src="https://viewpointcloud.blob.core.windows.net/profile-pictures/housing_director_signature_Tue_Mar_18_2025_16:36:22_GMT+0000_(Coordinated_Universal_Time).jpg" style="width: 300px;" class="fr-fic fr-dib"></span></td>
				<td style="width: 2.7539%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 45.401%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7411%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 26.3591%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
			</tr>
			<tr>
				<td style="width: 22.6714%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Keith D. O&#39;Connor</span></td>
				<td style="width: 2.7539%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 45.401%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7411%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 26.3591%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{#if FF1027300}}Christopher Bennett{{/if}}{{#if FF1027308}}William Brunton{{/if}}{{#if FF1027309}}Danny Cueto{{/if}}{{#if FF1027310}}Michelle Haska{{/if}}{{#if FF1027311}}Mike Jones{{/if}}{{#if FF1027312}}Jesus Martinez{{/if}}{{#if FF1027313}}Michael McNulty{{/if}}{{#if FF1027314}}Jermain Mitchell{{/if}}{{#if FF1027315}}Michael Whiting{{/if}}{{#if FF1027316}}James Murgolo{{/if}}</span></td>
			</tr>
			<tr>
				<td style="width: 22.6714%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Deputy Director of Code Enforcement</span></td>
				<td style="width: 2.7539%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 45.401%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7411%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 26.3591%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Code Enforcement Inspector</span></td>
			</tr>
			<tr>
				<td style="width: 22.6714%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Housing Division</span></td>
				<td style="width: 2.7539%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 45.401%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7411%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 26.3591%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
			</tr>
			<tr>
				<td style="width: 22.6714%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7539%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 45.401%; text-align: center;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 2.7411%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
				<td style="width: 26.3591%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{currentDate}}</span></td>
			</tr>
		</tbody>
	</table>

	<p style="page-break-before: always;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></p>
</div>

<table style="width: 100%;">
	<tbody>
		<tr>
			<td colspan="3" style="width: 99.9391%; text-align: center;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="color: rgb(255, 0, 0); font-size: 24px; font-weight: 700; font-style: normal; text-decoration: none;">VIOLATIONS</span><span style="font-size: 24px;"><br></span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="width: 61.6484%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Re:</strong><br><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>{{streetNo}} {{streetName}}</strong><span style="font-size: 14px;"><strong><span style="color: rgb(0, 0, 0); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</strong><span style="font-size: 14px;"><strong>{{#if FF39670}},&nbsp;</strong><span style="font-size: 14px;"><strong>{{FF1026624}}{{/if}}</strong><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><strong>, {{city}}, {{state}} {{zipCode}}</strong></span></span></span></span></span></span></span></span></span></span></span></td>
			<td style="width: 38.2908%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><span style="font-size: 12px;">Parcel: <strong>{{mbl}}</strong></span></strong><span style="font-size: 12px;"><br></span><strong><span style="font-size: 12px;">Case Number:&nbsp;{{recordId}}</span></strong>
				<br>
				</span></td>
		</tr>
	</tbody>
</table>
<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></div>
<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><span style="color: rgb(0, 0, 0); font-size: 10pt; font-weight: 700; font-style: normal; text-decoration: none;"><u>VIOLATIONS:</u></span></span></div>

<table style="width: 100%;">
	<thead>
		<tr>
			<td style="width:20%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
			<td style="padding:5px; width:8%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Unit</strong></span></td>
			<td style="padding:5px; width:19%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Responsibility</strong></span></td>
			<td style="padding:5px; width:11%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Fix By</strong></span></td>
			<td style="padding:5px; width:10%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Status</strong></span></td>
			<td style="padding:5px; width:32%;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong>Violation and Notes</strong></span></td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026635}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1027832}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1027836}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1027835}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026634}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1027831}}}</span></td>
		</tr>
	</tbody>
</table>
<div>
	<br>
</div>
<div><u><strong><span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px;">UNREGISTERED MOTOR VEHICLES:</span></strong></u></div>

<table style="width: 100%;">
	<thead>
		<tr>
			<td style="width: 21.0267%;">
				<br>
			</td>
			<td style="padding: 5px; width: 7.7959%; text-align: center;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Make</span></strong></td>
			<td style="padding: 5px; width: 15.8219%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Model</span></strong></td>
			<td style="padding: 5px; width: 9.3817%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Color</span></strong></td>
			<td style="padding: 5px; width: 8.7834%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">License Plate #</span></strong></td>
			<td style="width: 14.2857%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Status</span></strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br></span></td>
			<td style="padding: 5px; width: 26.2902%;"><strong><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">Notes</span></strong></td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026696}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026693}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026694}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026695}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026696}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1028539}}}</span></td>
			<td style="padding:5px;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{{OL1026698}}}</span>
				<br>
			</td>
		</tr>
	</tbody>
</table>
<div>
	<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><br><br></span></div>
	<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><span style="color: rgb(0, 0, 0); font-size: 10pt; font-weight: 400; font-style: normal; text-decoration: none;">Please note: &nbsp;You are required to apply for any permits necessary in accordance with applicable zoning requirements or any building permits necessary to gain compliance. &nbsp;</span>&nbsp;</strong></span></div>
	<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><br></strong></span></div>
	<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><span style="color: rgb(0, 0, 0); font-size: 9pt; font-weight: 400; font-style: normal; text-decoration: none;">RIGHT OF APPEAL: Receipt of this notice of Violation entitles the recipient to appeal the order to this department. Such petition must be in writing and filed within seven days after the day the order was received. Please refer to&nbsp;</span><span style="color: rgb(0, 0, 0); font-size: 11pt; font-weight: 400; font-style: normal; text-decoration: none;">105 CMR 410.800&nbsp;</span><span style="color: rgb(0, 0, 0); font-size: 9pt; font-weight: 400; font-style: normal; text-decoration: none;">et seq. for all rights and remedies in regard to this Notice.</span>&nbsp;</strong></span></div>
	<div>

		<p style="page-break-before: always;"><span style="font-family: Times New Roman,Times,serif,-webkit-standard;"><strong><br></strong></span></p>
	</div>
	<div><span style="font-family: Times New Roman,Times,serif,-webkit-standard;">{{/if}}</span></div></div>


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
