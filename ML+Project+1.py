
# coding: utf-8

# # Initialization

# In[122]:

import pandas as pd
import scipy.stats as sst
import scipy
import numpy
import math
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

dic = {
        "CS_Score": "1",
        "Research_Overhead":"2",
        "Base_Pay":"3",
        "Tuition_Out_State":"4"
      }

print("UBitName = " + UBITNAME)
print("personNumber = " + PERSON_NUMBER)


# # Task 1

# In[123]:

def mean(df,column):
    return numpy.mean(df[column])

def variance(df,column):
    return numpy.var(df[column])
    
def stddev(df,column):
    return numpy.std(df[column])


# In[124]:

mu1 = mean(df,"CS_Score")
mu2 = mean(df,"Research_Overhead")
mu3 = mean(df,"Base_Pay")
mu4 = mean(df,"Tuition_Out_State")
print("mu1 = " + str(mu1))
print("mu2 = " + str(mu2))
print("mu3 = " + str(mu3))
print("mu4 = " + str(mu4))
print("")
var1 = variance(df,"CS_Score")
var2 = variance(df,"Research_Overhead")
var3 = variance(df,"Base_Pay")
var4 = variance(df,"Tuition_Out_State")
print("var1 = " + str(var1))
print("var2 = " + str(var2))
print("var3 = " + str(var3))
print("var4 = " + str(var4))
print("")
sigma1 = stddev(df,"CS_Score")
sigma2 = stddev(df,"Research_Overhead")
sigma3 = stddev(df,"Base_Pay")
sigma4 = stddev(df,"Tuition_Out_State")
print("sigma1 = " + str(sigma1))
print("sigma2 = " + str(sigma2))
print("sigma3 = " + str(sigma3))
print("sigma4 = " + str(sigma4))


# # Task 2

# In[125]:

def plotter(df, column1, column2):
    return df.plot.scatter(x=column1, y=column2, style='o')

def covariance_matrix(df):
    array_like_variables = df.as_matrix()[:-1].T
    return numpy.cov(array_like_variables)

def correlation_matrix(df):
    array_like_variables = df.as_matrix()[:-1].T
    return numpy.corrcoef(array_like_variables)


# In[126]:

covarianceMat = covariance_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]])
print("covarianceMat = ")
print(covarianceMat)
print("")
correlationMat = correlation_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]])
print("correlationMat = ")
print(correlationMat)


# In[127]:

plotter(df,'CS_Score',"Research_Overhead")


# In[128]:

plotter(df,'CS_Score',"Base_Pay")


# In[129]:

plotter(df,'CS_Score',"Tuition_Out_State")


# In[130]:

plotter(df,'Base_Pay',"Research_Overhead")


# In[131]:

plotter(df,'Base_Pay',"Tuition_Out_State")


# In[132]:

plotter(df,'Research_Overhead',"Tuition_Out_State")


# # Task 3

# In[133]:

def univariate_pdf(df,column):
    pi = math.pi
    sigma = stddev(df,column)
    mu = mean(df,column)
    e = math.e
    root2pi = math.sqrt(2*pi)
    return [1/(root2pi*sigma)*e**(-1/2*((i-mu)/sigma)**2) for i in df[column]]


# In[175]:

pdf1 = univariate_pdf(df,"CS_Score")
pdf2 = univariate_pdf(df,"Research_Overhead")
pdf3 = univariate_pdf(df,"Base_Pay")
pdf4 = univariate_pdf(df,"Tuition_Out_State")

pdf_univariate = [pdf1[i]*pdf2[i]*pdf3[i]*pdf4[i] for i in range(49)]
independent_log_likelihood = sum(numpy.log(pdf_univariate))
print("logLikelihood = " + str(independent_log_likelihood))


# In[ ]:




# In[176]:

from scipy.stats import multivariate_normal
var = multivariate_normal(mean=[mu1,mu2,mu3,mu4], cov=covarianceMat, allow_singular=True)
multivariate_log_likelihood = sum([numpy.log(var.pdf(list(df.ix[i])[2:6])) for i in range(49)])


# In[177]:

print("BNlogLikelihood = " + str(multivariate_log_likelihood))


# In[ ]:




# In[ ]:



