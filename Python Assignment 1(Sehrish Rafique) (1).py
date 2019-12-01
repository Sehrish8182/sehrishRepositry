#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hi I am Sehrish Rafique and I am gonna write here Python List Methods")


# In[3]:


# animals list
animals = ['cat', 'dog', 'rabbit']
print('Animals List',animals)
# 'guinea pig' is appended to the animals list
animals.append('guinea pig')
# Updated animals list
print('Updated animals list: ', animals)


# In[5]:


print("Adding List to a List")
# animals list
animals = ['cat', 'dog', 'rabbit']
# list of wild animals
wild_animals = ['tiger', 'fox']
# appending wild_animals list to the animals list
animals.append(wild_animals)
print('Updated animals list: ', animals)


# In[6]:


# Python program to clear a list 
# using clear() method  
  
# Creating list 
GEEK = [6, 0, 4, 1] 
print('GEEK before clear:', GEEK)  
  
# Clearing list  
GEEK.clear()  
print('GEEK after clear:', GEEK)  


# In[9]:


print("A list can be copied with = operator")
old_list = [1, 2, 3]
new_list = old_list
print('New List:', new_list )
print('Old List:', old_list )


# In[10]:


# Python3 code to count the number of times 
list1 = [1, 1, 1, 2, 3, 2, 1]  
  
# Counts the number of times 1 appears in list1 
print(list1.count(1))  


# In[12]:


print("append in Python")
my_list = ['geeks', 'for'] 
my_list.append('geeks') 
print(my_list) 


# In[13]:


# of list index() method 
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
# Will print the index of '4' in list1 
print(list1.index(4)) 


# In[14]:


print("Inserting Element to List")
# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')

print('Updated List: ', vowel)


# In[16]:


print("Python List pop")
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)
# Updated List
print('Updated List:', languages)


# In[19]:


print("Python List remove")
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
print("Before Remove",animals)
# 'rabbit' is removed
animals.remove('rabbit')
# Updated animals List
print('Updated animals list: ', animals)


# In[21]:


mylist = [1, 2, 3, 4, 5]
print("list in original order",mylist)
mylist.reverse()
print("list in reverse order",mylist)


# In[23]:


# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
print('Unsorted list:', vowels)
# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)


# In[ ]:




