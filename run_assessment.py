"""
Assessment Runner
================

Main script to run the Python assessment, grade student implementations,
validate student tests, and generate comprehensive feedback reports.
"""

import unittest
import sys
import os
import traceback
from typing import Dict, List, Any, Tuple
import time
from datetime import datetime


from test_validator import TestValidator


class AssessmentRunner:
    """Runs the complete assessment and generates reports."""
    
    def __init__(self):
        self.results = {
            'implementation_score': 0,
            'test_quality_score': 0,
            'overall_score': 0,
            'implementation_details': {},
            'test_validation_details': {},
            'errors': [],
            'warnings': [],
            'timestamp': datetime.now().isoformat()
        }
    
    def run_instructor_tests(self) -> Dict[str, Any]:
        """Run instructor tests to check student implementation correctness."""
        print("Running instructor tests to check implementation correctness...")
        print("-" * 60)
        
        implementation_results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'errors': 0,
            'test_details': {},
            'score': 0
        }
        
        try:
            # Import and run instructor tests
            import test_questions
            
            # Create a test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(test_questions)
            
            # Run tests with detailed output
            runner = unittest.TextTestRunner(
                verbosity=2,
                stream=open(os.devnull, 'w'),  # Suppress default output
                descriptions=True,
                failfast=False
            )
            
            # Capture results
            result = runner.run(suite)
            
            implementation_results['total_tests'] = result.testsRun
            implementation_results['passed_tests'] = result.testsRun - len(result.failures) - len(result.errors)
            implementation_results['failed_tests'] = len(result.failures)
            implementation_results['errors'] = len(result.errors)
            
            # Calculate score (70% weight for implementation)
            if result.testsRun > 0:
                implementation_results['score'] = (implementation_results['passed_tests'] / result.testsRun) * 70
            
            # Store detailed results
            for test, error in result.failures + result.errors:
                test_name = str(test)
                error_msg = error[1] if isinstance(error, tuple) else str(error)
                implementation_results['test_details'][test_name] = {
                    'status': 'FAILED' if test in [f[0] for f in result.failures] else 'ERROR',
                    'error': error_msg
                }
            
            print(f"Implementation Tests Complete:")
            print(f"   Total Tests: {implementation_results['total_tests']}")
            print(f"   Passed: {implementation_results['passed_tests']}")
            print(f"   Failed: {implementation_results['failed_tests']}")
            print(f"   Errors: {implementation_results['errors']}")
            print(f"   Score: {implementation_results['score']:.1f}/70")
            
        except Exception as e:
            error_msg = f"Error running instructor tests: {str(e)}"
            print(f"ERROR: {error_msg}")
            implementation_results['errors'] = 1
            implementation_results['test_details']['system_error'] = {
                'status': 'ERROR',
                'error': error_msg
            }
            self.results['errors'].append(error_msg)
        
        return implementation_results
    
    def run_student_tests(self) -> Dict[str, Any]:
        """Run student tests to check their test quality."""
        print("\nRunning student tests to check test quality...")
        print("-" * 60)
        
        student_test_results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'errors': 0,
            'test_details': {},
            'score': 0
        }
        
        try:
            # Import and run student tests
            import student_tests
            
            # Create a test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(student_tests)
            
            # Run tests
            runner = unittest.TextTestRunner(
                verbosity=2,
                stream=open(os.devnull, 'w'),
                descriptions=True,
                failfast=False
            )
            
            result = runner.run(suite)
            
            student_test_results['total_tests'] = result.testsRun
            student_test_results['passed_tests'] = result.testsRun - len(result.failures) - len(result.errors)
            student_test_results['failed_tests'] = len(result.failures)
            student_test_results['errors'] = len(result.errors)
            
            # Store detailed results
            for test, error in result.failures + result.errors:
                test_name = str(test)
                error_msg = error[1] if isinstance(error, tuple) else str(error)
                student_test_results['test_details'][test_name] = {
                    'status': 'FAILED' if test in [f[0] for f in result.failures] else 'ERROR',
                    'error': error_msg
                }
            
            print(f"Student Tests Complete:")
            print(f"   Total Tests: {student_test_results['total_tests']}")
            print(f"   Passed: {student_test_results['passed_tests']}")
            print(f"   Failed: {student_test_results['failed_tests']}")
            print(f"   Errors: {student_test_results['errors']}")
            
        except Exception as e:
            error_msg = f"Error running student tests: {str(e)}"
            print(f" {error_msg}")
            student_test_results['errors'] = 1
            student_test_results['test_details']['system_error'] = {
                'status': 'ERROR',
                'error': error_msg
            }
            self.results['errors'].append(error_msg)
        
        return student_test_results
    
    def validate_student_tests(self) -> Dict[str, Any]:
        """Validate student tests for uniqueness and quality."""
        print("\nValidating student test uniqueness and quality...")
        print("-" * 60)
        
        try:
            validator = TestValidator()
            validation_results = validator.validate_tests()
            
            print(f"   Test Validation Complete:")
            print(f"   Total Tests: {validation_results['total_tests']}")
            print(f"   Implemented: {validation_results['implemented_tests']}")
            print(f"   Unique: {validation_results['unique_tests']}")
            print(f"   Quality Score: {validation_results['overall_score']:.1f}/100")
            
            return validation_results
            
        except Exception as e:
            error_msg = f"Error validating student tests: {str(e)}"
            print(f" {error_msg}")
            self.results['errors'].append(error_msg)
            return {
                'overall_score': 0,
                'total_tests': 0,
                'implemented_tests': 0,
                'unique_tests': 0,
                'detailed_feedback': {},
                'summary': [error_msg]
            }
    
    def generate_final_report(self) -> str:
        """Generate the final comprehensive report."""
        report = []
        report.append("=" * 80)
        report.append("PYTHON ASSESSMENT - FINAL REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {self.results['timestamp']}")
        report.append("")
        
        # Overall Score
        report.append("OVERALL SCORE")
        report.append("-" * 40)
        report.append(f"Implementation Score: {self.results['implementation_score']:.1f}/70")
        report.append(f"Test Quality Score: {self.results['test_quality_score']:.1f}/30")
        report.append(f"TOTAL SCORE: {self.results['overall_score']:.1f}/100")
        report.append("")
        
        # Implementation Details
        if 'implementation_details' in self.results:
            impl = self.results['implementation_details']
            report.append("IMPLEMENTATION DETAILS")
            report.append("-" * 40)
            report.append(f"Total Tests: {impl.get('total_tests', 0)}")
            report.append(f"Passed: {impl.get('passed_tests', 0)}")
            report.append(f"Failed: {impl.get('failed_tests', 0)}")
            report.append(f"Errors: {impl.get('errors', 0)}")
            
            if impl.get('test_details'):
                report.append("\nFailed/Error Tests:")
                for test_name, details in impl['test_details'].items():
                    if details['status'] in ['FAILED', 'ERROR']:
                        report.append(f"  • {test_name}: {details['status']}")
                        if len(details['error']) < 200:  # Only show short errors
                            report.append(f"    {details['error']}")
            report.append("")
        
        # Test Validation Details
        if 'test_validation_details' in self.results:
            validation = self.results['test_validation_details']
            report.append("TEST VALIDATION DETAILS")
            report.append("-" * 40)
            report.append(f"Student Tests Written: {validation.get('total_tests', 0)}")
            report.append(f"Properly Implemented: {validation.get('implemented_tests', 0)}")
            report.append(f"Unique from Instructor: {validation.get('unique_tests', 0)}")
            report.append(f"Quality Score: {validation.get('overall_score', 0):.1f}/100")
            
            if validation.get('summary'):
                report.append("\nValidation Summary:")
                for message in validation['summary']:
                    report.append(f"  {message}")
            report.append("")
        
        # Errors and Warnings
        if self.results['errors']:
            report.append("ERRORS ENCOUNTERED")
            report.append("-" * 40)
            for error in self.results['errors']:
                report.append(f"  • {error}")
            report.append("")
        
        if self.results['warnings']:
            report.append("WARNINGS")
            report.append("-" * 40)
            for warning in self.results['warnings']:
                report.append(f"  • {warning}")
            report.append("")
        
        # Detailed Feedback
        if 'test_validation_details' in self.results and 'detailed_feedback' in self.results['test_validation_details']:
            report.append("DETAILED FEEDBACK")
            report.append("-" * 40)
            
            for class_name, class_feedback in self.results['test_validation_details']['detailed_feedback'].items():
                report.append(f"\n{class_name}:")
                
                if class_feedback.get('issues'):
                    report.append("  Issues:")
                    for issue in class_feedback['issues']:
                        report.append(f"    • {issue}")
                
                if class_feedback.get('suggestions'):
                    report.append("  Suggestions:")
                    for suggestion in class_feedback['suggestions']:
                        report.append(f"    • {suggestion}")
        
        # Grading Scale
        report.append("\n" + "=" * 80)
        report.append("GRADING SCALE")
        report.append("=" * 80)
        report.append("A (90-100): Excellent implementation and comprehensive, unique tests")
        report.append("B (80-89):  Good implementation with mostly unique tests")
        report.append("C (70-79):  Adequate implementation with some unique tests")
        report.append("D (60-69):  Basic implementation with limited test coverage")
        report.append("F (0-59):   Incomplete or incorrect implementation")
        report.append("")
        report.append("Note: 70% of grade is based on correct implementation")
        report.append("      30% of grade is based on test quality and uniqueness")
        
        return "\n".join(report)
    
    def run_complete_assessment(self) -> Dict[str, Any]:
        """Run the complete assessment process."""
        print("Starting Python Assessment...")
        print("=" * 60)
        
        # Step 1: Run instructor tests (implementation correctness)
        implementation_results = self.run_instructor_tests()
        self.results['implementation_details'] = implementation_results
        self.results['implementation_score'] = implementation_results['score']
        
        # Step 2: Run student tests (if they exist)
        student_test_results = self.run_student_tests()
        
        # Step 3: Validate student tests
        validation_results = self.validate_student_tests()
        self.results['test_validation_details'] = validation_results
        
        # Calculate test quality score (30% weight)
        # This is based on how many unique, well-implemented tests the student wrote
        test_quality_score = (validation_results['overall_score'] / 100) * 30
        self.results['test_quality_score'] = test_quality_score
        
        # Calculate overall score
        self.results['overall_score'] = self.results['implementation_score'] + self.results['test_quality_score']
        
        # Generate and display final report
        final_report = self.generate_final_report()
        print("\n" + final_report)
        
        # Save report to file
        report_filename = f"assessment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_filename, 'w') as f:
            f.write(final_report)
        print(f"\nDetailed report saved to: {report_filename}")
        
        return self.results


def main():
    """Main function to run the assessment."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Python Assessment Runner')
    parser.add_argument('--quick', '-q', action='store_true', 
                       help='Run quick test (implementation only, no full validation)')
    parser.add_argument('--implementation-only', '-i', action='store_true',
                       help='Test only implementation correctness')
    parser.add_argument('--tests-only', '-t', action='store_true',
                       help='Validate only student tests')
    parser.add_argument('--help-feedback', '-h', action='store_true',
                       help='Show detailed feedback for improvement')
    
    args = parser.parse_args()
    
    try:
        runner = AssessmentRunner()
        
        if args.quick or args.implementation_only:
            # Quick test - just check implementation
            print("Running Quick Implementation Test...")
            print("=" * 50)
            implementation_results = runner.run_instructor_tests()
            
            if implementation_results['score'] >= 70:
                print(f"\nImplementation looks good! Score: {implementation_results['score']:.1f}/70")
                print("Tip: Run 'python run_assessment.py' for full assessment including test validation")
            else:
                print(f"\nImplementation needs work. Score: {implementation_results['score']:.1f}/70")
                print("Focus on fixing the failed tests above")
            
        elif args.tests_only:
            # Test validation only
            print("Validating Student Tests...")
            print("=" * 50)
            validation_results = runner.validate_student_tests()
            
            if validation_results['overall_score'] >= 80:
                print(f"\nTests look good! Quality Score: {validation_results['overall_score']:.1f}/100")
            else:
                print(f"\nTests need improvement. Quality Score: {validation_results['overall_score']:.1f}/100")
                print("Check the detailed feedback above for specific issues")
                
        else:
            # Full assessment
            results = runner.run_complete_assessment()
            
            # Exit with appropriate code
            if results['overall_score'] >= 70:
                print(f"\nAssessment completed successfully! Score: {results['overall_score']:.1f}/100")
                sys.exit(0)
            else:
                print(f"\nAssessment completed with issues. Score: {results['overall_score']:.1f}/100")
                sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nAssessment interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error during assessment: {str(e)}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
