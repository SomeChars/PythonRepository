Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
   
iterations = 21
   
def my_cos(x):
   partial_sum = 1
   nizhniy_factorial = 1
   x_pow = x
   for n in range(1, iterations):
      nizhniy_factorial *= (2*n-1)*(2*n)
      partial_sum += ((-1)**n)*(x_pow**(2*n))/(nizhniy_factorial))
   return partial_sum
   
print(help(math.cos), math.cos(0.4))
print(help(my_cos), my_cos(0.4))
