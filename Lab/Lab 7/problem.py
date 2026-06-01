"""
Name(s): Mackenzie and My
CSC 201
Lab7



    Document Assistance:

"""

import random

class QuizProblem:
    
    OPERATION_LIST = ['+', '-', '*', '/']
    
    """
    This class represents one (randomly generated) problem for
     use in a simple arithmetic quiz.
    Each problem must be generated so that the answers are always
    positive whole numbers (ie. 0, 1, 2, 3, ...)
    
    instance variables:
    operand1 (int): the number left of the operation symbol
    operand2 (int): the number right of the operation symbol
    answer (int): the answer to the problem
    operation (str): the symbol for the operation ('+','-','*', '/')
    """
    def __init__(self, maxRandom):
        self.operation = random.choice(QuizProblem.OPERATION_LIST)
        if self.operation == '+':
            self._randomizeAddition(maxRandom)
        elif self.operation == '-':
            self._randomizeSubraction(maxRandom)
        elif self.operation == '*':
            self._randomizeMultiplication(maxRandom)
        elif self.operation == '/':
            self._randomizeDivision(maxRandom)
            
    def _randomizeAddition(self, maxRandom):
        self.operand1 = random.randrange(maxRandom + 1)
        self.operand2 = random.randrange(maxRandom + 1)
        self.answer = self.operand1 + self.operand2
        
        
    def _randomizeSubraction(self, maxRandom):
        self.operand2 = random.randrange(maxRandom + 1)
        self.answer = random.randrange(maxRandom + 1)
        self.operand1 = self.operand2 + self.answer
    
    def _randomizeMultiplication(self, maxRandom):
        self.operand1 = random.randrange(maxRandom + 1)
        self.operand2 = random.randrange(maxRandom + 1)
        self.answer = self.operand1 * self.operand2
    
    def _randomizeDivision(self, maxRandom):
        self.operand2 = random.randrange(1, maxRandom + 1)
        self.answer = random.randrange(maxRandom + 1)
        self.operand1 = self.operand2 * self.answer
        
    def getAnswer(self):
        return self.answer
    
    def getQuestionString(self):
        return f'{self.operand1} {self.operation} {self.operand2} = '
    
    def __str__(self):
        return f'{self.operand1} {self.operation} {self.operand2} = {self.answer}'



    
def main():
    prob1 = QuizProblem(1)
    print('Question: ', prob1.getQuestionString())
    print('Answer: ', prob1.getAnswer())
    print('Equation:', prob1) #printing prob1 calls the prob1.__str__() method implicitly
    print()
    
    for count in range(25):
        prob = QuizProblem(10)
        print(prob)
        
if __name__ == '__main__':
    main()