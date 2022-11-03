array = [2, [3, 4], 5]

def arr_sum(arr):
    ans = 0
    for val in arr:
        if isinstance(val, list):
            ans += arr_sum(val)
        else:
            ans += val
    return ans

def factorial(num):
    if(num == 1):
        return 1
    else:
        return num + factorial(num-1)

def power_series(num):
    if(num == 0):
        return 1
    return 1/pow(3,num) + power_series(num-1)


print(power_series(5))

