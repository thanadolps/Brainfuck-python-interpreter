class BF:
    
    data = [0]
    index= 0
    
    def _extendTo(self,index):
        while index >= len(self.data):
            self.data.append(0)
    
    def add(self):
        self.data[self.index] += 1
    def subtract(self):
        self.data[self.index] -= 1
    def right(self):
        if self.index + 1 >= len(self.data):
            self.data.append(0)
        self.index += 1
    def left(self):
        self.index -= 1
    
    def findMatch(self,index,command):
        c = 0
        for i in range(index,len(command)):
            t = command[i]
            if t == '[':
                c += 1
            if t == ']':
                if c == 1:
                    return i
                else:
                    c -= 1
        
    def compile(self,command):
        i = 0
        while i < len(command):
            t = command[i]
            if t == '+' :
                self.add()
            if t == '-' :
                self.subtract()
            if t == '>' :
                self.right()
            if t == '<' :
                self.left()
            if t == '[' :
                k = self.findMatch(i,command)
                while self.data[self.index] != 0 :
                    self.compile(command[i+1:k])
                i = k
            if t == ',' :
                self.data[self.index] = ord(input())
            if t == '.' :
                print(chr(self.data[self.index]),end='')
                
                
            i += 1
            
BF1 = BF()

command = ""
line = ""

while True:
    line = input()
    if line:
        command += line
    else:
        break


BF1.compile(command)

print("\n\n"+str(BF.data))
        
