print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
	quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
	print('Correct!')
else:
	print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer == "read only memory":
	print('Correct!')
else:
	print("Incorrect!")

answer = input("What does RAM stand for?")
if answer == "read access memory":
	print('Correct!')
else:
	print("Incorrect!")
