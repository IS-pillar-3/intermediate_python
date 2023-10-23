
def primes(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes:
        # Is n prime?
        if not any(n%i==0 for i in p):
            p.append(n)
        n += 1
    return p
