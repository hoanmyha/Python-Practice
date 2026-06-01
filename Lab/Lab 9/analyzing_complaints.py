'''
Name(s): My Ha
CSC 201
Lab 9

This program provides a menu of options analyzing the complaints from the
Consumer Financial Protection Bureau's Consumer Complaint Database. The user
chooses from a menu to:
    1) Look up the number of complaints for a particular company
    2) Look up the number of complaints in a particular state
    3) Look up the number of complaints in a particular month
    4) Display the top N companies based on the number of complaints
    5) Display the top N states based on the number of complaints
    
If completed after class document assistance:


'''
import csv

DATA_FILE_NAME = 'consumer_complaints_2018.csv'
MAX_MENU_CHOICE = 6

VALID_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

VALID_MONTHS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def makeComplaintList():
    '''
    Makes a list of complaints using data from the Consumer Financial Protection
    Bureau's Consumer Complaint Database. Each complaint is a dictionary mapping
    from a complaint part to this complaint's value for that part.
    
   
    Returns:
    list of complaints where each complaint is a dictionary
    '''
    # DON'T MODIFY THIS FUNCTION!    
    complaints = []
    with open(DATA_FILE_NAME, mode='r', encoding='cp1252') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            dictVersion = dict(row)
            complaints.append(dictVersion)
            
    return complaints

def lookUpCompany(complaintList):
    '''
    Prompts user to enter a company name and prints the number of complaints for that company
    
    Params:
    complaintList (list): list of complaints where each complaint is a dictionary
    '''
    # TODO: ADD YOUR CODE HERE
    num_complaint = 0
    company = input('Enter company name: ')
    for complaint in complaintList:
        if complaint['Company'] == company:
            num_complaint = num_complaint + 1
    
    if num_complaint == 0:
        print(f'{company} not in list')
    else:
        print(f'{num_complaint} complaints')
        
   
def lookUpState(complaintList):
    '''
    Prompts user to enter a state abbreviation and prints the number of complaints for that state
    
    Params:
    complaintList (list): list of complaints where each complaint is a dictionary
    '''
    # TODO: ADD YOUR CODE HERE
    num_complaint = 0
    state = input('Enter state abbreviation: ')
    while state not in VALID_STATES:
        print('Invalid. Try again.')
        state = input('Enter state abbreviation: ')
    for complaint in complaintList:
        
        if complaint['State'] == state:
            num_complaint = num_complaint + 1
            
    if num_complaint == 0:
        print(f'{state} had no complaints')
    else:
        print(f'{num_complaint} complaints')    

def lookUpMonth(complaintList):
    '''
    Prompts user to enter a month number and prints the number of complaints for received in that month.
    
    Params:
    complaintList (list): list of complaints where each complaint is a dictionary
    '''
    num_complaint = 0
    month = input('Enter a month number (1-12): ')
    while month not in VALID_MONTHS:
        print('Invalid. Try again. ')
        month = input('Enter a month number (1-12): ')
    for complaint in complaintList:
        monthReceived = complaint['Date received'].split('/')
        if month == monthReceived[0]:
            num_complaint = num_complaint + 1
            
    if num_complaint == 0:
        print(f'No complaints for month {month}')
    else:
        print(f'{num_complaint} complaints') 
            
def printTopN(countsDict, numValues):
    '''
    Prints the top N values in a dictionary with their corresponding keys
    in reverse order from largest to smallest.
    
    Params:
    countsDict (dict): a dictionary with values that are "sortable"
    numValues (int): the number of items to be displayed in the table
    '''
    # DON'T MODIFY THIS FUNCTION!    
    #
    # Note: since list.sort(...) sorts by the 1st item in each tuple first, we
    # make a list of tuples where the count comes first, and the key second.
    savedList = [(count,key) for key,count in countsDict.items()]
    savedList.sort(reverse = True)
    
    for count,key in savedList[:numValues]:
        print(f'{count:7}  {key}')


def printTopCompanies(complaintList):
    '''
    Prompts the user for the number of companies they want displayed in the
    table and prints a table with the companies having the most complaints.
    
    Params:
    complaintList (list): list of complaints where each complaint is a dictionary
    '''  
    
    numberOfCompany = int(input('How many companies do you want to see? '))
    while numberOfCompany <= 0:
        print('Invalid. Try again.')
        numberOfCompany = int(input("How many companies do you want to see? "))

    mostComplaintDict = {}
    for complaint in complaintList:
        if complaint['Company'] in mostComplaintDict.keys():
            num_complaint = mostComplaintDict[complaint['Company']]
            num_complaint = num_complaint + 1
            mostComplaintDict[complaint['Company']] = num_complaint
        else:
            mostComplaintDict[complaint['Company']] = 1
        
    print()    
    print('Companies with the most complaints: ')
    printTopN(mostComplaintDict, numberOfCompany)

def printTopStates(complaintList):
    '''
    Prompts the user for the number of states they want displayed in the
    table and prints a table with the states having the most complaints.
    
    Params:
    complaintList (list): list of complaints where each complaint is a dictionary
    ''' 
    # TODO: ADD YOUR CODE HERE
    pass
    
         
def printMenu():
    ''' Prints menu of choices '''
    print('Choose from the following options\n')
    print('1  Get number of complaints for one company')
    print('2  Get number of complaints for one state')
    print('3  Get number of complaints for one month')
    print("4  Get companies with most complaints")
    print('5  Get states with most complaints')
    print('6  Quit')
    print()

def getMenuChoice():
    '''
    gets valid menu choice from the user

    Returns:
    valid menu choice (str)
    '''
    choice = input('Enter choice: ')
    while not choice.isdigit() or int(choice) < 1 or int(choice) > MAX_MENU_CHOICE:
        print('Invalid. Try again')
        choice = input('Enter choice: ')
    return int(choice)

def main():
    complaintList = makeComplaintList() # Each element is a dictionary
    
    printMenu()
    choice = getMenuChoice()
    print()
    while choice != MAX_MENU_CHOICE:
        if choice == 1:
            lookUpCompany(complaintList)
        elif choice == 2:
            lookUpState(complaintList)
        elif choice == 3:
            lookUpMonth(complaintList)           
        elif choice == 4:
            printTopCompanies(complaintList)
        else:
            printTopStates(complaintList)

        input("\nPress ENTER to return to the menu.\n")
        printMenu()
        choice = getMenuChoice()
        print()
    
if __name__ == '__main__':
    main()
        
        