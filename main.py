

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
    A = "3000000"
    B = "3000000"

    print(karatsuba(A,B))

