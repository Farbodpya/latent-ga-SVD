import numpy as np
import random
import time

from benchmarks import benchmarks
from ga import dynamic_ga_latent
from plots import plot_average_costs

np.random.seed(0)
random.seed(0)

all_results = {}
final_costs = {}
timings = {}

print("\nRunning Latent-Space GA (SVD) Once Per Benchmark:\n")

for name, fn in benchmarks.items():
    print(f"\nRunning: {name}")
    start = time.time()
    costs = dynamic_ga_latent(fn)
    end = time.time()

    all_results[name] = costs
    final_costs[name] = costs[-1]
    timings[name] = end - start

    print(f"  → Final Cost: {costs[-1]:.6e}")
    print(f"  → All Costs: {np.array2string(np.array(costs), precision=4, separator=', ')}")
    print(f"  → Time Taken: {end - start:.2f} seconds")

# Plot the results
plot_average_costs(all_results)

print("\nSummary:")
for name in benchmarks.keys():
    print(f"{name:15}: Final Cost = {final_costs[name]:.6e}, Time = {timings[name]:.2f}s")
