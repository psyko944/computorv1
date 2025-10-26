from fractions import Fraction

class cpx:
  real = 0
  imag = 0
  def __init__(self, r, i):
    self.real = r
    self.imag = i
  def __add__(self, p: int):
    return cpx(self.real + p, self.imag)
  def __add__(self, p):
    return cpx(self.real + p.real, self.imag + p.imag)
  def __radd__(self, n:int):
    return cpx(n + self.real, self.imag)

  def __sub__(self, p:int):
    return cpx(self.real - p, self.imag)
  def __sub__(self, p):
    return cpx(self.real - p.real, self.imag - p.imag)
  def __rsub__(self, n: int):
    return cpx(n - self.real, -self.imag)

  def __mul__(self, p: int):
    return cpx(self.real * p, self.imag * p)
  def __mul__(self, p):
    return cpx(
      self.real * p.real - self.imag * p.imag,
      self.real * p.imag + self.imag * p.real
    )
  def __rmul__(self, n: int):
    return cpx(self.real * n, self.imag * n)

  def __truediv__(self, p: int):
    return (cpx(
      self.real / p,
      self.imag / p
    ))
  def __truediv__(self, p):
    div = p.real*p.real + p.imag*p.imag
    return (cpx(
      (self.real * p.real + self.imag * p.imag) / div,
      (self.imag * p.real - self.real * p.imag) / div
    ))

  def __str__(self):
    return f"{self.real}{'' if self.imag <= 0 else '+'}{str(self.imag) + 'i' if self.imag else ''}"


def get_sqrt(n):
	if n < 0:
		raise ValueError("Cannot compute square root of negative number.")
	if n == 0 or n == 1: return n
	TOLERANCE = 0.0000001
	x = n / 2.0
	while True:
		root = 0.5 * (x + (n / x))
		if abs(root - x) < TOLERANCE:
			return root
		x = root

def sqrt(n: int) -> cpx:
  if n >= 0:
    return (cpx(get_sqrt(n), 0))
  return cpx(0, get_sqrt(-n))

def get_discriminant(a, b, c):
	return b*b - 4*a*c

def get_max_degree(lhs, rhs):
   return max(x.exponent for x in (lhs + rhs))

def fmt_num(n):
   return f"{float(n):.6f}".rstrip('0').rstrip('.')

def fmt_solution(equation):
    LIMIT_DENOMINATOR = 1000
    TOLERANCE = 1e-9
    if not isinstance(equation, cpx):
        try:
           f = Fraction(equation).limit_denominator(LIMIT_DENOMINATOR)
           if abs(equation - float(f)) > TOLERANCE:
                return fmt_num(equation)
        except OverflowError:
            return fmt_num(equation)
        if f.denominator == 1:
            return str(f.numerator)
        return f"{f.numerator}/{f.denominator}"
    else:
        re = equation.real
        im = equation.imag
        re_str = fmt_solution(re) if re != 0 else ''
        im_str = fmt_solution(abs(im))
        im_fraction = im_str.split('/')
        im_str = im_str+'i' if len(im_fraction) == 1 else f"{im_fraction[0]}i/{im_fraction[1]}"
        sign = '+' if im <= 0 else '-'
        if not re_str:
            return f"{'-' if im > 0 else ''}{im_str}"
        return f"{re_str} {sign} {im_str}"