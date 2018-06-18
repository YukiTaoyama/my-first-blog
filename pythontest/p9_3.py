import matplotlib.pyplot as plt
steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
colorlist = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33']
positions = range(1, num_bars+1)
plt.bar(positions, steps, color = ["r","g","b"] ,align='center')
plt.xticks(positions, labels)
plt.ylabel('Steps')
plt.xlabel('Day')
plt.title('Number of steps walked')
plt.show()
