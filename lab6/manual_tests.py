import os
import subprocess

LOG_DIR = "/Users/pavandeekshith/B-Tech/Btech_3rd_Year/6th_Sem/STT/lab6/manual_tests"
os.makedirs(LOG_DIR, exist_ok=True)

for i in range(1, 11):
    log_file = os.path.join(LOG_DIR, f"test_run{i}.log")
    print(f"Running test iteration {i}...")

    # Open the log file in append mode and capture output in real-time
    with open(log_file, "w") as f:
        process = subprocess.Popen(
            ["pytest", "--disable-warnings", "-o", "log_cli=true"],
            stdout=f,
            stderr=subprocess.STDOUT,
            bufsize=1,
            universal_newlines=True
        )
        process.communicate()  # Ensure all output is captured

print("All test runs completed!")
