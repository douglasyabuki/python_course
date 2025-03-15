import os
import re

# Use the current directory since the script is inside `python_course`
BASE_DIR = os.getcwd()
OUTPUT_FILE = "Directory-Structure.md"
GITHUB_URL = "https://github.com/douglasyabuki/python_course"

# Regex pattern to match lesson folders (e.g., lesson001, lesson002, ...)
LESSON_PATTERN = re.compile(r"^lesson\d+$")  # Matches "lesson001", "lesson002", etc.

def get_description(lesson_path):
    """Reads the description file inside each lesson folder."""
    description_file = os.path.join(lesson_path, "description.txt")
    if os.path.exists(description_file):
        with open(description_file, "r", encoding="utf-8", errors="replace") as file:
            return file.readline().strip()  # Get first line as description
    return "No description available"  # Default message if no description file

def generate_markdown():
    """Generates a Markdown tree with clickable lesson links and descriptions."""
    markdown_lines = [
        "# 📂 Project Directory Structure\n",
        "This page documents the structure of the project and the key concepts covered in each lesson.\n",
        f"**[/python-course/]({GITHUB_URL})**  "
    ]

    # Get sorted list of lesson folders that match the pattern
    lesson_folders = sorted(
        [d for d in os.listdir(BASE_DIR) if os.path.isdir(d) and LESSON_PATTERN.match(d)]
    )

    total_lessons = len(lesson_folders)

    for index, lesson in enumerate(lesson_folders):
        lesson_path = os.path.join(BASE_DIR, lesson)
        lesson_url = f"{GITHUB_URL}/tree/master/{lesson}"
        description = get_description(lesson_path)

        # Use └── for the last item, ├── for others
        prefix = "└──" if index == total_lessons - 1 else "├──"

        markdown_lines.append(f"&nbsp;&nbsp;&nbsp;&nbsp; {prefix} [{lesson}]({lesson_url}) - {description}  ")

    # Write output to file (fix encoding issue)
    with open(OUTPUT_FILE, "w", encoding="utf-8", errors="replace") as file:
        file.write("\n".join(markdown_lines))

    print(f"✅ Markdown file '{OUTPUT_FILE}' generated successfully!")

# Run script
generate_markdown()
