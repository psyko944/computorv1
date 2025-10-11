from utils import get_discriminant
import utils


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