from pdb import main
import parser
import sys

def find_degree(equation):
	max_degree = 0
	for x in equation:
		if x[0] == '^':
			if int(x[1:]) > max_degree:
				max_degree = int(x[1:])
	return max_degree

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python {sys.argv[0]} \"<your_equation>\"")
		raise ValueError("Error: One argument is required.")
	equation = sys.argv[1]
	print("equation: ", equation)
	# print("Reduced form: ", equation.split())
	parser.parse(equation)
	# print("Polynomial degree: ", find_degree(equation.split()))