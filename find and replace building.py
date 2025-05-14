import re
import os

# Step 1: Define the output directory name
output_directory = "accdemand"  # You can change this name here

# Step 2: Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

# Step 3: Define the mapping sections
mapping_text = """
# Ticket Details Transformation
First Ticket Details = Second Ticket Details
Second Ticket Details = Third Ticket Details
Third Ticket Details = Fourth Ticket Details
Fourth Ticket Details = Fifth Ticket Details
Fifth Ticket Details = Sixth Ticket Details
Sixth Ticket Details = Seventh Ticket Details
Seventh Ticket Details = Eighth Ticket Details
Eighth Ticket Details = Ninth Ticket Details
Ninth Ticket Details = Tenth Ticket Details

# Inspection Title Transformation
First Inspection = Second Inspection
Second Inspection = Third Inspection
Third Inspection = Fourth Inspection
Fourth Inspection = Fifth Inspection
Fifth Inspection = Sixth Inspection
Sixth Inspection = Seventh Inspection
Seventh Inspection = Eighth Inspection
Eighth Inspection = Ninth Inspection
Ninth Inspection = Tenth Inspection

# first to second
FF1028762 = FF1028791
FF1028737 = FF1028763
FF1028738 = FF1028766
FF1028739 = FF1028767
FF1028741 = FF1028768
FF1028751 = FF1028780
FF1028752 = FF1028781
FF1028753 = FF1028782
FF1028754 = FF1028783
FF1028755 = FF1028784
FF1028757 = FF1028785
FF1028749 = FF1028778
FF1028761 = FF1028790
FF1028748 = FF1028777
FF1029060 = FF1029064
FF1029058 = FF1029062
FF1029059 = FF1029063

# second to third
FF1028791 = FF1028820
FF1028763 = FF1028792
FF1028766 = FF1028795
FF1028767 = FF1028796
FF1028768 = FF1028797
FF1028770 = FF1028799
FF1028780 = FF1028809
FF1028781 = FF1028810
FF1028782 = FF1028811
FF1028783 = FF1028812
FF1028784 = FF1028813
FF1028785 = FF1028814
FF1028786 = FF1028815
FF1028787 = FF1028816
FF1028788 = FF1028817
FF1028789 = FF1028818
FF1028778 = FF1028807
FF1028790 = FF1028819
FF1028777 = FF1028806
FF1029064 = FF1029068
FF1029062 = FF1029067
FF1029063 = FF1029066

# third to fourth
FF1028820 = FF1028849
FF1028792 = FF1028821
FF1028795 = FF1028824
FF1028796 = FF1028825
FF1028797 = FF1028826
FF1028799 = FF1028828
FF1028809 = FF1028838
FF1028810 = FF1028839
FF1028811 = FF1028840
FF1028812 = FF1028841
FF1028813 = FF1028842
FF1028814 = FF1028843
FF1028815 = FF1028844
FF1028816 = FF1028845
FF1028817 = FF1028846
FF1028818 = FF1028847
FF1028807 = FF1028836
FF1028819 = FF1028848
FF1028806 = FF1028835
FF1029068 = FF1029072
FF1029067 = FF1029070
FF1029066 = FF1029071

# fourth to Fifth
FF1028849 = FF1028878
FF1028821 = FF1028850
FF1028824 = FF1028853
FF1028825 = FF1028854
FF1028826 = FF1028855
FF1028828 = FF1028857
FF1028838 = FF1028867
FF1028839 = FF1028868
FF1028840 = FF1028869
FF1028841 = FF1028870
FF1028842 = FF1028871
FF1028843 = FF1028872
FF1028844 = FF1028873
FF1028845 = FF1028874
FF1028846 = FF1028875
FF1028847 = FF1028876
FF1028836 = FF1028865
FF1028848 = FF1028877
FF1028835 = FF1028864
FF1029072 = FF1029076
FF1029070 = FF1029074
FF1029071 = FF1029075

# Fifth to Sixth
FF1028878 = FF1028907
FF1028850 = FF1028879
FF1028853 = FF1028882
FF1028854 = FF1028883
FF1028855 = FF1028884
FF1028857 = FF1028886
FF1028867 = FF1028896
FF1028868 = FF1028897
FF1028869 = FF1028898
FF1028870 = FF1028899
FF1028871 = FF1028900
FF1028872 = FF1028901
FF1028873 = FF1028902
FF1028874 = FF1028903
FF1028875 = FF1028904
FF1028876 = FF1028905
FF1028865 = FF1028894
FF1028877 = FF1028906
FF1028864 = FF1028893
FF1029076 = FF1029080
FF1029074 = FF1029078
FF1029075 = FF1029079

# Sixth to Seventh
FF1028907 = FF1028936
FF1028879 = FF1028908
FF1028882 = FF1028911
FF1028883 = FF1028912
FF1028884 = FF1028913
FF1028886 = FF1028915
FF1028896 = FF1028925
FF1028897 = FF1028926
FF1028898 = FF1028927
FF1028899 = FF1028928
FF1028900 = FF1028929
FF1028901 = FF1028930
FF1028902 = FF1028931
FF1028903 = FF1028932
FF1028904 = FF1028933
FF1028905 = FF1028934
FF1028894 = FF1028923
FF1028906 = FF1028935
FF1028893 = FF1028922
FF1029080 = FF1029084
FF1029078 = FF1029082
FF1029079 = FF1029083

# Seventh to Eighth
FF1028936 = FF1028965
FF1028908 = FF1028937
FF1028911 = FF1028940
FF1028912 = FF1028941
FF1028913 = FF1028942
FF1028915 = FF1028944
FF1028925 = FF1028954
FF1028926 = FF1028955
FF1028927 = FF1028956
FF1028928 = FF1028957
FF1028929 = FF1028958
FF1028930 = FF1028959
FF1028931 = FF1028960
FF1028932 = FF1028961
FF1028933 = FF1028962
FF1028934 = FF1028963
FF1028923 = FF1028952
FF1028935 = FF1028964
FF1028922 = FF1028951
FF1029084 = FF1029088
FF1029082 = FF1029086
FF1029083 = FF1029087

# Eighth to Ninth
FF1028965 = FF1028994
FF1028937 = FF1028966
FF1028940 = FF1028969
FF1028941 = FF1028970
FF1028942 = FF1028971
FF1028944 = FF1028973
FF1028954 = FF1028983
FF1028955 = FF1028984
FF1028956 = FF1028985
FF1028957 = FF1028986
FF1028958 = FF1028987
FF1028959 = FF1028988
FF1028960 = FF1028989
FF1028961 = FF1028990
FF1028962 = FF1028991
FF1028963 = FF1028992
FF1028952 = FF1028981
FF1028964 = FF1028993
FF1028951 = FF1028980
FF1029088 = FF1029092
FF1029086 = FF1029090
FF1029087 = FF1029091

# Ninth to Tenth
FF1028994 = FF1029023
FF1028966 = FF1028995
FF1028969 = FF1028998
FF1028970 = FF1028999
FF1028971 = FF1029000
FF1028973 = FF1029002
FF1028983 = FF1029012
FF1028984 = FF1029013
FF1028985 = FF1029014
FF1028986 = FF1029015
FF1028987 = FF1029016
FF1028988 = FF1029017
FF1028989 = FF1029018
FF1028990 = FF1029019
FF1028991 = FF1029020
FF1028992 = FF1029021
FF1028981 = FF1029010
FF1028993 = FF1029022
FF1028980 = FF1029009
FF1029092 = FF1029096
FF1029090 = FF1029094
FF1029091 = FF1029095
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