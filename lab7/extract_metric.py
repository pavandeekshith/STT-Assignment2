import os
import json
import pandas as pd

# Folder containing Bandit JSON reports
bandit_reports_folder = "bandit_reports"

# Initialize a dictionary to store results
results = []

# Loop through each JSON file in the folder
for report_file in sorted(os.listdir(bandit_reports_folder)):
    if report_file.endswith(".json"):
        commit_id = report_file.replace(".json", "")  # Extract commit ID
        report_path = os.path.join(bandit_reports_folder, report_file)
        
        with open(report_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Extract totals from the "_totals" section
        totals = data.get("metrics", {}).get("_totals", {})
        confidence_high = totals.get("CONFIDENCE.HIGH", 0)
        confidence_medium = totals.get("CONFIDENCE.MEDIUM", 0)
        confidence_low = totals.get("CONFIDENCE.LOW", 0)
        
        severity_high = totals.get("SEVERITY.HIGH", 0)
        severity_medium = totals.get("SEVERITY.MEDIUM", 0)
        severity_low = totals.get("SEVERITY.LOW", 0)
        
        # Extract unique CWEs from "results" section
        unique_cwes = set()
        for issue in data.get("results", []):
            if "issue_cwe" in issue and "id" in issue["issue_cwe"]:
                unique_cwes.add(issue["issue_cwe"]["id"])
        
        results.append({
            "commit_id": commit_id[7:],
            "confidence_high": confidence_high,
            "confidence_medium": confidence_medium,
            "confidence_low": confidence_low,
            "severity_high": severity_high,
            "severity_medium": severity_medium,
            "severity_low": severity_low,
            "unique_cwes": list(unique_cwes)
        })

# Convert results to DataFrame and save to CSV
df = pd.DataFrame(results)
df.to_csv("bandit_analysis_results.csv", index=False)

print("Analysis completed. Results saved to bandit_analysis_results.csv")
