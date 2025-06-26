import re
import os

# Step 1: Define the output directory name
output_directory = "court report"  # You can change this name here

# Step 2: Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

# Step 3: Define the mapping sections
mapping_text = """
# First to Second Court Inspection
FF1028236 = FF1028268
FF1028237 = FF1028269
FF1028239 = FF1028271
FF1028242 = FF1028273
FF1028247 = FF1028278
FF1028300 = FF1028299
FF1028243 = FF1028274
FF1028244 = FF1028275
FF1028245 = FF1028276
FF1028246 = FF1028277
FF1028240 = FF1028272
FF1028238 = FF1028270

# Second to Third Court Inspection
FF1028268 = FF1028281
FF1028269 = FF1028282
FF1028271 = FF1028284
FF1028273 = FF1028286
FF1028278 = FF1028291
FF1028299 = FF1028291  # Assuming Images also transforms to Inspector Findings in the third inspection
FF1028267 = FF1028280
FF1028274 = FF1028287
FF1028275 = FF1028288
FF1028276 = FF1028289
FF1028277 = FF1028290
FF1028272 = FF1031280
FF1028270 = FF1028283

# Third to Fourth Court Inspection
FF1028281 = FF1031257
FF1028282 = FF1031258
FF1028284 = FF1031265
FF1028286 = FF1031267
FF1028291 = FF1031263
FF1028280 = FF1028292
FF1028287 = FF1031260
FF1028288 = FF1031261
FF1028289 = FF1031266
FF1028290 = FF1031262
FF1031280 = FF1031281
FF1028283 = FF1031264

# Fourth to Fifth Court Inspection
FF1031257 = FF1031268
FF1031258 = FF1031272
FF1031265 = FF1031274
FF1031263 = FF1031271
FF1031267 = FF1031275
FF1028292 = FF1031270
FF1031260 = FF1031277
FF1031261 = FF1031278
FF1031262 = FF1031269
FF1031266 = FF1031279
FF1031281 = FF1031276
FF1031264 = FF1031273

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