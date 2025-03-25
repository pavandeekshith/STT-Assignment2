import matplotlib.pyplot as plt

def plot_coverage(total, covered, title, xlabel, ylabel, filename):
    if not total or not covered:
        print(f"Skipping {title} plot due to empty data.")
        return

    plt.figure(figsize=(10, 5))
    plt.scatter(total, covered, color='blue', label='Covered')
    plt.plot([0, max(total)], [0, max(total)], 'r--', label='Ideal Coverage (100%)')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved as {filename}")

# Read the coverage data from the text file
coverage_file = "coverage_report.txt"

total_lines = []
covered_lines = []

total_branches = []
covered_branches = []

with open(coverage_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if '%' in line and 'algorithms/' in line:
            parts = line.split()
            if len(parts) >= 4:
                try:
                    total = int(parts[1])  # Total statements
                    missed = int(parts[2])  # Missed statements
                    covered = total - missed
                    total_lines.append(total)
                    covered_lines.append(covered)
                except ValueError:
                    continue

# Generate plots
plot_coverage(
    total_lines, covered_lines, "Covered vs Total Lines", "Total Lines", "Covered Lines", "line_coverage_scatter.png"
)