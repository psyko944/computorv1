import re
from collections import namedtuple
from utils import get_max_degree

charset = "0123456789+-*=/^xX."
sign = r"([+-]?)"
number = r"(\d+(\.\d+)?)"
exponent = r"[xX](\^\d+)?"
monomial = rf"{sign}(?:{number}\*?{exponent}|{number}|{exponent})"
polynomial = rf"({monomial})+"


Monomial = namedtuple('Monomial', ['coefficient', 'exponent', 'explicit_exponent'])

def print_monomial(m):
	var = '' if m[4] else 'X'
	
	s = m[0] if m[0] else '+'
	e = m[3][1:] if m[3] else m[6][1:] if m[6] else '1' if not m[4] else '0'
	f = m[2] if m[2] else m[5] if m[5] else ''
	n = m[4] if m[4] else m[1] if m[1] else '1'
	n = float(n) if f else int(n)
	explicit_exponent = m[3] or m[6]
	# print(f"sign: '{s}', number: '{n}', fractional part: '{f}', exponent: '{e}', variable: '{var}'")
	return Monomial(-n if s == '-' else n, int(e), explicit_exponent)

def format_polynomial(lhs, rhs):
	max_degree = get_max_degree(lhs, rhs)
	formated = [0] * (max_degree + 1)
	explicit_exponents = [False] * (max_degree + 1)
	for m in lhs:
		formated[m[1]] += m[0]
		if m.explicit_exponent:
			explicit_exponents[m.exponent] = True
	for m in rhs:
		formated[m[1]] -= m[0]
		if m.explicit_exponent:
			explicit_exponents[m.exponent] = True	
	while len(formated) > 1 and formated[-1] == 0:
		formated.pop()
	terms = []
	for degree in range(len(formated)):
		coeff = formated[degree]
		if coeff == 0 and not explicit_exponents[degree]:
			continue

		if explicit_exponents[degree] or degree == 2:
			term = f"{abs(coeff)} * X^{degree}"
		else:
			if degree == 0:
				term = f"{abs(coeff)}"
			elif degree == 1:
				term = f"{abs(coeff)} * X"
		sign = ''
		if coeff < 0:
			sign = "-" if not terms else " - " 
		elif terms:
			sign = " + "
		term = sign + term
		terms.append(term)
	while formated and formated[-1] == 0:
		formated.pop()
	max_degree = len(formated) - 1
	reduced = "".join(terms) + " = 0" if terms else "0 = 0"
	print(f"Reduced form: {reduced}")
	return formated, max_degree

def parse_polynomial(equation):
	if not re.fullmatch(polynomial, equation):
		raise ValueError("Error: Invalid polynomial format.")	
	p = re.findall(monomial, equation)
	return p


#create a function which store all value by same degree then reduce
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
	# print("LHS terms before:", lhs)
	lhs, rhs = parse_polynomial(lhs), parse_polynomial(rhs)
	# print("LHS terms:", lhs)
	# print("RHS terms:", rhs)
	# print("monomials regex LHS:")
	monomials_left = []
	monomials_right = []
	for m in lhs:
		monomials_left.append(print_monomial(m))
	# print("monomials regex RHS:")
	for m in rhs:
		monomials_right.append(print_monomial(m))
	# print("monomials LHS:")
	# for term in monomials_left:
	# 	print(term)
	# print("monomials RHS:")
	# for term in monomials_right:
	# 	print(term)
	reduced, max_degree = format_polynomial(monomials_left, monomials_right)
	return reduced, max_degree