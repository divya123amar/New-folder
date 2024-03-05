import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)
plt.hist(data,bins=30,color='blue',edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

categories=['Category A','Category B','Category C','Category D','Category E']
values=[25,40,30,20,35]
plt.bar(categories,values,color='green',edgecolor='black')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()