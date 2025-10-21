"""
Individual Function Tester
==========================

Quick script to test individual functions as you implement them.
This helps you test your progress without running the full assessment.

Usage:
    python test_individual.py function_name
    python test_individual.py all
"""

import sys
import unittest
from questions import (
    calculate_area, reverse_string, is_even_or_odd, sum_of_squares,
    countdown_to_zero, find_maximum, count_word_frequency, calculate_bmi,
    filter_even_numbers, grade_calculator
)


def test_calculate_area():
    """Test calculate_area function."""
    print("Testing calculate_area...")
    try:
        # Basic test
        result = calculate_area(5, 3)
        print(f"  calculate_area(5, 3) = {result} (expected: 15)")
        assert result == 15, f"Expected 15, got {result}"
        
        # Square test
        result = calculate_area(4, 4)
        print(f"  calculate_area(4, 4) = {result} (expected: 16)")
        assert result == 16, f"Expected 16, got {result}"
        
        # Decimal test
        result = calculate_area(2.5, 3.2)
        print(f"  calculate_area(2.5, 3.2) = {result} (expected: 8.0)")
        assert abs(result - 8.0) < 0.001, f"Expected ~8.0, got {result}"
        
        print("  PASSED: calculate_area tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: calculate_area test failed: {e}")
        return False


def test_reverse_string():
    """Test reverse_string function."""
    print("Testing reverse_string...")
    try:
        # Basic test
        result = reverse_string("hello")
        print(f"  reverse_string('hello') = '{result}' (expected: 'olleh')")
        assert result == "olleh", f"Expected 'olleh', got '{result}'"
        
        # Single character
        result = reverse_string("a")
        print(f"  reverse_string('a') = '{result}' (expected: 'a')")
        assert result == "a", f"Expected 'a', got '{result}'"
        
        # Empty string
        result = reverse_string("")
        print(f"  reverse_string('') = '{result}' (expected: '')")
        assert result == "", f"Expected '', got '{result}'"
        
        print("  PASSED: reverse_string tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: reverse_string test failed: {e}")
        return False


def test_is_even_or_odd():
    """Test is_even_or_odd function."""
    print("Testing is_even_or_odd...")
    try:
        # Even number
        result = is_even_or_odd(4)
        print(f"  is_even_or_odd(4) = '{result}' (expected: 'even')")
        assert result == "even", f"Expected 'even', got '{result}'"
        
        # Odd number
        result = is_even_or_odd(7)
        print(f"  is_even_or_odd(7) = '{result}' (expected: 'odd')")
        assert result == "odd", f"Expected 'odd', got '{result}'"
        
        # Zero
        result = is_even_or_odd(0)
        print(f"  is_even_or_odd(0) = '{result}' (expected: 'even')")
        assert result == "even", f"Expected 'even', got '{result}'"
        
        print("  PASSED: is_even_or_odd tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: is_even_or_odd test failed: {e}")
        return False


def test_sum_of_squares():
    """Test sum_of_squares function."""
    print("Testing sum_of_squares...")
    try:
        # Basic test
        result = sum_of_squares(3)
        print(f"  sum_of_squares(3) = {result} (expected: 14)")
        assert result == 14, f"Expected 14, got {result}"
        
        # Single number
        result = sum_of_squares(1)
        print(f"  sum_of_squares(1) = {result} (expected: 1)")
        assert result == 1, f"Expected 1, got {result}"
        
        # Zero
        result = sum_of_squares(0)
        print(f"  sum_of_squares(0) = {result} (expected: 0)")
        assert result == 0, f"Expected 0, got {result}"
        
        print("  PASSED: sum_of_squares tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: sum_of_squares test failed: {e}")
        return False


def test_countdown_to_zero():
    """Test countdown_to_zero function."""
    print("Testing countdown_to_zero...")
    try:
        # Basic test
        result = countdown_to_zero(3)
        print(f"  countdown_to_zero(3) = {result} (expected: [3, 2, 1, 0])")
        assert result == [3, 2, 1, 0], f"Expected [3, 2, 1, 0], got {result}"
        
        # Single number
        result = countdown_to_zero(1)
        print(f"  countdown_to_zero(1) = {result} (expected: [1, 0])")
        assert result == [1, 0], f"Expected [1, 0], got {result}"
        
        # Zero
        result = countdown_to_zero(0)
        print(f"  countdown_to_zero(0) = {result} (expected: [0])")
        assert result == [0], f"Expected [0], got {result}"
        
        print("  PASSED: countdown_to_zero tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: countdown_to_zero test failed: {e}")
        return False


def test_find_maximum():
    """Test find_maximum function."""
    print("Testing find_maximum...")
    try:
        # Basic test
        result = find_maximum([1, 5, 3, 9, 2])
        print(f"  find_maximum([1, 5, 3, 9, 2]) = {result} (expected: 9)")
        assert result == 9, f"Expected 9, got {result}"
        
        # Single element
        result = find_maximum([42])
        print(f"  find_maximum([42]) = {result} (expected: 42)")
        assert result == 42, f"Expected 42, got {result}"
        
        # Negative numbers
        result = find_maximum([-5, -1, -10])
        print(f"  find_maximum([-5, -1, -10]) = {result} (expected: -1)")
        assert result == -1, f"Expected -1, got {result}"
        
        print("  PASSED: find_maximum tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: find_maximum test failed: {e}")
        return False


def test_count_word_frequency():
    """Test count_word_frequency function."""
    print("Testing count_word_frequency...")
    try:
        # Basic test
        result = count_word_frequency("hello world hello")
        expected = {"hello": 2, "world": 1}
        print(f"  count_word_frequency('hello world hello') = {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Single word
        result = count_word_frequency("test")
        expected = {"test": 1}
        print(f"  count_word_frequency('test') = {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Empty string
        result = count_word_frequency("")
        expected = {}
        print(f"  count_word_frequency('') = {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("  PASSED: count_word_frequency tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: count_word_frequency test failed: {e}")
        return False


def test_calculate_bmi():
    """Test calculate_bmi function."""
    print("Testing calculate_bmi...")
    try:
        # Basic test
        result = calculate_bmi(70, 1.75)
        print(f"  calculate_bmi(70, 1.75) = {result:.2f} (expected: ~22.86)")
        assert abs(result - 22.86) < 0.1, f"Expected ~22.86, got {result}"
        
        # Underweight
        result = calculate_bmi(50, 1.80)
        print(f"  calculate_bmi(50, 1.80) = {result:.2f} (expected: ~15.43)")
        assert abs(result - 15.43) < 0.1, f"Expected ~15.43, got {result}"
        
        print("  PASSED: calculate_bmi tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: calculate_bmi test failed: {e}")
        return False


def test_filter_even_numbers():
    """Test filter_even_numbers function."""
    print("Testing filter_even_numbers...")
    try:
        # Basic test
        result = filter_even_numbers([1, 2, 3, 4, 5, 6])
        print(f"  filter_even_numbers([1, 2, 3, 4, 5, 6]) = {result} (expected: [1, 3, 5])")
        assert result == [1, 3, 5], f"Expected [1, 3, 5], got {result}"
        
        # All odd
        result = filter_even_numbers([1, 3, 5, 7])
        print(f"  filter_even_numbers([1, 3, 5, 7]) = {result} (expected: [1, 3, 5, 7])")
        assert result == [1, 3, 5, 7], f"Expected [1, 3, 5, 7], got {result}"
        
        # Empty list
        result = filter_even_numbers([])
        print(f"  filter_even_numbers([]) = {result} (expected: [])")
        assert result == [], f"Expected [], got {result}"
        
        print("  PASSED: filter_even_numbers tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: filter_even_numbers test failed: {e}")
        return False


def test_grade_calculator():
    """Test grade_calculator function."""
    print("Testing grade_calculator...")
    try:
        # Grade A
        result = grade_calculator([95, 90, 92])
        print(f"  grade_calculator([95, 90, 92]) = '{result}' (expected: 'A')")
        assert result == "A", f"Expected 'A', got '{result}'"
        
        # Grade B
        result = grade_calculator([85, 80, 88])
        print(f"  grade_calculator([85, 80, 88]) = '{result}' (expected: 'B')")
        assert result == "B", f"Expected 'B', got '{result}'"
        
        # Grade F
        result = grade_calculator([50, 45, 55])
        print(f"  grade_calculator([50, 45, 55]) = '{result}' (expected: 'F')")
        assert result == "F", f"Expected 'F', got '{result}'"
        
        print("  PASSED: grade_calculator tests passed!")
        return True
    except Exception as e:
        print(f"  FAILED: grade_calculator test failed: {e}")
        return False


def test_all():
    """Test all functions."""
    print("Testing all functions...")
    print("=" * 50)
    
    tests = [
        test_calculate_area,
        test_reverse_string,
        test_is_even_or_odd,
        test_sum_of_squares,
        test_countdown_to_zero,
        test_find_maximum,
        test_count_word_frequency,
        test_calculate_bmi,
        test_filter_even_numbers,
        test_grade_calculator
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Add spacing between tests
    
    print("=" * 50)
    print(f"Results: {passed}/{total} functions working correctly")
    
    if passed == total:
        print("SUCCESS: All functions are working! You're ready for the full assessment.")
        print("Next: Run 'python run_assessment.py' to get your final grade.")
    else:
        print(f"WARNING: {total - passed} functions still need work.")
        print("Focus on the failed functions above, then test again.")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python test_individual.py function_name")
        print("  python test_individual.py all")
        print("")
        print("Available functions:")
        print("  calculate_area, reverse_string, is_even_or_odd, sum_of_squares")
        print("  countdown_to_zero, find_maximum, count_word_frequency")
        print("  calculate_bmi, filter_even_numbers, grade_calculator")
        return
    
    function_name = sys.argv[1].lower()
    
    if function_name == "all":
        test_all()
    elif function_name == "calculate_area":
        test_calculate_area()
    elif function_name == "reverse_string":
        test_reverse_string()
    elif function_name == "is_even_or_odd":
        test_is_even_or_odd()
    elif function_name == "sum_of_squares":
        test_sum_of_squares()
    elif function_name == "countdown_to_zero":
        test_countdown_to_zero()
    elif function_name == "find_maximum":
        test_find_maximum()
    elif function_name == "count_word_frequency":
        test_count_word_frequency()
    elif function_name == "calculate_bmi":
        test_calculate_bmi()
    elif function_name == "filter_even_numbers":
        test_filter_even_numbers()
    elif function_name == "grade_calculator":
        test_grade_calculator()
    else:
        print(f"Unknown function: {function_name}")
        print("Run 'python test_individual.py' to see available functions.")


if __name__ == "__main__":
    main()
