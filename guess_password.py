
import random
import sys
#sys.setExecutionLimit(60000) # 60 seconds
my_password = "abcd"
guess_num = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
done = False
while not done:

    guessed_pw = ""
    # your code here
    guess_num = guess_num+1
    i0 = random.randint(0, 25)
    i1 = random.randint(0, 25)
    i2= random.randint(0, 25)
    i3 = random.randint(0, 25)
    guessed_pw = alphabet[i0]+alphabet[i1]+alphabet[i2]+alphabet[i3]

    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True
