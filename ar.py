input_data = open('input.txt', 'r') 
data = input_data.read()
data = data.split
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
k = 0
for x in range(-100,100):
    if (d + x * (c + x * (b + a * x)) == 0):
output_data = open('output.txt', 'w')
output_data.write(str(k))
input_data.close()
output_data.close()