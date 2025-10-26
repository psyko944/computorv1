import unittest
import subprocess
import os
import sys
COMPUTOR_SCRIPT = "computor.py"

class TestComputorOutput(unittest.TestCase):
    
    def run_script_and_capture_output(self, equation: str) -> str:
        """
        Executes the main computor script with the given equation string 
        and captures all printed output (stdout).
        """
        try:
            # Execute the script as a command-line utility
            result = subprocess.run(
                [sys.executable, COMPUTOR_SCRIPT, equation],
                capture_output=True, # Capture stdout and stderr
                text=True,           # Decode the output as text
                check=True           # Raise an error if the script fails (non-zero exit code)
            )
            # Return the captured stdout, stripped of leading/trailing whitespace
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.fail(f"Script execution failed with error:\n{e.stderr}")
        except FileNotFoundError:
            self.fail(f"Error: The script '{COMPUTOR_SCRIPT}' was not found. Check the path.")

    def test_complex_solutions_irreducible_fractions(self):
        """
        Tests an equation resulting in complex solutions (Delta < 0) 
        and checks for irreducible fraction format.
        Equation: 5X^2 + 2X + 1 = 0
        Solutions: (-2 +/- sqrt(-16)) / 10 = -2/10 +/- 4i/10 = -1/5 +/- 2i/5
        """
        equation = "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"
        
        # Define the EXACT expected output (including newlines and formatting)
        expected_output = (
            "Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0\n" # Assuming the script reorders/reduces terms
            "Polynomial degree: 2\n"
            "Discriminant is strictly negative, the two complex solutions are:\n"
            "-1/5 + 2i/5\n"
            "-1/5 - 2i/5"
        )

        actual_output = self.run_script_and_capture_output(equation)
        self.assertEqual(actual_output, expected_output)

    def test_real_solutions_simple_integers(self):
        """
        Tests an equation resulting in simple integer solutions (Delta > 0).
        """
        equation = "1 * X^2 - 7 * X^1 + 10 * X^0 = 0"
        
        expected_output = (
            "Reduced form: 10 * X^0 - 7 * X^1 + 1 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant is strictly positive, the two solutions are:\n"
            "2\n"
            "5"
        )
        
        actual_output = self.run_script_and_capture_output(equation)
        self.assertEqual(actual_output, expected_output)

    def test_single_solution_delta_zero(self):
        """
        Tests an equation resulting in one real solution (Delta = 0).
        Equation: X^2 - 2X + 1 = 0 --> (X-1)^2 = 0
        """
        equation = "1 * X^2 - 2 * X^1 + 1 * X^0 = 0"
        
        expected_output = (
            "Reduced form: 1 * X^0 - 2 * X^1 + 1 * X^2 = 0\n"
            "Polynomial degree: 2\n"
            "Discriminant is zero, the unique solution is:\n"
            "1"
        )
        
        actual_output = self.run_script_and_capture_output(equation)
        self.assertEqual(actual_output, expected_output)
        
if __name__ == "__main__":
	unittest.main()