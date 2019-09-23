# EE5434 Assignment 1 - PLA-Learning-Algorithm
#### Name: Sin Bo Chi
#### Student Number: 54412731

### Target
  - Implement the PLA learning algorithm (using Python) and analyze its performance using different training sets

### Programs
  - DataEmit.py : Generate the training data
  - PLA.py : Output the learned weight and plot graph using PLA Algorithm

### Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
  - Python - Download & Install Python. Version: Python 2.7.15 (default, Jan 12 2019, 21:07:57)
  - Git(Optional) - Download & Install Git. MacOSX and Linux machines typically have this already installed.
  - Runtime Environment - Terminal in MacOSX

### Clone the files to local computer
```sh
$ git clone https://github.com/alexsbc303/PLA-Learning-Algorithm.git
```

### Run the programs 
Run DataEmit.py
```sh
$ cd PLA-Learning-Algorithm
$ python DataEmit.py [5,2,3] 10 10
```
Run PLA.py (after generating data by DataEmit.py)
```sh
$ cd PLA-Learning-Algorithm
$ python PLA.py train.txt
```

### How to read the graph
  - X-axis - x1
  - Y-axis - x2
  - Black line - Random generated line
  - Purple line - Final PLA line
