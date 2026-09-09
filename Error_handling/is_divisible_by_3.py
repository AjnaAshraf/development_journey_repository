def is_divisible_by_3(num):
    result = True
    if num%3 == 0:

        result = True

    else:

        result = False

    return result

assert is_divisible_by_3(9)==True,"test case 1 failed"
assert is_divisible_by_3(10)==False,"test case 2 failed"
assert is_divisible_by_3(14)==False,"test case 3 failed"
assert is_divisible_by_3(15)==True,"test case 4 failed"