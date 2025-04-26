import matplotlib.pyplot as plt

def plot_average_costs(avg_results):
    plt.figure(figsize=(12, 7))
    for name, avg_costs in avg_results.items():
        plt.semilogy(avg_costs, label=name)
    plt.xlabel("Iteration")
    plt.ylabel("Average Best Cost (log scale)")
    plt.title("Latent-Space GA (SVD): Average Cost over 30 Runs")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()
