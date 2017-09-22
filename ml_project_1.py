
# coding: utf-8

# # Initialization

# In[22]:

import pandas as pd
import scipy.stats as sst
import scipy
import numpy
get_ipython().magic(u'matplotlib inline')

EXCEL_LOCATION = "University data.xlsx"
UBITNAME = "suniluma"
PERSON_NUMBER = "50249002"

df = pd.read_excel(EXCEL_LOCATION)
df = df.replace("n","NaN")[:-1]
df.columns = ["Rank",
              "Name",
              "CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",
              "GradStudents",
              "TTFaculty",
              "Lecturers",
              "G_TTRatio",
              "G_TTLRatio"]

print "UBitName = " + UBITNAME
print "personNumber = " + PERSON_NUMBER


# # Task 1

# In[23]:

def mean(df,column):
    return str(numpy.mean(df[column]))

def variance(df,column):
    return str(numpy.var(df[column]))
    
def stddev(df,column):
    return str(numpy.std(df[column]))


# In[24]:

print "mu1 = " + mean(df,"CS_Score")
print "mu2 = " + mean(df,"Research_Overhead")
print "mu3 = " + mean(df,"Base_Pay")
print "mu4 = " + mean(df,"Tuition_Out_State")
print ""
print "var1 = " + variance(df,"CS_Score")
print "var2 = " + variance(df,"Research_Overhead")
print "var3 = " + variance(df,"Base_Pay")
print "var4 = " + variance(df,"Tuition_Out_State")
print ""
print "sigma1 = " + stddev(df,"CS_Score")
print "sigma2 = " + stddev(df,"Research_Overhead")
print "sigma3 = " + stddev(df,"Base_Pay")
print "sigma4 = " + stddev(df,"Tuition_Out_State")


# # Task 2

# In[25]:

def plotter(df, column1, column2):
    return df.plot.scatter(x=column1, y=column2, style='o')

def covariance_matrix(df):
    array_like_variables = df.as_matrix()[:-1].T
    return numpy.cov(array_like_variables)

def correlation_matrix(df):
    array_like_variables = df.as_matrix()[:-1].T
    return numpy.corrcoef(array_like_variables)


# In[26]:

print "covarianceMat = " 
print covariance_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]])
print ""
print "correlationMat = " 
print correlation_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]])


# In[27]:

plotter(df,'CS_Score',"Research_Overhead")


# In[28]:

plotter(df,'CS_Score',"Base_Pay")


# In[29]:

plotter(df,'CS_Score',"Tuition_Out_State")


# In[30]:

plotter(df,'Base_Pay',"Research_Overhead")


# In[31]:

plotter(df,'Base_Pay',"Tuition_Out_State")


# In[32]:

plotter(df,'Tuition_Out_State',"Research_Overhead")


# # Task 3

# In[33]:

logLikelihood = sst.norm(0,1).pdf(list(df["CS_Score"]))
print logLikelihood


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



