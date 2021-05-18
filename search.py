string = input("Type any string to search in and press Enter: ")
word = input("Type any word to search for in the string and press Enter: ")
length = len(word)
index = 0
times = 0
while index < len(string):
  if string[index:index+length] == word:
    times += 1
    index += length
  else:
    index += 1 
print(f"The word was repeated {times} times in the series")