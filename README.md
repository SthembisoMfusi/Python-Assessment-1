# Python Assessment - First Year Students

## Overview

This assessment tests your understanding of basic Python fundamentals through 10 programming problems. You will implement functions and write unit tests to demonstrate your knowledge.

## Assessment Structure

- **70% Implementation Score**: Correct implementation of all 10 functions
- **30% Test Quality Score**: Writing unique, comprehensive unit tests

## Files in This Project

- `questions.py` - Contains 10 function stubs you need to implement
- `student_tests.py` - Template for your unit tests (you must complete this)
- `test_questions.py` - Instructor tests (DO NOT MODIFY - used for grading)
- `test_validator.py` - Validates your tests are unique (DO NOT MODIFY)
- `run_assessment.py` - Runs the complete assessment and generates your grade
- `README.md` - This file with instructions

## Instructions

### Step 1: Implement the Functions

1. Open `questions.py`
2. Complete all 10 functions according to their docstrings
3. Make sure to handle edge cases appropriately
4. Test your functions manually to ensure they work

### Step 2: Write Unit Tests

1. Open `student_tests.py`
2. Write 2-3 unit tests for each function (20-30 tests total)
3. **IMPORTANT**: Your tests must be DIFFERENT from the instructor tests
4. Think about edge cases, boundary conditions, and various scenarios
5. Use descriptive test method names
6. Make sure your tests actually test the function behavior

### Step 3: Test Your Progress

You can test your progress in several ways:

#### Quick Implementation Test
```bash
python run_assessment.py --quick
```
This quickly checks if your functions work correctly (70% of your grade).

#### Test Individual Functions
```bash
python test_individual.py function_name
python test_individual.py all
```
Test specific functions as you implement them.

#### Test Your Unit Tests
```bash
python run_assessment.py --tests-only
```
Validate your unit tests for uniqueness and quality.

#### Full Assessment
```bash
python run_assessment.py
```
Complete assessment with detailed report and final grade.

## Function Requirements

### 1. `calculate_area(length, width)`
Calculate the area of a rectangle.

### 2. `reverse_string(text)`
Reverse a string.

### 3. `is_even_or_odd(number)`
Determine if a number is even or odd. Return "even" or "odd".

### 4. `sum_of_squares(n)`
Calculate the sum of squares from 1 to n (inclusive).

### 5. `countdown_to_zero(n)`
Count down from n to 0 using a while loop. Return a list.

### 6. `find_maximum(numbers)`
Find the maximum value in a list of numbers.

### 7. `count_word_frequency(text)`
Count the frequency of each word in a text. Return a dictionary.

### 8. `calculate_bmi(weight, height)`
Calculate Body Mass Index (BMI).

### 9. `filter_even_numbers(numbers)`
Filter out even numbers from a list, keeping only odd numbers.

### 10. `grade_calculator(scores)`
Calculate the average grade and return a letter grade (A, B, C, D, F).

## Test Writing Guidelines

### Good Test Examples:
```python
def test_negative_dimensions(self):
    """Test with negative dimensions."""
    self.assertEqual(calculate_area(-5, 3), -15)

def test_large_numbers(self):
    """Test with large numbers."""
    self.assertEqual(calculate_area(1000, 2000), 2000000)
```

### What Makes Tests Unique:
- Different input values
- Different edge cases
- Different boundary conditions
- Different data types
- Different error conditions

### Test Quality Checklist:
- ✅ Tests are implemented (not just `pass`)
- ✅ Tests have descriptive names
- ✅ Tests have docstrings
- ✅ Tests use appropriate assertions
- ✅ Tests cover different scenarios than instructor tests
- ✅ Tests actually verify expected behavior

## Grading Breakdown

| Component | Weight | Description |
|-----------|--------|-------------|
| Implementation | 70% | Correct implementation of all functions |
| Test Quality | 30% | Unique, comprehensive unit tests |

### Grading Scale:
- **A (90-100)**: Excellent implementation and comprehensive, unique tests
- **B (80-89)**: Good implementation with mostly unique tests
- **C (70-79)**: Adequate implementation with some unique tests
- **D (60-69)**: Basic implementation with limited test coverage
- **F (0-59)**: Incomplete or incorrect implementation

## Common Issues and Solutions

### "Test is too similar to instructor test"
- **Issue**: Your test uses the same inputs or logic as instructor tests
- **Solution**: Think of different test cases, edge cases, or boundary conditions

### "Test is not implemented"
- **Issue**: Your test contains only `pass` or TODO comments
- **Solution**: Write actual test code with assertions

### "Test lacks proper assertions"
- **Issue**: Your test doesn't verify the expected behavior
- **Solution**: Add appropriate assertions (assertEqual, assertTrue, etc.)

### "Test name might not be descriptive enough"
- **Issue**: Test method name is too short or unclear
- **Solution**: Use longer, more descriptive names that explain what the test does

## Recommended Workflow

1. **Start with one function**: Implement `calculate_area`, then test it:
   ```bash
   python test_individual.py calculate_area
   ```

2. **Test as you go**: After each function, test it individually:
   ```bash
   python test_individual.py function_name
   ```

3. **Quick check**: When you've implemented several functions:
   ```bash
   python run_assessment.py --quick
   ```

4. **Write unit tests**: Once functions work, write your unit tests in `student_tests.py`

5. **Validate your tests**: Check your unit tests are unique:
   ```bash
   python run_assessment.py --tests-only
   ```

6. **Final assessment**: When everything is ready:
   ```bash
   python run_assessment.py
   ```

## Tips for Success

1. **Read the docstrings carefully** - they explain exactly what each function should do
2. **Test your functions individually** as you implement them
3. **Think about edge cases** - empty inputs, negative numbers, boundary values
4. **Be creative with your tests** - don't just copy the instructor examples
5. **Use descriptive test names** - they help you and the grader understand your tests
6. **Run tests frequently** - catch issues early rather than at the end

## Getting Help

### Quick Reference
```bash
python help.py
```
Shows all available testing commands and workflow.

### If you encounter issues:
1. Check the error messages in the assessment report
2. Make sure all functions are implemented
3. Ensure your tests are unique and comprehensive
4. Verify your test syntax is correct
5. Test functions individually to isolate problems

## Submission

When you're ready to submit:
1. Make sure all functions in `questions.py` are implemented
2. Complete all tests in `student_tests.py`
3. Run `python run_assessment.py` to verify everything works
4. Submit all files together

Good luck! 🐍
