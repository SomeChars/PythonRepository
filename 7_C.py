def str_base(number, base):
        i = 0
        func_number = number
        sum = ""
        while number % base**i != number:
            i += 1
        i -= 1
        while func_number > base and i >= 0:
            a = int(func_number / base**i)
            func_number -= a*(base**i)
            i -= 1
            if a < 10:
                sum += str(a)
                if i == 0:
                    sum += str(func_number)
            else:
                sum += chr(65 + a - 10)
                if i == 0:
                    sum += chr(65 + func_number - 10)
        return sum
