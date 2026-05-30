"""
Name(s): My Ha, Anh Le
CSC 201
Lab6

grades reads data for a multiple choice exam from a file, scores
each exam, computes statistics for the exam, and scales the
exam if desired by the user. The stats are displayed in the console
window, while each student's score is written to a file.

Did you complete this lab file during the class period (yes or no)? No

If no, leave the one that applies. If yes, delete this entire section!
    I completed grades.py without my partner from class.

"""

import os

def getFileToRead():
    """
    Prompts the user to enter the file name until valid and opens the file for reading
    Returns:
        the file variable connected to the data file
        the name of the file without the extension
    """
    infileName = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
    infileNameWithExtension = infileName + '.txt'
    while not os.path.exists(infileNameWithExtension):
        print('File not found. Re-enter file name.')
        infileName = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
        infileNameWithExtension = infileName + '.txt'
    infile = open(infileNameWithExtension, 'r')
    return infile, infileName


def gradeExam(infile):
    """
    Reads through the file to grade each student's exam. The first line of the file
    is the answer key. They remaining lines are each student's answers. The method creates
    two parallel lists: a list of student id numbers and a list of the student's exam scores.
    It also computes the maximum possible exam score
    
    Params:
    infile: the file object connected to the data file
    
    Returns:
    the list of student id numbers
    a parallel list of exam scores for each student
    the maximum possible exam score
    """
    idList = []
    scoreList = []
    
    firstLine = infile.readline()
    firstLine = firstLine.strip()
    keyList = firstLine.split(',')
    keyList = keyList[1:]
    
    # your loop goes here to read through the rest of the file
    for line in infile:
        line = line.strip()
        data = line.split(',')
        studentid = data[0]
        idList.append(studentid)
        answerList = data[1:]
    
        score = 0
        maximumPossibleScore  =len(answerList) * 4
        for answer in range(len(answerList)):
            if keyList[answer] == answerList[answer]:
                score += 4
            elif answerList[answer] != '':
                score -= 1          
        
        scoreList.append(score)  
    
    return idList, scoreList, maximumPossibleScore    


def calculateMedian(scoreList):
    """
    Calculates the median score for the exam
    
    Params:
    scoreList: the list of exam scores (which needs to stay inorder)
    
    Returns:
    the median of the scores
    """
    copiedList = scoreList.copy()
    copiedList.sort()
    length = len(copiedList)
    if length % 2 == 1:
        median = copiedList[(len(copiedList)) // 2]
    elif length % 2 == 0:
        median = (copiedList[(len(copiedList) // 2)] + copiedList[(len(copiedList) // 2 - 1)]) / 2
    return median


def calculateStats(scoreList):
    """
    Calculates the highest score, lowest score, mean score, and median score for the exam
    
    Params:
    scoreList: the list of exam scores (which needs to stay inorder)
    
    Returns:
    the highest score, lowest score, mean score, and median score
    """
    median = calculateMedian(scoreList)
    
    copiedList = scoreList.copy()
    copiedList.sort()
    highest_score = copiedList[-1]
    lowest_score = copiedList[0]
    total = 0
    
    for index in range(len(copiedList)):
        total = total + copiedList[index]
    mean_score = total / len(copiedList)

    return highest_score, lowest_score, mean_score, median
 
def outputSummary(numScores, maximumPossibleScore, highest_score, lowest_score, mean_score, median):
    """
    Outputs a summary of the exam's stats
    
    Params:
    numScores: the number of scored exams
    maxPossibleScore: the maximum score that can be earned on this exam
    max: the highest score
    min: the lowest score
    mean: the arithmetic mean (average) of the exam scores
    median: the median of the exam scores
    
    """
    print('\nGrade Summary')
    print(f'Total students: {numScores}')
    print(f'Maximum possible score: {maximumPossibleScore}')
    print(f'Highest score: {highest_score}')
    print(f'Lowest score: {lowest_score}')
    print(f'Mean score: {mean_score:.2f}')
    print(f'Median score: {median:.2f}')
    print()
    
    
def scaleExam(scoreList, mean_score):
    """
    Prompts the user to determine if the exam will be scaled, and if so, prompt the user
    for the desired mean for the exam. The method modifies the scores by the amount required
    make the mean the desired value.
    
    Params:
    scoreList: the list of exam scores (which needs to stay inorder)
    mean: the arithmetic mean (average) of the current scores
    """
    difference = 0
    scaled_list = []
    
    valid_input = ['y', 'n']
    answer = input("Would you like to scale the exam? 'y' or 'n': ")
    answer = answer.lower()
    while answer not in valid_input:
        print("Invalid input. Enter 'y' or 'n'.")
        answer = input("Would you like to scale the exam? 'y' or 'n': ")
        answer = answer.lower()
       
    if answer == 'y':
        desired_mean = float(input(f'Enter desired mean: '))
        while desired_mean <= mean_score:
            print("Invalid input. That wouldn't raise the scores.")
            desired_mean = float(input(f'Enter desired mean: '))
    
        difference = desired_mean - mean_score
    
        for index in range(len(scoreList)):
            scaled_score = scoreList[index] + difference
            scaled_list.append(scaled_score)
        return scaled_list
      
    elif answer == 'n':
        return scoreList
    
def createResultsFile(idList, scaled_list, infileName):
    """
    Writes the exam data to a file. Each file of the file is the student's id
    followed by their score.
    
    Params:
    idList: the list of student ids
    scoreList: a parallel list of exam scores for each student
    infileName: the name of the data file without the extension
    """ 
    outFileName = infileName + '_grades.txt' 
    outFile = open(outFileName, 'w')
    for index in range(len(idList)):
        outFile.write(f'{idList[index]},{scaled_list[index]:.2f}\n')
    outFile.close()
    print(f'Check file {outFileName} for student scores!')


def main():
    infile, infileName = getFileToRead()
    idList, scoreList, maximumPossibleScore = gradeExam(infile)
    print(idList)
    print(scoreList)
    
    highest_score, lowest_score, mean_score, median = calculateStats(scoreList)
    
    numScores = len(idList)
    outputSummary(numScores, maximumPossibleScore, highest_score, lowest_score, mean_score, median)
    
    scaled_list = scaleExam(scoreList, mean_score)
    #print(scaled_list)
    
    createResultsFile(idList, scaled_list, infileName)
main()