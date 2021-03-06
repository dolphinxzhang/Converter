#Converter.py
#Cindy Zhang, Crystal Zhu, Joyce Yuan
#January 21st 2019

def DecimalToBinary(decimal):
  """
  Converts a decimal number entered by user
  into the corresponding binary number.

  decimal: type string
  return: type string
  """
  result_list= [ ] #binary list
  
  remainder= int(number) % 2 #the remainder is what we want
  result_list. append(remainder) #shifts the result list the right way
  quotient = int(number) / 2
    
  while quotient != 0:
    remainder = quotient % 2
    quotient = quotient / 2
    result_list. append(remainder) #reads the list backwards
  
  print result_list
  
  result= ' '
  for i in result_list:
    result=str(i) + result #gives the binary number
  
  return result



def BinaryToDecimal(binary):
    """
    Converts a binary number entered by user
    into the corresponding decimal number.

    binary: type string

    return: type string

    """
    
  
    sum=0
    

    for i in range(len(number)):   #iterates through every position of the string
      if number[i] =='1': #if "1" is found on this position 
        power= len(number)-1-i 
        sum = sum + 2**(power) #let 2 take the power of that "1"'s position and add up all the powers of 2 according to the postiion of "1" in the string  
      else: #if "0" is found
        pass #add nothing 
    
    results=str(sum) #return results in the form of a string 
    
    return results

    
    

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
