#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns


# In[3]:


df=pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[5]:


df.head(10)


# In[6]:


df.dtypes


# In[9]:


df[df['Event distance/length']=='50km']


# In[7]:


df[df['Event distance/length'].isin(['50km','50mi'])]


# In[8]:


df[df['Event distance/length'].isin(['50km','50mi']) & (df['Year of event']==2020)]


# In[10]:


df[df['Event distance/length'].isin(['50km','50mi']) & (df['Year of event']==2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]


# In[11]:


df2=df[df['Event distance/length'].isin(['50km','50mi']) & (df['Year of event']==2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]
df2.head(5)


# In[12]:


df2['athlete_age']=2020-df2['Athlete year of birth']


# In[13]:


df2['Athlete performance']=df2['Athlete performance'].str.split(' ').str.get(0)


# In[14]:


df2.head(5)


# In[20]:


df2=df2.drop(['Athlete club'],axis=1)


# In[21]:


df2.head(5)


# In[22]:


df2.isna().sum()


# In[23]:


df2=df2.dropna()


# In[26]:


df2['athlete_age']=df2['athlete_age'].astype(int)


# In[29]:


df2['Athlete average speed']=df2['Athlete average speed'].astype(float)


# In[28]:


df2.dtypes


# In[31]:


sns.histplot(df2['Event distance/length'])


# In[41]:


df2=df2.rename(columns={'Event distance/length':'Event_length'})


# In[42]:


sns.histplot(df2,x = 'Event_length',hue='Athlete gender')


# In[44]:


sns.displot(df2[df2['Event_length']=='50mi']['Athlete average speed'])


# In[45]:


sns.violinplot(data=df2,x='Event_length',y='Athlete average speed',hue='Athlete gender')


# In[49]:


sns.lmplot(data=df2,x='athlete_age',y='Athlete average speed',hue='Athlete gender')


# In[50]:


df2.groupby(['Event_length','Athlete gender'])['Athlete average speed'].mean()


# In[66]:


df2.query("Event_length=='50km'").groupby('athlete_age')['Athlete average speed'].agg(['mean','count']).sort_values('mean',ascending=False).query('count>19').head(10)

