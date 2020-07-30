import matplotlib.pyplot as plt

def show(weight):
  x_list = [0, 1, 2, 3]
  y_list = []
  for i in x_list:
    y = (weight[0] * i) / weight[1]
    y_list.append(y)

  print(x_list, y_list)
  plt.plot(x_list, y_list)
  plt.show()
