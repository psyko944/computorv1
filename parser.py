import re 

charset = "0123456789+-*=/^xX."
sign = r"([+-]?)"
number = r"(\d+(\.\d+)?)"
exponent = r"[xX](\^[0-3])?"
monomial = rf"{sign}(?:{number}\*{exponent}|{number}|{exponent})"
polynomial = rf"({monomial})+"


def print_monomial(m):
	var = '' if m[4] else 'X'
	
	s = m[0] if m[0] else '+' #sign
	e = m[3][1:] if m[3] else m[6][1:] if m[6] else '1' if not m[4] else '0'
	f = m[2] if m[2] else m[5] if m[5] else '0' # fractional part
	n = m[4] if m[4] else m[1] if m[1] else '1' # number with var
	print(f"sign: '{s}', number: '{n}', fractional part: '{f}', exponent: '{e}', variable: '{var}'")

def parse_polynomial(equation):
	if re.fullmatch(polynomial, equation):
		print("match")
	p = re.findall(monomial, equation)
	return p
	# return [create_monomial(*t) for t in p]

def parse(equation):
	s = equation.replace(" ", "")
	for x in s:
		if x not in charset:
			raise ValueError(f"Error: Invalid character '{x}' in equation.")
	if s.count('=') != 1:
		raise ValueError("Error: Equation must contain exactly one '=' sign.")
	lhs, rhs = s.split('=')
	if not lhs or not rhs:
		raise ValueError("Error: Both sides of the equation must be non-empty.")
	print("LHS terms before:", lhs)
	lhs, rhs = parse_polynomial(lhs), parse_polynomial(rhs)
	print("LHS terms:", lhs)
	print("RHS terms:", rhs)
	print("monomials LHS:")
	for m in lhs:
		print_monomial(m)