import matplotlib.pyplot as plt
#Line Chart Example
x_values=[1,2,3,4,5]
y_valus=[10,12,5,8,15]
plt.plot(x_values,y_values,marker='o',linestyle='-')
plt.title('Line Chart Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()
#Bar Chart Example
categories=['CategoryA','CategoryB','CategoryC','CategoryD','CategoryE']
values=[25,40,30,20,35]
plt.bar(categories,values,color='blue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('values')
plt.show() 