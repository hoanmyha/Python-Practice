def main():
    date = input('Enter a date in mm/dd/yyyy format: ')
    that_date = date.split('/')
    that_date = ''.join(that_date)
    print(f'{date} is {that_date[2:4]}-{that_date[:2]}-{that_date[-2:]}')
main()