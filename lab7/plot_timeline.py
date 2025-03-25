import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_all_severity_timeline(csv_file, output_file="all_severity_timeline.png"):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert commit timestamps to datetime format if available
    if 'commit_timestamp' in df.columns:
        df['commit_timestamp'] = pd.to_datetime(df['commit_timestamp'])
    else:
        df['commit_timestamp'] = range(len(df))  # Use commit order if timestamp is unavailable
    
    # Create figure
    plt.figure(figsize=(12, 6))

    # Plot Severity Trends
    plt.plot(df['commit_timestamp'], df['severity_high'], marker='o', linestyle='-', color='red', label='High Severity')
    plt.plot(df['commit_timestamp'], df['severity_medium'], marker='s', linestyle='-', color='orange', label='Medium Severity')
    plt.plot(df['commit_timestamp'], df['severity_low'], marker='d', linestyle='-', color='blue', label='Low Severity')
    
    # Identify fixing points (without adding to the legend)
    fixed_high = df[(df['severity_high'].shift(-1) - df['severity_high']) < 0]
    fixed_medium = df[(df['severity_medium'].shift(-1) - df['severity_medium']) < 0]
    fixed_low = df[(df['severity_low'].shift(-1) - df['severity_low']) < 0]
    
    plt.scatter(fixed_high['commit_timestamp'], fixed_high['severity_high'], color='green', marker='s', s=100, label="_nolegend_")
    plt.scatter(fixed_medium['commit_timestamp'], fixed_medium['severity_medium'], color='green', marker='s', s=100, label="_nolegend_")
    plt.scatter(fixed_low['commit_timestamp'], fixed_low['severity_low'], color='green', marker='s', s=100, label="_nolegend_")

    # Labels and formatting
    plt.xlabel("Commit Timeline")
    plt.ylabel("Number of Issues")
    plt.title("Introduction and Elimination of Vulnerabilities by Severity")
    plt.legend()  # Legend only includes severity trends now
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    
    # Save plot
    plt.savefig(output_file, bbox_inches='tight')
    plt.show()

# Example usage
plot_all_severity_timeline("/Users/pavandeekshith/B-Tech/Btech_3rd_Year/6th_Sem/STT/lab7/DK64-Randomizer/bandit_analysis_results.csv", "all_severity_timeline.png")
