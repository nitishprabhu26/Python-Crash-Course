print(2**3)

def raise_to_power(base_num, power_num):
    return base_num**power_num
    # or
    result = 1
    for index in range(power_num):
        result=result*base_num
    return result

print(raise_to_power(3,4))