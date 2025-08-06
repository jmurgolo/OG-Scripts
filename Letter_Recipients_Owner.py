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
			<td colspan="5" style="width: 99.9433%;"><span style="font-size: 14px;">{{FF1027852}}<br>{{streetNo}} {{streetName}}{{#if FF1027854}}, Unit {{FF1027854}} {{/if}}<br>{{city}}, {{state}} {{zipCode}} &nbsp;&nbsp;</span><span style="font-size: 14px; color: rgb(0, 0, 0);">&nbsp;&nbsp;</span><span style="font-size: 12px; color: rgb(0, 0, 0);">&nbsp;</span><span style="font-size: 14px; color: rgb(0, 0, 0);">&nbsp;</span>
				<br>
				<br>
			</td>
		</tr>
		<tr>
			<td colspan="3" style="width: 71.2533%;"><span style="font-size: 14px;"><strong>Re: {{streetNo}} {{streetName}}{{#if FF1027854}}, Unit {{FF1027854}} {{/if}} {{city}}, {{state}} {{zipCode}}</strong><strong><br></strong></span></td>
			<td style="width: 13.2022%; text-align: right; vertical-align: top;"><span style="font-size: 12px;">Parcel:&nbsp;</span></td>
			<td style="width: 15.4588%; text-align: left; vertical-align: top;"><span style="font-size: 12px;">{{mbl}}</span></td>
		</tr>
		<tr>
			<td style="width: 15.6939%;"><strong><br></strong></td>
			<td style="width: 21.8933%;"><strong><br></strong></td>
			<td style="width: 33.6719%;"><strong><br></strong></td>
			<td style="width: 13.2022%; text-align: right;"><span style="font-size: 12px;">Case Number:&nbsp;</span></td>
			<td style="width: 15.4588%;"><span style="font-size: 12px;">{{recordId}}</span><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: center;">
				<br><span style='font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 24px; font-weight: 700; font-style: normal; text-decoration: underline;'>CONDEMNATION</span><span style="font-size: 24px;">&nbsp;</span></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%; text-align: left;"><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>As a result of an inspection that was performed on the above property on {{FF1027645}}, conditions were found to exist that amount to a Condemnation. &nbsp;By the authority granted to me as the Deputy Director of the Department of Code Enforcement, Housing Division, City of Springfield, Massachusetts in accordance with the General Laws, I find that the Dwelling situated at&nbsp;</span><span style='box-sizing: border-box; font-size: 12px;box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>{{streetNo}} {{streetName}}</span><span style='box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; font-size: 12px;"><span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</span></span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;is unfit for human habitation. &nbsp;This finding is based upon violations of the &quot;State Sanitary Code, Chapter II: &nbsp;Minimum Standards of Fitness for Human Habitation, 105 CMR 410.000, Department of Public Health, Commonwealth of Massachusetts&quot; which are listed on the Attached Violation Sheet(s). <br style="box-sizing: border-box;">I determine in accordance with provisions of 105 CMR 410.650(E), that the danger to the life or health of the occupant(s) is so immediate that no delay may be permitted. &nbsp;I find that the Dwelling situated at&nbsp;</span><span style="box-sizing: border-box; color: rgb(65, 65, 65); font-family: sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; font-size: 12px;">{{streetNo}} {{streetName}}<span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}}, Unit {{unit}} {{/if}}</span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 12px;'>&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>is unfit for human habitation without providing the notification or hearing specified in 105 CMR 410.650(B) and (D).<br style="box-sizing: border-box;"><br style="box-sizing: border-box;">I ORDER that the&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: underline; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>SUBJECT PROPERTY</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;situated at&nbsp;</span><span style='box-sizing: border-box; font-size: 12px;box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>{{streetNo}} {{streetName}}</span><span style='box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; font-size: 12px;"><span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span>&nbsp;</span></span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;hereby is&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt; font-weight: 700;'>CONDEMNED</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>.<br style="box-sizing: border-box;"><br style="box-sizing: border-box;">I ORDER that the&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: underline; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>SUBJECT PROPERTY</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;situated at&nbsp;</span><span style='box-sizing: border-box; font-size: 12px;box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>{{streetNo}} {{streetName}}</span><span style='box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; font-size: 12px;"><span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span></span></span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;be&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt; font-weight: 700;'>VACATED</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>.<br style="box-sizing: border-box;"><br style="box-sizing: border-box;">I ORDER the OWNER TO SECURE the&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: underline; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>SUBJECT PROPERTY</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;situated at&nbsp;</span><span style='box-sizing: border-box; font-size: 12px;box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>{{streetNo}} {{streetName}}</span><span style='box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; font-size: 12px;"><span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span></span></span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>. <br style="box-sizing: border-box;"> <br style="box-sizing: border-box;">I advise you that the&nbsp;</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: underline; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>SUBJECT PROPERTY</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;situated at&nbsp;</span><span style='box-sizing: border-box; font-size: 14px;box-sizing: border-box; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt; font-weight: 400; font-style: normal; text-decoration: none;box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'><span style="box-sizing: border-box; font-size: 12px;">{{streetNo}} {{streetName}}</span><span style="box-sizing: border-box; font-size: 14px;"><span style="box-sizing: border-box; font-size: 12px;"><span style='box-sizing: border-box; color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;'>{{#if unit}}, Unit {{unit}} {{/if}}</span></span></span></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;Springfield, Massachusetts SHALL NOT AGAIN BE OCCUPIED, with out prior written approval from the Deputy Director of the Department of Code Enforcement, Housing Division. <br style="box-sizing: border-box;"> <br style="box-sizing: border-box;"></span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt; font-weight: 700;'>Right To A Hearing</span><span style='box-sizing: border-box; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration: none; font-family: "Times New Roman"; color: rgb(0, 0, 0); font-size: 9pt;'>&nbsp;- You have the right to a hearing pursuant to 105 CMR 410.000, in conjunction with the emergency procedures outlined in 105 CMR 400.200(B), the regulation which provides for a hearing whenever an emergency exists. &nbsp;You may request a hearing only upon compliance with this order and within seven days after the order has been served. &nbsp;This petition must be in writing to the attention of the Deputy Director. &nbsp;Upon receipt of the petition, you will be granted a hearing as soon as possible but, not later than ten days after the filing of the petition.<br style="box-sizing: border-box;">You have the right to inspect and obtain copies of all relevant inspection reports, orders, notices or other documentary information in the possession of the Department of Code Enforcement, Housing Division, and the right to be represented at the hearing. &nbsp;Any adverse party has a right to appear at said hearing.</span>
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
<div>{{/if}}</div>

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
with open("Results.html", "w", encoding="utf-8") as f:
    for block in output_blocks:
        f.write(block + "\n\n")

print("✅ All variations written to output.html")
