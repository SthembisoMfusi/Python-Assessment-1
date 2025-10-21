"""
Instructor Tests for Python Assessment
====================================

This file contains comprehensive unit tests for all functions in questions.py.
Students should NOT see this file - it's used for automated grading.

Each function has 3-4 test cases covering:
- Normal cases
- Edge cases
- Error conditions
"""

import unittest
from questions import (
    calculate_area, reverse_string, is_even_or_odd, sum_of_squares,
    countdown_to_zero, find_maximum, count_word_frequency, calculate_bmi,
    filter_even_numbers, grade_calculator
)


class TestCalculateArea(unittest.TestCase):
    """Test cases for calculate_area function."""
    
    def test_normal_rectangle(self):
        """Test normal rectangle calculation."""
        self.assertEqual(calculate_area(5, 3), 15)
    
    def test_square(self):
        """Test square calculation."""
        self.assertEqual(calculate_area(4, 4), 16)
    
    def test_decimal_values(self):
        """Test with decimal values."""
        self.assertAlmostEqual(calculate_area(2.5, 3.2), 8.0)
    
    def test_zero_dimensions(self):
        """Test with zero dimensions."""
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(5, 0), 0)


class TestReverseString(unittest.TestCase):
    """Test cases for reverse_string function."""
    
    def test_normal_string(self):
        """Test normal string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_single_character(self):
        """Test single character."""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_palindrome(self):
        """Test palindrome string."""
        self.assertEqual(reverse_string("racecar"), "racecar")


class TestIsEvenOrOdd(unittest.TestCase):
    """Test cases for is_even_or_odd function."""
    
    def test_even_number(self):
        """Test even number."""
        self.assertEqual(is_even_or_odd(4), "even")
    
    def test_odd_number(self):
        """Test odd number."""
        self.assertEqual(is_even_or_odd(7), "odd")
    
    def test_zero(self):
        """Test zero (even)."""
        self.assertEqual(is_even_or_odd(0), "even")
    
    def test_negative_even(self):
        """Test negative even number."""
        self.assertEqual(is_even_or_odd(-4), "even")
    
    def test_negative_odd(self):
        """Test negative odd number."""
        self.assertEqual(is_even_or_odd(-3), "odd")


class TestSumOfSquares(unittest.TestCase):
    """Test cases for sum_of_squares function."""
    
    def test_small_number(self):
        """Test with small number."""
        self.assertEqual(sum_of_squares(3), 14)  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    
    def test_single_number(self):
        """Test with n=1."""
        self.assertEqual(sum_of_squares(1), 1)
    
    def test_zero(self):
        """Test with n=0."""
        self.assertEqual(sum_of_squares(0), 0)
    
    def test_larger_number(self):
        """Test with larger number."""
        self.assertEqual(sum_of_squares(5), 55)  # 1² + 2² + 3² + 4² + 5² = 55


class TestCountdownToZero(unittest.TestCase):
    """Test cases for countdown_to_zero function."""
    
    def test_normal_countdown(self):
        """Test normal countdown."""
        self.assertEqual(countdown_to_zero(3), [3, 2, 1, 0])
    
    def test_single_number(self):
        """Test countdown from 1."""
        self.assertEqual(countdown_to_zero(1), [1, 0])
    
    def test_zero(self):
        """Test countdown from 0."""
        self.assertEqual(countdown_to_zero(0), [0])
    
    def test_larger_number(self):
        """Test countdown from larger number."""
        self.assertEqual(countdown_to_zero(5), [5, 4, 3, 2, 1, 0])


class TestFindMaximum(unittest.TestCase):
    """Test cases for find_maximum function."""
    
    def test_normal_list(self):
        """Test normal list."""
        self.assertEqual(find_maximum([1, 5, 3, 9, 2]), 9)
    
    def test_single_element(self):
        """Test single element list."""
        self.assertEqual(find_maximum([42]), 42)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(find_maximum([-5, -1, -10]), -1)
    
    def test_mixed_numbers(self):
        """Test with mixed positive and negative."""
        self.assertEqual(find_maximum([-3, 0, 5, -1]), 5)


class TestCountWordFrequency(unittest.TestCase):
    """Test cases for count_word_frequency function."""
    
    def test_normal_text(self):
        """Test normal text."""
        text = "hello world hello"
        expected = {"hello": 2, "world": 1}
        self.assertEqual(count_word_frequency(text), expected)
    
    def test_single_word(self):
        """Test single word."""
        self.assertEqual(count_word_frequency("test"), {"test": 1})
    
    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(count_word_frequency(""), {})
    
    def test_case_sensitive(self):
        """Test case sensitivity."""
        text = "Hello hello HELLO"
        expected = {"Hello": 1, "hello": 1, "HELLO": 1}
        self.assertEqual(count_word_frequency(text), expected)


class TestCalculateBMI(unittest.TestCase):
    """Test cases for calculate_bmi function."""
    
    def test_normal_bmi(self):
        """Test normal BMI calculation."""
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
    
    def test_underweight(self):
        """Test underweight BMI."""
        self.assertAlmostEqual(calculate_bmi(50, 1.80), 15.43, places=2)
    
    def test_overweight(self):
        """Test overweight BMI."""
        self.assertAlmostEqual(calculate_bmi(90, 1.70), 31.14, places=2)
    
    def test_zero_height(self):
        """Test zero height (should handle gracefully)."""
        # This might raise an exception or return a special value
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(70, 0)


class TestFilterEvenNumbers(unittest.TestCase):
    """Test cases for filter_even_numbers function."""
    
    def test_normal_list(self):
        """Test normal list."""
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [1, 3, 5])
    
    def test_all_odd(self):
        """Test list with all odd numbers."""
        self.assertEqual(filter_even_numbers([1, 3, 5, 7]), [1, 3, 5, 7])
    
    def test_all_even(self):
        """Test list with all even numbers."""
        self.assertEqual(filter_even_numbers([2, 4, 6, 8]), [])
    
    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(filter_even_numbers([]), [])


class TestGradeCalculator(unittest.TestCase):
    """Test cases for grade_calculator function."""
    
    def test_grade_a(self):
        """Test A grade."""
        self.assertEqual(grade_calculator([95, 90, 92]), "A")
    
    def test_grade_b(self):
        """Test B grade."""
        self.assertEqual(grade_calculator([85, 80, 88]), "B")
    
    def test_grade_c(self):
        """Test C grade."""
        self.assertEqual(grade_calculator([75, 70, 78]), "C")
    
    def test_grade_d(self):
        """Test D grade."""
        self.assertEqual(grade_calculator([65, 60, 68]), "D")
    
    def test_grade_f(self):
        """Test F grade."""
        self.assertEqual(grade_calculator([50, 45, 55]), "F")
    
    def test_single_score(self):
        """Test single score."""
        self.assertEqual(grade_calculator([85]), "B")
    
    def test_empty_scores(self):
        """Test empty scores list."""
        # This should handle empty list gracefully
        self.assertEqual(grade_calculator([]), "F")


if __name__ == "__main__":
    unittest.main()
