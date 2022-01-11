#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().system('move C:\\Users\\goong\\Downloads\\도로교통공단_부문별_고속도로_교통사고_20181231.csv .')


# In[17]:


# 주피터 노트북이 있는 폴더의 경로를 출력합니다.
get_ipython().run_line_magic('pwd', '')


# In[9]:


get_ipython().run_line_magic('ls', '')


# In[10]:


import pandas as pd


# In[14]:


# () 안에서 shift + tab 키를 누르시면 도움말을 보실 수 있습니다.
pd.read_csv("data/도로교통공단_부문별_고속도로_교통사고_20181231.csv", encoding = 'cp949')


# In[ ]:




