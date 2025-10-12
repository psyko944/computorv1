import re
from collections import namedtuple

charset = "0123456789+-*=/^xX."
sign = r"([+-]?)"
number = r"(\d+(\.\d+)?)"
exponent = r"[xX](\^[0-2])?"
monomial = rf"{sign}(?:{number}\*{exponent}|{number}|{exponent})"
polynomial = rf"({monomial})+"


Monomial = namedtuple('Monomial', ['coefficient', 'exponent'])

def print_monomial(m):
	var = '' if m[4] else 'X'
	
	s = m[0] if m[0] else '+'
	e = m[3][1:] if m[3] else m[6][1:] if m[6] else '1' if not m[4] else '0'
	f = m[2] if m[2] else m[5] if m[5] else ''
	n = m[4] if m[4] else m[1] if m[1] else '1'
	n = float(n) if f else int(n)
	print(f"sign: '{s}', number: '{n}', fractional part: '{f}', exponent: '{e}', variable: '{var}'")
	return Monomial(-n if s == '-' else n, int(e))

# def format_polynomial(lhs, rhs):

def parse_polynomial(equation):
	if re.fullmatch(polynomial, equation):
		print("match")
	p = re.findall(monomial, equation)
	return p


#create a function which store all value by same degree then reduice
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
	monomials_left = []
	monomials_right = []
	for m in lhs:
		monomials_left.append(print_monomial(m))
	for m in rhs:
		monomials_right.append(print_monomial(m))
	print("monomials RHS:")
	for term in monomials_left:
		print(term, term.coefficient)
	for term in monomials_right:
		print(term)