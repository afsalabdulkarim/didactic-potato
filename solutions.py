def biggest(l):
    # Problem 1
    a = max(l)
    return a

def average(l):
    # Problem 2
    n = len(l)
    sum = 0
    for i in range(0,n) :
        sum = sum + l[i]
    avg = sum/n
    return avg

def longest(s):
    # Problem 3
    lon = 0
    for i in s :
        if len(i)>lon :
            lon = len(i)
            wor = i
    return wor

def first_space(l):
    # Problem 4
    for i in l :
        if " " in i :
            wor = i
            break
    return wor        

def freq(s):
    # Problem 5
    fre = dict()
    for i in s :
        if i in fre:
            fre[i] += 1
        else :
            fre[i] = 1
    return fre

def panagram(s):
    # Problem 6
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet :
        if letter not in s.lower() :
            return False
    return True

def abbreviate(s):
    # Problem 7
    a = ""
    b = s.split()
    for i in b :
        if i.istitle() :
            a = a + i[0]
    return a

def split(amount, denominations):
    # Problem 8
    deno = dict()
    for i in denominations :
        if int(amount/i) > 0 :
            deno[i] = int(amount/i)
        amount = amount%i
    return deno

