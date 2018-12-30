from math import log
 

def getDigit(num, base, digit_num):
    return (num // base ** digit_num) % base  

def makeBlanks(size):
    return [ [] for i in range(size) ]  

def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        buckets[getDigit(num, base, digit_num)].append(num)  

    return buckets

def merge(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)

    return new_list
 
def maxAbs(a_list):
    return max(abs(num) for num in a_list)
 
def split_by_sign(a_list):
    buckets = [[], []]
    for num in a_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)

    return buckets
 
def radixSort(a_list, base=10):
    passes = int(round(log(maxAbs(a_list), base)) + 1) 
    new_list = list(a_list)
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))

    return merge(split_by_sign(new_list))