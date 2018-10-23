Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def repeat(n):
	def fake_func(true_func):
		def repeater(argument):
			if n == 0:
				print(argument)
			return argument
			for counter in range(n):
				result = true_func(argument)
				argument = result
			print(result)
			return result
		return repeater
	return fake_func

@repeat(2)
def plus_1(x):
	return x + 1

@repeat(0)
def mul_2(x):
	return x * 2

print(plus_1(3))
print(mul_2(4))
