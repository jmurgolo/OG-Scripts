# import re

# def contains_html(text):
#     # Detect any HTML tags inside the field
#     return bool(re.search(r'<[^>]+>', text))

# def check_field_formatting_with_line_numbers(document_text):
#     errors = []
#     # Pattern to match both {{...}} and {{{...}}}
#     field_pattern = re.compile(r'(\{\{\{?\s*.*?\s*\}?\}\})')

#     for line_number, line in enumerate(document_text.splitlines(), start=1):
#         for match in field_pattern.finditer(line):
#             full_match = match.group(0)
#             # Strip outer braces to isolate the content
#             inner_content = re.sub(r'^\{\{\{?|\}?\}\}$', '', full_match).strip()

#             if contains_html(inner_content):
#                 errors.append({
#                     "line": line_number,
#                     "match": full_match.strip(),
#                     "inner": inner_content
#                 })

#     return errors

# # === USAGE EXAMPLE ===
# if __name__ == "__main__":
#     with open("find and replace input.txt", "r", encoding="utf-8") as f:
#         content = f.read()

#     issues = check_field_formatting_with_line_numbers(content)

#     if not issues:
#         print("✅ No formatting issues found.")
#     else:
#         print("❌ Formatting issues found:\n")
#         for issue in issues:
#             print(f"Line {issue['line']}: {issue['match']} → contains HTML: '{issue['inner']}'")

import re
# import find and replace historical enf ticket go live.py

def fix_fields_with_html(document_text):
    fixed_lines = []
    issues = []

    # Matches {{...}} or {{{...}}}
    field_pattern = re.compile(r'(\{\{\{?\s*.*?\s*\}?\}\})')

    # HTML tag pattern
    html_tag_pattern = re.compile(r'^(<[^>]+>)(.*?)(</[^>]+>)$')

    for line_number, line in enumerate(document_text.splitlines(), start=1):
        fixed_line = line
        for match in field_pattern.finditer(line):
            full_match = match.group(0)
            # Strip outer braces
            inner = re.sub(r'^\{\{\{?|\}?\}\}$', '', full_match).strip()

            # Check if it's wrapped with a single pair of tags like <b>...</b>
            html_match = html_tag_pattern.match(inner)
            if html_match:
                open_tag, content, close_tag = html_match.groups()
                # Reconstruct: move tags outside the brackets
                is_triple = full_match.startswith("{{{")
                new_field = f"{open_tag}{{{{{'{' if is_triple else ''}{content}{'}' if is_triple else ''}}}}}{close_tag}"
                fixed_line = fixed_line.replace(full_match, new_field)
                issues.append({
                    "line": line_number,
                    "original": full_match,
                    "fixed": new_field
                })
        fixed_lines.append(fixed_line)

    return "\n".join(fixed_lines), issues

# === USAGE ===
if __name__ == "__main__":
    input_file = "find and replace input.txt"
    output_file = "find and replace input.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    fixed_content, issues = fix_fields_with_html(content)

    if not issues:
        print("✅ No formatting issues found.")
    else:
        print("❌ Fixes applied to the following lines:\n")
        for issue in issues:
            print(f"Line {issue['line']}:\n  Original: {issue['original']}\n  Fixed:    {issue['fixed']}\n")

        # Save fixed output
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(fixed_content)
        print(f"✅ Fixed content saved to: {output_file}")
