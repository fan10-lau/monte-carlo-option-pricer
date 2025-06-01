import unittest
import numpy as np
from src.simulator import generate_gbm_paths

class TestGBMSimulator(unittest.TestCase):

    def setUp(self):
        # Fixed parameters for testing
        self.S0 = 100
        self.r = 0.05
        self.sigma = 0.2
        self.T = 1.0
        self.M = 252
        self.I = 1000
        self.seed = 123

    def test_output_shape(self):
        paths = generate_gbm_paths(self.S0, self.r, self.sigma, self.T, self.M, self.I, seed=self.seed)
        self.assertEqual(paths.shape, (self.M + 1, self.I))

    def test_initial_price(self):
        paths = generate_gbm_paths(self.S0, self.r, self.sigma, self.T, self.M, self.I, seed=self.seed)
        initial_prices = paths[0]
        self.assertTrue(np.allclose(initial_prices, self.S0))

    def test_no_nan_values(self):
        paths = generate_gbm_paths(self.S0, self.r, self.sigma, self.T, self.M, self.I, seed=self.seed)
        self.assertFalse(np.isnan(paths).any())

    def test_reproducibility(self):
        paths1 = generate_gbm_paths(self.S0, self.r, self.sigma, self.T, self.M, self.I, seed=self.seed)
        paths2 = generate_gbm_paths(self.S0, self.r, self.sigma, self.T, self.M, self.I, seed=self.seed)
        self.assertTrue(np.allclose(paths1, paths2))

if __name__ == '__main__':
    unittest.main()
