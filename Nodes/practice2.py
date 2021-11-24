from customSingleLinkedList import CustomSingleLinkedList

words = CustomSingleLinkedList()
words.append('egg')
words.append('ham')
words.append('span')
current = words.tail

print("+++++++++++++++++++++++++++")
print("Size:", words.depth())

print("Print words 1:")
while current:
    print(current.data)
    current = current.next

print("+++++++++++++++++++++++++++")
print("Size:", words.depth())

print("Print words 2:")
for word in words.iter():
    print(word)

print("+++++++++++++++++++++++++++")
print("Search results:")
print(words.search('spam'))
print(words.search('juice'))

words.clear()

print("+++++++++++++++++++++++++++")
print("Print words 3:")
while current:
    print(current.data)
    current = current.next
