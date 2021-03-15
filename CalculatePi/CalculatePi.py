import random
import math
import statistics

results = []
numRolls = 10000
numSets = 50
i = 1
t = 1 
actualPi = 3.141592653589793

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

while t <= numSets:
    x = 0
    pi = 0
    isTrue = 0
    isFalse = 0
    i = 1
    while i <= numRolls:
        if is_coprime(random.randint(0,9999), random.randint(0,9999)):
            isTrue += 1
        #print("Yeah")
        else:
            isFalse += 1
        #print("Nah")
        i += 1
    print("Set", t, "|| Amount True:", isTrue, "| Amount False:", isFalse)
    x = 6 / (isTrue / numRolls)
    # print(x)
    pi = math.sqrt(x)
    print("Rough Pi estimate", pi)
    
    results.append(pi)
    t += 1
    
print("===========================================")
print("| Averaged Pi Estimate: |", round(statistics.mean(results), 12)," |")
print("===========================================")
print("| Over/Under Pi by:     |", round(100 - ((statistics.mean(results) / actualPi) * 100), 10), "% |")
print("===========================================")