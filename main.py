def main():

    number = int(input('Enter your number: '))
    if number <= 1:
        return False
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        return True
    
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(pnumber)

    ########################################
    # Do not delete the return statement
    ########################################
    return pnumber
##


if __name__ == '__main__':
    main()
