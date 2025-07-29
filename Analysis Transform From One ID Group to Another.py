import re

# Sample input blocks as multiline strings
left_block = """General Info
 {{FF1029174}}​ = Inspection Access Contact Name
 {{FF1029175}}​ = Inspection Access Contact Phone
 {{FF1029176}}​ = Inspection Access Contact Title
 {{FF1029178}}​ = Other Source
 {{FF1029186}}​ = When & how did you contact them
 {{FF1029187}}​ = Who did you contact
 {{FF1029189}}​ = Unit Number - to be printed on the inspection report
 {{FF1029192}}​ = Alternative Owner Name
 {{FF1029195}}​ = Second Owner Name
 {{FF1029198}}​ = Third Owner Name
 {{{FF1029172}}}​ = General Notes
 {{{FF1029188}}}​ = What was the response
 {{{FF1029193}}}​ = Alternative Owner Address
 {{{FF1029196}}}​ = Second Owner Address
 {{{FF1029199}}}​ = Third Owner Address
 {{{FF1029214}}}​ = Refer to Court Details
 {{{FF1029216}}}​ = Refer to Housing Enforcement Details
 {{{FF1029218}}}​ = Refer to Electrical Details
 {{{FF1029220}}}​ = Refer to Building Details
 {{{FF1029222}}}​ = Refer to Fire Details
 {{{FF1029224}}}​ = Refer to Police Ordinance Details
 {{{FF1029226}}}​ = Refer to Health Department Details
 {{{FF1029228}}}​ = Refer to Elderly Affairs Details
 {{{FF1029230}}}​ = Refer to Animal Control Details
 {{{FF1029232}}}​ = Refer to Office of Housing Details
 {{{FF1029234}}}​ = Refer to Zoning Details
 {{FF1029179}}​ = Interior
 {{FF1029180}}​ = Exterior
 {{FF1029181}}​ = Referral
 {{FF1029185}}​ = Have you contacted the owner
 {{FF1029191}}​ = Owner Different than GIS
 {{FF1029194}}​ = Add Second Additional Owner
 {{FF1029197}}​ = Add Third Additional Owner
 {{FF1029201}}​ = Section 105 Required
 {{FF1029213}}​ = Refer to Court
 {{FF1029215}}​ = Refer to Housing Enforcement
 {{FF1029217}}​ = Refer to Electrical Enforcement
 {{FF1029219}}​ = Refer to Building Enforcement
 {{FF1029221}}​ = Refer to Fire Department
 {{FF1029223}}​ = Refer to Police Ordinance
 {{FF1029225}}​ = Refer to Health Department
 {{FF1029227}}​ = Refer to Elderly Affairs
 {{FF1029229}}​ = Refer to Animal Control
 {{FF1029231}}​ = Refer to Office of Housing
 {{FF1029233}}​ = Refer to Zoning
 {{FF1029235}}​ = Add Parties Responsible for Payment
 {{FF1029177}}​ = Complaint Source
 {{FF1029182}}​ = Usage Group
 {{FF1029183}}​ = When did the problem first occur
First Inspection
 {{{FF1029292}}}​ = First Inspection Notes For Administrative Staff
 {{FF1029277}}​ = Court
 {{FF1029278}}​ = Emergency
 {{FF1029279}}​ = Inspection
 {{FF1029284}}​ = Paul Brodeur
 {{FF1029285}}​ = Roderick Cruz
 {{FF1029286}}​ = Sam Santaniello
 {{FF1029287}}​ = Thomas Witkop
 {{FF1031127}}​ = James Murgolo
 {{FF1029282}}​ = First Inspection Time
 {{FF1029291}}​ = First Inspection Result
 {{FF1029281}}​ = Date of First Inspection
Second Inspection
 {{{FF1029314}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1029293}}​ = Schedule Second Inspection
 {{FF1029296}}​ = Court
 {{FF1029297}}​ = Emergency
 {{FF1029298}}​ = Inspection
 {{FF1029303}}​ = Paul Brodeur
 {{FF1029304}}​ = Roderick Cruz
 {{FF1029305}}​ = Sam Santaniello
 {{FF1029306}}​ = Thomas Witkop
 {{FF1029312}}​ = James Murgolo
 {{FF1029301}}​ = Time of Second Inspection
 {{FF1029313}}​ = Second Inspection Result
 {{FF1029300}}​ = Date of Second Inspection
Third Inspection
 {{{FF1029336}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1029315}}​ = Schedule Third Inspection
 {{FF1029317}}​ = Court
 {{FF1029319}}​ = Emergency
 {{FF1029320}}​ = Inspection
 {{FF1029325}}​ = Paul Brodeur
 {{FF1029326}}​ = Roderick Cruz
 {{FF1029327}}​ = Sam Santaniello
 {{FF1029328}}​ = Thomas Witkop
 {{FF1029334}}​ = James Murgolo
 {{FF1029323}}​ = Time of Third Inspection
 {{FF1029335}}​ = Third Inspection Result
 {{FF1029322}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1029358}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1029337}}​ = Schedule Fourth Inspection
 {{FF1029340}}​ = Court
 {{FF1029341}}​ = Emergency
 {{FF1029342}}​ = Inspection
 {{FF1029347}}​ = Paul Brodeur
 {{FF1029348}}​ = Roderick Cruz
 {{FF1029349}}​ = Sam Santaniello
 {{FF1029350}}​ = Thomas Witkop
 {{FF1029356}}​ = James Murgolo
 {{FF1029345}}​ = Time of Fourth Inspection
 {{FF1029357}}​ = Fourth Inspection Result
 {{FF1029344}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1029380}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1029359}}​ = Schedule Fifth Inspection
 {{FF1029362}}​ = Court
 {{FF1029363}}​ = Emergency
 {{FF1029364}}​ = Inspection
 {{FF1029369}}​ = Paul Brodeur
 {{FF1029370}}​ = Roderick Cruz
 {{FF1029371}}​ = Sam Santaniello
 {{FF1029372}}​ = Thomas Witkop
 {{FF1029378}}​ = James Murgolo
 {{FF1029367}}​ = Time of Fifth Inspection
 {{FF1029379}}​ = Fifth Inspection Result
 {{FF1029366}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1029402}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1029381}}​ = Schedule Sixth inspection
 {{FF1029384}}​ = Court
 {{FF1029385}}​ = Emergency
 {{FF1029386}}​ = Inspection
 {{FF1029391}}​ = Paul Brodeur
 {{FF1029392}}​ = Roderick Cruz
 {{FF1029393}}​ = Sam Santaniello
 {{FF1029394}}​ = Thomas Witkop
 {{FF1029400}}​ = James Murgolo
 {{FF1029389}}​ = Time of Sixth Inspection
 {{FF1029401}}​ = Sixth Inspection Result
 {{FF1029388}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1029424}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1029403}}​ = Schedule Seventh inspection
 {{FF1029406}}​ = Court
 {{FF1029407}}​ = Emergency
 {{FF1029408}}​ = Inspection
 {{FF1029413}}​ = Paul Brodeur
 {{FF1029414}}​ = Roderick Cruz
 {{FF1029415}}​ = Sam Santaniello
 {{FF1029416}}​ = Thomas Witkop
 {{FF1029422}}​ = James Murgolo
 {{FF1029411}}​ = Time of Seventh Inspection
 {{FF1029423}}​ = Seventh Inspection Result
 {{FF1029410}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1029446}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1029425}}​ = Schedule Eighth inspection
 {{FF1029428}}​ = Court
 {{FF1029429}}​ = Emergency
 {{FF1029430}}​ = Inspection
 {{FF1029435}}​ = Paul Brodeur
 {{FF1029436}}​ = Roderick Cruz
 {{FF1029437}}​ = Sam Santaniello
 {{FF1029438}}​ = Thomas Witkop
 {{FF1029444}}​ = James Murgolo
 {{FF1029433}}​ = Time of Eighth Inspection
 {{FF1029445}}​ = Eighth Inspection Result
 {{FF1029432}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1029468}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1029447}}​ = Schedule Ninth inspection
 {{FF1029450}}​ = Court
 {{FF1029451}}​ = Emergency
 {{FF1029452}}​ = Inspection
 {{FF1029457}}​ = Paul Brodeur
 {{FF1029458}}​ = Roderick Cruz
 {{FF1029459}}​ = Sam Santaniello
 {{FF1029460}}​ = Thomas Witkop
 {{FF1029466}}​ = James Murgolo
 {{FF1029455}}​ = Time of Ninth Inspection
 {{FF1029467}}​ = Ninth Inspection Result
 {{FF1029454}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1029490}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1029469}}​ = Schedule Tenth inspection
 {{FF1029472}}​ = Court
 {{FF1029473}}​ = Emergency
 {{FF1029474}}​ = Inspection
 {{FF1029479}}​ = Paul Brodeur
 {{FF1029480}}​ = Roderick Cruz
 {{FF1029481}}​ = Sam Santaniello
 {{FF1029482}}​ = Thomas Witkop
 {{FF1029488}}​ = James Murgolo
 {{FF1029477}}​ = Time of Tenth Inspection
 {{FF1029489}}​ = Tenth Inspection Result
 {{FF1029476}}​ = Date of Tenth Inspection
Letters
 {{FF1029493}}​ = Send First Violation Letters
 {{FF1029494}}​ = Send Second Violation Letters
 {{FF1029495}}​ = Send Third Violation Letters
 {{FF1029496}}​ = Send Fourth Violation Letters
 {{FF1029497}}​ = Send Fifth Violation Letters
 {{FF1029498}}​ = Send Sixth Violation Letters
 {{FF1029499}}​ = Send Seventh Violation Letters
 {{FF1029500}}​ = Send Eighth Violation Letters
 {{FF1029501}}​ = Send Ninth Violation Letters
 {{FF1029502}}​ = Send Tenth Violation Letters
 {{FF1029526}}​ = First Stop Work Letter
 {{FF1029527}}​ = Second Stop Work Letter
 {{FF1029528}}​ = Third Stop Work Letter
 {{FF1029529}}​ = Fourth Stop Work Letter
 {{FF1029530}}​ = Fifth Stop Work Letter
 {{FF1029531}}​ = Sixth Stop Work Letter
 {{FF1029532}}​ = Seventh Stop Work Letter
 {{FF1029533}}​ = Eighth Stop Work Letter
 {{FF1029534}}​ = Ninth Stop Work Letter
 {{FF1029535}}​ = Tenth Stop Work Letter
First Ticket Details
 {{{FF1029560}}}​ = First Ticket Notes for Administrative Staff
 {{FF1029558}}​ = First Ticket Total
 {{FF1029559}}​ = First Ticket Due Date
Second Ticket Details
 {{{FF1029564}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1029562}}​ = Second Ticket Total
 {{FF1029563}}​ = Second Ticket Due Date
Third Ticket Details
 {{{FF1029568}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1029567}}​ = Third Ticket Total
 {{FF1029566}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{{FF1029572}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1029570}}​ = Fourth Ticket Total
 {{FF1029571}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{{FF1029576}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1029574}}​ = Fifth Ticket Total
 {{FF1029575}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{{FF1029580}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1029578}}​ = Sixth Ticket Total
 {{FF1029579}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{{FF1029584}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1029582}}​ = Seventh Ticket Total
 {{FF1029583}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{{FF1029588}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1029586}}​ = Eighth Ticket Total
 {{FF1029587}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{{FF1029592}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1029590}}​ = Ninth Ticket Total
 {{FF1029591}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{{FF1029596}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1029594}}​ = Tenth Ticket Total
 {{FF1029595}}​ = Tenth Ticket Due Date

Multi Entry Section Entries:
Please note that object list entries are marked with three curly brackets, not two.


Plumbing and Gas Violations
 {{{OL1029258}}}​ = Unit(s)
 {{{OL1029255}}}​ = Code / Description
 {{{OL1029257}}}​ = Responsible Party
 {{{OL1029259}}}​ = Status
 {{{OL1029261}}}​ = Correction Required By:
 {{{OL1029260}}}​ = Picture
Certified Letters
 {{{OL1029262}}}​ = Certified Number
 {{{OL1029264}}}​ = Recipient
 {{{OL1029265}}}​ = Cc
 {{{OL1029263}}}​ = Date sent
Emergency Violations
 {{{OL1029266}}}​ = Code / Description
 {{{OL1029270}}}​ = Unit
 {{{OL1029267}}}​ = Code / Description
 {{{OL1029269}}}​ = Responsible Party
 {{{OL1029272}}}​ = Status
 {{{OL1029271}}}​ = Correction Required By:
 {{{OL1029273}}}​ = Picture
Parties Responsible for Online Payment
 {{{OL1029274}}}​ = Email Address
First Ticket
 {{{OL1029491}}}​ = First Ticket Description
Second Ticket
 {{{OL1029561}}}​ = Second Ticket Description
Third Ticket
 {{{OL1029565}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1029569}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1029573}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1029577}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1029581}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1029585}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1029589}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1029593}}}​ = Tenth Ticket Description

Multi Entry Sections:
Please note that multiEntry sections are marked with three curly brackets, not two.


 {{{MES1012817}}}​ = Plumbing and Gas Violations
 {{{MES1012818}}}​ = Certified Letters
 {{{MES1012819}}}​ = Emergency Violations
 {{{MES1012820}}}​ = Parties Responsible for Online Payment
 {{{MES1012831}}}​ = First Ticket
 {{{MES1012834}}}​ = Second Ticket
 {{{MES1012836}}}​ = Third Ticket
 {{{MES1012838}}}​ = Fourth Ticket
 {{{MES1012840}}}​ = Fifth Ticket
 {{{MES1012842}}}​ = Sixth Ticket
 {{{MES1012844}}}​ = Seventh Ticket
 {{{MES1012846}}}​ = Eighth Ticket
 {{{MES1012848}}}​ = Ninth Ticket
 {{{MES1012850}}}​ = Tenth Ticket

Fees:
 {{FEE653}}​ = Violation Fee
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
 {{assignedToTS2261}}​ = Send Out Record Letters
 {{assignedToTS2357}}​ = Section 105 Letter
 {{assignedToTS2262}}​ = Send Out First Inspection Letters
 {{assignedToTS2287}}​ = First Stop Work Letter
 {{assignedToTS2293}}​ = First Violation Letter
 {{assignedToTS2263}}​ = Approve First Ticket
 {{assignedToTS2291}}​ = First Ticket
 {{assignedToTS2243}}​ = Send Out Second Inspection Letters
 {{assignedToTS2294}}​ = Second Violation Letter
 {{assignedToTS2325}}​ = Second Stop Work Letter
 {{assignedToTS2244}}​ = Approve Second Ticket
 {{assignedToTS2324}}​ = Second Ticket
 {{assignedToTS2245}}​ = Send Out Third Inspection Letters
 {{assignedToTS2295}}​ = Third Violation Letter Owner
 {{assignedToTS2284}}​ = Third Stop Work Letter
 {{assignedToTS2253}}​ = Approve Third Ticket
 {{assignedToTS2285}}​ = Third Ticket
 {{assignedToTS2246}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS2296}}​ = Fourth Violation Letter Owner
 {{assignedToTS2321}}​ = Fourth Stop Work Letter
 {{assignedToTS2254}}​ = Approve Fourth Ticket
 {{assignedToTS2323}}​ = Fourth Ticket
 {{assignedToTS2247}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS2297}}​ = Fifth Violation Letter Owner
 {{assignedToTS2318}}​ = Fifth Stop Work Letter
 {{assignedToTS2255}}​ = Approve Fifth Ticket
 {{assignedToTS2320}}​ = Fifth Ticket
 {{assignedToTS2248}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS2298}}​ = Sixth Violation Letter Owner
 {{assignedToTS2315}}​ = Sixth Stop Work Letter
 {{assignedToTS2256}}​ = Approve Sixth Ticket
 {{assignedToTS2317}}​ = Sixth Ticket
 {{assignedToTS2249}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS2299}}​ = Seventh Violation Letter Owner
 {{assignedToTS2313}}​ = Seventh Stop Work Letter
 {{assignedToTS2257}}​ = Approve Seventh Ticket
 {{assignedToTS2314}}​ = Seventh Ticket
 {{assignedToTS2250}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS2300}}​ = Eighth Violation Letter Owner
 {{assignedToTS2306}}​ = Eighth Stop Work Letter
 {{assignedToTS2258}}​ = Approve Eighth Ticket
 {{assignedToTS2311}}​ = Eighth Ticket
 {{assignedToTS2251}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS2301}}​ = Ninth Violation Letter Owner
 {{assignedToTS2309}}​ = Ninth Stop Work Letter
 {{assignedToTS2259}}​ = Approve Ninth Ticket
 {{assignedToTS2308}}​ = Ninth Ticket
 {{assignedToTS2252}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS2302}}​ = Tenth Violation Letter Owner
 {{assignedToTS2303}}​ = Tenth Stop Work Letter
 {{assignedToTS2260}}​ = Approve Tenth Ticket
 {{assignedToTS2305}}​ = Tenth Ticket
 {{assignedToTS2283}}​ = Tenth Inspection Date and Time
 {{assignedToTS2282}}​ = Ninth Inspection Date and Time
 {{assignedToTS2281}}​ = Eighth Inspection Date and Time
 {{assignedToTS2280}}​ = Seventh Inspection Date and Time
 {{assignedToTS2279}}​ = Sixth Inspection Date and Time
 {{assignedToTS2278}}​ = Fifth Inspection Date and Time
 {{assignedToTS2277}}​ = Fourth Inspection Date and Time
 {{assignedToTS2276}}​ = Third Inspection Date and Time
 {{assignedToTS2275}}​ = Second Inspection Date and Time
 {{assignedToTS2274}}​ = First Inspection Date and Time
 {{assignedToTS2264}}​ = Tenth Violation Fee
 {{assignedToTS2273}}​ = Ninth Violation Fee
 {{assignedToTS2272}}​ = Eighth Violation Fee
 {{assignedToTS2271}}​ = Seventh Violation Fee
 {{assignedToTS2270}}​ = Sixth Violation Fee
 {{assignedToTS2269}}​ = Fifth Violation Fee
 {{assignedToTS2268}}​ = Fourth Violation Fee
 {{assignedToTS2267}}​ = Third Violation Fee
 {{assignedToTS2266}}​ = Second Violation Fee
 {{assignedToTS2265}}​ = First Violation Fee
 {{assignedToTS2231}}​ = Refer to Court
 {{assignedToTS2234}}​ = Refer to Building Enforcement
 {{assignedToTS2236}}​ = Refer to Animal Control
 {{assignedToTS2233}}​ = Refer to Electrical Enforcement
 {{assignedToTS2237}}​ = Refer to Police Ordinance
 {{assignedToTS2238}}​ = Refer to Health Department
 {{assignedToTS2232}}​ = Refer to Housing Enforcement
 {{assignedToTS2241}}​ = Refer to Zoning
 {{assignedToTS2240}}​ = Refer to Office of Housing
 {{assignedToTS2239}}​ = Refer to Elderly Affairs
 {{assignedToTS2235}}​ = Refer to Fire"""



right_block = """General Info
 {{FF1023307}}​ = Inspection Access Contact Name
 {{FF1023308}}​ = Inspection Access Contact Phone
 {{FF1023309}}​ = Inspection Access Contact Title
 {{FF1023311}}​ = Other Source
 {{FF1023319}}​ = When & how did you contact them
 {{FF1023320}}​ = Who did you contact
 {{FF1023322}}​ = Unit Number - to be printed on the inspection report
 {{FF1023325}}​ = Alternative Owner Name
 {{FF1023328}}​ = Second Owner Name
 {{FF1023331}}​ = Third Owner Name
 {{{FF1023305}}}​ = General Notes
 {{{FF1023321}}}​ = What was the response
 {{{FF1023326}}}​ = Alternative Owner Address
 {{{FF1023329}}}​ = Second Owner Address
 {{{FF1023332}}}​ = Third Owner Address
 {{{FF1023337}}}​ = Refer to Court Details
 {{{FF1023339}}}​ = Refer to Housing Enforcement Details
 {{{FF1023341}}}​ = Refer to Electrical Details
 {{{FF1023343}}}​ = Refer to Building Details
 {{{FF1023345}}}​ = Refer to Fire Details
 {{{FF1023347}}}​ = Refer to Police Ordinance Details
 {{{FF1023349}}}​ = Refer to Health Department Details
 {{{FF1023351}}}​ = Refer to Elderly Affairs Details
 {{{FF1023353}}}​ = Refer to Animal Control Details
 {{{FF1023355}}}​ = Refer to Office of Housing Details
 {{{FF1023357}}}​ = Refer to Zoning Details
 {{FF1023312}}​ = Interior
 {{FF1023313}}​ = Exterior
 {{FF1023314}}​ = Referral
 {{FF1023318}}​ = Have you contacted the owner
 {{FF1023324}}​ = Owner Different than GIS
 {{FF1023327}}​ = Add Second Additional Owner
 {{FF1023330}}​ = Add Third Additional Owner
 {{FF1023334}}​ = Section 105 Required
 {{FF1023336}}​ = Refer to Court
 {{FF1023338}}​ = Refer to Housing Enforcement
 {{FF1023340}}​ = Refer to Electrical Enforcement
 {{FF1023342}}​ = Refer to Building Enforcement
 {{FF1023344}}​ = Refer to Fire Department
 {{FF1023346}}​ = Refer to Police Ordinance
 {{FF1023348}}​ = Refer to Health Department
 {{FF1023350}}​ = Refer to Elderly Affairs
 {{FF1023352}}​ = Refer to Animal Control
 {{FF1023354}}​ = Refer to Office of Housing
 {{FF1023356}}​ = Refer to Zoning
 {{FF1023358}}​ = Add Parties Responsible for Payment
 {{FF1023310}}​ = Complaint Source
 {{FF1023315}}​ = Usage Group
 {{FF1023316}}​ = When did the problem first occur
First Inspection
 {{{FF1023391}}}​ = First Inspection Notes For Administrative Staff
 {{FF1023378}}​ = Court
 {{FF1023379}}​ = Emergency
 {{FF1023380}}​ = Inspection
 {{FF1023385}}​ = Paul Brodeur
 {{FF1023386}}​ = Roderick Cruz
 {{FF1023387}}​ = Sam Santaniello
 {{FF1023388}}​ = Thomas Witkop
 {{FF1023389}}​ = James Murgolo
 {{FF1023383}}​ = First Inspection Time
 {{FF1023390}}​ = First Inspection Result
 {{FF1023382}}​ = Date of First Inspection
Second Inspection
 {{{FF1023407}}}​ = Second Inspection Notes For Administrative Staff
 {{FF1023392}}​ = Schedule Second Inspection
 {{FF1023394}}​ = Court
 {{FF1023395}}​ = Emergency
 {{FF1023396}}​ = Inspection
 {{FF1023401}}​ = Paul Brodeur
 {{FF1023402}}​ = Roderick Cruz
 {{FF1023403}}​ = Sam Santaniello
 {{FF1023404}}​ = Thomas Witkop
 {{FF1023405}}​ = James Murgolo
 {{FF1023399}}​ = Time of Second Inspection
 {{FF1023406}}​ = Second Inspection Result
 {{FF1023398}}​ = Date of Second Inspection
Third Inspection
 {{{FF1023423}}}​ = Third Inspection Notes For Administrative Staff
 {{FF1023408}}​ = Schedule Third Inspection
 {{FF1023410}}​ = Court
 {{FF1023411}}​ = Emergency
 {{FF1023412}}​ = Inspection
 {{FF1023417}}​ = Paul Brodeur
 {{FF1023418}}​ = Roderick Cruz
 {{FF1023419}}​ = Sam Santaniello
 {{FF1023420}}​ = Thomas Witkop
 {{FF1023421}}​ = James Murgolo
 {{FF1023415}}​ = Time of Third Inspection
 {{FF1023422}}​ = Third Inspection Result
 {{FF1023414}}​ = Date of Third Inspection
Fourth Inspection
 {{{FF1023439}}}​ = Fourth Inspection Notes For Administrative Staff
 {{FF1023424}}​ = Schedule Fourth Inspection
 {{FF1023426}}​ = Court
 {{FF1023427}}​ = Emergency
 {{FF1023428}}​ = Inspection
 {{FF1023433}}​ = Paul Brodeur
 {{FF1023434}}​ = Roderick Cruz
 {{FF1023435}}​ = Sam Santaniello
 {{FF1023436}}​ = Thomas Witkop
 {{FF1023437}}​ = James Murgolo
 {{FF1023431}}​ = Time of Fourth Inspection
 {{FF1023438}}​ = Fourth Inspection Result
 {{FF1023430}}​ = Date of Fourth Inspection
Fifth Inspection
 {{{FF1023455}}}​ = Fifth Inspection Notes For Administrative Staff
 {{FF1023440}}​ = Schedule Fifth Inspection
 {{FF1023442}}​ = Court
 {{FF1023443}}​ = Emergency
 {{FF1023444}}​ = Inspection
 {{FF1023449}}​ = Paul Brodeur
 {{FF1023450}}​ = Roderick Cruz
 {{FF1023451}}​ = Sam Santaniello
 {{FF1023452}}​ = Thomas Witkop
 {{FF1023453}}​ = James Murgolo
 {{FF1023447}}​ = Time of Fifth Inspection
 {{FF1023454}}​ = Fifth Inspection Result
 {{FF1023446}}​ = Date of Fifth Inspection
Sixth Inspection
 {{{FF1023471}}}​ = Sixth Inspection Notes For Administrative Staff
 {{FF1023456}}​ = Schedule Sixth inspection
 {{FF1023458}}​ = Court
 {{FF1023459}}​ = Emergency
 {{FF1023460}}​ = Inspection
 {{FF1023465}}​ = Paul Brodeur
 {{FF1023466}}​ = Roderick Cruz
 {{FF1023467}}​ = Sam Santaniello
 {{FF1023468}}​ = Thomas Witkop
 {{FF1023469}}​ = James Murgolo
 {{FF1023463}}​ = Time of Sixth Inspection
 {{FF1023470}}​ = Sixth Inspection Result
 {{FF1023462}}​ = Date of Sixth Inspection
Seventh Inspection
 {{{FF1023487}}}​ = Seventh Inspection Notes For Administrative Staff
 {{FF1023472}}​ = Schedule Seventh inspection
 {{FF1023474}}​ = Court
 {{FF1023475}}​ = Emergency
 {{FF1023476}}​ = Inspection
 {{FF1023481}}​ = Paul Brodeur
 {{FF1023482}}​ = Roderick Cruz
 {{FF1023483}}​ = Sam Santaniello
 {{FF1023484}}​ = Thomas Witkop
 {{FF1023485}}​ = James Murgolo
 {{FF1023479}}​ = Time of Seventh Inspection
 {{FF1023486}}​ = Seventh Inspection Result
 {{FF1023478}}​ = Date of Seventh Inspection
Eighth Inspection
 {{{FF1023503}}}​ = Eighth Inspection Notes For Administrative Staff
 {{FF1023488}}​ = Schedule Eighth inspection
 {{FF1023490}}​ = Court
 {{FF1023491}}​ = Emergency
 {{FF1023492}}​ = Inspection
 {{FF1023497}}​ = Paul Brodeur
 {{FF1023498}}​ = Roderick Cruz
 {{FF1023499}}​ = Sam Santaniello
 {{FF1023500}}​ = Thomas Witkop
 {{FF1023501}}​ = James Murgolo
 {{FF1023495}}​ = Time of Eighth Inspection
 {{FF1023502}}​ = Eighth Inspection Result
 {{FF1023494}}​ = Date of Eighth Inspection
Ninth Inspection
 {{{FF1023519}}}​ = Ninth Inspection Notes For Administrative Staff
 {{FF1023504}}​ = Schedule Ninth inspection
 {{FF1023506}}​ = Court
 {{FF1023507}}​ = Emergency
 {{FF1023508}}​ = Inspection
 {{FF1023513}}​ = Paul Brodeur
 {{FF1023514}}​ = Roderick Cruz
 {{FF1023515}}​ = Sam Santaniello
 {{FF1023516}}​ = Thomas Witkop
 {{FF1023517}}​ = James Murgolo
 {{FF1023511}}​ = Time of Ninth Inspection
 {{FF1023518}}​ = Ninth Inspection Result
 {{FF1023510}}​ = Date of Ninth Inspection
Tenth Inspection
 {{{FF1023535}}}​ = Tenth Inspection Notes For Administrative Staff
 {{FF1023520}}​ = Schedule Tenth inspection
 {{FF1023522}}​ = Court
 {{FF1023523}}​ = Emergency
 {{FF1023524}}​ = Inspection
 {{FF1023529}}​ = Paul Brodeur
 {{FF1023530}}​ = Roderick Cruz
 {{FF1023531}}​ = Sam Santaniello
 {{FF1023532}}​ = Thomas Witkop
 {{FF1023533}}​ = James Murgolo
 {{FF1023527}}​ = Time of Tenth Inspection
 {{FF1023534}}​ = Tenth Inspection Result
 {{FF1023526}}​ = Date of Tenth Inspection
Letters
 {{FF1023538}}​ = Send First Violation Letters
 {{FF1023539}}​ = Send Second Violation Letters
 {{FF1023540}}​ = Send Third Violation Letters
 {{FF1023541}}​ = Send Fourth Violation Letters
 {{FF1023542}}​ = Send Fifth Violation Letters
 {{FF1023543}}​ = Send Sixth Violation Letters
 {{FF1023544}}​ = Send Seventh Violation Letters
 {{FF1023545}}​ = Send Eighth Violation Letters
 {{FF1023546}}​ = Send Ninth Violation Letters
 {{FF1023547}}​ = Send Tenth Violation Letters
 {{FF1023549}}​ = First Stop Work Letter
 {{FF1023550}}​ = Second Stop Work Letter
 {{FF1023551}}​ = Third Stop Work Letter
 {{FF1023552}}​ = Fourth Stop Work Letter
 {{FF1023553}}​ = Fifth Stop Work Letter
 {{FF1023554}}​ = Sixth Stop Work Letter
 {{FF1023555}}​ = Seventh Stop Work Letter
 {{FF1023556}}​ = Eighth Stop Work Letter
 {{FF1023557}}​ = Ninth Stop Work Letter
 {{FF1023558}}​ = Tenth Stop Work Letter
First Ticket Details
 {{{FF1023561}}}​ = First Ticket Notes for Administrative Staff
 {{FF1023559}}​ = First Ticket Total
 {{FF1023560}}​ = First Ticket Due Date
Second Ticket Details
 {{{FF1023565}}}​ = Second Ticket Notes for Administrative Staff
 {{FF1023563}}​ = Second Ticket Total
 {{FF1023564}}​ = Second Ticket Due Date
Third Ticket Details
 {{{FF1023569}}}​ = Third Ticket Notes for Administrative Staff
 {{FF1023568}}​ = Third Ticket Total
 {{FF1023567}}​ = Third Ticket Due Date
Fourth Ticket Details
 {{{FF1023573}}}​ = Fourth Ticket Notes for Administrative Staff
 {{FF1023571}}​ = Fourth Ticket Total
 {{FF1023572}}​ = Fourth Ticket Due Date
Fifth Ticket Details
 {{{FF1023577}}}​ = Fifth Ticket Notes for Administrative Staff
 {{FF1023575}}​ = Fifth Ticket Total
 {{FF1023576}}​ = Fifth Ticket Due Date
Sixth Ticket Details
 {{{FF1023581}}}​ = Sixth Ticket Notes for Administrative Staff
 {{FF1023579}}​ = Sixth Ticket Total
 {{FF1023580}}​ = Sixth Ticket Due Date
Seventh Ticket Details
 {{{FF1023585}}}​ = Seventh Ticket Notes for Administrative Staff
 {{FF1023583}}​ = Seventh Ticket Total
 {{FF1023584}}​ = Seventh Ticket Due Date
Eighth Ticket Details
 {{{FF1023589}}}​ = Eighth Ticket Notes for Administrative Staff
 {{FF1023587}}​ = Eighth Ticket Total
 {{FF1023588}}​ = Eighth Ticket Due Date
Ninth Ticket Details
 {{{FF1023593}}}​ = Ninth Ticket Notes for Administrative Staff
 {{FF1023591}}​ = Ninth Ticket Total
 {{FF1023592}}​ = Ninth Ticket Due Date
Tenth Ticket Details
 {{{FF1023597}}}​ = Tenth Ticket Notes for Administrative Staff
 {{FF1023595}}​ = Tenth Ticket Total
 {{FF1023596}}​ = Tenth Ticket Due Date

Multi Entry Section Entries:
Please note that object list entries are marked with three curly brackets, not two.


Plumbing and Gas Violations
 {{{OL1023361}}}​ = Unit(s)
 {{{OL1023359}}}​ = Code / Description
 {{{OL1023360}}}​ = Responsible Party
 {{{OL1023362}}}​ = Status
 {{{OL1023364}}}​ = Correction Required By:
 {{{OL1023363}}}​ = Picture
Certified Letters
 {{{OL1023365}}}​ = Certified Number
 {{{OL1023367}}}​ = Recipient
 {{{OL1023368}}}​ = Cc
 {{{OL1023366}}}​ = Date sent
Emergency Violations
 {{{OL1023369}}}​ = Code / Description
 {{{OL1023372}}}​ = Unit
 {{{OL1023370}}}​ = Code / Description
 {{{OL1023371}}}​ = Responsible Party
 {{{OL1023374}}}​ = Status
 {{{OL1023373}}}​ = Correction Required By:
 {{{OL1023375}}}​ = Picture
Parties Responsible for Online Payment
 {{{OL1023376}}}​ = Email Address
First Ticket
 {{{OL1023536}}}​ = First Ticket Description
Second Ticket
 {{{OL1023562}}}​ = Second Ticket Description
Third Ticket
 {{{OL1023566}}}​ = Third Ticket Description
Fourth Ticket
 {{{OL1023570}}}​ = Fourth Ticket Description
Fifth Ticket
 {{{OL1023574}}}​ = Fifth Ticket Description
Sixth Ticket
 {{{OL1023578}}}​ = Sixth Ticket Description
Seventh Ticket
 {{{OL1023582}}}​ = Seventh Ticket Description
Eighth Ticket
 {{{OL1023586}}}​ = Eighth Ticket Description
Ninth Ticket
 {{{OL1023590}}}​ = Ninth Ticket Description
Tenth Ticket
 {{{OL1023594}}}​ = Tenth Ticket Description

Multi Entry Sections:
Please note that multiEntry sections are marked with three curly brackets, not two.


 {{{MES1012206}}}​ = Plumbing and Gas Violations
 {{{MES1012207}}}​ = Certified Letters
 {{{MES1012208}}}​ = Emergency Violations
 {{{MES1012209}}}​ = Parties Responsible for Online Payment
 {{{MES1012220}}}​ = First Ticket
 {{{MES1012223}}}​ = Second Ticket
 {{{MES1012225}}}​ = Third Ticket
 {{{MES1012227}}}​ = Fourth Ticket
 {{{MES1012229}}}​ = Fifth Ticket
 {{{MES1012231}}}​ = Sixth Ticket
 {{{MES1012233}}}​ = Seventh Ticket
 {{{MES1012235}}}​ = Eighth Ticket
 {{{MES1012237}}}​ = Ninth Ticket
 {{{MES1012239}}}​ = Tenth Ticket

Fees:
 {{FEE504}}​ = Violation Fee
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
 {{assignedToTS1243}}​ = Send Out Record Letters
 {{assignedToTS1296}}​ = Section 105 Letter
 {{assignedToTS1244}}​ = Send Out First Inspection Letters
 {{assignedToTS1268}}​ = First Stop Work Letter
 {{assignedToTS1270}}​ = First Violation Letter
 {{assignedToTS1245}}​ = Approve First Ticket
 {{assignedToTS1269}}​ = First Ticket
 {{assignedToTS1225}}​ = Send Out Second Inspection Letters
 {{assignedToTS1271}}​ = Second Violation Letter
 {{assignedToTS1295}}​ = Second Stop Work Letter
 {{assignedToTS1226}}​ = Approve Second Ticket
 {{assignedToTS1294}}​ = Second Ticket
 {{assignedToTS1227}}​ = Send Out Third Inspection Letters
 {{assignedToTS1272}}​ = Third Violation Letter Owner
 {{assignedToTS1266}}​ = Third Stop Work Letter
 {{assignedToTS1235}}​ = Approve Third Ticket
 {{assignedToTS1267}}​ = Third Ticket
 {{assignedToTS1228}}​ = Send Out Fourth Inspection Letters
 {{assignedToTS1273}}​ = Fourth Violation Letter Owner
 {{assignedToTS1292}}​ = Fourth Stop Work Letter
 {{assignedToTS1236}}​ = Approve Fourth Ticket
 {{assignedToTS1293}}​ = Fourth Ticket
 {{assignedToTS1229}}​ = Send Out Fifth Inspection Letters
 {{assignedToTS1274}}​ = Fifth Violation Letter Owner
 {{assignedToTS1290}}​ = Fifth Stop Work Letter
 {{assignedToTS1237}}​ = Approve Fifth Ticket
 {{assignedToTS1291}}​ = Fifth Ticket
 {{assignedToTS1230}}​ = Send Out Sixth Inspection Letters
 {{assignedToTS1275}}​ = Sixth Violation Letter Owner
 {{assignedToTS1288}}​ = Sixth Stop Work Letter
 {{assignedToTS1238}}​ = Approve Sixth Ticket
 {{assignedToTS1289}}​ = Sixth Ticket
 {{assignedToTS1231}}​ = Send Out Seventh Inspection Letters
 {{assignedToTS1276}}​ = Seventh Violation Letter Owner
 {{assignedToTS1286}}​ = Seventh Stop Work Letter
 {{assignedToTS1239}}​ = Approve Seventh Ticket
 {{assignedToTS1287}}​ = Seventh Ticket
 {{assignedToTS1232}}​ = Send Out Eighth Inspection Letters
 {{assignedToTS1277}}​ = Eighth Violation Letter Owner
 {{assignedToTS1282}}​ = Eighth Stop Work Letter
 {{assignedToTS1240}}​ = Approve Eighth Ticket
 {{assignedToTS1285}}​ = Eighth Ticket
 {{assignedToTS1233}}​ = Send Out Ninth Inspection Letters
 {{assignedToTS1278}}​ = Ninth Violation Letter Owner
 {{assignedToTS1284}}​ = Ninth Stop Work Letter
 {{assignedToTS1241}}​ = Approve Ninth Ticket
 {{assignedToTS1283}}​ = Ninth Ticket
 {{assignedToTS1234}}​ = Send Out Tenth Inspection Letters
 {{assignedToTS1279}}​ = Tenth Violation Letter Owner
 {{assignedToTS1280}}​ = Tenth Stop Work Letter
 {{assignedToTS1242}}​ = Approve Tenth Ticket
 {{assignedToTS1281}}​ = Tenth Ticket
 {{assignedToTS1265}}​ = Tenth Inspection Date and Time
 {{assignedToTS1264}}​ = Ninth Inspection Date and Time
 {{assignedToTS1263}}​ = Eighth Inspection Date and Time
 {{assignedToTS1262}}​ = Seventh Inspection Date and Time
 {{assignedToTS1261}}​ = Sixth Inspection Date and Time
 {{assignedToTS1260}}​ = Fifth Inspection Date and Time
 {{assignedToTS1259}}​ = Fourth Inspection Date and Time
 {{assignedToTS1258}}​ = Third Inspection Date and Time
 {{assignedToTS1257}}​ = Second Inspection Date and Time
 {{assignedToTS1256}}​ = First Inspection Date and Time
 {{assignedToTS1246}}​ = Tenth Violation Fee
 {{assignedToTS1255}}​ = Ninth Violation Fee
 {{assignedToTS1254}}​ = Eighth Violation Fee
 {{assignedToTS1253}}​ = Seventh Violation Fee
 {{assignedToTS1252}}​ = Sixth Violation Fee
 {{assignedToTS1251}}​ = Fifth Violation Fee
 {{assignedToTS1250}}​ = Fourth Violation Fee
 {{assignedToTS1249}}​ = Third Violation Fee
 {{assignedToTS1248}}​ = Second Violation Fee
 {{assignedToTS1247}}​ = First Violation Fee
 {{assignedToTS1214}}​ = Refer to Court
 {{assignedToTS1217}}​ = Refer to Building Enforcement
 {{assignedToTS1219}}​ = Refer to Animal Control
 {{assignedToTS1216}}​ = Refer to Electrical Enforcement
 {{assignedToTS1220}}​ = Refer to Police Ordinance
 {{assignedToTS1221}}​ = Refer to Health Department
 {{assignedToTS1215}}​ = Refer to Housing Enforcement
 {{assignedToTS1224}}​ = Refer to Zoning
 {{assignedToTS1223}}​ = Refer to Office of Housing
 {{assignedToTS1222}}​ = Refer to Elderly Affairs
 {{assignedToTS1218}}​ = Refer to Fire"""

# Regex to extract field code and label
pattern = r"\{\{(?:{)?(FF\d+)\}?\}\}.*?=\s(.+)$"

def parse_block(text):
    return dict(re.findall(pattern, text, flags=re.MULTILINE))

# Parse both blocks
left_dict = parse_block(left_block)
right_dict = parse_block(right_block)

# Reverse right_dict to lookup by label
reverse_right_dict = {label.strip(): code for code, label in right_dict.items()}

# Perform mapping
mapped = []
unmatched = []
for left_code, label in left_dict.items():
    cleaned_label = label.strip()
    if cleaned_label in reverse_right_dict:
        mapped.append(f"{left_code} = {reverse_right_dict[cleaned_label]}")
    else:
        unmatched.append((left_code, cleaned_label))

# Output results
print("=== MAPPED FIELDS ===")
for line in mapped:
    print(line)

if unmatched:
    print("\n=== UNMATCHED FIELDS ===")
    for code, label in unmatched:
        print(f"{code} = '{label}'  # No match found")
else:
    print("\nAll fields matched successfully.")
