import os

from gaem import rulette

def main():
    print("welcome to russian rulette. do you want to play?")
    cmd = input("> ")
    if cmd == "yes":
        rulette()
    else:
        print("ok")

if os.geteuid()==0:
  main()
else:
  print("no root no gaem")






