import re 

charset = "0123456789+-*=/^xX."
sign = r"([+-]?)"
number = r"(\d+(\.\d+)?)"
exponent = r"[xX]\^([0-3])?"
monomial = rf"{sign}{number}\*?{exponent}?"
polynomial = rf"({monomial})+"


# def create_monomial(term):

def parse_polynomial(equation):
	if re.fullmatch(polynomial, equation):
		print("match")
	p = re.split(monomial, equation)
	return p
	# return [create_monomial(*t) for t in p]

def parse(equation):
	s = equation.replace(" ", "")
	if s.count('=') != 1:
		raise ValueError("Error: Equation must contain exactly one '=' sign.")
	for x in s:
		if x not in charset:
			raise ValueError(f"Error: Invalid character '{x}' in equation.")
	lhs, rhs = s.split('=')
	if not lhs or not rhs:
		raise ValueError("Error: Both sides of the equation must be non-empty.")
	lhs, rhs = parse_polynomial(lhs), parse_polynomial(rhs)
	print("LHS terms:", lhs)
	print("RHS terms:", rhs)