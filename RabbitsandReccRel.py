# number of offspring in any month is equal to the number of
# rabbits that were alive two months prior.

# Fn is number of rabbits alive after the nth month
# Fn = Fn-1 + Fn-2

def f(n,k):
    if n >= 3: 
        return f(n-1,k) + (k * f(n-2,k))
    else:
        return 1

print(f(32,2))