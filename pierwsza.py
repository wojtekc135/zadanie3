def isPrime(n):
    for i in range(2,n+1):
        if n%i==0:
            return False
    return True
def first_10_primes():
    licznik=0
    n=1
    while liczniik<100:
        n+=1
        if isPrime(n):
            licznik+=1
            print(n)
    
