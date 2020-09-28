import time
import pickle


def dweeb(x):
	return(int(bin(x)[2:]))

def flagwrap():
  y = dweeb(65), dweeb(115), dweeb(116), dweeb(114), dweeb(97),dweeb(102),dweeb(116),dweeb(119)
  return("HAC{",y,"}")

def friends():
	print("Bonsoir") #opening challenges
	time.sleep(2)
	print("welcome to my challenge")
	time.sleep(2)
	print("I hope you like")
	time.sleep(2)
	user = input("Greetings....")
	if user == "hi":
		print("hello! So simple to crack isn't it?")
		print("Here's your flag")
		print("HAC{lol}")
		return
	else:
		pickle_out = open("flag.pict","wb")
		pickle.dump(flagwrap(), pickle_out)
		pickle_out.close()
		print("Check the directory you copied this to ;)")
		extra = input("Anything else I can do for you?")
		if extra == "y":
			input("What is it then?")
			print("sorry I can't do that, have you tried holding a pickle?")
		else:
			time.sleep(2)
			print("Okay, don't forget to hold the pickle.")
			


friends()
