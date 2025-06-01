import unittest
from src.black_scholes import call_price, put_price, delta
from src.pricer import monte_carlo_pricer
from src.greeks import delta_mc
from src.payoff import european_call_payoff, european_put_payoff

class TestBlackScholesComparison(unittest.TestCase):

    def setUp(self):
        self.S0 = 100
        self.K = 100
        self.r = 0.05
        self.sigma = 0.2
        self.T = 1.0
        self.M = 252
        self.I = 100000
        self.seed = 42

    def test_call_price_close(self):
        mc = monte_carlo_pricer(self.S0, self.K, self.r, self.sigma, self.T, self.M, self.I, european_call_payoff, self.seed)
        bs = call_price(self.S0, self.K, self.r, self.sigma, self.T)
        self.assertAlmostEqual(mc, bs, delta=0.5)

    def test_call_delta_close(self):
        mc = delta_mc(self.S0, self.K, self.r, self.sigma, self.T, self.M, self.I, european_call_payoff, seed=self.seed)
        bs = delta(self.S0, self.K, self.r, self.sigma, self.T, option_type='call')
        self.assertAlmostEqual(mc, bs, delta=0.02)
