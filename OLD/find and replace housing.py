import re
import os

# Step 1: Define the output directory name
output_directory = "ticket"  # You can change this name here

# Step 2: Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

# Step 3: Define the mapping sections
mapping_text = """
# first to second
FF1027300 = FF1027328
FF1027308 = FF1027329
FF1027309 = FF1027330
FF1027310 = FF1027331
FF1027311 = FF1027332
FF1027312 = FF1027333
FF1027313 = FF1027334
FF1027314 = FF1027335
FF1027315 = FF1027336
FF1027316 = FF1027337
FF1028306 = FF1027338
FF1031116 = FF1031115
FF1028442 = FF1028557
FF1028441 = FF1028554
FF1028555 = FF1028556
OL1028425 = OL1028553
FIRST VIOLATION TICKET = SECOND VIOLATION TICKET

# second to third
FF1027328 = FF1027471
FF1027329 = FF1027472
FF1027330 = FF1027473
FF1027331 = FF1027474
FF1027332 = FF1027475
FF1027333 = FF1027476
FF1027334 = FF1027477
FF1027335 = FF1027478
FF1027336 = FF1027479
FF1027337 = FF1027480
FF1027338 = FF1027481
FF1031115 = FF1031117
FF1028557 = FF1028562
FF1028554 = FF1028561
FF1028556 = FF1028560
OL1028553 = OL1028559
SECOND VIOLATION TICKET = THIRD VIOLATION TICKET

# third to fourth
FF1027471 = FF1027558
FF1027472 = FF1027559
FF1027473 = FF1027560
FF1027474 = FF1027561
FF1027475 = FF1027562
FF1027476 = FF1027563
FF1027477 = FF1027564
FF1027478 = FF1027565
FF1027479 = FF1027566
FF1027480 = FF1027567
FF1027481 = FF1027568
FF1031117 = FF1031114
FF1028562 = FF1028566
FF1028561 = FF1028564
FF1028560 = FF1028565
OL1028559 = OL1028563
THIRD VIOLATION TICKET = FOURTH VIOLATION TICKET

# fourth to Fifth
FF1027558 = FF1027646
FF1027559 = FF1027647
FF1027560 = FF1027648
FF1027561 = FF1027649
FF1027562 = FF1027650
FF1027563 = FF1027651
FF1027564 = FF1027652
FF1027565 = FF1027653
FF1027566 = FF1027654
FF1027567 = FF1027655
FF1027568 = FF1027579
FF1031114 = FF1031118
FF1028566 = FF1028570
FF1028564 = FF1028568
FF1028565 = FF1028569
OL1028563 = OL1028567
FOURTH VIOLATION TICKET = FIFTH VIOLATION TICKET

# Fifth to Sixth
FF1027646 = FF1027656
FF1027647 = FF1027657
FF1027648 = FF1027658
FF1027649 = FF1027659
FF1027650 = FF1027660
FF1027651 = FF1027661
FF1027652 = FF1027662
FF1027653 = FF1027663
FF1027654 = FF1027664
FF1027655 = FF1027665
FF1027579 = FF1027590
FF1031118 = FF1031122
FF1028570 = FF1028574
FF1028568 = FF1028572
FF1028569 = FF1028573
OL1028567 = OL1028571
FIFTH VIOLATION TICKET = SIXTH VIOLATION TICKET

# Sixth to Seventh
FF1027656 = FF1027666
FF1027657 = FF1027667
FF1027658 = FF1027668
FF1027659 = FF1027669
FF1027660 = FF1027670
FF1027661 = FF1027671
FF1027662 = FF1027672
FF1027663 = FF1027673
FF1027664 = FF1027674
FF1027665 = FF1027675
FF1027590 = FF1027601
FF1031122 = FF1031123
FF1028574 = FF1028578
FF1028572 = FF1028576
FF1028573 = FF1028577
OL1028571 = OL1028575
SIXTH VIOLATION TICKET = SEVENTH VIOLATION TICKET

# Seventh to Eighth
FF1027666 = FF1027676
FF1027667 = FF1027677
FF1027668 = FF1027678
FF1027669 = FF1027679
FF1027670 = FF1027680
FF1027671 = FF1027681
FF1027672 = FF1027682
FF1027673 = FF1027683
FF1027674 = FF1027684
FF1027675 = FF1027685
FF1027601 = FF1027612
FF1031123 = FF1031119
FF1028578 = FF1028583
FF1028576 = FF1028581
FF1028577 = FF1028582
OL1028575 = OL1028580
SEVENTH VIOLATION TICKET = EIGHTH VIOLATION TICKET

# Eighth to Ninth
FF1027676 = FF1027686
FF1027667 = FF1027687
FF1027668 = FF1027688
FF1027669 = FF1027689
FF1027670 = FF1027690
FF1027671 = FF1027691
FF1027672 = FF1027692
FF1027673 = FF1027693
FF1027674 = FF1027694
FF1027675 = FF1027695
FF1027612 = FF1027623
FF1031119 = FF1031121
FF1028583 = FF1028587
FF1028581 = FF1028585
FF1028582 = FF1028586
OL1028580 = OL1028584
EIGHTH VIOLATION TICKET = NINTH VIOLATION TICKET

# Ninth to Tenth
FF1027686 = FF1027698
FF1027667 = FF1027699
FF1027668 = FF1027700
FF1027669 = FF1027701
FF1027670 = FF1027702
FF1027671 = FF1027703
FF1027672 = FF1027704
FF1027673 = FF1027705
FF1027674 = FF1027706
FF1027675 = FF1027840
FF1027623 = FF1027634
FF1031121 = FF1031120
FF1028587 = FF1028591
FF1028585 = FF1028589
FF1028586 = FF1028590
OL1028584 = OL1028588
NINTH VIOLATION TICKET = TENTH VIOLATION TICKET
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