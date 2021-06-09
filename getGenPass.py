from utils import inputHandler, stringLengthPartitioner, generatePasswordString
import pyperclip

'''
    Driver Code
'''
def main():
    totalStringLength, shuffleDepth = inputHandler()
    RESULT_STR = generatePasswordString(totalStringLength, shuffleDepth)
    if(RESULT_STR == "" or len(RESULT_STR) < totalStringLength):
        print("Failed to generate password. Try Again.")
    else:
        pyperclip.copy(RESULT_STR)
        print("Generated Password: {0} is copied to clipboard".format(RESULT_STR))


if __name__ == '__main__':
    main()