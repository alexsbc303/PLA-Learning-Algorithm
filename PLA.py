import numpy as np
import argparse
import random as rand
import matplotlib.pyplot as plt

# Initialization
x_list = []
y_list = []
sign_list = []
data_load = []
done = False

# Generate initial random line with black colour
w0 = rand.randint(-10,10)
w1 = rand.randint(-10,10)
w2 = rand.randint(1,10)
x = np.linspace(-100,100,100)
y = -(w1/w2) * x + -(w0/w2)
plt.xlabel('x1')
plt.ylabel('x2')
plt.plot(x,y,'-k')

# Load data from txt file
parser = argparse.ArgumentParser(description='Input txt file')
parser.add_argument("input", help="txt file")
args = parser.parse_args()
i = args.input
fid = open(i)
lines = fid.readlines()
for line in lines:
    line = line.strip('\n')
    line_split = line.split('\t')
    data_load.append([float(line_split[0]), float(line_split[1]), str(line_split[2])]) 
# print(data_load)

# Plot positive and negative points onto the diagram 
for data in data_load:
	x_list.append(data[0])
	y_list.append(data[1])
	sign_list.append(data[2])
  	if data[2] == '+':
		plt.scatter(data[0], data[1], c = 'b', marker = 'o')
  	else:
		plt.scatter(data[0], data[1], c = 'r', marker = 'x')

# PLA algorithm
while not done:
	for i in range(len(sign_list)):
		# Get temp sign in every cycle
		if (w1 * x_list[i] + w2 * y_list[i] + w0) > 0:
			tempsign = '+'
		elif (w1 * x_list[i] + w2 * y_list[i] + w0) < 0:
			tempsign = '-'
		else:
			i = 0
			break
		
		# Wt+1 <- Wt + Yn(t) * Xn(t)
		if tempsign != sign_list[i]:
			if sign_list[i] == '+':
				tempsign_num = 1
			else:
				tempsign_num = -1
			w0 += tempsign_num
			w1 += tempsign_num * x_list[i]
			w2 += tempsign_num * y_list[i]
			i = 0
			break

		# done loop when a full cycle of no mistakes 
		if i == len(sign_list) - 1:
			done = True

# Generate finalised line with purple colour
y = -(w1/w2) * x + -(w0/w2)
plt.plot(x,y,'-m')

# Print vector and plot graph
print(w0,w1,w2)
plt.show()