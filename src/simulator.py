import numpy as np

def generate_gbm_paths(S0, r, sigma, T, M, I, seed=None):
    """
    Generate Geometric Brownian Motion stock price paths using Monte Carlo simulation.
    
    Parameters:
    - S0: float, initial stock price
    - r: float, risk-free interest rate
    - sigma: float, volatility of the underlying asset
    - T: float, time to maturity (in years)
    - M: int, number of time steps
    - I: int, number of simulation paths
    - seed: int or None, for reproducibility

    Returns:
    - paths: np.ndarray of shape (M+1, I), simulated stock paths
    """
    if seed is not None:
        np.random.seed(seed)
        
    dt = T / M  # time increment
    paths = np.zeros((M + 1, I))
    paths[0] = S0

    # simulate paths
    for t in range(1, M + 1):
        z = np.random.standard_normal(I)  # standard normal random numbers
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

    return paths
