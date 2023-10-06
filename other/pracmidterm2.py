# def ct1(s):
#     x = set()
#     y = set()
#     for elem in s:
#         if elem in x:
#             y.add(elem)
#         x.add(elem)
#     print(f"x: {x}")
#     print(f"y: {y}")
    
#     z = {}
#     for i in range(len(s)-len(y)):
#         if s[i] not in z:
#             z[s[i]] = i
#         else:
#             z[i] = z[s[i]]
#     print(f"z: {z}")
# s = 'dodopod'
# ct1(s)

# def ct2(d, key):
#     while (key in d) and ((key+2) not in d):
#         d[key+2] = key+1
#         key = d[key]
#     L = [ ]
#     for key in d:
#         L.append(10*key + d[key])
# # Hint: if we sort L, does it matter the order in which we loop
# # through elements in d?
#     return sorted(L)
# print(ct2({1:5, 0:2}, 0))

# def ct4(L, s=1, depth=1):
#     if L == []:
#         result = 0
#     elif len(L) == 1:
#         result = L[0] * s
#     else:
#         mid = len(L) // 2
#         newS = s if mid % 2 == 0 else -s
#         a = ct4(L[:mid], s, depth+1)
#         b = ct4(L[mid:], newS, depth+1)
#         result = a + b
#     print('*' * depth, result)
#     return result
# L = [15, 112, 10]
# print(ct4(L))

def getCounts(d):
    result = dict()
    for key in d:
        if key not in result:
            result[key] = 1
        else:
            result[key] += 1
    for key in d:
        value = d[key]
        if value not in result:
            result[value] = 1
        else:
            result[value] += 1
    return result
    
def greaterThanAppearances(d):
    #make a counts dict
    #loop through the dict and return the set
    counts = getCounts(d)
    result = set()
    for key in counts:
        value = counts[key]
        if value > abs(key):
            result.add(key)
    return result

class Schedule:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
        self.classList = []
    def getUnits(self):
        units = 0
        for c in self.classList:
            units += c[1]
        return units
    def addClass(self, className, units):
        for c in self.classList:
            if c[0] == className or c[1] == units:
                return self.classList
        self.classList.append([className, units])
    def __str__(self):
        result = f"{self.name}'s {self.semester} Schedule"
        for c in self.classList:
            result += f'\n{c[0]}: {c[1]} units'
        return result
    def __hash__(self):
        return hash(str(self))
    def __eq__(self, other):
        return (isinstance(other, Schedule) and
                set(self.classList) == set(other.classList))
    def removeHardClass(self):
        if self.classList == []:
            return self.classList
        highestClass = None
        highestUnits = None
        for c in self.classList:
            if c[1] > highestUnits:
                highestUnits = c[1]
                highestUnitClass = c
        self.classList.remove(highestUnitClass)

def countGosomi(L):
    if L == []:
        return 0 
    else:
        item = L[0]
        rest = L[1:]
        
        if type(item) == str:
            return item.count('gosomi') + countGosomi(rest)
        elif type(item) == list:
            return countGosomi(item) + countGosomi(rest)
        else:
            return countGosomi(rest)

def reorderRainbow(dict):
    return reorderRainbowHelper(dict, [])

def reorderRainbowHelper(dict, result):
    if len(dict) == 0:
        return result
    else:
        for color in dict:
            if isLegal(dict, color, result):
                result.append(color)
                solution = reorderRainbowHelper(dict, result)
                if solution != None:
                    return solution
                result.remove(color)
        return None

def isLegal(dict, color, result):
    if color in result:
        return False
    for item in result:
        if color not in dict[item]:
            return False
    return True



