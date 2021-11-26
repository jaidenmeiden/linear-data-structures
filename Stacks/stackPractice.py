from stack import Stack

food = Stack()
food.push('egg')
food.push('ham')
food.push('spam')
print("Top: ", food.pop())
print("Top: ", food.pop())
food.clear()
print("Top: ", food.pop())
