file_path = 'input.txt'
nums=[]
# Reading all lines into a list
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        nums.append(line.strip())

# Convert numbers to characters and join them into a string
ascii_string = ''.join(chr(int(num)) for num in nums)

print(ascii_string)
