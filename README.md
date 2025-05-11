# Latent-Space Genetic Algorithm with SVD Projection

This repository provides an implementation of a **Genetic Algorithm (GA)** that operates in a **low-dimensional latent space**, which is derived from a high-dimensional input space using **Singular Value Decomposition (SVD)**. The framework optimizes various benchmark functions efficiently by leveraging dimensionality reduction, improving search performance and convergence in high-dimensional optimization problems.

---

## 🚀 Features

- **SVD-based Dimensionality Reduction**: Reduces high-dimensional input space to a lower-dimensional latent space for efficient optimization.
- **Genetic Operators**: Implements core genetic algorithm operators including **blend crossover** and **mutation** for exploration and exploitation.
- **Dynamic Population Size**: The population size adapts during the optimization process to maintain diversity and convergence balance.
- **Benchmark Suite**: Optimizes well-known benchmark functions:
  - Sphere
  - Rastrigin
  - Ackley
  - Griewank
  - Zakharov
  - Rastrigin II
- **Performance Visualization**: Track the performance of the algorithm through visualizations of convergence and fitness over time.

---

## 📈 Benchmark Functions

This project includes the following benchmark functions for optimization:

- **Sphere**: A simple quadratic function used to evaluate optimization algorithms.
- **Rastrigin**: A highly multimodal function with a large search space and many local minima.
- **Ackley**: A commonly used benchmark for testing optimization algorithms in highly multimodal landscapes.
- **Griewank**: A function with a large number of local minima and a relatively flat global optimum.
- **Zakharov**: A function with a smooth global optimum and linear constraints for optimization.
- **Rastrigin II**: A variant of the Rastrigin function designed for more complex optimization challenges.

---

## ⚡ Installation & Usage

To get started with the Latent-Space Genetic Algorithm with SVD Projection, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Farbodpya/latent-ga-SVD.git
   cd latent-ga-SVD
