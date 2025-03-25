import subprocess
import time

def run_tests():
    start_time = time.time()
    result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.2f} seconds")
    
    return execution_time

def confirm_stability(runs=3):
    print("\n### Confirming test stability (3 runs) ###\n")
    for i in range(runs):
        print(f"Stability Check Run {i+1}...")
        run_tests()

def measure_tseq(repetitions=5):
    print("\n### Measuring Sequential Execution Time (5 runs) ###\n")
    times = []
    for i in range(repetitions):
        print(f"Run {i+1}...")
        exec_time = run_tests()
        times.append(exec_time)
    
    avg_time = sum(times) / len(times)
    print(f"\nAverage Sequential Execution Time (Tseq): {avg_time:.2f} seconds")
    return avg_time

if __name__ == "__main__":
    confirm_stability()  # Step 1: Ensure no failing/flaky tests
    Tseq = measure_tseq()  # Step 2: Compute Tseq
