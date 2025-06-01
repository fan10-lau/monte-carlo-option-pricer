from src.pricer import monte_carlo_pricer

def delta_mc(S0, K, r, sigma, T, M, I, payoff_fn, h=1e-2, seed=None):
    """
    Estimate Delta: dPrice/dS0
    """
    price_up = monte_carlo_pricer(S0 + h, K, r, sigma, T, M, I, payoff_fn, seed)
    price_down = monte_carlo_pricer(S0 - h, K, r, sigma, T, M, I, payoff_fn, seed)
    return (price_up - price_down) / (2 * h)

def vega_mc(S0, K, r, sigma, T, M, I, payoff_fn, h=1e-4, seed=None):
    """
    Estimate Vega: dPrice/dSigma
    """
    price_up = monte_carlo_pricer(S0, K, r, sigma + h, T, M, I, payoff_fn, seed)
    price_down = monte_carlo_pricer(S0, K, r, sigma - h, T, M, I, payoff_fn, seed)
    return (price_up - price_down) / (2 * h)

def rho_mc(S0, K, r, sigma, T, M, I, payoff_fn, h=1e-4, seed=None):
    """
    Estimate Rho: dPrice/dr
    """
    price_up = monte_carlo_pricer(S0, K, r + h, sigma, T, M, I, payoff_fn, seed)
    price_down = monte_carlo_pricer(S0, K, r - h, sigma, T, M, I, payoff_fn, seed)
    return (price_up - price_down) / (2 * h)
