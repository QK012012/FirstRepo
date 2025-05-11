import random

num_list = []
def fill():
  global num_list
  for x in range(10):
    num_list.append(random.randint(0,10))
  print(num_list)

fill()