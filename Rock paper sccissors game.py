import random
randno= random.randint(1,3)
if randno==1:
    comp="r"
elif randno==2:
    comp="s"
elif randno==3:
    comp="p"
def gamewin(comp,you):
    if comp==you:
        return print("its a tie")
    if (comp== "r" and you=="s") or (comp=="p" and you=="r") or (comp=="s" and you=="p"):
         return print("you lose")
    elif (comp=="s" and you=="r") or (comp=="p" and you=="s") or (comp=="r" and you=="p"):
        return print("you won!")


you=input("to play the game choose (r) for rock, (s) for scissors, (p) for paper")
print(f"comp chose {comp}")
print(f"you chose {you}")
s=gamewin(comp,you)

