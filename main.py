import math
def is_superprime(n: int) -> bool:
    ok = 1
    while ok == 1 and n != 0:
        nr = 0
        for j in range(2, int(n // 2)):
            if n % j == 0:
                nr = nr + 1
        if nr > 0:
            ok = 0
        else:
            n = n / 10
    return ok


def test_is_superprime():
    assert is_superprime(30) is False
    assert is_superprime(233) is True
    assert is_superprime(333) is True


def get_largest_prime_below(n):
    ok = 0
    if n < 2:
        return False
    else:
        while ok == 0:
            nr = 0
            for j in range(2, n// 2):
                if n % j == 0:
                    nr = nr + 1
            if nr == 0:
                ok = 1
            else:
                n = n - 1
    return n


def test_get_largest_prime_below():
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(2) == 2
    assert get_largest_prime_below(17) == 13


def get_perfect_squares(a: int, b: int):
    for i in range(a, b):
        if math.sqrt(i) == int(math.sqrt(i)):
            print(i)
            print(" ")


def test_get_perfect_squares():
    assert get_perfect_squares(1, 10)
    assert get_perfect_squares(2, 5)
    assert get_perfect_squares(6, 20)


def main():
    test_is_superprime()
    test_get_largest_prime_below()
    test_get_perfect_squares()

main()
