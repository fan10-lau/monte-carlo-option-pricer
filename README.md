# Monte Carlo Option Pricer

This project implements a modular Monte Carlo simulation engine to price European vanilla options and estimate option Greeks. It validates numerical results against closed-form Black-Scholes prices and is designed to be easily extended to support exotic options.

## Features

- Simulate stock price paths using Geometric Brownian Motion (GBM)
- Price European call and put options using Monte Carlo simulation
- Estimate Greeks (Delta, Vega, Rho) using finite difference methods
- Validate Monte Carlo outputs against Black-Scholes closed-form solutions
- Modular structure for easy extension (Asian, Barrier, Digital options)
- Unit-tested for pricing accuracy and gradient correctness
- Notebook walkthrough for interactive visualization and explanation

## Project Structure
1. Simulate GBM stock paths using `simulator.py`
2. Evaluate payoffs using `payoff.py`
3. Compute the discounted average payoff in `pricer.py`
4. Estimate Greeks with bump-and-reprice in `greeks.py`
5. Compare to Black-Scholes values from `black_scholes.py`

## Notebooks

`example_usage.ipynb`: Demonstrates how to simulate paths, compute MC prices and Greeks, and compare to Black-Scholes.

## Future Work
- Exotic option support (Asian, Barrier)
- Support for American options via Least-Squares Monte Carlo (LSM)
- Integration with real market data via `yfinance`
