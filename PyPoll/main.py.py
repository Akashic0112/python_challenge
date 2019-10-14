#!/usr/bin/env python
# coding: utf-8

# In[1]:


#VOTE COUNTING
import csv


# In[2]:


file = open("election_data.csv")


# In[3]:


file_reader = csv.reader(file, delimiter=",")


# In[4]:


#print....
header = next(file_reader)
print(header)


# In[5]:


voter_count = 0
county_l = []
candidates = []
voter_id = []
#voter_count = sum(0 in row for file_reader)


# In[6]:


candidate_and_votes = {}


# In[ ]:





# In[7]:


for row in file_reader:
    voter_count = voter_count + 1
#     voter_id.append(row[0])
#     county = row[1]
    candidate_name = row[2]
    if candidate_name not in candidates:
        candidates.append(candidate_name)
        candidate_and_votes[candidate_name] = 1
    candidate_and_votes[candidate_name] += 1


# In[ ]:





# In[8]:


print(candidates)


# In[9]:


print(candidate_and_votes)


# In[10]:


output_file = open("output.txt", "w")


# In[11]:


output_file.write(f"Election Results \n")
print(f"Election Results")
output_file.write(f"------------------- \n")
print(f"-------------------")
output_file.write(f"Total Votes: {voter_count} \n")
print(f"Total Votes: {voter_count}")
output_file.write(f"------------------- \n")
print(f"-------------------")

winner = ""
winner_count = 0 
for key in candidate_and_votes:
    votes_per_candidate = candidate_and_votes[key]
    percentage = (votes_per_candidate / voter_count)*100
    output_file.write(f"{key}: {percentage:.3f}% ({votes_per_candidate}) \n")
    print(f"{key}: {percentage:.3f}% ({votes_per_candidate}) \n")
    if votes_per_candidate > winner_count:
        winner_count = votes_per_candidate
        winner = key
        
output_file.write(f"------------------- \n")
print(f"------------------- ")
output_file.write(f"Winner: {winner}   \n")
print(f"Winner: {winner}")
output_file.write(f"------------------- \n")  
print(f"-------------------")


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


output_file.close()


# In[ ]:




