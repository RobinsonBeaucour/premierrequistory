def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

file=input('enter a file')
with open(file) as f:
    text=f.read()
print(count_char(text,'r'))
f.close()


