def main():

    number = int(input('Enter your number: '))
    pnumber = number + 1
    while True:
        prime = True
        for i in range (2, int(pnumber ** 0.5) + 1):
            if pnumber % i == 0:
                prime = False
                break
        if prime:
            break
        pnumber += 1
    
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
