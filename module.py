###
import math

print("-----p119-----")
a = math.pow(2, 3)
print("2 ^ 3 =", a)


###
print("-----p120-----")
import random
b = random.randint(0, 100)
print("rondomint =", b)


###
print("-----p120-----")
import statistics

#mean
nums = [1, 5, 33, 12, 46, 33, 2]
c = statistics.mean(nums)

#median
d = statistics.median(nums)

#mode
e = statistics.mode(nums)

print("mean =", c)
print("median =", d)
print("mode =", e)