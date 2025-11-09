from pdb import main
from utils import *
import parser
import solver
import sys

if __name__ == "__main__":
	if len(sys.argv) == 2:
		equation = sys.argv[1]
	elif len(sys.argv) == 1:
		equation = input("Enter the equation : ")
	else:
		print(f"Usage: python {sys.argv[0]} \"<your_equation>\"")
		sys.exit(1)
	equation = sys.argv[1]
	reduced, max_degree = parser.parse(equation)
	print("Polynomial degree:", max_degree) if max_degree > 0 else ''
	solver.print_solution(reduced, max_degree)