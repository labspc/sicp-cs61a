def sum_digits(n):
    """Return the sum of the digits of positive integers"""
    if n < 10: # base case, when n is a single digit
        return n # sum of digits is the number itself
    else:
        # 元组赋值（tuple unpacking）
        # all_but_last, last = n // 10, n % 10
        
        all_but_last = n // 10  # 202
        last = n % 10 # 4
        return sum_digits(all_but_last) + last

# 计算字符串 "123" 的校验和
checksum = sum_digits(ord("1") + ord("2") + ord("3"))
print(checksum)  

# python recursion.py
# 6
