import os
import sys
import re

def read_file_content(filepath):
    """
    Reads the content of a given file.

    Args:
        filepath (str): The path to the file.

    Returns:
        list: A list of strings, where each string is a line from the file.
              Returns an empty list if the file cannot be read.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return []
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        return []

def check_trailing_whitespace(lines):
    """
    Checks for trailing whitespace at the end of lines.

    Args:
        lines (list): A list of strings, each representing a line from the file.

    Returns:
        list: A list of line numbers where trailing whitespace is found.
    """
    issues = []
    for i, line in enumerate(lines):
        if line.rstrip() != line.strip('\n'): # Check if rstrip removes more than just newline
            issues.append(i + 1)
    return issues

def check_line_length(lines, max_length=79):
    """
    Checks if lines exceed a specified maximum length.

    Args:
        lines (list): A list of strings, each representing a line from the file.
        max_length (int): The maximum allowed line length.

    Returns:
        list: A list of tuples, where each tuple contains the line number and its length,
              for lines exceeding the max_length.
    """
    issues = []
    for i, line in enumerate(lines):
        # Strip newline character before checking length
        if len(line.rstrip('\n')) > max_length:
            issues.append((i + 1, len(line.rstrip('\n'))))
    return issues

def check_mixed_indentation(lines):
    """
    Checks for mixed usage of tabs and spaces for indentation.

    Args:
        lines (list): A list of strings, each representing a line from the file.

    Returns:
        bool: True if mixed indentation is found, False otherwise.
    """
    has_tabs = False
    has_spaces = False
    for line in lines:
        if line.startswith('\t'):
            has_tabs = True
        elif line.startswith(' '):
            # Check for leading spaces, but ignore lines that are just whitespace or empty
            if line.strip():
                has_spaces = True
        if has_tabs and has_spaces:
            return True
    return False

def check_missing_docstrings(lines):
    """
    Checks for missing docstrings in functions and classes.
    This is a basic check and might not catch all cases.

    Args:
        lines (list): A list of strings, each representing a line from the file.

    Returns:
        list: A list of tuples, where each tuple contains the line number and the
              name of the function/class with a missing docstring.
    """
    issues = []
    in_function_or_class = False
    function_or_class_name = ""
    docstring_found = False
    indent_level = 0

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check for function definition
        func_match = re.match(r'^(def|class)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*[:(]', stripped_line)
        if func_match:
            if in_function_or_class and not docstring_found:
                # Previous function/class ended without a docstring
                issues.append((i, function_or_class_name))

            in_function_or_class = True
            function_or_class_name = func_match.group(2)
            docstring_found = False
            indent_level = len(line) - len(line.lstrip()) # Get current indent level

        elif in_function_or_class:
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= indent_level and stripped_line: # If indentation decreases or line is not empty
                if not docstring_found:
                    issues.append((i, function_or_class_name))
                in_function_or_class = False
                function_or_class_name = ""
                docstring_found = False
                indent_level = 0 # Reset indent level

            # Check for docstring (simple check for triple quotes)
            if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
                docstring_found = True
            elif stripped_line and not docstring_found and not stripped_line.startswith('#'):
                # If we encounter a non-comment, non-empty line and no docstring was found
                # This means the docstring is missing for the current function/class
                pass # Will be caught when the function/class block ends

    # After loop, check if the last function/class had a missing docstring
    if in_function_or_class and not docstring_found:
        issues.append((len(lines), function_or_class_name)) # Use end of file line number

    # Filter out duplicates and format for output
    unique_issues = []
    seen_names = set()
    for line_num, name in issues:
        if name not in seen_names:
            unique_issues.append((line_num, name))
            seen_names.add(name)
    return unique_issues


def check_todo_fixme_comments(lines):
    """
    Checks for 'TODO' and 'FIXME' comments.

    Args:
        lines (list): A list of strings, each representing a line from the file.

    Returns:
        list: A list of tuples, where each tuple contains the line number and the comment text.
    """
    issues = []
    for i, line in enumerate(lines):
        if 'TODO' in line.upper() or 'FIXME' in line.upper():
            issues.append((i + 1, line.strip()))
    return issues

def check_bare_excepts(lines):
    """
    Checks for bare 'except:' statements.

    Args:
        lines (list): A list of strings, each representing a line from the file.

    Returns:
        list: A list of line numbers where bare 'except:' statements are found.
    """
    issues = []
    for i, line in enumerate(lines):
        if re.search(r'^\s*except:\s*$', line):
            issues.append(i + 1)
    return issues

def analyze_file(filepath):
    """
    Analyzes a file for common programming mistakes and prints the results.

    Args:
        filepath (str): The path to the file to analyze.
    """
    print(f"\n--- Analyzing: {filepath} ---")
    lines = read_file_content(filepath)

    if not lines:
        print("No content to analyze or file not found.")
        return

    # Trailing Whitespace
    trailing_whitespace_issues = check_trailing_whitespace(lines)
    if trailing_whitespace_issues:
        print("\n[WARNING] Trailing Whitespace Found on Lines:")
        for line_num in trailing_whitespace_issues:
            print(f"  Line {line_num}")
    else:
        print("\n[OK] No trailing whitespace found.")

    # Line Length
    line_length_issues = check_line_length(lines)
    if line_length_issues:
        print("\n[WARNING] Lines Exceeding 79 Characters:")
        for line_num, length in line_length_issues:
            print(f"  Line {line_num}: {length} characters")
    else:
        print("\n[OK] All lines within recommended length (79 characters).")

    # Mixed Indentation
    if check_mixed_indentation(lines):
        print("\n[CRITICAL] Mixed Indentation (tabs and spaces) detected. Please use one or the other.")
    else:
        print("\n[OK] Consistent indentation detected.")

    # Missing Docstrings
    missing_docstring_issues = check_missing_docstrings(lines)
    if missing_docstring_issues:
        print("\n[WARNING] Missing Docstrings for Functions/Classes:")
        for line_num, name in missing_docstring_issues:
            print(f"  '{name}' (around line {line_num})")
    else:
        print("\n[OK] All detected functions/classes have docstrings.")

    # TODO/FIXME Comments
    todo_fixme_issues = check_todo_fixme_comments(lines)
    if todo_fixme_issues:
        print("\n[INFO] TODO/FIXME Comments Found:")
        for line_num, comment in todo_fixme_issues:
            print(f"  Line {line_num}: {comment}")
    else:
        print("\n[OK] No TODO/FIXME comments found.")

    # Bare Excepts
    bare_except_issues = check_bare_excepts(lines)
    if bare_except_issues:
        print("\n[CRITICAL] Bare 'except:' statements found. Consider specifying exception types for better error handling:")
        for line_num in bare_except_issues:
            print(f"  Line {line_num}")
    else:
        print("\n[OK] No bare 'except:' statements found.")

    print(f"\n--- Analysis of {filepath} Complete ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_script.py <filepath>")
        print("Example: python analyze_script.py my_code.py")
    else:
        file_to_analyze = sys.argv[1]
        analyze_file(file_to_analyze)
