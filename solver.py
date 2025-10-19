from utils import get_discriminant
import utils

def print_solution(reduced, max_degree):
    if max_degree == 0:
        print("There are no solutions.")
    elif max_degree == 1:
        solve_first_degree(reduced)
    elif max_degree == 2:
        cal_roots(reduced[2], reduced[1], reduced[0])
    else: 
        print("The polynomial degree is strictly greater than 2, I can't solve.")

def solve_first_degree(reduced):
    print(f"The solution is\n{ -reduced[0] / reduced[1] }", -reduced[0], reduced[1])

def cal_roots(a, b, c):
  if a == 0:
    if b == 0:
      return ["Any number is a solution"]
    return [c/b]
  d = get_discriminant(a, b, c)
  if d == 0:
    print("one root")
    return [-b/(2*a)]
  elif d > 0:
    print("Two real roots")
    return [(-b-utils.get_sqrt(d))/(2 * a), (-b+utils.get_sqrt(d))/(2 * a)]
  else:
    print("Two imaginary roots")
    return [(-b-utils.sqrt(d))/(2 * a), (-b+utils.sqrt(d))/(2 * a)]

def solve(a1, b1, c1, a2, b2, c2):
  return cal_roots(a1-a2, b1-b2, c1-c2)


def solve_quadratic(a, b, c):
	discriminant = get_discriminant(a, b, c)
	print(f"The discriminant is: {discriminant}")
	if discriminant > 0:
		print("the discriminant(Δ) is positive, the quadratic equation has two real solutions:")
	elif discriminant == 0:
		print("the discriminant(Δ) is zero, the quadratic equation has one real solution:")
	else:
		print("the discriminant(Δ) is negative, the quadratic equation has no real solutions, complex roots exist:")