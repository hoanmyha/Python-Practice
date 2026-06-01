"""
Name(s): Mackenzie and My
CSC 201
Lab7

This program randomly generates arithmetic problems to quiz a student.
All of the problems use only whole numbers. A progress bar shows the
student's progress when taking the quiz. The number of problems the
student answered correctly and the student's percentage is displayed
when the quiz is completed.

Did you complete this lab file during the class period (yes or no)? no

If no, leave the one that applies. If yes, delete this entire section!
    
    I completed grades.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:

"""

from problem import QuizProblem
from progress_bar import ProgressBar
from button import Button
import time
from graphics2 import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
NUM_PROBLEMS = 10

def setUp():
    """
    Create the window and gives directions.
    
    Returns:
    window created to use in the quiz
    """
    window = GraphWin("Arthimetic quiz", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    directions = Text(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/4), f"You'll be given {NUM_PROBLEMS} problems.\n\n"
                                                                "Enter the answer in the box and click submit.")
    goOnText = Text(Point(WINDOW_WIDTH/2, 3 *WINDOW_HEIGHT/4), "Click to continue")
    directions.setSize(18)
    directions.draw(window)
    goOnText.draw(window)
    window.getMouse()
    directions.undraw()
    goOnText.undraw()
    return window

def displayProblem(window, problem):
    """
    displays the problem and and entry box for the answer
    
    Params:
    window (GraphWin): window displaying the quiz
    problem (QuizProblem): the problem that will be displayed
    
    Returns:
    the Text object displaying the problem and the Entry object for the answer as a tuple
    """
    questionString = problem.getQuestionString()
    offset = len(questionString) * 5
    problemText = Text(Point(WINDOW_WIDTH/2 - offset, WINDOW_HEIGHT/5), questionString)
    problemText.setSize(18)
    problemText.draw(window)
    answerBox = Entry(Point(WINDOW_WIDTH/2 + offset + 20, WINDOW_HEIGHT/5), 3)
    answerBox.setSize(18)
    answerBox.setText('')
    answerBox.draw(window)
    return (problemText, answerBox)

def getStudentAnswer(window, answerBox, submit):
    """
    requires the user to enter a whole number for the answer.
    
    Params:
    window (GraphWin): the window displaying the quiz
    answerBox (Entry): the Entry object which the answer is entered in
    submit (Button): the button clicked to submit an answer
    
    Returns:
    the answer entered in the answer box when it is finally a whole number
    """
    click = window.getMouse()
    while not submit.isClicked(click):
        click = window.getMouse()
    studentAnswer = answerBox.getText()
    while not studentAnswer.isdigit():
        error = Text(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), "Try again")
        error.draw(window)
        time.sleep(1)
        error.undraw()
        answerBox.setText('')
        click = window.getMouse()
        while not submit.isClicked(click):
            click = window.getMouse()
        studentAnswer = answerBox.getText()
    return int(studentAnswer)

def report(window, numCorrect):
    """
    Displays the number of problems answered correctly and the percent correct
    
    Params:
    window (GraphWin): the window displaying the quiz
    numCorrect (int): the number of problems answered correctly.
    """
    reportText = f'{numCorrect} correct out of {NUM_PROBLEMS} problems'
    text = Text(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2), reportText)
    text.setSize(24)
    text.draw(window)
    percentText = f'{round(100 *(numCorrect/NUM_PROBLEMS))}%'
    percent = Text(Point(WINDOW_WIDTH/2, 3 * WINDOW_HEIGHT / 4), percentText)
    percent.setSize(24)
    percent.draw(window)
    
    
            
def main():
    #set up the window and the submit button
    window = setUp()
    submit = Button(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/3), 100, 30, "Submit")
    submit.activate()
    submit.draw(window)

    # Create a ProgressBar object and draw it in the window
    quizbar = ProgressBar(Point(250, 300), 300, 40, 'black')
    quizbar.draw(window)
    
    
    # display the quiz problems comparing the user's answer with the correct one
    numCorrect = 0
    for count in range(NUM_PROBLEMS):
        problem = QuizProblem(10) # new random problem using numbers 0...10
        problemText, answerBox = displayProblem(window, problem)
        
        studentAnswer = getStudentAnswer(window, answerBox, submit)
       
        if studentAnswer == problem.getAnswer():
            numCorrect = numCorrect + 1 
    
        problemText.undraw()
        answerBox.undraw()
        
        #compute percent completed and update ProgressBar
        newPercent = ((count + 1) / NUM_PROBLEMS) * 100
        quizbar.update(window, newPercent)
        
        
    submit.undraw()
    
    # undraw the ProgressBar
    quizbar.undraw()
    
    report(window, numCorrect)
    
    time.sleep(3)
    window.close()
      
main()