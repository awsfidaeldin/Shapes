import matplotlib.pyplot as plt
sales=[5000,3044,8294,5986,4950,9323,7566]
days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
plt.bar(days,sales)
plt.title('Plot for displaying the Weekly Sales')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.show()