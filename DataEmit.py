import numpy as np
import argparse
import random as rand
import matplotlib.pyplot as plt

# input: python DataEmit.py [5,2,3] 4 5

# Initialixation
data_list = []
finish = False

# Arguments Parser
parser = argparse.ArgumentParser(description='Generate training data, output to txt file')
parser.add_argument("w", help="3D Vector")
parser.add_argument("m", type=int, help="Number of positive signs")
parser.add_argument("n", type=int, help="Number of negative signs")
args = parser.parse_args()
# print(args)

# Get w0 w1 w2 from input w 
w = args.w.strip('[')
w = w.strip(']')
w = w.split(',')
w0, w1, w2 = w
w0 = int(w0)
w1 = int(w1)
w2 = int(w2)

# Get number of positive and negative signs from input m and n
m = args.m
n = args.n

# Generate data 
while not finish: 
  x1 = round(rand.uniform(-100,100), 2)
  x2 = round(rand.uniform(-100,100), 2)  
  sign = x1*w1 + x2*w2 + w0
  if sign > 0 and m > 0:
    sign = '+'
    m -= 1
    data_list.append([x1,x2,'+'])
  elif sign < 0 and n > 0:
    sign = '-'
    n -= 1
    data_list.append([x1,x2,'-'])
  elif m == 0 and n == 0: 
      finish = True
# print(data_list)

# Save data to train.txt
savepath = "train.txt"
with open(savepath, 'w') as f:
    for item in data_list:
        f.write("%s\t%s\t%s\n" % (item[0], item[1], item[2])) 
