"""
Student Tests Template
=====================

INSTRUCTIONS:
1. Write 2-3 unit tests for each function in questions.py
2. Your tests must be DIFFERENT from the instructor tests
3. Think about edge cases, boundary conditions, and various scenarios
4. Use descriptive test method names
5. Make sure your tests actually test the function behavior

IMPORTANT: Your tests will be validated to ensure they are unique and comprehensive.
Don't copy the instructor tests - be creative and think of different test cases!

Example test structure:
def test_your_descriptive_name(self):
    \"\"\"Brief description of what this test does.\"\"\"
    # Your test code here
    self.assertEqual(your_function_call, expected_result)
"""

import unittest
from questions import (
    calculate_area, reverse_string, is_even_or_odd, sum_of_squares,
    countdown_to_zero, find_maximum, count_word_frequency, calculate_bmi,
    filter_even_numbers, grade_calculator
)


class TestCalculateArea(unittest.TestCase):
    """Your tests for calculate_area function."""
    
    # TODO: Write 2-3 tests for calculate_area
    # Think about: negative values, very large numbers, decimal precision, etc.
    
    def test_negative_dimensions(self):
        """Test with negative dimensions."""
        # TODO: Implement this test
        pass
    
    def test_large_numbers(self):
        """Test with large numbers."""
        # TODO: Implement this test
        pass
    
    def test_decimal_precision(self):
        """Test decimal precision."""
        # TODO: Implement this test
        pass


class TestReverseString(unittest.TestCase):
    """Your tests for reverse_string function."""
    
    # TODO: Write 2-3 tests for reverse_string
    # Think about: special characters, numbers, spaces, etc.
    
    def test_numbers_in_string(self):
        """Test string with numbers."""
        # TODO: Implement this test
        pass
    
    def test_special_characters(self):
        """Test string with special characters."""
        # TODO: Implement this test
        pass
    
    def test_spaces_in_string(self):
        """Test string with spaces."""
        # TODO: Implement this test
        pass


class TestIsEvenOrOdd(unittest.TestCase):
    """Your tests for is_even_or_odd function."""
    
    # TODO: Write 2-3 tests for is_even_or_odd
    # Think about: large numbers, decimal inputs, etc.
    
    def test_large_even_number(self):
        """Test with large even number."""
        # TODO: Implement this test
        pass
    
    def test_large_odd_number(self):
        """Test with large odd number."""
        # TODO: Implement this test
        pass
    
    def test_decimal_input(self):
        """Test with decimal input."""
        # TODO: Implement this test
        pass


class TestSumOfSquares(unittest.TestCase):
    """Your tests for sum_of_squares function."""
    
    # TODO: Write 2-3 tests for sum_of_squares
    # Think about: negative numbers, large numbers, etc.
    
    def test_negative_input(self):
        """Test with negative input."""
        # TODO: Implement this test
        pass
    
    def test_large_number(self):
        """Test with large number."""
        # TODO: Implement this test
        pass
    
    def test_ten_squares(self):
        """Test sum of first 10 squares."""
        # TODO: Implement this test
        pass


class TestCountdownToZero(unittest.TestCase):
    """Your tests for countdown_to_zero function."""
    
    # TODO: Write 2-3 tests for countdown_to_zero
    # Think about: negative inputs, large numbers, etc.
    
    def test_negative_input(self):
        """Test with negative input."""
        # TODO: Implement this test
        pass
    
    def test_large_number(self):
        """Test with large number."""
        # TODO: Implement this test
        pass
    
    def test_countdown_from_ten(self):
        """Test countdown from 10."""
        # TODO: Implement this test
        pass


class TestFindMaximum(unittest.TestCase):
    """Your tests for find_maximum function."""
    
    # TODO: Write 2-3 tests for find_maximum
    # Think about: duplicate maximums, floating point numbers, etc.
    
    def test_duplicate_maximums(self):
        """Test with duplicate maximum values."""
        # TODO: Implement this test
        pass
    
    def test_floating_point_numbers(self):
        """Test with floating point numbers."""
        # TODO: Implement this test
        pass
    
    def test_mixed_data_types(self):
        """Test with mixed data types."""
        # TODO: Implement this test
        pass


class TestCountWordFrequency(unittest.TestCase):
    """Your tests for count_word_frequency function."""
    
    # TODO: Write 2-3 tests for count_word_frequency
    # Think about: punctuation, numbers, special characters, etc.
    
    def test_text_with_punctuation(self):
        """Test text with punctuation marks."""
        # TODO: Implement this test
        pass
    
    def test_text_with_numbers(self):
        """Test text with numbers."""
        # TODO: Implement this test
        pass
    
    def test_long_text(self):
        """Test with longer text."""
        # TODO: Implement this test
        pass


class TestCalculateBMI(unittest.TestCase):
    """Your tests for calculate_bmi function."""
    
    # TODO: Write 2-3 tests for calculate_bmi
    # Think about: very small/large values, negative values, etc.
    
    def test_very_small_height(self):
        """Test with very small height."""
        # TODO: Implement this test
        pass
    
    def test_very_large_weight(self):
        """Test with very large weight."""
        # TODO: Implement this test
        pass
    
    def test_negative_values(self):
        """Test with negative values."""
        # TODO: Implement this test
        pass


class TestFilterEvenNumbers(unittest.TestCase):
    """Your tests for filter_even_numbers function."""
    
    # TODO: Write 2-3 tests for filter_even_numbers
    # Think about: negative numbers, floating point numbers, etc.
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        # TODO: Implement this test
        pass
    
    def test_floating_point_numbers(self):
        """Test with floating point numbers."""
        # TODO: Implement this test
        pass
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        # TODO: Implement this test
        pass


class TestGradeCalculator(unittest.TestCase):
    """Your tests for grade_calculator function."""
    
    # TODO: Write 2-3 tests for grade_calculator
    # Think about: boundary values, negative scores, etc.
    
    def test_boundary_grade_a(self):
        """Test boundary case for grade A (90)."""
        # TODO: Implement this test
        pass
    
    def test_negative_scores(self):
        """Test with negative scores."""
        # TODO: Implement this test
        pass
    
    def test_very_high_scores(self):
        """Test with very high scores."""
        # TODO: Implement this test
        pass


if __name__ == "__main__":
    # You can run your tests individually or all together
    unittest.main()
