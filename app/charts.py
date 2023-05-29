import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  plt.style.use('Solarize_Light2')
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.tight_layout()
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  plt.style.use('bmh')
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.tight_layout()
  plt.savefig('pie.png')
  plt.close()
  
if __name__ == '__main__':
  name = 0
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart(name, labels, values)
  generate_pie_chart(labels, values)
  