import math
def printMenu():
    print("1. citire element, iar in cazul optiunii 4,cele doua elemente vor fi cerute dupa apelul optiunii")
    print("2. verifica daca numarul este superprim")
    print("3. cautarea celui mai mare numar prim, mai mic decat cel dat")
    print("4. scrierea patratelor perfecte dintre cele doua numere")
    print("5. iesire")

def is_superprime(n: int):
    '''
    verifica daca numarul este superprim
    :param n: un nr intreg
    :return: returneaza True, daca este superprim si false in caz contrar
    '''
    while n != 0:
        for j in range(2, int(n // 2 + 1)):
            if n % j == 0:
                return False
        else:
            n = n / 10
    return True


def test_is_superprime():
    assert is_superprime(237) is False
    assert is_superprime(331) is True

def get_largest_prime_below(n):
    '''
    returneaza cel mai mare numar prim, mai mic decat cel dat
    :param n: nr intreg
    :return: returneaza cel mai mare numar prim, mai mic decat cel dat
    '''
    ok = 0
    if n < 2:
        return False
    else:
        while True:
            nr = 0
            for j in range(2, n//2 + 1):
                if n % j == 0:
                    nr = nr + 1
            if nr == 0:
                return n
            else:
                n = n - 1


def test_get_largest_prime_below():
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(8) == 7


def get_perfect_squares(a: int, b: int):
    '''

    :param a: primeste un nr. intreg
    :param b: primeste un numar intreg
    :return: returneaza o lista cu toate numerele patrate perfecte din interval
    '''
    l = []
    for i in range(a, b):
        if math.sqrt(i) == int(math.sqrt(i)):
            l.append(i)
    return l



def test_get_perfect_squares():

    assert get_perfect_squares(1, 10) == [1,4,9]
    assert get_perfect_squares(2, 5) == [4]


def main():
    test_is_superprime()
    test_get_largest_prime_below()
    test_get_perfect_squares()
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == '1':
          n = int(input(" n = "))
        elif optiune == '2':
            print(is_superprime(n))
        elif optiune == '3':
            print(get_largest_prime_below(n))
        elif optiune == '4':
            a = int(input("primul numar din interval, a = "))
            b = int(input("al doilea numar din interval, b = "))
            print(get_perfect_squares(a, b))
        elif optiune == '5':
            break
        else:
            print("optiune gresita, reincercati!")

main()
