from utils import get_discriminant
from fractions import Fraction
import utils

def print_solution(reduced, max_degree):
    if max_degree == 0:
        print("No solution.")
    elif max_degree == -1:
        print("Any real number is a solution.")
    elif max_degree == 1:
        solve_first_degree(reduced)
    elif max_degree == 2:
        cal_roots(reduced[2], reduced[1], reduced[0])
    else: 
        print("The polynomial degree is strictly greater than 2, I can't solve.")

def solve_first_degree(reduced):
    print(f"X = {-reduced[0]} / {reduced[1]}")
    print(f"The solution is:\n{ utils.fmt_solution(-reduced[0] / reduced[1]) }")

def cal_roots(a, b, c):
  if a == 0:
    if b == 0:
      return ["Any number is a solution"]
    return [c/b]
  d = get_discriminant(a, b, c)
  print(f"Discriminant: {b}^2 - 4 * {a} * {c} = {d}")
  if d == 0:
    print(f"X = {-b} / (2 * {a})")
    print("Discriminant is zero, the unique solution is:")
    print(f"{utils.fmt_solution(-b/(2*a))}")

  elif d > 0:
    print("Discriminant is strictly positive, the two solutions are:")
    print(f"X_1 = {-b} - sqrt({d}) / {2*a}")
    print(f"{utils.fmt_solution((-b-utils.get_sqrt(d))/(2 * a))}\n")
    print(f"X_2 = {-b} + sqrt({d}) / {2*a}")
    print(f"{utils.fmt_solution((-b+utils.get_sqrt(d))/(2 * a))}")

  else:
    print("Discriminant is strictly negative, the two complex solutions are:")
    print(f"X_1 = {-b} - i * sqrt({-d})/{2*a}")
    print(f"{utils.fmt_solution((-b-utils.sqrt(d))/(2 * a))}\n")
    print(f"X_2 = {-b} + i * sqrt({-d})/{2*a}")
    print(f"{utils.fmt_solution((-b+utils.sqrt(d))/(2 * a))}")


def solve(a1, b1, c1, a2, b2, c2):
  return cal_roots(a1-a2, b1-b2, c1-c2)