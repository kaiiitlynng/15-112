
# set rows, cols
# M = []
# splitlines
# split within each -> list 
# command = index
# if command is follow:
# first user = index
# second user = index
# if first user not in M or second user not in M:
# user[first user][second user] = True
# elif command is unfollow:
# first user = index
# second user = index
# if first user not in M or second user in M: 
# user[first][second] = False
# elif command is deactivate:
# user = index - int
# for row in rnage(rows):
# if row == user: set L[row] = False
# for col in range(cols):
# if col == user: set L[row][col] = False
# M.append(user)

####

def decode(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += char
    return result

print(decode('aBcDeF'))


####
def interleave(L):
    rows, cols = len(L), len(L[0])
    M = [0] * (rows * cols)
    i = 0
    for col in range(cols):
        for row in range(rows):
            M[i] = M[i] + L[row][col]
            i += 1
    return M

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(interleave(L))

####
def nthPalindromicPrime(n):
    found = 0
    guess = 0
    
    while found <= n:
        guess += 1
        if isPalindromicPrime(guess):
            found += 1
    return guess

def isPalindromicPrime(n):
    return isPrime(n) and isPalindromic(n)

def isPrime(n):
    if n < 2: return False
    for factor in range(2, n):
        if n % factor == 0: return False
    return True

def isPalindromic(n):
    if n <= 9: return True
    split = int(digitCount(n) / 2)
    n = str(n)
    firstHalf = n[:split]
    secondHalf = n[split:]
    secondHalf = secondHalf[::-1]
    return firstHalf == secondHalf
    
def digitCount(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(nthPalindromicPrime(5))
######
def shortenLongRuns(L, k):
    count = 1
    i = 0
    
    while i < len(L):
        if i == len(L) - 1:
            break
        
        curr = L[i]
        next = L[i + 1]
        if curr == next:
            count += 1
            if count >= k:
                L.pop(i)
            else:
                i += 1
        else:
            count = 1
            i += 1

L = [2, 3, 5, 5, 5, 3]
shortenLongRuns(L, 2)
print(L)

L = [-1, -1, -1, 3, 5, 5, 5, 5]
shortenLongRuns(L, 3)
print(L)

L = [2, 3, 5, 5, 5, 3]
shortenLongRuns(L, 3)
print(L)
###########
def makeTable(n):
    L = [[1] * n for i in range(n)]
    rows, cols = len(L), len(L[0])
    
    i = 1
    for row in range(rows):
        L[row][0] = i
        i += 1
       
    for row in range(rows):
        for col in range(cols):
            value = L[row][0] * (col+1)
            L[row][col] = value
    return L
    
print(makeTable(2))

    
            
        
    