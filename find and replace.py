import re

# 🔹 Paste the original raw text block here
input_text = """{{#if FF1027300}}Christopher Bennett{{/if}}{{#if FF1027308}}William Brunton{{/if}}{{#if FF1027309}}Danny Cueto{{/if}}{{#if FF1027310}}Michelle Haska{{/if}}{{#if FF1027311}}Mike Jones{{/if}}{{#if FF1027312}}Jesus Martinez{{/if}}{{#if FF1027313}}Michael McNulty{{/if}}{{#if FF1027314}}Jermain Mitchell{{/if}}{{#if FF1027315}}Michael Whiting{{/if}}{{#if FF1027316}}James Murgolo{{/if}}"""

# 🔹 Paste your raw mapping data here
raw_mapping_data = """
{{FF1027328}}​ = Christopher Bennett
{{FF1027329}}​ = William Brunton
{{FF1027330}}​ = Danny Cueto
{{FF1027331}}​ = Michelle Haska
{{FF1027332}}​ = Mike Jones
{{FF1027333}}​ = Jesus Martinez
{{FF1027334}}​ = Michael McNulty
{{FF1027335}}​ = Jermain Mitchell
{{FF1027336}}​ = Michael Whiting
{{FF1027337}}​ = James Murgolo
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
