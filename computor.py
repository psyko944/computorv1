from pdb import main
from utils import *
import parser
import solver
import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python {sys.argv[0]} \"<your_equation>\"")
		raise ValueError("Error: One argument is required.")
	equation = sys.argv[1]
	# print("equation: ", equation)
	reduced, max_degree = parser.parse(equation)
	print("Polynomial degree:", max_degree)
	solver.print_solution(reduced, max_degree)