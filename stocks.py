#!/usr/bin/env python
# coding: utf-8

# In[29]:


import csv,os
all_stocks = {}

def get_stocks(input_csv):
    global all_stocks
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            date, stock = (row[0].split('|'))
            if date != 'Date' :
                if date in all_stocks:
                    all_stocks[date].append(stock)
                else :
                    all_stocks[date]=[stock]

def invest_in_stocks():
    for key in (sorted(all_stocks.keys())) :
        all_stocks[key] = sorted(all_stocks[key],key=float)
        #strategy 1
        #strategy 2
                    
for file in os.listdir(os.path.join(os.path.abspath(''),'csv_files')):
    if file.split('.')[-1] == 'csv' :
        get_stocks(os.path.join(os.path.abspath(''),'csv_files',file))

invest_in_stocks()


# In[21]:


import csv,os
print(os.path.abspath(''))
a,b=[1,2]
print(a,b)


# In[ ]:




