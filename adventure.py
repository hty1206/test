import time
t = 1.5

''' intro_1.txt
ans1 = input("\"Adam actually has a special identity. Do you want to know?\"(yes/no)")
'''

print("")

if ans1 in "no":
    # identity_No_2.txt
    time.sleep(t)

'''identity_Yes_2.txt & identity_No_2.txt
print("""\"What people don't know is that Adam is actually a vampire, 
hiding among humans with great wealth.\"\n""")

time.sleep(t)

input("(press enter to continue)\n")

print("\"One night, after staying late at the school library, Jenny accidentally falls down the stairs\"\n")

time.sleep(t)

ans2 = input("\"Adam, do you want to save her? (yes/no)\"")
'''
print("")

while True:
    if ans2 in "yes":
        # Save or not_Yes_3.txt      
        time.sleep(t)
    else:
        # Save or not_No_4.txt

        time.sleep(t)

        ans4 = input("\"Adam, do you want to change her perception of you and pursue her? (yes/no)\"")

        print("")

        if ans4 in "yes": # Save or not_No_4_01.txt
            '''
            ans2 = "y"
            print("(Yes, I want to save her)\n")
            continue
            '''
        else: # Save or not_No_4_02.txt
            '''
            print("The two will have no further interaction and become strangers.")
            print("(The story ends.)")
            break
            '''
    
    ''' Save or not_Yes_3.txt
    print("However, Jenny's father is a very traditional man who could never accept the existence of a \"non-human\" being. \nThe financial pressures on her family also make it hard for Jenny to pursue her own happiness.\n")
    '''

    time.sleep(t)

    ans3 = input("Father: \"Adam, if you want to pursue my daughter, are you willing to agree to one of three conditions?\" (yes/no)")
    if ans3 in "yes":
        # Agree Condition or not_Yes_5.txt
        while True:
            ans5 = input("Please answer 1,2 or 3:")
            print("")
            if ans5 == "1":
                print("(I will give up your chance at immortality and become an ordinary human.)") # Agree Condition or not_Yes_5_01.txt
                break
            elif ans5 == "2":
                print("(I will sever all ties with your family)") # Agree Condition or not_Yes_5_02.txt
                break
            elif ans5 == "3":
                print("(I will become a vegetarian from now on.)") # Agree Condition or not_Yes_5_03.txt
                break
            else:
                print("Please type again") # Agree Condition or not_Yes_5_other.txt
                continue

        time.sleep(t)

    else:
        # Agree Condition or not_No_6.txt
        break

    print("\nFather: Very well, you've earned the chance to propose to my daughter.\n")
    print("\"Adam, thrilled, prepares a \"??\" layers diamond ring, ready to propose...\"")

    while True:
        layer = int(input("How many layers you want the diamond to be?(At least 4 layers)"))
        if layer >= 4:
            top = (layer-3)*2+1
            print(" " + "*"*top)
            for i in range(layer-1):    
                print(" "*i+"*"*(top+2-i*2))
            break
        else:
            print("\nThat's too small!! Please input again!") # dimond(<4).txt

    if layer >= 7:
        print("Wow, this diamond is so big and beautiful!") # dimond(>=7).txt
    else :
        print("It's too small. Are you poor?") # # dimond(4-6).txt

    time.sleep(t)

    print("From then on, the two lived happily ever after.")







    break