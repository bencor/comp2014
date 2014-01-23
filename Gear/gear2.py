from fractions import Fraction, gcd
 
gears = map(int, raw_input().split())
 
ratios = [Fraction(1)]*len(gears)
for i in xrange(1, len(gears)):
    ratios[i] = Fraction(ratios[i-1]*gears[i-1], gears[i])

print reduce(gcd, ratios).denominator