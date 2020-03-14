#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:01:58 2020

@author: natnem
"""

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def stacksize(self):
        return len(self.items)
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        top = self.items.pop()
        return top
    def peek(self):
        return self.items[self.stacksize() - 1]
    def push(self,item):
        self.items.append(item) 
    def stack(self):
        return self.items
    

#mystack = Stack()
#mystack.push("cat")
#mystack.push("dog")
#mystack.push("yay")
#print(mystack.stack())
#print(mystack.peek())
#mystack.pop()
#mystack.pop()
#mystack.pop()
#mystack.pop()
#print(mystack.stack())


def ReverseString(mystring): #using a stack
    mystack = Stack()
    for i in mystring:
        mystack.push(i)
    print(mystack.stack())
    
    reverse = ''
    for k in range(len(mystring)):
        reverse += mystack.pop()
    return reverse

print(ReverseString("ABCDEF"))


def BaseConvertion(dec , base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while dec > 0:
        rem = dec % base
        s.push(rem)
        dec = dec//base
        print(rem, dec, s.stack())
    b = ""
    while not s.isEmpty():
        b += (digits[s.pop()])
    return b
print(BaseConvertion(233,8))
    


def ParCheckerGeneral(symbol): 
    mystack = Stack()
    opens = "({["
    closes = ")}]"
    for i in symbol:
        if i in  "({[":
            mystack.push(i)
            print(i)
        else:
            print(i)
            if mystack.isEmpty() and symbol[symbol.index(i):] != "":
                return False
            else:
                top = mystack.pop()
                if opens.index(top) != closes.index(i):
                    return False
    
    if mystack.stack() == []:
        return True
    else: return False
    
print(ParCheckerGeneral('[{()}]'))



#INPUT THE INFIX EXPRESSION AS A STRING SEPARATED BY SPACES
def InfixToPostfix(infixExp): 
    s = Stack()
    infixList = infixExp.split(" ")
    OutputList = []
#    operator  = "*/+-"
    operand  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    precedence = {"*":3, "/":3 , "+":2 , "-":2, "(":1}
    
    for token in infixList:
        if token in operand:
            OutputList.append(token)
        elif token == "(" :
            s.push(token)
        elif token == ")" :
            while not s.isEmpty():
                top = s.pop()
                if top =="(" :
                    break
                else:
                    OutputList.append(top)
        else:
            if s.isEmpty():
                s.push(token)
            else:
                opr = s.peek()
                if precedence[opr] >= precedence[token]:
                    OutputList.append(opr)
                    s.pop()
                    s.push(token)
                else:
                    s.push(token)
    
    while not s.isEmpty():
        t = s.pop()
        OutputList.append(t)
    
    return "".join(OutputList)
INFIX = "( 5 * 2 ) - 2"
print(InfixToPostfix(INFIX))

def  PostfixEvaluation(infix):
    result = Stack()
    postfix = InfixToPostfix(infix)
    
    for token in postfix:
        if token not in "*/+-":
            result.push(int(token))
        else:
            opr1 = result.pop()
            opr2 = result.pop()
            if token == "*":
                result.push(opr2 * opr1)
            elif token == "/":
                result.push(opr2/opr1)
            elif token == "+":
                result.push(opr2+opr1)
            else:
                result.push(opr2-opr1)
    
    return result.peek()


print(PostfixEvaluation(INFIX))             

        
    
        
    
                
        
            
            
    
    




        
    