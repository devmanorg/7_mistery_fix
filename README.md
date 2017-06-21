# Quadratic Equations Solver

The script helps to solve Quadratic Equations.

# How to Use

quadratic_eqation.py contains function get_roots(a,b,c) for calculating roots of Quadratic Equation with coefficients: a, b, c.
You can import quadratic_eqation module into your script by:
```bash
import quadratic_eqation.py 
```
You can use the next example to calculating roots of Quadratic Equation in ypour script:
```bash
root1, root2 = get_roots(a, b, c)
# a, b, c - coefficients of Quadratic Equation
```
Function returns 2 roots. If root/roots couldn't be calcalated or not excist, function will return None.

Example of using:
```bash
import quadratic_eqation.py 

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

root1, root2 = quadratic_eqation.get_roots(a, b, c)

if root1 is None:
    print("root1 =  None ")
else:
    print("root1 =  %f " % (root1))

if root2 is None:
    print("root2 =  None " )
else:
    print("root2 =  %f " % (root2))

```


# How to Launch Tests

```bash
python tests.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
