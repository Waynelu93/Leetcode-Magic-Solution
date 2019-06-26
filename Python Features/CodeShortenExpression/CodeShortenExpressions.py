# 1. one line for loop
x = [1, 3, 4, 6, 9]
y = [2*a for a in x if a % 2 == 1]

# 2. use any for intersection
characters = ['a','b','h','d']
if any(c in 'hello' for c in characters):
    print("Contains Intersection")

# 3. one line if else
num = 1
print (1 if num == 1 else 2)  # intersection empty?
