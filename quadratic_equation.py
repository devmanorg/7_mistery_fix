from math import sqrt

def get_roots(a,b,c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2


if __name__ == '__main__':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    root1, root2 = get_roots(a, b, c)
    
    if root1 is None:
        print("root1 =  None ")
    else:
        print("root1 =  %f " % (root1))

    if root2 is None:
        print("root2 =  None " )
    else:
        print("root2 =  %f " % (root2))


