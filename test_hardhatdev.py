# test_hardhatdev.py
"""
Tests for HardhatDev module.
"""

import unittest
from hardhatdev import HardhatDev

class TestHardhatDev(unittest.TestCase):
    """Test cases for HardhatDev class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HardhatDev()
        self.assertIsInstance(instance, HardhatDev)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HardhatDev()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
