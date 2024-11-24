import unittest
import inspect
from fundamentals import check_number 


def test_check_number_odd_number(self):
                                        
        self.assertEqual(check_number(3), 'Weird')

        self.assertEqual(check_number(9), 'Weird')

def test_check_number_even_range_2_to_5(self):
        self.assertEqual(check_number(2), 'Not Weird')
        
        self.assertEqual(check_number(4), 'Not Weird')

def test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_number(6), 'Weird')
        self.assertEqual(check_number(18), 'Weird')

def test_check_number_even_greater_than_20(self):
        self.assertEqual(check_number(22), 'Not Weird')
        self.assertEqual(check_number(100), 'Not Weird')

def test_check_number_negative_even_number(self):
        self.assertEqual(check_number(-2), 'Very Weird')
        self.assertEqual(check_number(-4), 'Very Weird')

def test_check_number_negative_odd_number(self):
        self.assertEqual(check_number(-1), 'Extremely Weird')
        self.assertEqual(check_number(-3), 'Extremely Weird')

def test_check_number_neutral(self):
        self.assertEqual(check_number(0), 'Neutral')