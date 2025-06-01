import numpy as np
from src.simulator import generate_gbm_paths

def monte_carlo_pricer(
    S0, K, r, sigma, T, M, I, payoff_fn, seed=None
):
    """
    Monte Carlo pricer for European-style options.

    Parameters:
    - S0: float, initial stock price
    - K: float, strike price
    - r: float, risk-free rate
    - sigma: float, volatility
    - T: float, time to maturity (in years)
    - M: int, number of time steps
    - I: int, number of simulations
    - payoff_fn: function, payoff function like european_call_payoff or european_put_payoff
    - seed: int or None, for reproducibility

    Returns:
    - float: estimated option price
    """
    paths = generate_gbm_paths(S0, r, sigma, T, M, I, seed)
    S_T = paths[-1]  # terminal stock prices
    payoffs = payoff_fn(S_T, K)
    discounted_payoff = np.exp(-r * T) * np.mean(payoffs)
    return discounted_payoff
