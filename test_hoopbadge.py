# test_hoopbadge.py
"""
Tests for HoopBadge module.
"""

import unittest
from hoopbadge import HoopBadge

class TestHoopBadge(unittest.TestCase):
    """Test cases for HoopBadge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HoopBadge()
        self.assertIsInstance(instance, HoopBadge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HoopBadge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
