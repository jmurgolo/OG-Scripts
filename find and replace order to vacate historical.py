import os

# --- Configuration ---
# 1. Define the path to your document
#    Make sure to change this to your actual document path.
document_to_modify = 'find and replace input.txt' 

# 2. Provide your mapping data as a multi-line string.
#    Ensure your mapping is exactly as provided in your prompt. 
mapping = r"""
FF1035688 = FF1036648
FF1035689 = FF1036646
FF1035690 = FF1036647
FF1035691 = FF1036651
FF1035695 = FF1036599
FF1035696 = FF1036620
FF1035697 = FF1036621
FF1035698 = FF1036609
FF1035699 = FF1036600
FF1035700 = FF1036631
FF1035701 = FF1036610
FF1035702 = FF1036624
FF1035703 = FF1036632
FF1035704 = FF1036635
FF1035705 = FF1036603
FF1035706 = FF1036625
FF1035707 = FF1036612
FF1035708 = FF1036615
FF1035709 = FF1036597
FF1035710 = FF1036636
FF1035711 = FF1036637
FF1035712 = FF1036629
FF1035713 = FF1036616
FF1035714 = FF1036605
FF1035715 = FF1036630
FF1035720 = FF1036641
FF1035721 = FF1036607
FF1035722 = FF1036644
FF1035789 = FF1036645
FF1035790 = FF1036619
FF1035791 = FF1036618
FF1035794 = FF1036649
FF1035902 = FF1036696
FF1035904 = FF1036626
FF1035905 = FF1036634
FF1035906 = FF1036623
FF1035907 = FF1036601
FF1035908 = FF1036611
FF1035910 = FF1036608
FF1035911 = FF1036642
FF1035912 = FF1036840
FF1035914 = FF1036617
FF1035915 = FF1036638
FF1035916 = FF1036598
FF1035917 = FF1036614
FF1035918 = FF1036643
FF1035925 = FF1036606
FF1035926 = FF1036769
FF1035937 = FF1036655
FF1036117 = FF1036650
FF1035939 = FF1036692
FF1035940 = FF1036703
FF1035941 = FF1036704
FF1035942 = FF1036695
FF1035943 = FF1036696
FF1035944 = FF1036698
FF1035945 = FF1036706
FF1035946 = FF1036697
FF1035947 = FF1036705
FF1035948 = FF1036688
FF1035949 = FF1036708
FF1035950 = FF1036700
FF1035951 = FF1036701
FF1035952 = FF1036680
FF1035953 = FF1036689
FF1035954 = FF1036690
FF1035955 = FF1036679
FF1035956 = FF1036694
FF1035957 = FF1036693
FF1035958 = FF1036702
FF1036093 = FF1036682
FF1036150 = FF1036699
OL1035726 = OL1036817
OL1035727 = OL1036818
OL1035732 = OL1036819
OL1036144 = OL1036820
OL1035723 = OL1036821
OL1035777 = OL1036574
OL1036107 = OL1036575
OL1036108 = OL1036573
OL1036141 = OL1036578
OL1036196 = OL1036577
OL1035724 = OL1036715
OL1035725 = OL1036716
OL1035776 = OL1036712
OL1036109 = OL1036717
OL1036110 = OL1036709
OL1036111 = OL1036710
OL1036112 = OL1036711
OL1036142 = OL1036714
OL1036195 = OL1036713
OL1035733 = OL1036850
OL1035775 = OL1036848
OL1036105 = OL1036849
OL1036106 = OL1036846
OL1036143 = OL1036851
OL1036194 = OL1036847
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
    print(f'' + old + ' ' + new)

# Overwrite the original file with the modified content
try:
    with open(document_to_modify, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Successfully replaced text in '{document_to_modify}'.")
except Exception as e:
    print(f"Error writing to document file: {e}")

