#CT1
class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def f(self):
        return self.x + self.y
    def g(self):
        self.x += 2
        return self.f()/10

class B(A):
    def g(self):
        return self.f()*10
    
def ct1(x):
    a = A(x, 2*x)
    print(a.g())
    b = B(x, a.x)
    print(b.g())

ct1(4)

#CT2
def ct2(L):
    if (len(L) == 0):
        return [ ]
    else:
        return [max(L)] + ct2(L[1:-1]) + [min(L)]
print(ct2([1,5,9,5,1]))

#CT3
def ct3(L):
    d = dict()
    print(f(L, d))
    return d

def f(L, d):
    if len(d) >= 3:
        return L
    elif len(L) <= 1:
        return False
    else:
        d[L[0]] = L[1]
        return f(L[1:], d)
print(ct3([15, 1, 1, 2, 'mid', 'two']))

#FRQ1
def findNewValues(dA, dB):
    setA, setB = set(), set()
    for key in dA: #o(n)
        setA.add(dA[key]) #o(1)
    for key in dB: #o(n)
        setB.add(dB[key]) #o(1)
    result = set()
    for value in setB: #o(n)
        if value not in setA: #o(1)
            result.add(value) #o(1)
    return result
            
dA = {'item1': 'a',
 'item2': 'b',
 'item3': 'c'}

dB = {'thing1': 'c',
 'thing2': 'b',
 'thing3': 'cat',
 'thing4': 'dog'}

findNewValues(dA, dB)
findNewValues(dB, dA)

#FRQ2
def gapSum(n):
    n = abs(n)
    if n < 10:
        return 0
    else:
        digit1, digit2 = n//10%10, n%10
        rest = n//10
        return gapSum(rest) + abs(digit1-digit2)

#FRQ3
class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def getTitle(self):
        return self.title

class Book:
    def __init__(self, bTitle, chapters):
        self.bTitle = bTitle
        self.chapters = chapters
    def getChapterCount(self):
        count = 0
        for chapter in self.chapters:
            count += 1
        return count
    def getPageCount(self):
        count = 0
        for chapter in self.chapters:
            count += chapter.pages
        return count
    def getChapter(self, index):
        return self.chapters[index]
    def moveChapter(self, index, book):
        chapters = book.chapters
        chapters.append(self.chapters[index])

#FRQ4
def makeLegalString(s):
    return legalString(s, '')

def legalString(s, result):
    if len(s) <= 1:
        return s
    else:
        for i in range(len(s)):
            nextChr = s[i]
            rest = s[i+1:]
            if isLegal(nextChr, result, s):
                result += nextChr
                solution = legalString(rest, result)
                if solution != None:
                    return solution
                result -= nextChr
        return None

def isLegal(chr, result, s):
    if result == '':
        return True
    else:
        lastChr = result[-1]
        if result not in s and abs(ord(lastChr) - ord(chr)) == 1:
            return False
        return True
    
    



