import os

# --- Configuration ---
# 1. Define the path to your document
#    Make sure to change this to your actual document path.
document_to_modify = 'find and replace input.txt' 

# 2. Provide your mapping data as a multi-line string.
#    Ensure your mapping is exactly as provided in your prompt. 
mapping = r"""
FF1022993 = FF1036646
FF1022994 = FF1036647
FF1022992 = FF1036648
FF1022996 = FF1036651
FF1022990 = FF1036649
FF1022995 = FF1036650
FF1023046 = FF1036599
FF1023047 = FF1036620
FF1023049 = FF1036609
FF1023050 = FF1036600
FF1023052 = FF1036631
FF1023053 = FF1036610
FF1023055 = FF1036624
FF1023056 = FF1036632
FF1023058 = FF1036635
FF1023059 = FF1036603
FF1023061 = FF1036625
FF1023062 = FF1036612
FF1023062 = FF1036613
FF1023045 = FF1036608
FF1023048 = FF1036611
FF1023051 = FF1036601
FF1023054 = FF1036623
FF1023057 = FF1036634
FF1023060 = FF1036626
FF1023010 = FF1036641
FF1023013 = FF1036607
FF1023016 = FF1036644
FF1023011 = FF1036618
FF1023014 = FF1036619
FF1023017 = FF1036645
FF1023009 = FF1036606
FF1023012 = FF1036642
FF1023015 = FF1036643
FF1023093 = FF1036745
FF1023093 = FF1036669
FF1023093 = FF1036744
FF1023093 = FF1036729
FF1023093 = FF1036731
FF1023081 = FF1036675
FF1023081 = FF1036661
FF1023081 = FF1036704
FF1023081 = FF1036721
FF1023081 = FF1036732
FF1023082 = FF1036676
FF1023082 = FF1036660
FF1023082 = FF1036695
FF1023082 = FF1036722
FF1023082 = FF1036742
FF1023083 = FF1036677
FF1023083 = FF1036671
FF1023083 = FF1036698
FF1023083 = FF1036723
FF1023083 = FF1036733
FF1023088 = FF1036672
FF1023089 = FF1036673
FF1023090 = FF1036674
FF1023091 = FF1036683
FF1023086 = FF1036687
FF1023086 = FF1036657
FF1023086 = FF1036682
FF1023086 = FF1036724
FF1023086 = FF1036743
FF1023085 = FF1036686
FF1023085 = FF1036667
FF1023085 = FF1036699
FF1023085 = FF1036737
FF1023085 = FF1036726
FF1036825 = FF1036762
FF1036826 = FF1036761
FF1023254 = FF1036770
FF1023255 = OL1036749
FF1023255 = OL1036748
FF1023255 = OL1036750
FF1023255 = OL1036821
FF1023255 = OL1036822
FF1023252 = FF1036747
FF1023253 = FF1036746
FF1023101 = FF1036762
FF1023100 = FF1036761
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

