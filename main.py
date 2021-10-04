import math
def is_superprime(n) -> bool:
    ok = 1
    x = int(n)
    while ok == 1 and x != 0:
        nr = 0
        for j in range(2, int(x//2)):
            if x % j == 0:
                nr = nr + 1
        if nr > 0:
            ok = 0
        else:
            x = x/10
    return bool(ok)

def test_is_superprime():
        assert is_superprime(30) is False
        assert is_superprime(233) is True
        assert is_superprime(333) is True

def get_largest_prime_below(n):

    x = int(n)
    ok = 0
    if n < 2:
        return False
    else:
        while ok == 0:
            nr = 0
            for j in range (2, int(x//2)):
                if x % j == 0:
                    nr = nr + 1
            if nr == 0:
                ok = 1
            else:
                x = x-1
    return x

def test_get_largest_prime_below():
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(2) == 2
    assert get_largest_prime_below(17) == 13

def get_perfect_squares(a, b):
    x = int(a)
    y = int(b)
    for i in range(x, y):
        if math.sqrt(i) == int(math.sqrt(i)):
            print(i + " ")

def test_get_perfect_squares():
    assert get_perfect_squares(1, 10)
    assert get_perfect_squares(2, 5)
    assert get_perfect_squares(6, 20)
def main():
    test_is_superprime()
    test_get_largest_prime_below()
    test_get_perfect_squares()
