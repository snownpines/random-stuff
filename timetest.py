# The purpose here is to compare execution speed
# for different functions solving the same problem.


from timeit import default_timer as timer
from sys import argv

script, y = argv

z = int(y)

# My (and many others) solution to a codewars.com exercise
def multiple(x):
    
    if x%15 == 0:
        return "BangBoom"
    elif x%3 == 0:
        return "Bang"
    elif x%5 == 0:
        return "Boom"
    else:
        return "Miss"

# Some other guy on codewars.com's solution
def multipel(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'

start = timer()
multiple(z)
end = timer()

strat = timer()
multipel(z)
edn = timer()

print("My function: {} seconds".format(end-start))
print("Other's function: {} seconds".format(edn-strat))
