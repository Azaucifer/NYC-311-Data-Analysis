#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Loading and Understanding the Dataset
# Loading the dataset

data = pd.read_csv(r'E:\Data Science with Python Simplilearn\311_Service_Requests_from_2010_to_Present.csv')
data


# In[4]:


# Identifying the shape and general info of the dataset

print("Dataset Shape:", data.shape)


# In[17]:


data.columns.values


# In[18]:


data.info


# In[5]:


# Identify variables with null values

null_counts = data.isnull().sum()
print("Variables with Null Values:")
print(null_counts[null_counts > 0])


# In[6]:


# Performing basic data exploratory analysis
# Utilizing missing value treatment
# Let's drop rows with missing 'Closed Date' and fill 'Descriptor' with a placeholder value.

data.dropna(subset=['Closed Date'], inplace=True)
data['Descriptor'].fillna("No Descriptor", inplace=True)


# In[7]:


# Analyzing the date column and remove entries if it has an incorrect timeline

data['Created Date'] = pd.to_datetime(data['Created Date'], errors='coerce')
data.dropna(subset=['Created Date'], inplace=True)
data


# In[19]:


# Displaying Complaint type and city together

data.loc[:,['Complaint Type','City']]


# In[8]:


# Plotting a frequency plot for city-wise complaints

plt.figure(figsize=(12, 6))
sns.countplot(x='City', data=data, order=data['City'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Frequency of Complaints by City')
plt.xlabel('City')
plt.ylabel('Frequency')
plt.show()


# In[9]:


# Plotting scatter and hexbin plots for complaint concentration across Brooklyn

brooklyn_data = data[data['Borough'] == 'BROOKLYN']
plt.figure(figsize=(12, 6))

# Scatter plot
plt.subplot(1, 2, 1)
plt.scatter(brooklyn_data['Longitude'], brooklyn_data['Latitude'], alpha=0.2)
plt.title('Scatter Plot of Complaints in Brooklyn')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Hexbin plot
plt.subplot(1, 2, 2)
plt.hexbin(brooklyn_data['Longitude'], brooklyn_data['Latitude'], gridsize=50, cmap='Blues')
plt.title('Hexbin Plot of Complaints in Brooklyn')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()
plt.show()


# In[10]:


# Finding major types of complaints
# Ploting a bar graph of count vs. complaint types

plt.figure(figsize=(12, 6))
sns.countplot(x='Complaint Type', data=data, order=data['Complaint Type'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Major Types of Complaints')
plt.xlabel('Complaint Type')
plt.ylabel('Count')
plt.show()


# In[11]:


# Finding the top 10 types of complaints

top_10_complaints = data['Complaint Type'].value_counts().head(10)
print("Top 10 Complaint Types:")
print(top_10_complaints)


# In[21]:


data['Complaint Type'].unique()


# In[22]:


data['Complaint Type'].nunique()


# In[12]:


# Displaying the types of complaints in each city in a separate dataset

complaints_by_city = data.groupby('City')['Complaint Type'].value_counts().unstack(fill_value=0)
print("Complaints by City:")
print(complaints_by_city)


# In[13]:


# Visualizing the major types of complaints in each city
# Creating a subset of the data containing only the top 10 complaint types

top_10_complaint_types = data['Complaint Type'].value_counts().head(10).index
data_top_10 = data[data['Complaint Type'].isin(top_10_complaint_types)]


# In[23]:


# Creating a pivot table to count complaints by city and complaint type

complaints_by_city_type = data_top_10.pivot_table(index='City', columns='Complaint Type', aggfunc='size', fill_value=0)
complaints_by_city_type


# **Conclusion:**
# The analysis of the dataset reveals the top 10 types of complaints reported in New York City, along with their respective counts:
# 
# 1. **Blocked Driveway:** With a staggering count of 100,624 complaints, "Blocked Driveway" is the most frequently reported issue. This suggests that parking-related problems, specifically vehicles blocking driveways, are a major concern for residents.
# 
# 2. **Illegal Parking:** "Illegal Parking" ranks second with 91,716 complaints. This further underscores the significance of parking-related issues in the city.
# 
# 3. **Noise - Street/Sidewalk:** Noise disturbances on streets and sidewalks, such as loud gatherings or construction, are the third most common complaint type, with 51,139 reports.
# 
# 4. **Noise - Commercial:** Complaints related to noise from commercial establishments rank fourth, with 43,751 instances. This indicates that noise pollution from businesses is a notable concern.
# 
# 5. **Derelict Vehicle:** "Derelict Vehicle" complaints, which refer to abandoned or inoperable vehicles, are the fifth most reported issue, with 21,518 cases.
# 
# 6. **Noise - Vehicle:** Complaints about noise originating from vehicles, including loud engines or music, are the sixth most common, with 19,301 reports.
# 
# 7. **Animal Abuse:** Reports of "Animal Abuse" rank seventh, indicating concerns about the welfare of animals in the city, with 10,530 complaints.
# 
# 8. **Traffic:** "Traffic" complaints, encompassing various traffic-related issues, are the eighth most reported, with 5,196 instances.
# 
# 9. **Homeless Encampment:** "Homeless Encampment" complaints, reflecting concerns about people living in public spaces, rank ninth, with 4,879 reports.
# 
# 10. **Vending:** The tenth most common complaint type is "Vending," which may involve unlicensed street vending or related issues, with 4,185 complaints.
# 
# **Key Insights:**
# 
# 1. **Parking and Noise:** Parking-related complaints, including blocked driveways and illegal parking, dominate the top positions, highlighting the challenges related to vehicular congestion and parking violations in the city.
# 
# 2. **Noise Pollution:** Noise-related complaints, both from commercial establishments and vehicles, are significant issues, indicating the impact of noise pollution on residents' quality of life.
# 
# 3. **Quality of Life Concerns:** Complaints about animal abuse, homeless encampments, and street vending underscore concerns related to public safety, animal welfare, and urban living conditions.
# 
# 4. **Traffic Issues:** While traffic-related complaints are present in the top 10, they are relatively lower in frequency compared to parking and noise complaints.
# 
# *Understanding these top complaint types is essential for city officials and agencies to allocate resources effectively, address priority concerns, and enhance the overall urban experience for residents. It also highlights the need for proactive measures and policies to mitigate these common issues and improve the livability of New York City.

# In[15]:


# Plotting a stacked bar chart to visualize the major types of complaints in each city

plt.figure(figsize=(12, 8))
complaints_by_city_type.plot(kind='bar', stacked=True)
plt.title('Major Types of Complaints in Each City')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Complaint Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# In[16]:


# Checking the average response time across various types of complaints

data['Closed Date'] = pd.to_datetime(data['Closed Date'], errors='coerce')
data['Response Time'] = (data['Closed Date'] - data['Created Date']).dt.total_seconds() / 3600  # in hours

average_response_time = data.groupby('Complaint Type')['Response Time'].mean().sort_values(ascending=False)
print("Average Response Time by Complaint Type:")
print(average_response_time)


# **Conclusions:**
# 
# 1. **Variation in Response Times:** There is significant variation in the average response times for different types of complaints. Some complaint types have much longer average response times than others.
# 
# 2. **Longest Response Time:** "Animal in a Park" has the longest average response time, with an average of approximately 336.84 hours (or about 14 days). This suggests that complaints related to animals in parks may require a longer response time, possibly due to the nature of the issue.
# 
# 3. **Shortest Response Time:** "Posting Advertisement" has the shortest average response time, with an average of approximately 2.02 hours. This indicates that complaints related to posting advertisements typically receive quicker responses.
# 
# 4. **Middle Range Response Times:** Complaint types like "Derelict Vehicle," "Graffiti," "Agency Issues," "Animal Abuse," and others have response times in the middle range, ranging from a few hours to several days.
# 
# 5. **Service Improvement Insights:** Understanding the variation in response times can provide insights into areas where service improvements may be needed. For example, if response times for certain complaint types are consistently long, it might indicate a need for more efficient handling of those issues.
# 
# 6. **Resource Allocation:** This information can also help in resource allocation and prioritizing response efforts. Complaint types with longer response times may require additional resources or process optimizations to reduce the waiting time for residents.
# 
# *Overall, analyzing average response times by complaint type can assist in better managing service requests and improving the efficiency of the response process, ensuring that the most critical issues receive prompt attention while also addressing less urgent matters in a timely manner.*

# In[ ]:




