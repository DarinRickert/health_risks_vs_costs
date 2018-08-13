
# coding: utf-8

# # Project: How Health Risk Factors Affect Healthcare Costs
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > The purpose of this report is to compare how certain risk factors affect both individual healthcare costs and the overall healthcare costs of a country. The data sets used in this analysis were obtained from <a href="https://www.gapminder.org/data/">GapMinder</a>. Data sets were downloaded as Excel spreadsheets and specific columns were selected to fit the needs of the analysis. Data from 40 countries was selected from across the world from 2002 (Alcohol consumption data is from 2005 due to no data from 2002.) 
# 
# ### This analysis compares the consumption of 3 risk factors:
# 
# <ol>
#     <li>Alcohol (Average amount of liters consumed per adult (+15))</li>
#     <li>Sugar (Average amount of grams consumed per person)</li>
#     <li>Tobacco (Percent of adult (+15) population that smoke tobacco)</li>
# </ol>
# 
# ### Health risk factors are analyzed together and individually with two types of healthcare costs:
# 
# <ol>
#     <li>Individual healthcare costs (US Dollars)</li>
#     <li>Overall healthcare costs (Percentage of healthcare costs of a country's GDP)</li>
# </ol>
# 
# ### There are 2 questions to be addressed:
# 
# <ol>
#     <li>Do countries with higher rates of consumption of risk factors have higher healthcare costs?</li>
#     <li>Which health risk factor contributes to healthcare costs the most?</li>
# </ol>
# 
# 
# 

# ### 1. Import Python Libraries

# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > In this section of the report, data is loaded, checked for cleanliness, and then trimmed and cleaned for analysis. 
# 
# ### 2. Load Data

# In[3]:


df = pd.read_csv('health_risks_costs.csv')
df.head(10)


# ### 3. Check the size of the data and how many null values it contains

# In[4]:


df.shape


# In[5]:


df.info()


# ## Data Cleaning 
# 
# > Data is cleaned so that there are no null values.
# 
# ### 4. Null values are dropped and the data frame is renamed to reflect the change

# In[6]:


df_clean = df.dropna(axis=0, inplace=False)
df_clean.info()
df_clean.head()


# ### 5. The data is explored by obtaining the <i>mean</i> and <i>median</i> values of each column for further analysis

# In[7]:


df_clean.describe()


# In[8]:


df_clean.median()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > Data is manipulated in order to answer the posed questions and plots are used to visualize any correlations.

# ### Question 1:  Do countries with higher rates of consumption of risk factors have higher healthcare costs?
# 
# ##### Data is separated by the overall healthcare costs (low and high) in order to better understand any correlations

# In[10]:


df_high_spending = df_clean.query('health_cost_by_gdp > 7.25')
df_low_spending = df_clean.query('health_cost_by_gdp <= 7.25')



df_high_spending.groupby('health_cost_by_gdp')['alcohol_con', 'sugar_con', 'tobacco_con'].mean()


# In[12]:


df_low_spending.groupby('health_cost_by_gdp')['alcohol_con', 'sugar_con', 'tobacco_con'].mean()


# #### These bar graphs show how the consumption of risk factors affect a country's healthcare spending

# In[52]:


# The code for this was assisted by this website: http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html
y = df_high_spending['health_cost_by_gdp']
ax = plt.subplot()
ax.bar(df_high_spending['alcohol_con'], y,color='b',align='center')
ax.bar(df_high_spending['sugar_con'], y,color='g',align='center')
ax.bar(df_high_spending['tobacco_con'], y,color='r',align='center')
plt.xlabel('Consumption')
plt.ylabel('Healthcare Spending (% of GDP)')
plt.title('Consumption of Risk Factors vs High Healthcare Spending')
ax.legend(('alcohol (L)', 'sugar (g)', 'tobacco (%)'))
plt.show()


y2 = df_low_spending['health_cost_by_gdp']
ax = plt.subplot()
ax.bar(df_low_spending['alcohol_con'], y2,color='b',align='center')
ax.bar(df_low_spending['sugar_con'], y2,color='g',align='center')
ax.bar(df_low_spending['tobacco_con'], y2,color='r',align='center')
plt.xlabel('Consumption')
plt.ylabel('Healthcare Spending (% of GDP)')
plt.title('Consumption of Risk Factors vs Low Healthcare Spending')
ax.legend(('alcohol (L)', 'sugar (g)', 'tobacco (%)'))
plt.show()


# ### Analysis: 
# 
# Based on the comparison of the graphs between low spending countries and high spending countries, there seems to be correlation, albeit small, between the consumption of risk factors and a country's healthcare spending. 

# #### Data is separated by individual healthcare costs (both high and low)

# In[14]:


df_high_costs = df_clean.query('cost_per_person > 225.36')
df_low_costs = df_clean.query('cost_per_person <= 225.36')

df_high_costs.groupby('cost_per_person')['alcohol_con', 'sugar_con', 'tobacco_con'].mean()


# In[16]:


df_low_costs.groupby('cost_per_person')['alcohol_con', 'sugar_con', 'tobacco_con'].mean()


# #### These bar graphs show how the consumption of risk factors affect an individual's healthcare costs

# In[54]:


y = df_high_costs['cost_per_person']
ax = plt.subplot()
ax.bar(df_high_costs['alcohol_con'], y,color='b',align='center')
ax.bar(df_high_costs['sugar_con'], y,color='g',align='center')
ax.bar(df_high_costs['tobacco_con'], y,color='r',align='center')
plt.xlabel('Consumption')
plt.ylabel('Healthcare Costs per person (US $)')
plt.title('Effect of Risk Factors on Individual Healthcare Costs (High)')
ax.legend(('alcohol (L)', 'sugar (g)', 'tobacco (%)'))
plt.show()

y2 = df_low_costs['cost_per_person']
ax = plt.subplot()
ax.bar(df_low_costs['alcohol_con'], y2,color='b',align='center')
ax.bar(df_low_costs['sugar_con'], y2,color='g',align='center')
ax.bar(df_low_costs['tobacco_con'], y2,color='r',align='center')
plt.xlabel('Consumption')
plt.ylabel('Healthcare Costs per person (US $)')
plt.title('Effect of Risk Factors on Individual Healthcare Costs (Low)')
ax.legend(('alcohol (L)', 'sugar (g)', 'tobacco (%)'))
plt.show()


# ### Analysis:
# 
# There seems to be a correlation between risk factor consumption and individual healthcare costs based on the higher rates of consumption in the first graph with high costs.

# ### Question 2: Which health risk factor contributes to healthcare costs the most?
# 
# > In this section each risk factor will be compared individually against healthcare costs.
# 
# The medians of individual and overall healthcare costs are obtained for comparative purposes.

# In[13]:


df_clean['cost_per_person'].median()


# In[14]:


df_clean['health_cost_by_gdp'].median()


# #### Alcohol consumption is compared with healthcare costs

# In[15]:


df_clean.groupby('alcohol_con')['cost_per_person', 'health_cost_by_gdp'].mean().head(10)


# In[16]:


df_clean.groupby('alcohol_con')['cost_per_person', 'health_cost_by_gdp'].mean().tail(10)


# #### A scatter plot is used to visualize any correlation that exists between alcohol consumption and rising costs

# In[45]:


y = df_clean['cost_per_person']
y2 = df_clean['health_cost_by_gdp']
ax = plt.subplot()
ax.scatter(df_clean['alcohol_con'], y, linestyle='-', color='b')
plt.xlabel('Alcohol Consumption (L)')
plt.ylabel('Healthcare Costs per person (US $)')
plt.title('Effect of Alcohol Consumption on Individual Health Costs')
plt.show()

ax = plt.subplot()
ax.scatter(df_clean['alcohol_con'], y2, linestyle='-', color='b')
plt.xlabel('Alcohol Consumption (L)')
plt.ylabel('Healthcare Spending (% of GDP)')
plt.title('Effect of Alcohol Consumption on Overall Health Costs')
plt.show()


# ### Analysis: 
# 
# Individual: Healthcare costs show an increase after 8 liters of alcohol consumption, but don't show a difinitive trend.
# 
# Overall: There seems to be a correlation between alcohol consumption and overall healthcare spending.

# #### Sugar consumption is compared with healthcare costs

# In[17]:


df_clean.groupby('sugar_con')['cost_per_person', 'health_cost_by_gdp'].mean().head(10)


# In[18]:


df_clean.groupby('sugar_con')['cost_per_person', 'health_cost_by_gdp'].mean().tail(10)


# #### A scatter plot is used to visualize any correlation that exists between sugar consumption and rising costs

# In[46]:


y = df_clean['cost_per_person']
y2 = df_clean['health_cost_by_gdp']

ax = plt.subplot()
ax.scatter(df_clean['sugar_con'], y, linestyle='-', color='g')
plt.xlabel('Sugar Consumption (g)')
plt.ylabel('Healthcare Costs per person (US $)')
plt.title('Effect of Sugar Consumption on Individual Health Costs')
plt.show()

ax = plt.subplot()
ax.scatter(df_clean['sugar_con'], y2, linestyle='-', color='b')
plt.xlabel('Sugar Consumption (g)')
plt.ylabel('Healthcare Spending (% of GDP)')
plt.title('Effect of Sugar Consumption on Overall Health Costs')
plt.show()


# ### Analysis: 
# 
# Individual: The correlation between sugar consumption and individual healthcare costs is salient.
# 
# Overall: An increase in sugar consumption also appears to increase a country's overall healthcare expenditures.

# In[19]:


df_clean.groupby('tobacco_con')['cost_per_person', 'health_cost_by_gdp'].mean().head(10)


# #### Tobacco consumption is compared with healthcare costs

# In[20]:


df_clean.groupby('tobacco_con')['cost_per_person', 'health_cost_by_gdp'].mean().tail(10)


# #### A scatter plot is used to visualize any correlation that exists between tobacco consumption and rising costs

# In[55]:


y = df_clean['cost_per_person']
y2 = df_clean['health_cost_by_gdp']

ax = plt.subplot()
ax.scatter(df_clean['tobacco_con'], y, linestyle='-', color='b')
plt.xlabel('Tobacco Consumption (% of population that smokes)')
plt.ylabel('Healthcare Costs per person (US $)')
plt.title('Effect of Tobacco Consumption on Individual Health Costs')
plt.show()

ax = plt.subplot()
ax.scatter(df_clean['tobacco_con'], y2, linestyle='-', color='b')
plt.xlabel('Tobacco Consumption (%)')
plt.ylabel('Healthcare Spending (% of GDP)')
plt.title('Effect of Tobacco Consumption on Overall Health Costs')
plt.show()


# ### Analysis: 
# 
# Individual: Tobacco usage seems to have a weak correlation to healthcare costs. There is an increase in costs after 20% of the population is smoking, but there is no clear connection between usage and costs.
# 
# Overall: A country's overall healthcare costs typically appear to increase with more of the population smoking.

# <a id='conclusions'></a>
# ## Conclusions
# 
# > Countries that have higher rates of consumption of alcohol, sugar and tobacco typically have higher overall healthcare costs and higher individual costs -- at least past a certain threshold. The risk factor with the strongest correlation of increasing healthcare costs was sugar while the weakest correlation between consumption and cost was smoking tobacco.
# 
# > It is important to take into consideration the limitations of this study. One consideration is the small sample size from which the data was drawn. Another consideration is that the population of each country was not factored into the analysis. With a larger data set and statistical adjustments for population the correlations could be rendered differently.   

# In[57]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

