import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_vulnerability_timeline(csv_file, output_file="high_severity_timeline.png"):
    # Load the CSV file containing the extracted metrics
    df = pd.read_csv(csv_file)
    
    # Convert commit timestamps to datetime format if available
    if 'commit_timestamp' in df.columns:
        df['commit_timestamp'] = pd.to_datetime(df['commit_timestamp'])
    else:
        df['commit_timestamp'] = range(len(df))  # Use commit order if timestamp is unavailable
    
    # Plot High Severity Issue Trends
    plt.figure(figsize=(12, 6))
    plt.plot(df['commit_timestamp'], df['severity_high'], marker='o', linestyle='-', label='High Severity Issues')
    
    # Highlight elimination (fixing) points only
    fixed = df[(df['severity_high'].shift(-1) - df['severity_high']) < 0]  # Identifying decreasing trends
    
    plt.scatter(fixed['commit_timestamp'], fixed['severity_high'], color='green', label='Fixed', marker='s', s=100)
    
    # Labels and formatting
    plt.xlabel("Commit Timeline")
    plt.ylabel("Number of High Severity Issues")
    plt.title("Fixing of High Severity Issues over Time")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    
    # Save plot as PNG file
    plt.savefig(output_file, bbox_inches='tight')
    plt.show()

# Example usage
plot_vulnerability_timeline("bandit_analysis_results.csv", "high_severity_timeline.png")
