answer = input ("Welcome to the geography quiz! do you want to play?")
if answer == " yes":
   print("let's continue, type ion the correct answert. remeber to use capital letters")
   
else:
    print("let's play")

myguess = input("what is the capital city of China?")
print("you said", myguess)
if myguess == "Beijing":
     print("that is correct")
else:
     print("wrong. the answer was Beijing")

myguess2 = input("what is the tallest mountain in the world called?")
print("you said", myguess2)
if myguess2 == "Mount Everest":
     print("that is correct")
if myguess2 == "Mt Everest":
     print("that is correct")
else: 
     print("that is wrong. the answer was Mount Everest?")

print("level 2- these questions will be harder")

myguess3 = input("What is the largest ocean in the world")
print("you said", myguess3)
if myguess3 == "Pacific":
     print("that is correct")
if myguess3 == ("Pacific"):
     print("that is correct")
if myguess3 == "The Pacific":
     print("that is correct")

else: print("that is wrong. the correct answer was Pacific")

myguess4 = input("what is the largest city in the world by population?")
print("you said", myguess4)
if myguess4 == "Tokyo":
     print("That is correct.")
else: print("That is wrong. the correct answer was Tokyo")

print("level 3- this is the hardest. good luck!")

myguess6 = input("what country is the city of Baku in?")
if myguess == "Azerbaijan":
     print("that is correct. good job")
else: print("that is wrong. the correct answer was Azerbaijan")


myguess5 =input("a megacity is defined as a city with more than how many people?")
if myguess5 == "10 million":
     print("that is correct")
if myguess5 == "10,000,000":
     print("that is correct")
else: print(" a clue?")
clue = input("type help for a clue")
if clue == "help":
     print(" it is more than 5 million")
else: print("ok") 

myguess7 = input("guess again")
if myguess7 == "10 million":
     print(" that is correct. well done")
else: print("that is wrong. the correct answer is 10 million")

print("that is the end of the quiz. i hope you had fun! :->")
print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
