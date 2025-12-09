import re

def fix_fields_with_html(document_text):
    issues = []
    
    # Matches {{...}} or {{{...}}}. Using a non-greedy match (.*?) AND re.DOTALL (re.S) 
    # to catch the *smallest* valid field, even if it spans multiple lines. 
    # This should capture {{#unless ...}} as one block if its closing }} is soon after.
    field_pattern = re.compile(r'(\{\{\{?.*?\s*\}?\}\})', re.DOTALL)

    # HTML tag pattern - This is used to VALIDATE if the content inside the braces is 
    # a single field wrapped in a single tag (e.g., <b>field</b>).
    html_tag_pattern = re.compile(r'^(<[^>]+>)(.*?)(</[^>]+>)$')

    processed_text = document_text
    
    # Find all matches in the entire document
    for match in field_pattern.finditer(document_text):
        full_match = match.group(0)
        
        # Strip outer braces
        inner = re.sub(r'^\{\{\{?|\}?\}\}$', '', full_match).strip()

        # Check if it's wrapped with a single pair of tags
        html_match = html_tag_pattern.match(inner)
        
        if html_match:
            open_tag, content, close_tag = html_match.groups()
            
            # Reconstruct: move tags outside the brackets
            is_triple = full_match.startswith("{{{")
            
            # Determine correct braces for reconstruction
            start_braces = "{{{" if is_triple else "{{"
            end_braces = "}}}" if is_triple else "}}"

            new_field = f"{open_tag}{start_braces}{content}{end_braces}{close_tag}"
            
            # Replace the field in the processed text. We use 1 to only replace the first occurrence 
            # of the matched string to avoid accidental replacement if the text appears elsewhere.
            processed_text = processed_text.replace(full_match, new_field, 1)
            
            # Get the line number for the issue report (approximate)
            line_number = document_text[:match.start()].count('\n') + 1

            issues.append({
                "line": line_number,
                "original": full_match,
                "fixed": new_field
            })
            
    return processed_text, issues

# === USAGE ===
if __name__ == "__main__":
    input_file = "Analysis Input.txt"
    output_file = "Analysis Output.txt"
    
    try:
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
            
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' was not found.")