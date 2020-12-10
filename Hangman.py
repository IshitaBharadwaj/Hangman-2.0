import cs50
import random

already= []
def main():

    flag=0
    name = input("What is your name? \n")
    print("HELLO "+ name)

    text = input("Type in the Genre for playing Hangman: \nMovies|Countries|Food|General Words: " )
    print()
    if text.lower()== "general words":
        print("check")
        text= "generalwords"
    text = text.lower() + ".txt"
    with open(text) as txt_file:
        #word=random_line(txt_file)
        file = open(text)
        lines = [line.strip() for line in file]
        #lines = open(txt_file).read().splitlines()
        word= random.choice(lines).lower()
        #print(word)
        word1= ['_']*len(word)
        word_og=['_']*len(word)
        for i in range(len(word)):
            word_og[i]=word[i]
            if word[i] == '.' or word[i] == ' ' or word[i] == ':' or word[i] == ',' or word[i] == '\'' or word[i] == '!' or word[i] == '&' or word[i] == '-':
                word1[i]= word[i]

        print("Guess the word! :")
        for i in range(len(word1)):
            print(word1[i] + " ", end=" ")
        print()
        tries=7
        while True:
            x= input("Enter an alphabet:")
            if x in already:
                print("You have already entered this alphabet!")
                continue
            else:
                already.append(x)
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
                    for i in range(len(word1)):
                        print(word1[i],end=" ")
                    print()

                if tries == 0:
                    print("Sorry, you lost and Game Over! ")
                    print("The word is: "+ word.upper())
                    break

                if flag ==1:
                    for i in range(len(word1)):
                        print(word1[i],end=" ")
                    print()
                if tries!=0 and word1==word_og:
                    print()
                    print("CONGRATULATIONS!")
                    print("Game Over!!! You won!!!")
                    break

if __name__ == "__main__":
    main()
