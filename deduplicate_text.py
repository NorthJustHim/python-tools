# deduplicate_text.py
# Removes duplicates from a text file and sorts lines
# Creates input.txt automatically if missing

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# Sample lines to write if input.txt doesn't exist
sample_lines = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "grape"
]

# Step 1: Ensure input file exists
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        raise FileNotFoundError  # Treat empty file as missing
except FileNotFoundError:
    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        for line in sample_lines:
            f.write(line + "\n")
    print(f"Created {INPUT_FILE} with sample text.")
    lines = sample_lines.copy()

# Step 2: Remove duplicates and sort
unique_sorted_lines = sorted(set(lines))

# Step 3: Write to output.txt
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for line in unique_sorted_lines:
        f.write(line + "\n")

# Step 4: Print results
print(f"Done! Cleaned file saved as {OUTPUT_FILE}. Contents:")
for line in unique_sorted_lines:
    print(line)


