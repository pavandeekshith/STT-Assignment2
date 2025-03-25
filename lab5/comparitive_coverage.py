import re

# Define file paths
coverage_a_path = "coverage_report.txt"
coverage_b_path = "coverage_report_pynguin.txt"

# Function to extract coverage data from a coverage report file
def extract_coverage_data(file_path):
    coverage_data = {}
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r"(\S+)\s+\d+\s+\d+\s+(\d+)%", line)
            if match:
                file_name = match.group(1)
                coverage_percent = int(match.group(2))
                coverage_data[file_name] = coverage_percent
    return coverage_data

# Extract coverage data from both reports
coverage_a = extract_coverage_data(coverage_a_path)
coverage_b = extract_coverage_data(coverage_b_path)

# Find common files in both reports
common_files = set(coverage_a.keys()) & set(coverage_b.keys())

# Separate files based on coverage improvement
improved_files = []
other_files = []

for file in common_files:
    coverage_a_value = coverage_a[file]
    coverage_b_value = coverage_b[file]

    if coverage_b_value > 0:  # Only consider files where B > 0
        if coverage_b_value > coverage_a_value:
            improved_files.append((file, coverage_a_value, coverage_b_value))
        else:
            other_files.append((file, coverage_a_value, coverage_b_value))

# Print comparative coverage analysis
print("\nComparative Coverage Analysis (Common Files Only):\n")
print(f"{'File':<50} {'Coverage A (%)':<15} {'Coverage B (%)'}")
print("-" * 80)

# Print improved coverage files first
print("\nFiles with Improved Coverage:\n")
for file, coverage_a_value, coverage_b_value in improved_files:
    print(f"{file:<50} {coverage_a_value:<15} {coverage_b_value}")

# Print files with no change or decreased coverage
print("\nFiles with No Change or Decreased Coverage:\n")
for file, coverage_a_value, coverage_b_value in other_files:
    print(f"{file:<50} {coverage_a_value:<15} {coverage_b_value}")
