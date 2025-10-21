"""
Assessment Helper
================

Quick reference for all testing options available in this assessment.
"""

def show_help():
    """Display all available testing commands."""
    print("=" * 60)
    print("PYTHON ASSESSMENT - TESTING OPTIONS")
    print("=" * 60)
    print()
    
    print("INDIVIDUAL FUNCTION TESTING")
    print("-" * 40)
    print("Test specific functions as you implement them:")
    print("  python test_individual.py calculate_area")
    print("  python test_individual.py reverse_string")
    print("  python test_individual.py is_even_or_odd")
    print("  python test_individual.py sum_of_squares")
    print("  python test_individual.py countdown_to_zero")
    print("  python test_individual.py find_maximum")
    print("  python test_individual.py count_word_frequency")
    print("  python test_individual.py calculate_bmi")
    print("  python test_individual.py filter_even_numbers")
    print("  python test_individual.py grade_calculator")
    print("  python test_individual.py all")
    print()
    
    print("QUICK TESTING")
    print("-" * 40)
    print("Quick implementation check (70% of grade):")
    print("  python run_assessment.py --quick")
    print()
    print("Test only your unit tests (30% of grade):")
    print("  python run_assessment.py --tests-only")
    print()
    
    print("FULL ASSESSMENT")
    print("-" * 40)
    print("Complete assessment with detailed report:")
    print("  python run_assessment.py")
    print()
    
    print("RECOMMENDED WORKFLOW")
    print("-" * 40)
    print("1. Implement one function")
    print("2. Test it: python test_individual.py function_name")
    print("3. Repeat for all functions")
    print("4. Quick check: python run_assessment.py --quick")
    print("5. Write unit tests in student_tests.py")
    print("6. Validate tests: python run_assessment.py --tests-only")
    print("7. Final assessment: python run_assessment.py")
    print()
    
    print("FILES TO WORK ON")
    print("-" * 40)
    print("• questions.py - Implement the 10 functions")
    print("• student_tests.py - Write your unit tests")
    print("• README.md - Full instructions and guidelines")
    print()
    
    print("NEED HELP?")
    print("-" * 40)
    print("• Read README.md for detailed instructions")
    print("• Check error messages in test output")
    print("• Make sure functions handle edge cases")
    print("• Ensure your tests are unique from instructor tests")
    print()
    
    print("=" * 60)


if __name__ == "__main__":
    show_help()
