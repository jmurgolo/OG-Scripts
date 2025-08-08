import os

# --- Configuration ---
# 1. Define the path to your document
#    Make sure to change this to your actual document path.
document_to_modify = 'find and replace input.txt' 

# 2. Provide your mapping data as a multi-line string.
#    Ensure your mapping is exactly as provided in your prompt.

mapping = r"""
FF1026202 = FF1036646
FF1026203 = FF1036647
FF1026201 = FF1036648
FF1026204 = FF1036651
FF1026273 = FF1036649
FF1026492 = FF1036650
FF1026225 = FF1036615
FF1026226 = FF1036612
FF1026226 = FF1036613
FF1026215 = FF1036599
FF1026216 = FF1036620
FF1026217 = FF1036609
FF1026218 = FF1036600
FF1026219 = FF1036631
FF1026220 = FF1036610
FF1026221 = FF1036624
FF1026222 = FF1036632
FF1026223 = FF1036635
FF1026224 = FF1036603
FF1026441 = FF1036608
FF1026439 = FF1036611
FF1026438 = FF1036601
FF1026437 = FF1036623
FF1026470 = FF1036634
FF1026469 = FF1036626
FF1026208 = FF1036641
FF1026209 = FF1036607
FF1026210 = FF1036644
FF1026271 = FF1036618
FF1026270 = FF1036619
FF1026269 = FF1036645
FF1026422 = FF1036606
FF1026420 = FF1036642
FF1026423 = FF1036643
FF1026477 = FF1036670
FF1026478 = FF1036661
FF1026479 = FF1036660
FF1026480 = FF1036671
FF1026471 = FF1036658
FF1026472 = FF1036664
FF1026473 = FF1036668
FF1026474 = FF1036659
FF1026475 = FF1036665
FF1026488 = FF1036657
FF1026540 = FF1036667
FF1026233 = FF1036770
FF1026282 = FF1036747
FF1026518 = FF1036746
OL1026227 = OL1036568
OL1026254 = OL1036566
OL1026483 = OL1036570
OL1026485 = OL1036567
OL1026539 = OL1036571
OL1026585 = OL1036569
OL1026228 = OL1036819
OL1026229 = OL1036817
OL1026230 = OL1036818
OL1026538 = OL1036820
OL1026506 = OL1036750
FF1026255 = FF1036669
"""

# --- Script Logic ---

# Check if the document file exists
if not os.path.exists(document_to_modify):
    print(f"Error: The document file '{document_to_modify}' was not found. Please check the path.")
    exit() # Exit the script if the file isn't found

try:
    # Read the content of the document
    with open(document_to_modify, 'r', encoding='utf-8') as file:
        content = file.read()
except Exception as e:
    print(f"Error reading document file: {e}")
    exit() # Exit if there's an error reading the file

# Parse the mapping data
replacements = {}
for line in mapping.splitlines():
    if '=' in line:
        parts = line.split('=', 1)  # Split only on the first '='
        old_text = parts[0].strip()
        new_text = parts[1].strip()
        replacements[old_text] = new_text

# Perform the replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Overwrite the original file with the modified content
try:
    with open(document_to_modify, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Successfully replaced text in '{document_to_modify}'.")
except Exception as e:
    print(f"Error writing to document file: {e}")

