import random
words_INPUTS=["zebra","zerda","zibet","zoril","zorro","yapok","whale","whelp","vison","vixen","urial","urson","tiger","takin","tatou","tigon","tapir","tabby","stoat","swine","sloth","shote","sasin","saiga","steer","sheep","serow","spado","sorel","stirk","skunk","spade","shoat","sabel","sajou","shrew","ratel","royal","rhino","pongo","puppy","panda","pekan","phoca","potto","oribi","otary","ounce","orang","otter","okapi","nagor","nyala","mhorr","morse","moose","manul","mouse","magot","liger","llama","loris","lemur","kyloe","kiang","kaama","kulan","koala","jocko","indri","izard","hinny","horse","hutia","hyena","hyrax","hippo","goral","gayal","genet","grice","gryce","filly","fossa","fitch","felis","equus","eland","daman","dhole","drill","dogie","dingo","coati","chimp","cuddy","camel","crone","coney","civet","coypu","canis","chiru","burro","broke","bison","bobac","bongo","bruin","bitch","bobak","aguti","ariel","addax","ammon"]
words_RESPONSE=["animal"]

#choose random word from the list
guessed_word = random.choice(words_INPUTS)
guessed_word
hint=guessed_word[0]+guessed_word[-1]
hint
store_g_l=[]
try_p=4
a=input("enter your name ")
print("Welcome to the game world",a)
print("We are going to give you 5 attempts for the guessing")
print("Your hint is", words_RESPONSE)
for guess in range(try_p):
    while True:
        letter = input("Guess the letter: ")
        
        if len(letter)==1:
            break
        else:
            print("Oops!Please Guess the letter! ")
    
    if letter in guessed_word:
        print("Yes!")
        store_g_l.append(letter)
    else:
        print("No!")
        
    if guess==3:
        print()
        clue_request = input ("Would you like a hint?")
        if clue_request.lower().startswith("y"):
            print()
            print("Hint: The first and last letter of the word is:", hint)
        else:
            print('You\'re very Confident!')
            
    print()
    print('''Now Let's see what have you guessed so far.You have guessed:''',len(store_g_l),'letters correctly.')
    print('These letters are:', store_g_l)

word_guess=input('Guess the whole word: ')
if word_guess.lower()==guessed_word:
    print('Congrats! You are right')
else:
    print('Sorry! The answer was,',guessed_word)
    
print()
input('Please press Enter to leave the program')
