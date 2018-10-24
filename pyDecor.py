def repeat(n):
	def fake_func(true_func):
		def repeater(argument):
			result = argument
			for counter in range(n):
				result = true_func(argument)
				argument = result
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
