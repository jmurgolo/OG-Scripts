import os

# --- Configuration ---
# 1. Define the path to your document
#    Make sure to change this to your actual document path.
document_to_modify = 'find and replace input.txt' 

# 2. Provide your mapping data as a multi-line string.
#    Ensure your mapping is exactly as provided in your prompt.

mapping = r"""
FF1031353​ = FF1022400​
FF1020947​ = FF1022419​
FF1020950​ = FF1022420​
FF1021005​ = FF1022421​
FF1031344​ = FF1022422​
FF1021004​ = FF1022425​
FF1020959​ = FF1022361​
FF1020952​ = FF1022367​
FF1020953​ = FF1022368​
FF1020954​ = FF1022369​
FF1020955​ = FF1022370​
FF1020956​ = FF1022371​
FF1020957​ = FF1022372​
FF1020958​ = FF1022373​
FF1025672​ = FF1022418​
FF1025667​ = FF1022410​
FF1025668​ = FF1022411​
FF1025669​ = FF1022412​
FF1025670​ = FF1022413​
FF1025671​ = FF1022414​
FF1031332​ = FF1022363​
FF1031330​ = FF1022395​
FF1031331​ = FF1022398​
FF1031334​ = FF1022396​
FF1031337​ = FF1022397​
FF1031338​ = FF1022394​
FF1031335​ = FF1022423​
FF1031339​ = FF1022417​
FF1031333​ = FF1022430​
FF1031345​ = FF1022389​
FF1031346​ = FF1022388​
FF1031347​ = FF1022390​
FF1031348​ = FF1022391​
FF1031354​ = FF1022392​
FF1031355​ = FF1022393​
FF1031350​ = FF1022365​
FF1031351​ = FF1022366​
FF1031349​ = FF1022424​
OL1020962​ = OL1022352​
OL1020963​ = OL1022353​
OL1020964​ = OL1022354​
OL1020965​ = OL1022355​
OL1020966​ = OL1022356​
OL1020960​ = OL1022432​
OL1020968​ = OL1022357​
OL1020969​ = OL1022381​
OL1020971​ = OL1022382​
OL1020972​ = OL1022383​
OL1020973​ = OL1022384​
OL1020974​ = OL1022385​
OL1020976​ = OL1022386​
OL1020977​ = OL1022387​
OL1020967​ = OL1022426​
OL1020979​ = OL1022358​
OL1020980​ = OL1022374​
OL1020981​ = OL1022375​
OL1020982​ = OL1022376​
OL1020983​ = OL1022377​
OL1020984​ = OL1022378​
OL1020985​ = OL1022379​
OL1020986​ = OL1022380​
OL1020978​ = OL1022427​
OL1020988​ = OL1022359​
OL1020990​ = OL1022360​
OL1020991​ = OL1022402​
OL1020992​ = OL1022403​
OL1020993​ = OL1022404​
OL1020994​ = OL1022405​
OL1020996​ = OL1022401​
OL1020998​ = OL1022399​
OL1020997​ = OL1022415​
OL1020987​ = OL1022428​
OL1020995​ = OL1022433​
OL1021000​ = OL1022406​
OL1021001​ = OL1022407​
OL1021002​ = OL1022408​
OL1021003​ = OL1022409​
OL1020999​ = OL1022431​
OL1031341​ = OL1022362​
OL1031343​ = OL1022416​
OL1031342​ = OL1022429​
OL1031340​ = OL1022435​
OL1031352​ = OL1022364​
MES1011845​ = MES1012108​
MES1011846​ = MES1012109​
MES1011847​ = MES1012110​
MES1011848​ = MES1012111​
MES1011849​ = MES1012112​
MES1013001​ = MES1012114​
MES1013004​ = MES1012117​
FEE431​ = FEE473​
FEE432​ = FEE474​
FEE433​ = FEE475​
FEE434​ = FEE476​
FEE435​ = FEE477​
FEE436​ = FEE478​
FEE437​ = FEE479​
FEE438​ = FEE480​
FEE439​ = FEE481​
FEE440​ = FEE482​
FEE441​ = FEE483​
FEE442​ = FEE484​
FEE443​ = FEE485​
FEE444​ = FEE486​
FEE445​ = FEE487​
FEE446​ = FEE488​
FEE447​ = FEE489​
FEE448​ = FEE490​
FEE449​ = FEE491​
FEE450​ = FEE492​
totalPaid​ = totalPaid​
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

