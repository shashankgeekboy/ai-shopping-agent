import unittest
from agent import agent_response

class TestAgent(unittest.TestCase):
    
    # Task A test
    def test_item_search(self):
        response = agent_response("Find a floral skirt under $40 in size S.")
        self.assertIn("Floral Skirt", response)
        self.assertIn("$31.5", response)
        self.assertIn("in stock", response)
    
    # Task B test
    def test_shipping(self):
        response = agent_response("I need shipping details.")
        self.assertIn("Shipping cost", response)
        self.assertIn("Estimated arrival", response)
    
    # Task C test
    def test_price_comparison(self):
        response = agent_response("Any better deals for casual denim jacket?")
        self.assertIn("Price comparison", response)
    
    # Task D test
    def test_return_policy(self):
        response = agent_response("What is SiteB's return policy?")
        self.assertIn("Return policy", response)
    
    # Task E test (combining tasks)
    def test_combined_query(self):
        response = agent_response("Find a floral skirt under $40 in size S. Can I apply a discount code and get shipping details?")
        self.assertIn("Found: Floral Skirt", response)
        self.assertIn("Shipping cost", response)
        self.assertIn("Price comparison", response)

if __name__ == "__main__":
    unittest.main()
