#!/usr/bin/env python
# coding: utf-8

# In[107]:


import csv


# In[108]:


file = open("budget_data.csv")


# In[109]:


#print(file)
#file is an object 
#<_io.TextIOWrapper name='budget_data.csv' mode='r' encoding='UTF-8'>


# In[110]:


file_reader = csv.reader(file, delimiter= ",")


# In[111]:


#print(file_reader)
#<_csv.reader object at 0x105234828>


# In[112]:


header = next(file_reader)
print(header)


# In[113]:


total_months = 0


# In[114]:


net_total_amount = 0 


# In[115]:


change = 0


# In[116]:


changes_l = []


# In[117]:


months_l = []


# In[118]:


for every_row in file_reader:
    total_months = total_months + 1
    #print(total_months)
    ##Error:"unsupported operand type()->Type-casting to change str to int
    net_total_amount = net_total_amount + int(every_row[1])
    #print(net_total_amount)
    #avg of change
    previous = int(every_row[1])
    #print(previous)
    change = previous - change
    #print(change)
    changes_l.append(change)
    months_l.append(every_row[0])


# In[119]:


print(total_months)
print(net_total_amount)


# In[120]:


#len(changes_l)
changes_l.remove(changes_l[0])


# In[121]:


count_of_changes = len(changes_l)
print(count_of_changes)


# In[122]:


sum_changes = 0
for x in changes_l:
    sum_changes =  sum_changes + x 


# In[123]:


avg_of_changes = sum_changes/ count_of_changes
print(avg_of_changes)


# In[124]:


greatest_inc_prof = (max(changes_l))
print(greatest_inc_prof)


# In[125]:


greatest_dcr_loss = (min(changes_l))
print(greatest_dcr_loss)


# In[126]:


greatest_index = changes_l.index(greatest_inc_prof)


# In[127]:


losses_index = changes_l.index(greatest_dcr_loss)


# In[128]:


months_l.remove(months_l[0])


# In[129]:


months_l[greatest_index]


# In[130]:


months_l[losses_index]


# In[131]:


#Creat txt
# your final script should both print the analysis to the terminal and export a text file with the results.

line1 = "Fianalcial Analysis"
line2 = "---------------------"
line3 = "Total Months:"+ str(total_months)
line4 = "(Net)Total: "+ str(net_total_amount)
line5 = "Average Change: "+ str(avg_of_changes)
line6 = "Greatest Increase of Profits: "+ str(months_l[greatest_index])+":  " +  str(greatest_inc_prof)
line7 = "Greatest Decrease of Profits: "+ str(months_l[losses_index])+":  " + str(greatest_dcr_loss) 

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)


# In[132]:



f = open("Analysis.txt", "w")
f.write(line1)
f.write(line2)
f.write(line3)
f.write(line4)
f.write(line5)
f.write(line6)
f.write(line7)
f.close()
file.close()


# In[ ]:




