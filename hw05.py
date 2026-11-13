"""
Name: (Diane Okong'o)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""
 
def get_letter():
    
    while True:
        x = (input("Give an single uppercase letter: "))
        if len(x) != 1: #evaluate length first of string
            print(f"Error: it needs to be a single character.")
            continue
        elif x != "A" and x !="B" and x !="C": #evaluate character to match one of these
            print(f"Error: You provided the wrong character.")
            continue
        #I do not need to print return or continue here because, I typed in the input again. If it passes this it goes onto the next criteria.
        else:
            return x #returns value x to the main
        

def get_digit():
    while True:
        y = (input("Give an single number character: "))
        if not y.isdigit(): #method isdigit checks if the string y is a digit
            print(f"Error: your input should be only digits.")
            continue
        digits = ["1","2","3"]
        if y not in digits: #list shows which digits are allowed to be input. By putting each one in quotations it means that those digits are considered individually.
            print("Error: a single digit needs to be in [1,3].")
            continue
        else:
            return y


def check_pattern(letter, digit, lst):
    print("Strings with the pattern: ")#must type this out before doing loop 
    for element in lst:# first element in list st_list
        for pos in range(len(element)):#iterates each postion in the length of the element
            if letter == element[pos]: #found letter!
                for idx in range(pos + 1, len(element)):
                    if digit == element[idx]:
                        print(element, end=" ")
                        #This was the nested loop which is made with for and if statements. The indentation below each if statement indicates that if the statement above is true the code in the indented libne directly belwo should run. Also in for statements the word after for does not need to inherently mean anything to python it could be idx, element, bread whatever you want! 
    
            
#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""
    
    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    #while loop in the main ensures that all functions are run in this order.
    while True:
        letter = get_letter()
        digits = get_digit()
        check_pattern(letter, digits, st_list)   
        
        m = (input("\nTry again? (y/n): "))
        if m.lower() != "y":
            break
        
    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("\nThe End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()