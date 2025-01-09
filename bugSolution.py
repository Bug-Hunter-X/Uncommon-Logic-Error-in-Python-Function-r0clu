def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b != 0:
        return a / b
    else:
        return "Undefined"

result = function_with_uncommon_error(5, 0)
print(result) # Output: 5
result = function_with_uncommon_error(5, 2)
print(result) # Output: 2.5
result = function_with_uncommon_error(0,2)
print(result) # Output: 2
result = function_with_uncommon_error(0,0)
print(result) # Output: 0