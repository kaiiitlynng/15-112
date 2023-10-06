#Backtracking
#write fn takes dict mapping ach person to set of their friends
#and as well as integer k -> returns set of k people from dictionary so that 
#all k people are friends with each other

def harmonySet(friendDict, k):
    return harmonySetHelper(friendDict, k, set())

def harmonySetHelper(friendDict, k, setSoFar):
    #base case - check if reached a solution
    if len(setSoFar) == k:
        return setSoFar
    #recursive case
    else:
        #loop through all possible moves from this state
        for person in friendDict: 
            #if move is legal
            if canAdd(friendDict, person, setSoFar):
                #apply move
                setSoFar.add(person)
                #try to recursively solve from new state
                solution = harmonySetHelper(friendDict, k, setSoFar)
                if solution != None:
                    return solution
                #backtrack if mutated 
                setSoFar.remove(person)
        return None

def canAdd(friendDict, person, harmonySet):
    if person in harmonySet:
        return False 
    for friend in harmonySet:
        if person not in friendDict[friend]:
            return False
    return True 

 #OOP
class Channel:
    highestFrequency = 0
    def __init__(self, name, frequency):
        self.name, self.frequency = name, frequency
        Channel.highestFrequency = max(frequency, Channel.highestFrequency)
    
    def __repr__(self):
        return f"Channel {self.name} on {self.frequency}"
    
    def __eq__(self, other):
        return (isinstance(other, Channel) and self. name == other.name
                and self.frequency == other.frequency)

class Radio:
    #class attribute
    mostChannels = None
    def __init__(self, channels, frequency):
        self.channels = channels
        self.frequency = frequency
        #set class attribute 
        if (Radio.mostChannels == None or 
            len(self.channels) > len(Radio.mostChannels.channels)):
            Radio.mostChannels = self
    
    def getCurrentChannel(self):
        for key in self.channels:
            if abs(self.frequency - key) <= 0.05:
                return self.channels[key].name
        return None
    
    def addChannel(self, channel):
        frequency = channel.frequency
        self.channels[frequency] = channel
        #update class attribute 
        if len(self.channels) > len(Radio.mostChannels.channels):
            Radio.mostChannels = self


# wrapper
# use when you need another parameter / extra variable
# need more info -> use wrapper 