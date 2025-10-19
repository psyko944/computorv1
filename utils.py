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