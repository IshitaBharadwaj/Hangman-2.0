import cs50
import random

'''def random_line(txt_file):
    lines = open(txt_file).read().splitlines()
    word2= random.choice(lines)
    txt_file.close()
    return word2
'''

def main():

    flag=0
    name = input("What is your name? \n")
    print("HELLO "+ name)

    text = input("Type in the Genre for playing Hangman : \n Movies|Countries|Food|General Words: \n " )
    text = text.lower() + ".txt"
    with open(text) as txt_file:
        #word=random_line(txt_file)
        file = open(text)
        lines = [line.strip() for line in file]
        #lines = open(txt_file).read().splitlines()
        word= random.choice(lines).lower()
        print(word)
        word1= [0]*len(word)
        print("Guess the word! :")
        print(word1)
        tries=7
        while True:
            x= input("Enter an alphabet:")
            flag=0
            for j in range(len(word)):
                if word[j]== x:
                    word1[j]=x
                    flag=1
                else:
                    continue
            if flag==0:
                tries-=1
                print("You have " + str(tries) + " tries left!")

            if tries == 0:
                print("Sorry, you lost and Game Over! ")
                print("The word is: "+ word.upper())
                break

            if flag ==1:
                print(word1)
            if tries!=0 and word1==word:
                print("CONGRATULATIONS!")

if __name__ == "__main__":
    main()
