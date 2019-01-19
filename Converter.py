def DecimalToBinary(decimal):
    """
    Converts a decimal number entered by user
    into the corresponding binary number.

    decimal: type string

    return: type string

    """
     if decimal >1:
        while int(decimal/2)!=1:
            number = int(decimal/2) + decimal%2
            decimal = int (decimal/2)
                break
    print number
        
        
    return ''
        
    return ''


def BinaryToDecimal(binary):
    """
    Converts a binary number entered by user
    into the corresponding decimal number.

    binary: type string

    return: type string

    """

        
    return ''




if __name__ == '__main__':

    number = raw_input("Enter a decimal number to convert to Binary: ")
    binary = DecimalToBinary(number)

    print
    print 'Entered Decimal: %s' % number
    print 'Binary: %s' % binary
    print
    
    number = raw_input("Enter a binary number to convert to Decimal: ")
    decimal = BinaryToDecimal(number)

    print
    print 'Entered Binary: %s' % number
    print 'Decimal: %s' % decimal
    print
    hahahaha
