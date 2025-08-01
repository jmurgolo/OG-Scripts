import re
import os

# Step 1: Define the output directory name
output_directory = "zoning sc"  # You can change this name here

# Step 2: Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

# Step 3: Define the mapping sections
mapping_text = """
# first to second
FF1030150 = FF1030172
FF1030151 = FF1030173
FF1030142 = FF1030164
FF1030126 = FF1030143
FF1030127 = FF1030145
FF1030128 = FF1030146
FF1030129 = FF1030147
FF1030134 = FF1030153
FF1030135 = FF1030154
FF1030136 = FF1030155
FF1030137 = FF1030156
FF1030138 = FF1030157
FF1030139 = FF1030158
FF1030140 = FF1030159
FF1030132 = FF1030151
FF1030141 = FF1030163
FF1030131 = FF1030150
FF1030410 = FF1030414
FF1030408 = FF1030412
FF1030409 = FF1030413
OL1030341 = OL1030411
FIRST NOTICE OF VIOLATIONS = SECOND NOTICE OF VIOLATIONS
FIRST VIOLATION TICKET = SECOND VIOLATION TICKET
FIRST NOTICE = SECOND NOTICE

# second to third
FF1030172 = FF1030194
FF1030173 = FF1030195
FF1030164 = FF1030186
FF1030143 = FF1030165
FF1030145 = FF1030167
FF1030146 = FF1030168
FF1030147 = FF1030169
FF1030148 = FF1030170
FF1030153 = FF1030175
FF1030154 = FF1030176
FF1030155 = FF1030177
FF1030156 = FF1030178
FF1030157 = FF1030179
FF1030158 = FF1030180
FF1030159 = FF1030181
FF1030160 = FF1030182
FF1030161 = FF1030183
FF1030162 = FF1030184
FF1030151 = FF1030173
FF1030163 = FF1030185
FF1030150 = FF1030172
FF1030414 = FF1030418
FF1030412 = FF1030417
FF1030413 = FF1030416
OL1030411 = OL1030415
SECOND NOTICE OF VIOLATIONS = THIRD NOTICE OF VIOLATIONS
SECOND VIOLATION TICKET = THIRD VIOLATION TICKET
SECOND NOTICE = THIRD NOTICE

# third to fourth
FF1030194 = FF1030216
FF1030195 = FF1030217
FF1030186 = FF1030208
FF1030165 = FF1030187
FF1030167 = FF1030189
FF1030168 = FF1030190
FF1030169 = FF1030191
FF1030170 = FF1030192
FF1030175 = FF1030197
FF1030176 = FF1030198
FF1030177 = FF1030199
FF1030178 = FF1030200
FF1030179 = FF1030201
FF1030180 = FF1030202
FF1030181 = FF1030203
FF1030182 = FF1030204
FF1030183 = FF1030205
FF1030184 = FF1030206
FF1030173 = FF1030195
FF1030185 = FF1030207
FF1030172 = FF1030194
FF1030418 = FF1030422
FF1030417 = FF1030420
FF1030416 = FF1030421
OL1030415 = OL1030419
THIRD NOTICE OF VIOLATIONS = FOURTH NOTICE OF VIOLATIONS
THIRD VIOLATION TICKET = FOURTH VIOLATION TICKET
THIRD NOTICE = FOURTH NOTICE

# fourth to Fifth
FF1030216 = FF1030238
FF1030217 = FF1030239
FF1030208 = FF1030230
FF1030187 = FF1030209
FF1030189 = FF1030211
FF1030190 = FF1030212
FF1030191 = FF1030213
FF1030192 = FF1030214
FF1030197 = FF1030219
FF1030198 = FF1030220
FF1030199 = FF1030221
FF1030200 = FF1030222
FF1030201 = FF1030223
FF1030202 = FF1030224
FF1030203 = FF1030225
FF1030204 = FF1030226
FF1030205 = FF1030227
FF1030206 = FF1030228
FF1030195 = FF1030217
FF1030207 = FF1030229
FF1030194 = FF1030216
FF1030422 = FF1030426
FF1030420 = FF1030424
FF1030421 = FF1030425
OL1030419 = OL1030423
FOURTH NOTICE OF VIOLATIONS = FIFTH NOTICE OF VIOLATIONS
FOURTH VIOLATION TICKET = FIFTH VIOLATION TICKET
FOURTH NOTICE = FIFTH NOTICE

# Fifth to Sixth
FF1030238 = FF1030260
FF1030239 = FF1030261
FF1030230 = FF1030252
FF1030209 = FF1030231
FF1030211 = FF1030233
FF1030212 = FF1030234
FF1030213 = FF1030235
FF1030214 = FF1030236
FF1030219 = FF1030241
FF1030220 = FF1030242
FF1030221 = FF1030243
FF1030222 = FF1030244
FF1030223 = FF1030245
FF1030224 = FF1030246
FF1030225 = FF1030247
FF1030226 = FF1030248
FF1030227 = FF1030249
FF1030228 = FF1030250
FF1030217 = FF1030239
FF1030229 = FF1030251
FF1030216 = FF1030238
FF1030426 = FF1030430
FF1030424 = FF1030428
FF1030425 = FF1030429
OL1030423 = OL1030427
FIFTH NOTICE OF VIOLATIONS = SIXTH NOTICE OF VIOLATIONS
FIFTH VIOLATION TICKET = SIXTH VIOLATION TICKET
FIFTH NOTICE = SIXTH NOTICE

# Sixth to Seventh
FF1030260 = FF1030282
FF1030261 = FF1030283
FF1030252 = FF1030274
FF1030231 = FF1030253
FF1030233 = FF1030255
FF1030234 = FF1030256
FF1030235 = FF1030257
FF1030236 = FF1030258
FF1030241 = FF1030263
FF1030242 = FF1030264
FF1030243 = FF1030265
FF1030244 = FF1030266
FF1030245 = FF1030267
FF1030246 = FF1030268
FF1030247 = FF1030269
FF1030248 = FF1030270
FF1030249 = FF1030271
FF1030250 = FF1030272
FF1030239 = FF1030261
FF1030251 = FF1030273
FF1030238 = FF1030260
FF1030430 = FF1030434
FF1030428 = FF1030432
FF1030429 = FF1030433
OL1030427 = OL1030431
SIXTH NOTICE OF VIOLATIONS = SEVENTH NOTICE OF VIOLATIONS
SIXTH VIOLATION TICKET = SEVENTH VIOLATION TICKET
SIXTH NOTICE = SEVENTH NOTICE

# Seventh to Eighth
FF1030282 = FF1030304
FF1030283 = FF1030305
FF1030274 = FF1030296
FF1030253 = FF1030275
FF1030255 = FF1030277
FF1030256 = FF1030278
FF1030257 = FF1030279
FF1030258 = FF1030280
FF1030263 = FF1030285
FF1030264 = FF1030286
FF1030265 = FF1030287
FF1030266 = FF1030288
FF1030267 = FF1030289
FF1030268 = FF1030290
FF1030269 = FF1030291
FF1030270 = FF1030292
FF1030271 = FF1030293
FF1030272 = FF1030294
FF1030261 = FF1030283
FF1030273 = FF1030295
FF1030260 = FF1030282
FF1030434 = FF1030438
FF1030432 = FF1030436
FF1030433 = FF1030437
OL1030431 = OL1030435
SEVENTH NOTICE OF VIOLATIONS = EIGHTH NOTICE OF VIOLATIONS
SEVENTH VIOLATION TICKET = EIGHTH VIOLATION TICKET
SEVENTH NOTICE = EIGHTH NOTICE

# Eighth to Ninth
FF1030304 = FF1030326
FF1030305 = FF1030327
FF1030296 = FF1030318
FF1030275 = FF1030297
FF1030277 = FF1030299
FF1030278 = FF1030300
FF1030279 = FF1030301
FF1030280 = FF1030302
FF1030285 = FF1030307
FF1030286 = FF1030308
FF1030287 = FF1030309
FF1030288 = FF1030310
FF1030289 = FF1030311
FF1030290 = FF1030312
FF1030291 = FF1030313
FF1030292 = FF1030314
FF1030293 = FF1030315
FF1030294 = FF1030316
FF1030283 = FF1030305
FF1030295 = FF1030317
FF1030282 = FF1030304
FF1030438 = FF1030442
FF1030436 = FF1030440
FF1030437 = FF1030441
OL1030435 = OL1030439
EIGHTH NOTICE OF VIOLATIONS = NINTH NOTICE OF VIOLATIONS
EIGHTH VIOLATION TICKET = NINTH VIOLATION TICKET
EIGHTH NOTICE = NINTH NOTICE

# Ninth to Tenth
FF1030318 = FF1030340
FF1030297 = FF1030319
FF1030299 = FF1030321
FF1030300 = FF1030322
FF1030301 = FF1030323
FF1030302 = FF1030324
FF1030307 = FF1030329
FF1030308 = FF1030330
FF1030309 = FF1030331
FF1030310 = FF1030332
FF1030311 = FF1030333
FF1030312 = FF1030334
FF1030313 = FF1030335
FF1030314 = FF1030336
FF1030315 = FF1030337
FF1030316 = FF1030338
FF1030305 = FF1030327
FF1030317 = FF1030339
FF1030304 = FF1030326
FF1030442 = FF1030446
FF1030440 = FF1030444
FF1030441 = FF1030445
OL1030439 = OL1030443
NINTH NOTICE OF VIOLATIONS = TENTH NOTICE OF VIOLATIONS
NINTH VIOLATION TICKET = TENTH VIOLATION TICKET
NINTH NOTICE = TENTH NOTICE
"""

# Step 4: Parse the mappings into an ordered list of dictionaries
mappings = []
current_mapping = {}
for line in mapping_text.strip().splitlines():
    line = line.strip()
    if line.startswith('#'):
        if current_mapping:
            mappings.append(current_mapping.copy())
            current_mapping = {}
        continue
    parts = line.split('=')
    if len(parts) == 2:
        left = parts[0].strip().replace('\u200b', '')
        right = parts[1].strip().replace('\u200b', '')
        current_mapping[left] = right
if current_mapping:
    mappings.append(current_mapping.copy())

# Step 5: Load input from a separate file
with open('find and replace input.txt', 'r', encoding='utf-8') as f:
    input_text = f.read()

# Step 6: Function to replace tokens
def replace_tokens(text, mapping):
    pattern = re.compile('|'.join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)))
    return pattern.sub(lambda match: mapping.get(match.group(0), match.group(0)), text)

# Step 7: Define output filenames
output_filenames = [
    "letter_version_second.txt",
    "letter_version_third.txt",
    "letter_version_fourth.txt",
    "letter_version_fifth.txt",
    "letter_version_sixth.txt",
    "letter_version_seventh.txt",
    "letter_version_eighth.txt",
    "letter_version_ninth.txt",
    "letter_version_tenth.txt",
]

# Step 8: Perform sequential replacements and generate output files
current_text = input_text
for i, mapping in enumerate(mappings):
    current_text = replace_tokens(current_text, mapping)
    output_path = os.path.join(output_directory, output_filenames[i])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(current_text)
    print(f"Generated: '{output_path}' after applying the '{mapping_text.strip().splitlines()[i*12]}' mapping") # Added mapping name for clarity

print(f"Done. Ten versions of the letter have been generated in the '{output_directory}' directory.")