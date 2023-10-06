from cmu_cs3_utils import rounded

def gradeAverages(grades):
    result = ''
    
    for line in grades.splitlines():
        name = line[:line.find(',')]
        scores = line[line.find(',')+1:] #should be + not -
        
        #sum, count intialized here 
        sum = 0
        count = 0
        
        for grade in scores.split(','):
            count += 1
            number = grade[grade.find(' '):]
            sum += int(number)
            
        #average should be after for loop
        average = rounded(sum/count)
        
        #new line should be in quotes
        result += name + ', ' + str(average) + '\n'
    result = result.strip()
    return result
    
grades1 = '''Jimothy, 80, 50, 80
Chee, 99, 100, 102, 91
Jackie, 105
Bundt, 32, 50, 73, 84, 80'''

grades2 = '''Jimothy, 0
Chee, 99'''

grades3 = '''Wilfred, 0, 10, 90
Wobbston, 95
Wiggles, 95, 90'''

print(gradeAverages(grades1))
print(gradeAverages(grades2))
print(gradeAverages(grades3))