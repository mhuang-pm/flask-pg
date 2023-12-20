import re
import os


def extract_function_names(file_content):
    pattern = r'@app\.route\(.*?\)\s*\ndef\s+([^\(]+)\('
    matches = re.findall(pattern, file_content, re.DOTALL)
    return matches


def main():
    function_names = []
    for filename in os.listdir("."):
        if filename.endswith(".py"):
            with open(filename, "r") as file:
                content = file.read()
                matches = extract_function_names(content)
                if matches:
                    function_names.extend(matches)

    if not function_names:
        print("No matching lines found in Python files.")
    else:
        print("Function names:", function_names)


if __name__ == "__main__":
    main()
