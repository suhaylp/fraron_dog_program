dog_name = input("enter your dogs name: ")
dog_treats = 0
print ("hello " + dog_name + ". What an epic name! Your dog has " + str(dog_treats) + " treats.")


def dog_command_executor():
    global dog_treats
    dog_command = input("enter a command, either sit or jump, check treats or end game: ")
    if dog_command == "sit":
        print(dog_name + " is sitting")
        dog_treats = dog_treats + 1
        dog_command_executor()
    elif dog_command == 'jump':
        print(dog_name + " is jumping")
        dog_treats = dog_treats + 2
        dog_command_executor()
    elif dog_command == "check treats":
        print("Your dog has " + str(dog_treats) + " treats.")
        dog_command_executor()
    elif dog_command == "end game":
        print("goodbye " + dog_name)

    else:
        print("say either sit or jump")
        dog_command_executor()

dog_command_executor()



