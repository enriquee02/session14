def cook():
    print("I'm making sushi")
    
def is_prime(n):
    """
    checks if n is prime
    :param n: number to check
    :return: true if prime, false otherwise
    """
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("testing my function")
    assert is_prime(5) is True, "Error in function 5 is prime" #more powerful than ==
    assert is_prime(6) is False, "Error in function 6 is not prime"
    assert is_prime(7) is True, "Error in function 7 is prime"
    #print(is_prime(5))
    #print(is_prime(7))
    #print(is_prime(9))
    #print(is_prime(11))
    #print(is_prime(15))
    #print(is_prime(18))