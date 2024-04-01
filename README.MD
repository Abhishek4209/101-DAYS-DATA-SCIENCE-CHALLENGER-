# **101-DAYS-DATA-SCIENCE-CHALLENGE**


### **➡️Day-1:-** 
```bash

Python basic
variable
Data type
Operator
Condition
Loops
```

### **➡️Day-2:-**

```bash

Data Structure
String slicing
List 
Tuple
Dictionaries
Set
```

### **➡️Day-3:-**

```bash
FUNCTION
PASS KEYWORD
ARGUMENTS
DOCSTRING
*ARGS
**KWARGS


GENRATOR FUNCTION

yield

Iterator  (iter)--> next
Iterable

working of for loop


lambda function
fun=lambda a,b:a+b

map(function, *iterable)

reduce(function, *iterable)


filter(function,iterable)




```


### **➡️Day-4:-**
```bash

OOPS

class
self
__init__

1.POLYMORPHISM
2.ENCAPSULATION
3.INHERITENCE
Simple Inheritence
Multiple Inheritence
Multilevel Inheritence


```

### **➡️Day-5:-**
```bash


4.ABSTRATION


DECORATOR

CLASS METHOD

STATIC METHOD

Magic Method
Dunder Method

PROPERTIES OF DECORATOR
getters
setters
delters



```

### **➡️Day-6:-**
```bash


Working with File
open in diffrent mode
read
append
write
readline


OS module

file size
remove file

rename the file

SHUTILS module

copy the file

json module

Dictionary data(json data)

csv module



BUFFER READ AND WRITE MODULE
buferedwriter
buferedread

```




### **➡️Day-7:-**
```bash

LOGGER 
LEVEL:-

1.NOTSET
2.DEBUG
3.INFO
4.WARNING
5.ERROR
6.CRITICAL

```
### **➡️Day-8:-**
```bash

MODULES AND IMPORT STATEMENT
MODULE
PACKAGE
```
```bash
import os
import sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))
```


### **➡️Day-9:-**
```bash

Exceptions Handling With Try-Except
finally block always executed
Lecture : Custom Exception Handling

raise


Lecture : List Of General Use Exceptions

['__cause__',
 '__class__',
 '__context__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__suppress_context__',
 '__traceback__',
 'add_note',
 'args',
 'with_traceback']




Lecture : Best Practice Exception Handling


```

### **➡️Day-10:-**
```bash

Multithreading:-
Multiple process executed  at same time

thread=[threading.Thread(target =test,args = (i,)) for i in range(10)]


Multiprocessing:-
Multiple process executed but not at same time





```

### **➡️Day-11:-**
```bash

Working with SQL
pip install MySQL-python

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9336",
    
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)   

```






### **➡️Day-12:-**
```bash
Working with MongoDB:-

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db=client.test
print(db)




What Is Web Api:-

Difference B/W Api And Web Api:-

Rest And Soap Architecture:-

Rest:-put,get ,post,delete
Soap:-XML based Data used ,WSDL


Restful Services:-






Flask Introduction, Application, Open Link Flask, App Routing Flask & Url Building Flask:-



from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hellow world </h1>"
if __name__ =="main":
    app.run(host='0.0.0.0')




Git:-

Git Initialization:-


git init
git remote add origin URL
git add .
git commit -m "Commit name"
git branch master -mv main
git push origin main


Git push:-
git add .
git commit -m "commit name"
git push origin main



Flask Http Methods, Templates, Project & Postman:-








```

### **➡️Day-13:-**
```bash


Pandas Basic:-

series
series is equvalent to the list.

DataFrame:-
DataFrame is the list of series

read_csv
read_excel
read on given link




Pandas Advance:-

Data manpulation
iloc
loc



Pandas Part 3:-


Pandas Part 4:-


set_index
reset_index
data conversion from dict
groupe by
concat
merge
apply


Pandas Part 5:-

Time data




```

### **➡️Day-14:-**
```bash

Numpy:-

Data Type:-


arange:-
linspace:-
random:-

 Numpy part-2:-

 Numpy part-3:-


```
### **➡️Day-15:-**
```bash

Matplotlib:-





Seaborn:-


```

### **➡️Day-16:-**
```bash

Plotly:-


Bokeh:-

```
### **➡️Day-17:-**
```bash

Statistics Basic:-

Statistics is a science of collecting organizing and analyzing data.
 
Data:-

peaces of information


Type of Statistics;-



Papultion Data:-
Sample Data:-

Type of Data:-

1.Quantitative Data(Numerical Data)
a.Descrete Data
b.Continues Data

2.Qualitative Data(Categorical Data)
a.Nominal Data
b.Ordinal Data



Scale of Mesurement Of Data:-

Nominal Scale Data
Ordinal Scale Data
Interval Scale Data
Ratio Scale Data


Random Variable:-

Random variable is the process of mapping the outputs of a random process or experiment to a number.


Set:-



Skewness and Histogram:-
Left Skewed
Mean < Median < Mode

Right Skewed

Mean > Median > Mode


Covariance and Corelation:-

Covvariance:-

Correlation:-
1.spearman
2.Karl-Pearson Rank correlation



```

### **➡️Day-18:-**
```bash
Revision of basic Statistics



```

### **➡️Day-19:-**
```bash

1.Probability Density function:-
a.Probability mass function:-
b.Probability Density function:-



Cumalative Destribution Function:-







Types of Distribution:-
1.Normal / Gaussian Distribution :- bell curve,    [pdf]
2.Bernauli Distribution :- 0 or 1 ,always binary outcome ,   [pmf]
3.Uniform Distribution [Pmf]
4.Poisson Distribution;- [pmf]
5.Log Normal Distribution :- [pdf]
6.Binomial Distribution:- [pmf]  , Special case of bernauli distribution like more time an experiment was happen.





```

### **➡️Day-20:-**
```bash


Advanced Stats Revision
```

### **➡️Day-21:-**
```bash


Advanced Stats Revision
```

### **➡️Day-22:-**
```bash

Normal Distribution:- [pdf]

Continues Random Variable
Bell Curve  
Symetrical Curve (mean=median=mode) 

Variance increased then Gradient is also increased

Emperical Rule of Normal Distribution:-
1  S.D---> 68% Data
2  S.D---> 95% Data
3  S.D---> 99.7% Data



```

### **➡️Day-23:-**
```bash

Uniform Distribution:-

1. Continuous Uniform Distribution (PDF)

PDF:-
  1    for x E[a,b]     
_____
 (b-a)

 0 othervise.

 mean,median.varinance.



2. Discrete Uniform Distribution (PMF)

PMF:-

  1/n

mean= (a+b)/2

median= (a+b)/2



Z-stats:-

Z-score= (Xi-mean)
         _________
         S.D.


mean=0
S.D.=1



Central Limit Theorm:-
The CLT says that The sampling  distribution of the mean will alawys be normaly distributed , as the sample size in large enough. Regardless of whether the population has a normal , Poisson , binomial ,or any other distribution , the sampling distribution ,the sampling distribution of the mean will be normal.



Infrenctial Stats:-

Estimate:-
1- Point Estimate:-
2- Interval Estimate:-



Hypothesis Testing:-

P-value:-

Confidence Interval:-

Significance Value (alpha):-


```



### **➡️Day-24:-**
```bash

T- test:-
DOF


Student T-distribution:-


T-test vs Z-test:-


Type -1 Error Type -2 Error:-

```


### **➡️Day-25:-**
```bash

Bayes Statistics(Bayes Therom):-
P(A and B)=p(A)*p(B/A)


P(A/B)=  P(B) * p(A/B) 
        ---------------
            P(A)




Confidence Interval And Margin of Error:-
Point Estimate ± Margin of Error:-



Chi-Square test:-
It is a Non parametric test that is perform on categorical data.


             
x2= sum  (O-E)^2
        --------
           E

Chi-Square -test with python:-


Analysis of variance (Anova):-
ANOVA is a statistical method used to compare the means of 2 or more group.


Assumptions in Anova Test:-

1-Normality of Smapling Distribution of mean:-
The Distribution of sample mean is Normaly Distributed.

2-Absence of Outlier:-
Outlying score need to remove from Datasets.

3-Homogenty of variance:-
Each one of the population it should have same Variance.
Population variance in diffrent levels of each independet variable are equal.

4-Sample are independent and random:-



Type of ANOVA:-
1-One way ANOVA :- 


2-Repeated Measurre Anova:-
One factor with atleast 2 levels and thes levles are dependent.


3-Factorial ANOVA:-
Two or more factor (each of which with atach 2 levels ) levels can be either dependent or independent.



Partitioning of Variance in the ANOVA:-

F-Distribution:-

F- Test(variance ratio test):-


F-test with python:-


```


### **➡️Day-26:-**
```bash

AI VS ML VS DL VS DS:-

Types Of Machine Learning:-

1.Supervised Machine Learning:-
a.Classification------->Used for categries data.
b.Regression------->Used for Continuous data.

2.UnSupervised Machine Learning:-

3.SemiSupervised Machine Learning:-

4.Reinforcement Learning:-



Datasets:-
1.Training Datasets.
2.Testing Datasets.
3.Validation Datasets.



Model performence:-
Overfiting and Underfitting:-
Train Accuracy---->high  || Test Accuracy----->Low  -------------------> Overfitting (Low bias[Training acc] high Variance[Test Acc])
Train Accuracy---->Low  || Test Accuracy----->Low  -------------------> Underfitting (high bias[training Acc] high Variance[Test Acc])
Train Accuracy---->high  || Test Accuracy----->high  ------------------->Genral model (Low bias[training acc] Low Variance[testing Acc])



Missing Value:-
1.Missing Completly at Random (MCAR):-
2.Missing At Random (MAR):-
3.Missing Not At Random (MAR):-


Imputation method for handling missing value:-



```

### **➡️Day-27:-**
```bash
Handling Imbalanced Datasets:-
from sklearn.utils import resample
1.Upsampling:-
2.Down Sampling:-



SMOTE:-
from imblearn.over_sampling import SMOTE



Data Interpolation:-
1.Linear interpolation:- -
2.Cubic interpolation:-
from scipy.interpolate import interp1d

3.Polynomial Interpolation:-



Handling Outliers:-
🔴5-Number Summary:-**
1.Minimum Value
2.Q1-25 percentile
3.Median
4.Q3-75 percentile
5.Maximum value

IQR=Q3-Q1
Lower_fence=Q1-1.5*(IQR)
Upper_fence=Q1+1.5*(IQR)

Boxplot:-


Feature Extraction:-




Feature Scaling:-
1.Standard Scaler:- (mean=0,std=1)


mean=0,std=1

Z-Score=    Xi-mean(X)
           ------------
              std(x)



2.Normalization:- ( 0 to 1)



Min Max Scaler(used in Deep learning):-


X         = X  -  X
 scaled      i    min
            ----------
            X  -  X
             max   min 







3.Unit Vector:-



```