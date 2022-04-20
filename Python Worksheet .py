#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number.

# In[1]:


n = int(input("enter the number: "))

fact = 1

while(n>0):
    fact = fact*n
    n = n-1

print(fact)


# In[ ]:





# In[ ]:





# Write a python program to find whether a number is prime or composite.

# In[3]:


n = int(input("Enter the number: "))

count = 0
i = 1

while(i<=n):
    if n%i == 0:
        count = count +1
    i = i+1


if count == 2:
    
    print("nnumber is prime")
else:
    print("number is composite")


# In[ ]:





# Write a python program to check whether a given string is palindrome or not.

# In[8]:


num = input("Enter the String: ")

if num == num[::-1]:
    print("String is Palindrome")

else:
    print("String is Not Palindrome")


# In[ ]:





# Write a python program to print the frequency of each of the characters present in a given string.

# In[ ]:





# In[9]:


stir = input('enter the stirng: ')
d1 = dict()

for c in stir:
    if c in d1:
        d1[c] = d1[c] + 1
    else:
        d1[c] = 1
        
print(d1)


# In[ ]:





# Write a Python program to get the third side of right-angled triangle from two given sides.

# In[ ]:





# In[10]:


a = int(input("enter the perpendicular: "))
b = int(input("enter the base: "))

c = ((a**2) + (b**2))**0.5

print(c)


# In[ ]:





# In[ ]:





# In[ ]:




