### Assignment Shipping calculator
### Author: Raiden Borunda

print('=================\n Shipping Calculator\n=================')

cont = 'y'
while cont == 'y' :
    ## Gather user input for cost
    costItems = float(input('Cost of items ordered: '))

    ## Verify user input was a positive integer
    while True : 
        if costItems < 0 :
            costItems = float(input('You must enter a positive number. Please try again: '))
        else :
            break

    ## Shipping cost base on User's item cost
    if costItems < 30 :
        shipCost = 5.95
    elif costItems >= 30.00 and costItems <= 49.99 :
        shipCost = 7.95
    elif costItems >= 50.00 and costItems <= 74.99 :
        shipCost = 9.95
    else :
        shipCost = 0

    ## Add Cost + Shipping Cost
    print('Shipping cost: ' + str(shipCost))
    print('Total cost: ' + str(round((float(costItems) + float(shipCost)), 2)))

    ## Restart Option
    cont = input('\nContinue? (y/n)')

print('Thank you for using the Shipping Calculator!')


