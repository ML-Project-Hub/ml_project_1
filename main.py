
# coding: utf-8

# # Initialization

# In[1]:

import pandas as pd
import scipy.stats as sst
import scipy
import numpy
import math
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

EXCEL_LOCATION = "./university data.xlsx"
UBITNAME1 = "suniluma"
PERSON_NUMBER1 = "50249002"
UBITNAME2 = "a45"
PERSON_NUMBER2 = "50244979"
UBITNAME3 ="prajnaga"
PERSON_NUMBER3 = "50244304"

df = pd.read_excel(EXCEL_LOCATION)
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

print("Group members\n")
print("UBITName = {}".format(UBITNAME1))
print("personNumber = {}\n".format(PERSON_NUMBER1))
print("UBITName = {}".format(UBITNAME2))
print("personNumber = {}\n".format(PERSON_NUMBER2))
print("UBITName = {}".format(UBITNAME3))
print("personNumber = {}\n".format(PERSON_NUMBER3))


# # Task 1

# In[2]:

def mean(df,column):
    return numpy.mean(df[column])

def variance(df,column):
    return numpy.var(df[column])
    
def stddev(df,column):
    return numpy.std(df[column])


# In[3]:

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

# In[4]:

#def plotter(df, column1, column2):
#    return df.plot.scatter(x=column1, y=column2, style='o')

def covariance_matrix(df):
    array_like_variables = df.as_matrix().T
    return numpy.cov(array_like_variables)

def correlation_matrix(df):
    array_like_variables = df.as_matrix().T
    return numpy.corrcoef(array_like_variables)


# In[5]:

covarianceMat = numpy.matrix(covariance_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]]))
print("covarianceMat = ")
print(covarianceMat)
print("")
correlationMat = numpy.matrix(correlation_matrix(df[["CS_Score",
              "Research_Overhead",
              "Base_Pay",
              "Tuition_Out_State",]]))
print("correlationMat = ")
print(correlationMat)


# In[6]:

#plotter(df,'CS_Score',"Research_Overhead")

#plotter(df,'CS_Score',"Base_Pay")

#plotter(df,'CS_Score',"Tuition_Out_State")

#plotter(df,'Base_Pay',"Research_Overhead")

#plotter(df,'Base_Pay',"Tuition_Out_State")

#plotter(df,'Research_Overhead',"Tuition_Out_State")


# # Task 3

# In[30]:

def univariate_pdf(df,column):
    pi = numpy.pi
    sigma = stddev(df,column)
    mu = mean(df,column)
    e = numpy.e
    root2pi = numpy.sqrt(2*pi)
    return [1/(root2pi*sigma)*e**(-1/2.0*((i-mu)/sigma)**2) for i in df[column]]

pdf1 = univariate_pdf(df,"CS_Score")
pdf2 = univariate_pdf(df,"Research_Overhead")
pdf3 = univariate_pdf(df,"Base_Pay")
pdf4 = univariate_pdf(df,"Tuition_Out_State")

pdf_univariate = [pdf1[i]*pdf2[i]*pdf3[i]*pdf4[i] for i in range(49)]
independent_log_likelihood = sum(numpy.log(pdf_univariate))
print("logLikelihood = " + str(independent_log_likelihood))


# In[29]:

def multivariate_pdf(df,covarianceMat,no_of_columns,formula=True):
    if formula == True:
        inverse_covarianceMat = covarianceMat**-1
        determinant_covarianceMat = numpy.linalg.det(covarianceMat)
        mu = numpy.matrix([mu1,mu2,mu3,mu4]).T
        multivariate_list = [numpy.matrix(list(df.iloc[i][2:2+no_of_columns])) for i in range(49)]
        
        pdf = []
        for i in range(49):
            x = numpy.matrix(multivariate_list[i].tolist()[0]).T
            pdf.append(math.e**(-1/2.0*((x-mu).T*inverse_covarianceMat*(x-mu)).tolist()[0][0])*(1/((math.pi*2)**2*math.sqrt(determinant_covarianceMat))))
        return pdf

multivariate_log_likelihood = sum([numpy.log(i) for i in multivariate_pdf(df,covarianceMat,4)])
print("MultivariatelogLikelihood = " + str(multivariate_log_likelihood))
