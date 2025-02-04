want_insructions = input("Do you want to see the instructions? ").lower()

# check the user says yes / no
if want_insructions == "yes" or want_insructions == "y":
    print("you said yes")
elif want_insructions == "no" or want_insructions== "n":
    print("you said no")
else:
    print("please enter yes / no")


