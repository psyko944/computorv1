import unittest
import subprocess
import sys
from typing import List, Dict
COMPUTOR_SCRIPT = "computor.py"


TEST_CASES: List[Dict[str,str]]= [
    {
        "equation": "1 * X^0 + 2 * X^1 + 5 * X^2 = 0",
        "expected": (
            "Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant: 2^2 - 4 * 5 * 1 = -16\n"
            "Discriminant is strictly negative, the two complex solutions are:\n"
            "X_1 = -2 - i * sqrt(16)/10\n"
            "-1/5 + 2i/5\n\n"
            "X_2 = -2 + i * sqrt(16)/10\n"
            "-1/5 - 2i/5"
        )
    },
    {
        "equation": "1 * X^2 - 7 * X^1 + 10 * X^0 = 0",
        "expected": (
            "Reduced form: 10 * X^0 - 7 * X^1 + 1 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant: -7^2 - 4 * 1 * 10 = 9\n"
            "Discriminant is strictly positive, the two solutions are:\n"
            "X_1 = 7 - sqrt(9) / 2\n"
            "2\n\n"
            "X_2 = 7 + sqrt(9) / 2\n"
            "5"
        )
    },
    {
        "equation": "5 * X^0 + 4 * X^1- 9.3 * X^2 = 1 * X^0",
        "expected": (
            "Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant: 4^2 - 4 * -9.3 * 4 = 164.8\n"
            "Discriminant is strictly positive, the two solutions are:\n"
            "X_1 = -4 - sqrt(164.8) / -18.6\n"
            "0.905239\n\n"
            "X_2 = -4 + sqrt(164.8) / -18.6\n"
            "-0.475131"
        )
    },
    {
        "equation": "1 * X^2 - 2 * X^1 + 1 * X^0 = 0",
        "expected": (
            "Reduced form: 1 * X^0 - 2 * X^1 + 1 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant: -2^2 - 4 * 1 * 1 = 0\n"
            "X = 2 / (2 * 1)\n"
            "Discriminant is zero, the unique solution is:\n"
            "1"
        )
    },
    {
        "equation": "5 * X^0 + 4 * X^1 = 4 * X^0",
        "expected": (
            "Reduced form: 1 * X^0 + 4 * X^1 = 0\n"
            "Polynomial degree: 1\n"
            "X = -1 / 4\n"
            "The solution is:\n"
            "-1/4"
        )
    },
    {
        "equation": "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
        "expected": (
            "Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0\n"
            "Polynomial degree: 3\n"
            "The polynomial degree is strictly greater than 2, I can't solve."
        )
    },
    {
        "equation": "6 * X^0 = 6 * X^0",
        "expected": (
            "Reduced form: 0 * X^0 = 0\n"
            "Any real number is a solution."
        )
    },
    {
        "equation": "10 * X^0 = 15 * X^0",
        "expected": (
            "Reduced form: -5 * X^0 = 0\n"
            "No solution."
        )
    },
    {
        "equation": "5 + 4 * X + X^2= X^2",
        "expected": (
            "Reduced form: 5 + 4 * X = 0\n"
            "Polynomial degree: 1\n"
            "X = -5 / 4\n"
            "The solution is:\n"
            "-5/4"
        )
    },
    {
        "equation": "6 * X = 5",
        "expected": (
            "Reduced form: -5 + 6 * X = 0\n"
            "Polynomial degree: 1\n"
            "X = 5 / 6\n"
            "The solution is:\n"
            "5/6"
        )
    }
]


ERROR_CASES: List[Dict[str,str]] = [
    {
        "equation": "1 * X^2 = 5 * Y^1",
        "expected_error_substring": "Error: Invalid character"
    },
    {
        "equation": "5x + 5 == 0",
        "expected_error_substring": "Error: Equation must contain exactly one '=' sign."
    },
    {
        "equation": "2 * X^2 + 3 = ",
        "expected_error_substring": "Error: Both sides of the equation must be non-empty."
    },
    {
        "equation": "2 ** X^2 + 3 = 0",
        "expected_error_substring": "Error: Invalid polynomial format."
    },
    {
        "equation": "2 * X^2 + = 4",
        "expected_error_substring": "Error: Invalid polynomial format."
    },
]

class TestComputorOutput(unittest.TestCase):
    
    def run_script_and_capture_output(self, equation: str, expect_error: bool = False) -> str:
        """
        Executes the main computor script with the given equation string 
        and captures all printed output (stdout).
        """
        try:
            result = subprocess.run(
                [sys.executable, COMPUTOR_SCRIPT, equation],
                capture_output=True,
                text=True,
                check=False
            )
            if expect_error:
                if result.returncode == 0:
                    self.fail(f"Expected an error but the script executed successfully.\nOutput:\n{result.stdout}")
                return (result.stderr or result.stdout).strip()    
            if result.returncode != 0:
                self.fail(f"Script execution failed with error:\n{result.stderr}")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            if not expect_error:
                self.fail(f"Script execution failed with error:\n{e.stderr}")
            return e.stderr.strip()
        except FileNotFoundError:
            self.fail(f"Error: The script '{COMPUTOR_SCRIPT}' was not found. Check the path.")
        

    def test_all_cases(self):
        for case in TEST_CASES:
            with self.subTest(equation=case["equation"]):
                actual_output = self.run_script_and_capture_output(case["equation"])
                self.assertEqual(actual_output, case["expected"])
    
    def test_error_cases(self):
        for case in ERROR_CASES:
            with self.subTest(equation=case["equation"]):
                actual_output = self.run_script_and_capture_output(case["equation"], expect_error=True)
                self.assertIn(case["expected_error_substring"], actual_output)

if __name__ == "__main__":
	unittest.main()