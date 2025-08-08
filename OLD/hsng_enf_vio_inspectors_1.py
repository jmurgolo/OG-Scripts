"""
 THi is used per inspection to replace the inspector names and eventually phone numbers.
 

"""

import re

# 🔹 Paste the original raw text block here
input_text = """<table style="width: 100%; margin-left: calc(0%);">
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
			<td style="width: 38.58%;"><strong><br></strong></td>
			<td style="width: 8.4766%;"><strong><br></strong></td>
			<td style="width: 15.2973%;"><strong><br></strong></td>
		</tr>
		<tr>
			<td colspan="5" style="width: 99.9433%;">&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: rgb(0, 0, 0);">&nbsp;{{#if FF1027709}}{{FF1027838}}<br>&nbsp; &nbsp; &nbsp; &nbsp; {{FF1027839}} else</span>
				<br><span style="color: rgb(0, 0, 0);">&nbsp; &nbsp; &nbsp; &nbsp; {{ownerName}}<br></span><span style="font-size: 14px; color: rgb(0, 0, 0);">&nbsp; &nbsp; &nbsp; &nbsp; {{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}}<br>&nbsp; &nbsp; &nbsp; &nbsp; {{ownerCity}},{{ownerState}} {{ownerZipCode}}</span>{{/if}}</td>
		</tr>
		<tr>
			<td colspan="3" style="width: 76.1689%;"><span style="font-size: 14px;"><span style="font-size: 14px;">&nbsp; &nbsp; &nbsp; &nbsp; <span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">Re:&nbsp;</span>{{streetNo}} {{streetName}}<span style="font-size: 14px;"><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span> <span style="font-size: 14px;">{{#if FF39670}}, <span style="font-size: 14px;">{{FF1026624}}{{/if}}<span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;">, {{city}}, {{state}} {{zipCode}}</span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
			<td style="width: 8.4766%; text-align: right; vertical-align: top;">Parcel &nbsp;</td>
			<td style="width: 15.2973%; text-align: left; vertical-align: top;">{{mbl}}</td>
		</tr>
		<tr>
			<td style="width: 15.6939%;"><strong><br></strong></td>
			<td style="width: 21.8933%;"><strong><br></strong></td>
			<td style="width: 38.58%;"><strong><br></strong></td>
			<td style="width: 8.4766%;">Case Number:</td>
			<td style="width: 15.2973%;">{{recordId}}<strong><br></strong></td>
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
			<td colspan="3" style="width: 99.9432%;"><strong>R</strong>e: <span style="color: rgb(0, 0, 0);">&nbsp;<strong>{{#if FF1027709}}{{FF1027838}} {{FF1027839}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></td>
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
					<div style="margin-top:-34px; margin-left:60px;">{{{OL1026634}}}</div>{{{OL1027834}}}</td>
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
	</div>{{#if FF1027819}}

	<p style="page-break-before: always;">
		<br>
	</p>

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
				<td style="width: 38.58%;"><strong><br></strong></td>
				<td style="width: 8.4766%;"><strong><br></strong></td>
				<td style="width: 15.2973%;"><strong><br></strong></td>
			</tr>
			<tr>
				<td colspan="5" style="width: 99.9433%;">&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: rgb(0, 0, 0);">&nbsp; {{FF1027821}} {{{FF1027823}}}</span></td>
			</tr>
			<tr>
				<td colspan="3" style="width: 76.1689%;"><span style="font-size: 14px;"><span style="font-size: 14px;">&nbsp; &nbsp; &nbsp; &nbsp; <span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">Re:&nbsp;</span>{{streetNo}} {{streetName}}<span style="font-size: 14px;"><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span> <span style="font-size: 14px;">{{#if FF39670}}, <span style="font-size: 14px;">{{FF1026624}}{{/if}}<span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;">, {{city}}, {{state}} {{zipCode}}</span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
				<td style="width: 8.4766%; text-align: right; vertical-align: top;">Parcel &nbsp;</td>
				<td style="width: 15.2973%; text-align: left; vertical-align: top;">{{mbl}}</td>
			</tr>
			<tr>
				<td style="width: 15.6939%;"><strong><br></strong></td>
				<td style="width: 21.8933%;"><strong><br></strong></td>
				<td style="width: 38.58%;"><strong><br></strong></td>
				<td style="width: 8.4766%;">Case Number:</td>
				<td style="width: 15.2973%;">{{recordId}}<strong><br></strong></td>
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
				<td colspan="3" style="width: 99.9432%;"><strong>Re:&nbsp;</strong><span style="color: rgb(0, 0, 0);">&nbsp;<span style="color: rgb(0, 0, 0);"><strong>{{#if FF1027709}}{{FF1027838}} {{FF1027839}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></span></td>
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
					<td style="width: 18.2517%; vertical-align: top;">{{{OL1026795}}}</td>
					<td style="width: 81.7483%; display: inline-block; vertical-align: top;">Responsibility:
						<div style="margin-top:-34px; margin-left:110px;">{{{OL1027837}}}</div>Unit:
						<div style="margin-top:-34px; margin-left:35px;">{{{OL1027833}}}</div>Corrections Required By:
						<div style="margin-top:-34px; margin-left:190px;">{{{OL1026794}}}</div>Status:
						<div style="margin-top:-34px; margin-left:60px;">{{{OL1026796}}}</div>{{{OL1027834}}}</td>
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
			</p>{{/if}} {{#if FF1027820}}

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
						<td style="width: 38.58%;"><strong><br></strong></td>
						<td style="width: 8.4766%;"><strong><br></strong></td>
						<td style="width: 15.2973%;"><strong><br></strong></td>
					</tr>
					<tr>
						<td colspan="5" style="width: 99.9433%;">&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: rgb(0, 0, 0);">&nbsp;{{FF1027822}} {{{FF1027824}}}</span></td>
					</tr>
					<tr>
						<td colspan="3" style="width: 76.1689%;"><span style="font-size: 14px;"><span style="font-size: 14px;">&nbsp; &nbsp; &nbsp; &nbsp; <span style="font-family:Times New Roman;color:#000000;font-size:11pt;font-weight:400;font-style:normal;text-decoration:none;">Re:&nbsp;</span>{{streetNo}} {{streetName}}<span style="font-size: 14px;"><span style='color: rgb(0, 0, 0); font-family: "Benton Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>{{#if unit}},&nbsp;Unit&nbsp;{{unit}} {{/if}}</span> <span style="font-size: 14px;">{{#if FF39670}}, <span style="font-size: 14px;">{{FF1026624}}{{/if}}<span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;"><span style="font-size: 14px;">, {{city}}, {{state}} {{zipCode}}</span></span></span></span></span></span></span></span></span></span><strong><br></strong></td>
						<td style="width: 8.4766%; text-align: right; vertical-align: top;">Parcel &nbsp;</td>
						<td style="width: 15.2973%; text-align: left; vertical-align: top;">{{mbl}}</td>
					</tr>
					<tr>
						<td style="width: 15.6939%;"><strong><br></strong></td>
						<td style="width: 21.8933%;"><strong><br></strong></td>
						<td style="width: 38.58%;"><strong><br></strong></td>
						<td style="width: 8.4766%;">Case Number:</td>
						<td style="width: 15.2973%;">{{recordId}}<strong><br></strong></td>
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
						<td colspan="3" style="width: 99.9432%;"><strong>Re:&nbsp;</strong><span style="color: rgb(0, 0, 0);">&nbsp;<span style="color: rgb(0, 0, 0);"><strong>{{#if FF1027709}}{{FF1027838}} {{FF1027839}} {{else}} {{ownerName}} &nbsp;{{ownerStreetNo}} {{ownerStreetName}} {{ownerUnit}} {{ownerCity}},{{ownerState}} {{ownerZipCode}}{{/if}}</strong></span></span></td>
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
							<td style="width: 18.2517%; vertical-align: top;">{{{OL1026795}}}</td>
							<td style="width: 81.7483%; display: inline-block; vertical-align: top;">Responsibility:
								<div style="margin-top:-34px; margin-left:110px;">{{{OL1027837}}}</div>Unit:
								<div style="margin-top:-34px; margin-left:35px;">{{{OL1027833}}}</div>Corrections Required By:
								<div style="margin-top:-34px; margin-left:190px;">{{{OL1026794}}}</div>Status:
								<div style="margin-top:-34px; margin-left:60px;">{{{OL1026796}}}</div>{{{OL1027834}}}</td>
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


# 2nd inspection
# raw_mapping_data = """
# {{FF1027328}}​ = Christopher Bennett
# {{FF1027329}}​ = William Brunton
# {{FF1027330}}​ = Danny Cueto
# {{FF1027331}}​ = Michelle Haska
# {{FF1027332}}​ = Mike Jones
# {{FF1027333}}​ = Jesus Martinez
# {{FF1027334}}​ = Michael McNulty
# {{FF1027335}}​ = Jermain Mitchell
# {{FF1027336}}​ = Michael Whiting
# {{FF1027337}}​ = James Murgolo
# {{FF1028306}}​ = Date of Inspection
# """

# 3rd inspection
raw_mapping_data = """
 {{FF1027471}}​ = Christopher Bennett
 {{FF1027472}}​ = William Brunton
 {{FF1027473}}​ = Danny Cueto
 {{FF1027474}}​ = Michelle Haska
 {{FF1027475}}​ = Mike Jones
 {{FF1027476}}​ = Jesus Martinez
 {{FF1027477}}​ = Michael McNulty
 {{FF1027478}}​ = Jermain Mitchell
 {{FF1027479}}​ = Michael Whiting
 {{FF1027480}}​ = James Murgolo
 {{FF1027481}}​ = Date of Inspection
"""

# 🔹 Step 1: Clean the mapping and build a name → new_code dictionary
cleaned_mapping = re.sub(r"[\u200b\u00a0]", "", raw_mapping_data)
pattern = re.compile(r"\{\{(FF\d+)\}}\s*=\s*(.+?)\s*$")

replacement_dict = {}
for line in cleaned_mapping.strip().splitlines():
    match = pattern.search(line.strip())
    if match:
        code, name = match.groups()
        replacement_dict[name.strip()] = code.strip()

# 🔹 Step 2: Replace each {{#if old_code}}Name{{/if}} block with the new one
def replacer(match):
    old_code = match.group(1)
    name = match.group(2).strip()
    new_code = replacement_dict.get(name)
    if new_code:
        return f"{{{{#if {new_code}}}}}{name}{{{{/if}}}}"
    else:
        print(f"⚠️ No replacement found for: {name}")
        return match.group(0)  # leave unchanged if not found

# Pattern to match: {{#if FF1234}}Name{{/if}}
pattern = re.compile(r"\{\{#if (FF\d+)\}\}(.+?)\{\{\/if\}\}")

# 🔹 Step 3: Apply the replacements
output_text = pattern.sub(replacer, input_text)

# 🔹 Step 4: Save the result
with open("find and replace.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("✅ Done! Cleaned output saved to 'replaced_output.txt'.")
