#Practical 3
# Stack operations
# some operations with stack
#isEMPTY is a operatio use to check whether the stack is empty or not if it is empty it returns false
def isEMPTY(stack):
    if len(stack) == 0:
        return True
    else:
        return False
print("")   #........space
print("")   #........space
def stckPush(stack, item):
    stack.append(item)
    print("--",item, "is inserted")

def stackPop(stack):
    if isEMPTY(stack):
        print("stack is empty")
    else:
        item = stack.pop()
        print("--",item,"is poped/removed")

def stackDisplay(stack):
    if isEMPTY(stack):
        print("-- stack is empty.")
    else:
        print("-- stack elemnets :",stack)

def stackTop(stack):
    if isEmpty(stack):
        print("-- stack is empty.")
    else:
        return stack[-1]

stack = []
#print("stack initially")
print(">>>IT CEHCKS WHETHER THE STACK IS EMPTY OR NOT ")
print("stack initially",stackDisplay(stack))
print("")   #........space
print("")   #........space

print(">>> PUSH OPERATION IS USED TO INSERT ELEMNET IN THE STACK")
stckPush(stack,10)
stckPush(stack,50)
print("")   #........space
print("")   #........space
print(">>> stackDisplay IS USE TO DIAPLAY AVALIABLE ELEMENTS IN THE STACK ")
stackDisplay(stack)
print("")#.....space
print("")#.....space
print(">>> POP OPERATION IS USED TO DELETE SOME ELEMENT FROM THE STACK ")
stackPop(stack)
