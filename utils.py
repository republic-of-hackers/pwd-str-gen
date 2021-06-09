from constants import CAPITAL_ALPHA, SMALL_ALPHA, DIGITs, SPECIAL_CHAR
import random

'''
    @Description - It handles the input for the driver program.
    @Returns - Integer, Integer
'''
def inputHandler():

    total_len_string = None
    shuffle_depth = None

    try:
        total_len_string = int(input("Enter length of password string to be : "))
        temp_input = input("Enter shuffle depth (i.e. times string get shuffled press {Enter} to set default as 10) : ")
    except TypeError:
        print("Length must be of Integer Type. Try Again.")
    except ValueError:
        print("Please use the Integer Value Type. Try Again.")
    
    if(temp_input.strip() == ''):
        shuffle_depth = 10
    else:
        try:
            shuffle_depth = int(temp_input)
        except ValueError:
            print("Please use the Integer Value Type for shuffle depth paramter. Try Again.")
    
    if(shuffle_depth != None and total_len_string != None):
        return total_len_string, shuffle_depth

'''
    @Description - It partitions the required string length of password.
    @Returns - Integer, Integer
'''
def stringLengthPartitioner(str_len):
    p = 0
    while p == 0 or p == (str_len-1):
        p = random.randint(1, str_len-1)
    return p, str_len-p

'''
    @Description - It gets the Random Index.
    @Returns - Integer
'''
def getRandomIndex(explicit_range):
    return random.randint(0, explicit_range-1)

'''
    @Description - It shuffles the given list according to given repeat times.
    @Returns -  void
'''
def shufflePassword(arr, repeat):
    for i in range(repeat):
        random.shuffle(arr)

'''
    @Description - It generates the password string.
    @Return - string
'''
def generatePasswordString(total_str_len, shuffle_depth):
    
    part1, part2 = stringLengthPartitioner(total_str_len)
    
    CAP_ALPHA = list(CAPITAL_ALPHA)
    SML_ALPHA = list(SMALL_ALPHA)
    DGTS = list(DIGITs)
    SPL_CHAR = list(SPECIAL_CHAR)
    
    temp_result = []

    for i in range(part1//2):
        temp_result.append(CAP_ALPHA[getRandomIndex(explicit_range=len(CAPITAL_ALPHA))])
        temp_result.append(SML_ALPHA[getRandomIndex(explicit_range=len(SMALL_ALPHA))])
    
    for i in range(part2//2):
        temp_result.append(DGTS[getRandomIndex(explicit_range=len(DIGITs))])
        temp_result.append(SPL_CHAR[getRandomIndex(explicit_range=len(SPECIAL_CHAR))])
    
    shufflePassword(temp_result, shuffle_depth)
    return ''.join(temp_result)