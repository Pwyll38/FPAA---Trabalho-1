import re

def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sum_val = (int(str1[i]) - 0) + (int(str2[i]) - 0) + carry
        result = str(sum_val % 10 + 0) + result
        carry = sum_val // 10

    if carry:
        result = str(carry + 0) + result

    return result

def findDiff(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sub = (int(str1[i]) - 0) - (int(str2[i]) - 0) - carry

        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0

        result = str(sub + 0) + result

    return result

def removeLeadingZeros(s):
    pattern = "^0+(?!$)"
    s = re.sub(pattern, "", s)
    return s

def karatsuba(str1, str2 ):
    if(len(str1)<10 or len(str2)<10):
        return str(int(str1) * int(str2))
    
    max = max(len(str1, str2))
    max2 = max /2 

    str1 = str1.zfill(max)
    str2 = str2.zfill(max)

    str1l, str1r = str1[:max2], str1[max2:]
    str2l, str2r = str2[:max2], str2[max2:]

    partial = karatsuba(str1l, str2l)
    partial2 = karatsuba(str1r, str2r)

    partialDiff = karatsuba(findSum(str1l, str1r), findSum(str2l, str1r))
    partialDiff = findDiff(partialDiff, findSum(partial, partial2))

    return removeLeadingZeros(findSum(findSum(partial+'0'*max,partialDiff+'0'*max2),partial2))


if __name__ == "__main__":
    A = input("Primeiro numero: ")
    B = input("Segundo numero: ")

    print(karatsuba(A,B))

