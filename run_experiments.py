import numpy as np
import random
import time

from benchmarks import benchmarks
from ga import dynamic_ga_latent
from plots import plot_average_costs

np.random.seed(0)
random.seed(0)

all_results = {}
avg_results = {}
final_costs_per_run = {}
timings = {}
run_times_per_function = {}

print("\nRunning Latent-Space GA (SVD) 30 Times Per Benchmark:\n")

for name, fn in benchmarks.items():
    print(f"Running: {name}")
    run_costs = []
    final_costs = []
    per_run_times = []
    total_start = time.time()

    for _ in range(30):
        start = time.time()
        costs = dynamic_ga_latent(fn)
        end = time.time()

        run_costs.append(costs)
        final_costs.append(costs[-1])
        per_run_times.append(end - start)

    total_end = time.time()

    all_results[name] = run_costs
    avg_results[name] = [np.mean([run[i] for run in run_costs]) for i in range(len(run_costs[0]))]
    final_costs_per_run[name] = final_costs
    run_times_per_function[name] = per_run_times
    timings[name] = total_end - total_start

plot_average_costs(avg_results)

print("\nFinal Average Best Costs and Execution Time:")
for name in benchmarks.keys():
    final_avg_cost = np.mean(final_costs_per_run[name])
    avg_runtime = np.mean(run_times_per_function[name])
    total_runtime = timings[name]
    print(f"{name:15}: Final Cost = {final_avg_cost:.6e}, Avg Time = {avg_runtime:.2f}s, Total = {total_runtime:.2f}s")
