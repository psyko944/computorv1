📟 Computor v1: Polynomial Equation Solver
---
The program must be able to solve polynomial equations of the second degree or lower.

🐍 Technologies Used
---
Python 3	Chosen for its clarity and strong string manipulation capabilities, ideal for parsing and reducing the polynomial expression.


🧠 Reminder
---
Solve Second Degree Equation (Quadratic): $$aX^2 +bX+c=0$$ (where a !=0)

discriminant (Δ = $$b^2 - 4ac$$)
<br>
<br>
<br>
Two Distinct Real Solutions (Δ>0)
<br>
<br>
|  $$X_{1} = \frac{-b + \sqrt{\Delta}}{2a}$$ | $$X_{2} = \frac{-b - \sqrt{\Delta}}{2a}$$ |
<br>
<br>
One Unique Real Solution (Δ=0)\
<br>
| $$X = \frac{-b}{2a}$$ |\
<br>

Two Distinct Complex Solutions (Δ<0)
<br>\
|  $$X_{1} = \frac{-b}{2a} + i \frac{\sqrt{-\Delta}}{2a}$$ |  $$X_{2} = \frac{-b}{2a} - i \frac{\sqrt{-\Delta}}{2a}$$ |

<br>
<br>
<br>
First Degree Equation (Linear): bX+c=0 (where a=0 and b !=0)
<br>
<br>

| $$X = \frac{-c}{b}$$ |

⚙️ Usage
---
python3 computor.py "EQUATION"\
<br>
example:\
python computor.py "5 * X^0 + 4 * X^1- 9.3 * X^2 = 1 * X^0"
<br>
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0\
Polynomial degree: 2\
Discriminant is strictly positive, the two solutions are:
<br>
0.905239\
-0.475131
