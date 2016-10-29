import Interpreter

BF1 = Interpreter.BF()

command = ""
line = ""

while True:
    line = input()
    if line:
        command += line
    else:
        break


BF1.compile(command)

#print("\n\n"+str(BF.data))