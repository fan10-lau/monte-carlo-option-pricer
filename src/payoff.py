import numpy as np

def european_call_payoff(S_T, K):
    """
    Payoff function for a European call option.

    Parameters:
    - S_T: np.ndarray, terminal stock prices at maturity
    - K: float, strike price

    Returns:
    - np.ndarray of payoffs: max(S_T - K, 0)
    """
    return np.maximum(S_T - K, 0)

def european_put_payoff(S_T, K):
    """
    Payoff function for a European put option.

    Parameters:
    - S_T: np.ndarray, terminal stock prices at maturity
    - K: float, strike price

    Returns:
    - np.ndarray of payoffs: max(K - S_T, 0)
    """
    return np.maximum(K - S_T, 0)
