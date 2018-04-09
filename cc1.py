"""
import the libraries that are used here.
we import xlrd library for getting the excel cells data.
pandas library are imported for providing high performance, easy to use data structures
and data analysistool.
sklearn is imported for data mining and data analysis for user interactable purposes.
these libraries are used for machine learning purposes.
"""
import os
import http.server
import socketserver

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

#print("serving at port", PORT)
httpd.serve_forever()

import xlrd
import pandas as pd
from pandas import Series, DataFrame
from sklearn import tree

#get the decisiontree classifier for different tree operations

clf=tree.DecisionTreeClassifier()

#bring the excel sheeta data into the train_df and test_df variables

train_df=pd.read_excel('train11.xlsx',"customer")
test_df=pd.read_excel('test11.xlsx',"customer")

#print the training and testing data

print("training data")
print train_df
print("testing data")
print test_df

#only the stores and customer attributes are stored in X
#only the sales attribute is stored in Y

X=train_df.drop(["DayOfWeek","Date","Sales","Open","Promo","StateHoliday","SchoolHoliday"],axis=1)
Y=train_df.drop(["Store","DayOfWeek","Date","Customers","Open","Promo","StateHoliday","SchoolHoliday"],axis=1)

#print the X and Y values

print X
print Y

#use the fit() function to create the tree using CART algorithm
#This algorithm helps us to build the best tree when given different attributes.
#Here, on one scale we give[store id , customer] attribute and on another scale we give the [sales] attribute

clf.fit(X,Y)
print()

#Take the store id and customer number from the user to predict the sales and the range
#of his sales relative to the maximum sales of that store.

sid=int(raw_input("enter the store id"))
cus=int(raw_input("enter the number of customers"))
print sid
print cus

#Here, we call the inbuilt predict function to calculate the prediction value.

prediction=clf.predict([[sid,cus]])


#using linear regression method for predicting the sales of the company
#x is the sales of the company
#y is the rate of its sales
#when the sales of the company is given, we get the rate of the company i.e at what rate the company can achive its profit 
"""
The following steps are performed:
1.Open the excell sheet which contains the prediction details.
2.Take x as sales and y as predictions(they are the assumed values taken by us)
3.Define the variables xx,xy,sx,sy and bring square of x,product of x and y,sum of x,sum of y into these variables
respectively.
4.Now using these values calculate the values of a,b.They are the intercept and slope of regression line
formed by the given prediction data.
5.Using these a and b values evaluate the rate of the predicted sales.
Here, we take predicted sale value as x to get the rate.
"""

pp=pd.read_excel('prediction.xlsx',"predict")
x=pp.drop(["prediction","s*p","s*s"],axis=1)
y=pp.drop(["Sales","s*p","s*s"],axis=1)

print x
print y

workbook=xlrd.open_workbook("prediction.xlsx")
worksheet=workbook.sheet_by_name("predict")
xy=worksheet.cell(100,2).value
xx=worksheet.cell(100,3).value
sx=worksheet.cell(100,0).value
sy=worksheet.cell(100,1).value

print sx
print sy
print xy
print xx

n=99

b=((n*xy)-(sx*sy))/((n*xx)-(sx*sx))
b=round(b,6)
print b

a=round(((sy-b*sx)/n),5)
print a

print("the  future sales can be")
print prediction
print(a+b*prediction)


