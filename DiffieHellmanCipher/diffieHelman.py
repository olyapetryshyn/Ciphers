from random import randint


def get_primary_root(p):
    for i in range(p):
        if is_primary_root(p, i):
            return i
    return None


def is_primary_root(p, a):
    if a == 0 or a == 1:
        return False
    last = 1
    my_set = set()
    for i in range(p-1):
        last = (last * a) % p
        if last in my_set:
            return False
        my_set.add(last)
    return True


def is_prime(p):
    if p % 2 == 0 or p == 1:
        return False
    for i in range(3, p, 2):
        if p % i == 0:
            return False
        return True


def generate_rand():
    return randint(3000, 23000)


def generate(a, p, rand):
    result = (a ** rand) % p
    return result


def main():
    p = 0
    while not is_prime(p):
        p = int(input("p: "))

    a = get_primary_root(p)
    if a == None:
        print("a is not found!")

    print(f"p = {p} \ta = {a}")
    print()

    print("A generates x, sends to B")
    x = generate_rand()
    X = generate(a, p, x)
    print("B generated y, sends to A")
    y = generate_rand()
    Y = generate(a, p, y)

    print("A calculates k")
    k1 = (Y ** x) % p
    print("B calculates k")
    k2 = (X ** y) % p

    print(f"x: {x} - y: {y}")
    print(f"X: {X} - Y: {Y}")
    print(f"k1: {k1} - k2: {k2}")


main()

