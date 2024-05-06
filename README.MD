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


### **➡️Day-28:-**
```bash
PCA Basics:-

Data Encoding:-
#### Types:-
1.Nominal or One Hot Encoding (OHE):-

No specific order or Rank
Nominal Encoding is a technique used to transform categorical variable that have no intrisic ordering into numerical value that can be used in machine learning models.One common method for nominal encoding is one-hot-Encoding. Which create a binart vector for each category in the variable.


2.Ordinal or Label Encoding:-

Order matter




3.Target guided Ordinal Encoding:-

It is a technique used to encode categorical variables based on their relationship with the target variable. This encoding technique is useful when we have a categorical variable with a large number of unique categories, and we want to use this variable as a feature in our machine learning model.

In Target Guided Ordinal Encoding, we replace each category in the categorical variable with a numerical value based on the mean or median of the target variable for that category. This creates a monotonic relationship between the categorical variable and the target variable, which can improve the predictive power of our model.



Covarriance and Correlation:-
Relationship b/w features.


```



### **➡️Day-29:-**
```bash


1.Check Missing Value.
2.Check Duplicate Value.
3.Check Data Type.
4.Check the number of unique value of each column.
5.Check Statistics of data set.
6.Check various categories present in the different categories column.



EDA WITH RED WINE DATASET:-

EDA With Student Performence Datasets:-

EDA WITH FOREST FIRE DATASETS:-



```

### **➡️Day-30:-**
```bash

EDA AND FEATURE ENGINEERING WITH FLIGHT PRICES DATASETS:-


EDA AND FEATURE ENGINEERING WITH Google Play Store DATASETS:-

```


### **➡️Day-31:-**
```bash

Simple Linear Regression:-
Finding a best fit in such way if we calculated the overall sum of error should be minmum.

Simple linear regression is a statistical method that uses a straight line to estimate the relationship between two continuous variables. The goal is to find a linear relationship that describes the correlation between the variables. The regression line can then be used to predict or estimate missing values. 


## Cost Function:-

                 n
                -----                             2
                \     [Actual_value-Predict_Value]
J(0o,01) =      /     ----------------------------- 
                -----       n
                 i=1           




Gradient Decent :-

Gradient Decent is a optimization method to reduce cost using to chenge the 0o,01 value in order to get to find local minima in curve by which our error should be minimum. 




Convergence Algorithm:-

0j  : 0j  -alpha *   d   [J(0j)]
                    -----
                    d(0j)

j:0,1


```


### **➡️Day-32:-**
```bash

* Multiple Linear Regression:-


More than one independent variable.
h0(x)=0o + 01x1 +02x2 +03x3 +04x4 +05x5 +06x6 + ........


* Polynomial Linear Regression:-


* Simple Polynomial Regression:-
h0(x) = 0o (x1)^0 + 01 (x1)^1 +02 (x1)^2 + .......



* Multiple Polynomial Regression:-
h0(x) = 0o + 01 (x1)^1 + 02 (x2)^2 +03 (x3)^3 + .......

* R squared Adjusted R squared:-

* R_square= 1 - SS (res)
              -------
              SS (total)



                n
* R2_score=       -----                             2
                \     [Actual_value-Predict_Value]
        1  -    /     ----------------------------- 
                -----       
                i=1              
               ---------------------------------------
                n
                -----                           
                \                2
                /   [Yi - mean(Yi)]  
                -----       
                i=1  









* Adjusted R2_score  =   1 - (1-R^2)(N-1)
                           -------------
                            N-P-1

                        

* N =no of data points.
* R2= R2_score.
* p= No of Independent Features.





                 n
                -----                             2
                \     [Actual_value-Predict_Value]
* MSE      =      /     ----------------------------- 
                -----       n
                 i=1           





                 n
                -----                             
                \     |Actual_value-Predict_Value|
* MAE      =      /     ----------------------------- 
                -----       n
                 i=1    

* RMSE = (MSE)^1/2


* Ridge Regression(L2 Regularization) :-
* Reduce Overfitting.

                 n                                              n
                -----                             2            -----
                \     [Actual_value-Predict_Value]             \         2
J(0o,01) =      /     -----------------------------    + L     /  (slope)
                -----       n                                  ------ 
                 i=1                                            i=1




* Lasso Regression(L1 regularization:-)
to used for Feature selcetion:-




* Cost Function:-

                 n                                              n
                -----                             2            -----
                \     [Actual_value-Predict_Value]             \         
J(0o,01) =      /     -----------------------------    + L     /  |slope|
                -----       n                                  ------ 
                 i=1                                            i=1






* Lasso Regression:-
* To perform both `Feature Selection` and `Overfitting`.


                 n                                              n                       n
                -----                             2            -----                  ------
                \     [Actual_value-Predict_Value]             \         2            \ 
* J(0o,01) =      /     -----------------------------    + L     /  (slope)      + L    /      |slope|    
                -----       n                                  ------                 ------  
                 i=1                                            i=1                   i=1 










* from sklearn.linear_model import ElasticNet
* from sklearn.linear_model import Ridge
* from sklearn.linear_model import Lasso


```




### **➡️Day-33:-**

```bash


Logistic Regression Indepth Intuition:-

Can we solve this `classification` problem using `Linear Regression`:-
* `Besr fit line change` because of outlier -----> prediction goes wrong .
* The `Outcomes` comes >1` and `less than 0`.
* To solve this problem we can use `Logistic regression by using Sqacing technique`.



Best fit Equation:-
           1
* h0(x) =  ------
              -z
        (1 + e   )

* z=sig(0o + 01x1)






* We can not use this type of cost function because they give us a `non convex function` which have `more than one local mininma and one local maxinma`.:-

                 n
                -----                             2
                \     [Actual_value-Predict_Value]
J(0o,01) =      /     ----------------------------- 
                -----       n
                 i=1           

h0(x) [predict_value] =          

           1
h0(x) =  ------
              -z
        (1 + e   )


Binary Loss or Log loss :- 

J(0o,01) = -ylog(h0(x)) - (1-y)log(1-h0(x))


L2 Regularization:- To reduce Overfiting------>


                                                  


                                                     n
                                                    ------
* J(0o,01) = -ylog(h0(x)) - (1-y)log(1-h0(x))  + L  \         2
                                                    / (slope)
                                                    ------
                                                    i=1



* L1 Regularization:- Feature Selection--->

                                                  

                                                     n
                                                    ------
* J(0o,01) = -ylog(h0(x)) - (1-y)log(1-h0(x))  + L  \         
                                                    / |slope|
                                                    ------
                                                     i=1





Elasticnet  Regularization :-   Feature Selection , Reduce Overfiting---->


* J(0o,01) = -ylog(h0(x)) - (1-y)log(1-h0(x))  + L2 + L1






* Performance Metrics Confusion Matrix, Accuracy, Precision & Recall:-



CONFUSION MATRIX:-

   Actual Value---->

Predict
Value         _1_     _0_
            1| TP    FP  |
             |           |  
            0| FN    TN  |
             ---       --- 
            




* Accuracy:-            

              TP + TN
ACCURACY  =  -----------
            TP+FP+FN+TN





* Precision:-
FP IS MORE IMPORTENT THEN USED THIS .

                TP 
PRECISION  =  -------
               TP+FP




Recall:-
FN IS MORE IMPORTENT THEN USED THIS .

                 TP 
PRECISION  =  --------
                TP+FN







F-b score:-

* when both `FP` and `FN` both is importent.
        2
    (1+b ) (Precision x Recall) 
           --------------------
           (Precision + Recall)




* when both `FP` and `FN` both is importent.
b=1

* F-1 score =
        
        2* (Precision x Recall) 
           --------------------
           (Precision + Recall)






* when  `FP` is much importent than `FN`.

F-0.5 score:-------> 

b=0.5

* (1+0.25) * (Precision x Recall) 
           --------------------
           (Precision + Recall)






* when  `FN` is much importent than `FP`.

F-2 score:-------> 

b=2


(5) *      (Precision x Recall) 
           --------------------
           (Precision + Recall)




```



### **➡️Day-34:-**

```bash

* Cross Validation & Types:-
Devide the whole data into 3 part.
1.Train Data ------------> Train the model with this data.
2.Validation Data ---------> Model Hyperparameter Tuning Of our model.
3.Test Data -----------------> Test the model with this data. Test data always hide with your model on training time.




## Types of CV:-
* 1.Leave One Out Cross Validation(LOOCV):-
* One data is for model validation.
* remaining all are used for model training.

## Disadvantage:-
* Time Complexcity is Huge for training biig dataset.
* Model Overfit -------> Training Acc--> High  Validation Acc --> Low 



* 2.Leave P Out CV:-
* P data is for model validation. p---> Hyperparameter.
* remaining all are used for model training.



* 3. K fold Cross Validation:-

* K=5(Hyperparameter) ----------> How many times you can perform Cross Validation.

* n=500 (Size of Datasets):-

* Validation Size = 500
                    --- = 100
                     5

* First 100  records will be Validation data and remaining 400 will be training data. 

* This can perform many times.





* 4.Stratified K Fold  CV:-
* Used for `Imbalanced Datasets`.



* 5.Time Series CV:-


##  Hyperparameter Tuning:-
* Finding the best parameter while training the model.



1.GridSearch CV[Grid Search + Cross Validation]:-
* Give the Input In lIst Form.
* Increase the model Performence or Accuracy.

* Time Complexity Increases for training the model.




2.RandomisedSearch CV

* n_iter=10   cv=5
* 10 diffrent combination + CV=5 

* Time complexcity Decrease


## Logistic Regression Implementation:-

```




### **➡️Day-35:-**

```bash

Decision Tree Classifier Intuition:-


### Decision Tree Classifier:-
* Type:-
* ID3[Iterative Dichotomiser 3]
* CART [Classification and Regression Tree]




## Purity Check :-
* Pure Split   --------> No futher split that feature.
* Impure Split --------> futher split that feature.



### Measure the Purity of Split:-
* When Datasets is small  ---> Entropy
* When Datasets is Huge----> G.I


* Entropy   ------->

H(s) = -P+ Log ( P+ )  - P- Log ( P- )
              2                2   

* P+ -----> Probability of postive Category.
* P- -----> Probability of Negative Category.
* Impure Split (50% -50%)  ----> H(s) =1
* Pure Split (50% -50%)  ----> H(s) =0



* Gini Inpurity------>

            n
           ------  
G.I = 1 -  \      2
           /   (p)
           ------
           i=1

* p is both positive and negative class Probability. 
* Impure Split (50% -50%)  ----> G>I = 0.5
* Pure Split (50% -50%)  ----> G>I = 0





### Information Gain:-

                        
                      -----
Gain(s,f1) = H(s) -   \      |Sv| 
                      /      ----- H(Sv)
                      -----   |S|
                      v E val


* H(s) = -P+ Log ( P+ )  - P- Log ( P- )    ------> Root Node (Entropy)
                2                2   
  

* H(Sv) = -P+ Log ( P+ )  - P- Log ( P- )   ---------> Child Node (Entropy)
                 2                2   
  




## Decision Tree For Numerical Split:-
* Time Complexcity is very large.
* All Instences are split.


### Post Pruning:-
If we can perform Whole spplit on data then they faces overfitting.
For reducet the overfitting we can used Pruning Technoique.



* If we have (9Y /0 N) then we can perform pruning technique.
* First Construct Decision tree then perform Pruning Technique in our model.
* max_depth 




### larger datasets:--------> Prepruning
### Small datasets:--------> Postpruning



## Decision Tree Classifier Implementation:-




## Decision Tree Regressor In-depth Intuition:-

### Variance Reduction:-



                 n
                -----                             2
                \     [Actual_value-Predict_Value]
*  Variance  =   /     ----------------------------- 
                -----       n
                 i=1           


### Variance Reduction:-

var(Root) - Sum(Wi Var(child))


### Decision Tree Regressor Implementation:-

```

### **➡️Day-36:-**

```bash
## Support Vector Classifier Indepth Intuition:-
* SVC
* SVR


* Marginal Plane ----> maximum distance covered.
* Support vector  ----> nearest point from best fit line.
* best fit line


* Soft Margin:- many points are missclassified.
* Hard Margin:- No one points will be misclassified.

## Cost function:-


Maximize (w,b) = 2 ------------> Distance b/w marginal plane.
                ---
                ||w||




## Cost Function:-(HInge Loss)

                     n  
 Min   ||w||        -----
 w,b   -----  + C   \     E
         2       i  /      i 
                    ----- 
                    i=1

* C ----> how many datapoints are misclassified(Hyperparameter)
   i 

* E ---> Summation of all distance of incorrect data points from marginal plane.
   i

## Support Vector Machines Classifier:-

## Support Vector Regressor Indepth Intuition:-

## SVM Kernels Intuition:-
* Polynomial Kernel
* RBF Kernel
* Sigmoid Kernel


## SVM Kernels Implementation:-

```


### **➡️Day-37:-**

```bash

## Naive Bayes Indepth Intuition:-
Only For Classification Problems:-

* Independent Events:-

* dependent Events:-



* P(A and B) =P(A) * P(B/A)--------(1)
* P(B and A) =P(B) * P(A/B)--------(2)

### Bayes Therom:-

* Pr(A/B) = P(A)
           ------ * P(B/A)
            P(B)



## Variants Of Naive Bayes Algorithms:-

* Bernauli Naive Bayes:-
When Your Output is Binary then We can use Bernauli Naive Bayes(Bernauli Distribution)



* MultiNomial Naive Bayes:-
When your data is Text related.Then use this algorithym.


* Gaussian Naive Bayes:-
When Your Data is Dstributed in Normal form then we can used Gaussian Naive Bayes.


## Naive Bayes Practical Implementation:-



##  Ensemble Techniques And Bagging:-
Ensemble Techniques-------->Combining multiple model.

###  BAGGING:-
* ALL MULTIPLE MODEL ON TRAINING TIME THEY ARE CALLED BASE LEARNENR.

## Out Of Bag Score Decision Trees:-
Some data are not given to the model for model training.


### Random Forest Practical Implementation:-


```


### **➡️Day-38:-**

```bash

## Boosting Algorithms:-
* Weak learners ----> Sequential connecyed multiple ecision tree.

1.Adabost
2.Xgboost
3.Gradientboost

## Adaboost classifier indepth intuition:-
We create Decision Tree Stump and we select the best stump.

Depth of Decision Tree Stump ------>1


## Xgboost Classification Algorithms:-

## Xgboost Regresor Algorithm:-


## Gradient Bosting Indepth Intuition:-


```

### **➡️Day-39:-**

```bash

## KNN Classification And Regression:-

1.Euclidian Distance:-
              2          2
dis = [(X2-X1)  + (Y2-Y1)  ]


2.Manhatten Distance:-

dis =  | ((X2-X1) |  + | (Y2-Y1)) |


##  Variants Of KNN.:-
* KD Tree:-
* Ball Tree:-

## Knn Classifier and Refressor:-
```

### **➡️Day-40:-**

```bash
## Curse of Dimensionality Reduction

* Principal Components Analysis:-
If we have 3 features then we find excatly 3 PC and all PC are Orthogonal to each other.


## Eigen Value Decompostions:-


## PCA steps:-

* 1.Covariance Matrix Between Features.   cov[f1,f2,f3,----,n]

* 2.Eigen Value Eigen Vector will be found out using this covariance matrix.

* A * v=lambda * v

* lambda ----> Eigen Value.  

* 3.Eigen Vector ----> Eigen Value is high ----> select it this cover maximum varriance.



## Linear Transformation:-

## PCA Implimentation:-




```


### **➡️Day-41:-**
```bash


# Unsupervised Machine Learning:-

## Clustering
* KMeans Clustering
* Hierarichal Clustering
* DBSCAN Clustering





## KMeans Clustering-

### Steps in KMeans Clustering:-

* 1.Initalize some K centroids.
* 2.Points that are nearest to centroid just group them.
* 3.Move the centroids by calculating the means.


## Intialization of K value:-

### WCSS :-

### Random Intialization Trap:-
This condition where a different set of clusters is generated when a different set of centroids are provided to the K-means algorithm making it inconsistent and unreliable is called the Random initialization trap.


## Hierarichal Clustering:-

* There will be no centroid value.

## Aglomerative Clustering
## Devisive Clusteing

## Dendogram:-
A dendrogram is a tree-structured graph used in heat maps to visualize the result of a hierarchical clustering calculation



##  K-Means vs Heirarical Clustering:-
```


### **➡️Day-42:-**
```bash


## DBSCAN Clustering:-


## Silhoutte_score.:-



Practical Implimentations:-
* K-Means 
* Agglomerative-Clustering
* DBSCAN Clustering


```
# Deep Learning:-

### **➡️Day-43:-**
```bash

## Introduction To Deep Learning:-
1. ML ----> (F.E)/(F.S)--->(Domain knowldge) ----> Tell by us.            | 1.  DL ----> (F.E)/(F.S)--->(Domain knowldge) -----> Automatic learn.
                                                                          |
                                                                          |
2.Model Performence is decrese when Data is Increses.                     | 2. Model Performence is increse when Data is Increses.
                                                                          |
                                                                          |
3.ML can not identify complex patterns                                    | 3. DL can identify complex patterns. 
                                                                          |






## Need For Deep Learning:-
1. TO solve very complex problems.
2. Data managment become easier .
3. Handling large data sets. 




## Use Case:-
1. Youtube recomendation system.
2. Google Translate.
3. Face Id.
4. Chat-GPT.


##  Neural Network Perceptron:-


## Derivation of Basic MatheMatics:-

* Vectors.
* Diffrentiaons.
* Partial Diffrention.
* Gradient.
* Maxima And Minima.

```

### **➡️Day-44:-**

## Activation Function:-

* Help to understand non linearty into neural networks.

*Sigmoid 

$$\sigma (x) = \frac{1}{1+e^{-x}}$$

$$where\ \sigma(x) \in (0, 1),\\
and\ x \in [-\infty, +\infty]$$



* Relu


$$ReLU(x)= max(x,0)$$

$$where\ ReLU(x) \in (0, x),\\
and\ x \in [-\infty, +\infty]$$




* Leaky Relu:-

$$ 
leaky\_relu(x, \alpha) = \left\{\begin{matrix} 
x & x\geq 0 \\ 
\alpha x & x \lt 0 
\end{matrix}\right.
$$

$$where\ x \in [-\infty, +\infty]$$



* Parametric Relu:-


$$f(y_i) = \left\{\begin{matrix} y_i & y_i>0\\ \alpha_i \cdot y_i & y_i \leq 0 \end{matrix}\right.$$

We look at the formula of PReLU. The parameter α is generally a number between 0 and 1, and it is generally relatively small, such as a few zeros. When α = 0.01, we call PReLU as Leaky Relu , it is regarded as a special case PReLU it.

Above, yᵢ is any input on the ith channel and aᵢ is the negative slope which is a learnable parameter.
* if $\alpha_i=0$, f becomes ReLU
* if $\alpha_i>0$, f becomes leaky ReLU
* if $\alpha_i$ is a learnable parameter, f becomes PReLU

* Tanh:-


$$tanh(x) = \frac{(e^{x} - e^{-x})}{(e^{x} + e^{-x})}$$

$$where\ \tanh(x) \in (-1, 1),\\
and\ x \in [-\infty, +\infty]$$



* Softmax:-

$$S(x_j)=\frac{e^{x_j}}{\sum_{k=1}^{K} e^{x_k}}, where\ j = 1,2, \cdots, K $$






##  Forward Propagation:-


### **➡️Day-45:-**
```bash
## Revision:-



## ANN implementation:-

```

### **➡️Day-46:-**
```bash
## Callback Functions:-
* ModelCheck point
* Early Stoping callback 
* Tensorboar callback


## Regression using ANN:-

## Loss Function:-
### For Reggresion model:-
* MSE:-L2 loss


$$MSE = \frac{1}{m}\sum_{i=1}^m (y^{(i)} - \hat{y}^{(i)})^2$$


* MAE:-l1 loss

$$MAE = \frac{1}{m}\sum_{i=1}^m |y^{(i)} - \hat{y}^{(i)}|$$

* RMSE:-



* Huber loss:-
Huber Loss is often used in regression problems. Compared with L2 loss, Huber Loss is less sensitive to outliers(because if the residual is too large, it is a piecewise function, loss is a linear function of the residual).

$$L_\delta(y, \hat{y}) = \left\{\begin{matrix}
\frac{1}{2}(y - \hat{y})^2, & for\ |y - \hat{y}| \le \delta\\ 
\delta(|y - \hat{y}| - \frac{1}{2}\delta), & otherwise
\end{matrix}\right.
$$


### For Classification Problems:-


* binary cross entropy:-log loss-

$$J(w) = -y.log(\hat{y}) - (1 - y).log(1-\hat{y}) = - \sum_{i}p_i. log(q_i)$$



* Categorical cross entropy:-

* sparse categorical_crossentropy:-




*  Hinge loss:-
Hinge loss is often used for binary classification problems, such as ground true: t = 1 or -1, predicted value y = wx + b

In the svm classifier, the definition of hinge loss is

$$l(y) = max(0, 1-t.y)$$



```

### **➡️Day-47:-**



## Batch Normalisation:-
* By using this method our training is so fast.
* And our model should be stable.
* Internal Covarriance shift.

##  Regularization:-
Regularization is the process of adding information in order to solve an ill-posed problem or to prevent overfitting. Regularization can be applied to objective functions in ill-posed optimization problems.



# L1 Regularization | Lasso | Least Absolute:
$j_n(\theta ) = j_0(\theta ) + \alpha \sum_{i=1}^{m}\left | \theta_i \right |$

# L2 Regularization | Ridge
$j_n(\theta ) = j_0(\theta ) + \frac{\alpha}{2} \sum_{i=1}^{m}(\theta_i)^2$


# L1 - L2 Regularization 
$j_n(\theta ) = j_0(\theta ) + r\alpha \sum_{i=1}^{m}\left | \theta_i \right | + \frac{(1-r)}{2} \alpha \sum_{i=1}^{m}(\theta_i)^2$


## Weight Initialisation:-

### Table for choosing weight initialization technique based on the Activation function

|Authors| Initialization |Activation function |
|--|--|--|
|Xavier Glorot and yoshna benjio| Glorot| tanh,sigmoid,softmax|
|kaiming He | He | Relu and its variants|



## Optimizers:-

* Gradient Descent
* Stochastic Gradient Decent:-



![sgd1](https://user-images.githubusercontent.com/115534733/232980366-756db69a-2343-4387-8f52-01799d87b4d1.png)
 
 **<center>Figure :- SGD without Momentum &&&  SGD without Momentum</center>**




* Mini batch Gradient Decent
* Momentum + GD
* Adagrad
* RMS Prop
* Adam

### ➡️Day -48:-
```bash


*HAND WRITTEN NUMBER PREDICTION USING MNIST DATASETS.



```



### ➡️Day -49:-
```bash
## Revision:-
```


### ➡️Day -50:-


## CNN :-

## LeNet:-
# Basic Introduction

LeNet-5, from the paper Gradient-Based Learning Applied to Document Recognition, is a very efficient convolutional neural network for handwritten character recognition.


<a href="http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf" target="_blank">Paper: <u>Gradient-Based Learning Applied to Document Recognition</u></a>

**Authors**: Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner

**Published in**: Proceedings of the IEEE (1998)

### Structure of the LeNet network

LeNet5 is a small network, it contains the basic modules of deep learning: convolutional layer, pooling layer, and full link layer. It is the basis of other deep learning models. Here we analyze LeNet5 in depth. At the same time, through example analysis, deepen the understanding of the convolutional layer and pooling layer.

![lenet](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/lenet-5.png)


LeNet-5 Total seven layer , does not comprise an input, each containing a trainable parameters; each layer has a plurality of the Map the Feature , a characteristic of each of the input FeatureMap extracted by means of a convolution filter, and then each FeatureMap There are multiple neurons.

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/arch.jpg)

Detailed explanation of each layer parameter:

#### **INPUT Layer**

The first is the data INPUT layer. The size of the input image is uniformly normalized to 32 * 32.

> Note: This layer does not count as the network structure of LeNet-5. Traditionally, the input layer is not considered as one of the network hierarchy.


#### **C1 layer-convolutional layer**

>**Input picture**: 32 * 32

>**Convolution kernel size**: 5 * 5

>**Convolution kernel types**: 6

>**Output featuremap size**: 28 * 28 (32-5 + 1) = 28

>**Number of neurons**: 28 * 28 * 6

>**Trainable parameters**: (5 * 5 + 1) * 6 (5 * 5 = 25 unit parameters and one bias parameter per filter, a total of 6 filters)

>**Number of connections**: (5 * 5 + 1) * 6 * 28 * 28 = 122304

**Detailed description:**

1. The first convolution operation is performed on the input image (using 6 convolution kernels of size 5 * 5) to obtain 6 C1 feature maps (6 feature maps of size 28 * 28, 32-5 + 1 = 28).

2. Let's take a look at how many parameters are needed. The size of the convolution kernel is 5 * 5, and there are 6 * (5 * 5 + 1) = 156 parameters in total, where +1 indicates that a kernel has a bias.

3. For the convolutional layer C1, each pixel in C1 is connected to 5 * 5 pixels and 1 bias in the input image, so there are 156 * 28 * 28 = 122304 connections in total. There are 122,304 connections, but we only need to learn 156 parameters, mainly through weight sharing.


#### **S2 layer-pooling layer (downsampling layer)**

>**Input**: 28 * 28

>**Sampling area**: 2 * 2

>**Sampling method**: 4 inputs are added, multiplied by a trainable parameter, plus a trainable offset. Results via sigmoid

>**Sampling type**: 6

>**Output featureMap size**: 14 * 14 (28/2)

>**Number of neurons**: 14 * 14 * 6

>**Trainable parameters**: 2 * 6 (the weight of the sum + the offset)

>**Number of connections**: (2 * 2 + 1) * 6 * 14 * 14

>The size of each feature map in S2 is 1/4 of the size of the feature map in C1.

**Detailed description:**

The pooling operation is followed immediately after the first convolution. Pooling is performed using 2 * 2 kernels, and S2, 6 feature maps of 14 * 14 (28/2 = 14) are obtained.

The pooling layer of S2 is the sum of the pixels in the 2 * 2 area in C1 multiplied by a weight coefficient plus an offset, and then the result is mapped again.

So each pooling core has two training parameters, so there are 2x6 = 12 training parameters, but there are 5x14x14x6 = 5880 connections.

#### **C3 layer-convolutional layer**

>**Input**: all 6 or several feature map combinations in S2

>**Convolution kernel size**: 5 * 5

>**Convolution kernel type**: 16

>**Output featureMap size**: 10 * 10 (14-5 + 1) = 10

>Each feature map in C3 is connected to all 6 or several feature maps in S2, indicating that the feature map of this layer is a different combination of the feature maps extracted from the previous layer.

>One way is that the first 6 feature maps of C3 take 3 adjacent feature map subsets in S2 as input. The next 6 feature maps take 4 subsets of neighboring feature maps in S2 as input. The next three take the non-adjacent 4 feature map subsets as input. The last one takes all the feature maps in S2 as input.

>**The trainable parameters are**: 6 * (3 * 5 * 5 + 1) + 6 * (4 * 5 * 5 + 1) + 3 * (4 * 5 * 5 + 1) + 1 * (6 * 5 * 5 +1) = 1516

>**Number of connections**: 10 * 10 * 1516 = 151600

**Detailed description:**

After the first pooling, the second convolution, the output of the second convolution is C3, 16 10x10 feature maps, and the size of the convolution kernel is 5 * 5. We know that S2 has 6 14 * 14 feature maps, how to get 16 feature maps from 6 feature maps? Here are the 16 feature maps calculated by the special combination of the feature maps of S2. details as follows:




The first 6 feature maps of C3 (corresponding to the 6th column of the first red box in the figure above) are connected to the 3 feature maps connected to the S2 layer (the first red box in the above figure), and the next 6 feature maps are connected to the S2 layer The 4 feature maps are connected (the second red box in the figure above), the next 3 feature maps are connected with the 4 feature maps that are not connected at the S2 layer, and the last is connected with all the feature maps at the S2 layer. The convolution kernel size is still 5 * 5, so there are 6 * (3 * 5 * 5 + 1) + 6 * (4 * 5 * 5 + 1) + 3 * (4 * 5 * 5 + 1) +1 * (6 * 5 * 5 + 1) = 1516 parameters. The image size is 10 * 10, so there are 151600 connections.

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/c31.png)


The convolution structure of C3 and the first 3 graphs in S2 is shown below:

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/c32.png)


#### **S4 layer-pooling layer (downsampling layer)**

>**Input**: 10 * 10

>**Sampling area**: 2 * 2

>**Sampling method**: 4 inputs are added, multiplied by a trainable parameter, plus a trainable offset. Results via sigmoid

>**Sampling type**: 16

>**Output featureMap size**: 5 * 5 (10/2)

>**Number of neurons**: 5 * 5 * 16 = 400

>**Trainable parameters**: 2 * 16 = 32 (the weight of the sum + the offset)

>**Number of connections**: 16 * (2 * 2 + 1) * 5 * 5 = 2000

>The size of each feature map in S4 is 1/4 of the size of the feature map in C3

**Detailed description:**

S4 is the pooling layer, the window size is still 2 * 2, a total of 16 feature maps, and the 16 10x10 maps of the C3 layer are pooled in units of 2x2 to obtain 16 5x5 feature maps. This layer has a total of 32 training parameters of 2x16, 5x5x5x16 = 2000 connections.

*The connection is similar to the S2 layer.*

#### **C5 layer-convolution layer**

>**Input**: All 16 unit feature maps of the S4 layer (all connected to s4)

>**Convolution kernel size**: 5 * 5

>**Convolution kernel type**: 120

>**Output featureMap size**: 1 * 1 (5-5 + 1)

>**Trainable parameters / connection**: 120 * (16 * 5 * 5 + 1) = 48120

**Detailed description:**


The C5 layer is a convolutional layer. Since the size of the 16 images of the S4 layer is 5x5, which is the same as the size of the convolution kernel, the size of the image formed after convolution is 1x1. This results in 120 convolution results. Each is connected to the 16 maps on the previous level. So there are (5x5x16 + 1) x120 = 48120 parameters, and there are also 48120 connections. The network structure of the C5 layer is as follows:

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/c5.png)


#### **F6 layer-fully connected layer**

>**Input**: c5 120-dimensional vector

>**Calculation method**: calculate the dot product between the input vector and the weight vector, plus an offset, and the result is output through the sigmoid function.

>**Trainable parameters**: 84 * (120 + 1) = 10164

**Detailed description:**

Layer 6 is a fully connected layer. The F6 layer has 84 nodes, corresponding to a 7x12 bitmap, -1 means white, 1 means black, so the black and white of the bitmap of each symbol corresponds to a code. The training parameters and number of connections for this layer are (120 + 1) x84 = 10164. The ASCII encoding diagram is as follows:

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/f61.png)

The connection method of the F6 layer is as follows:

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/f62.png)


#### **Output layer-fully connected layer**

The output layer is also a fully connected layer, with a total of 10 nodes, which respectively represent the numbers 0 to 9, and if the value of node i is 0, the result of network recognition is the number i. A radial basis function (RBF) network connection is used. Assuming x is the input of the previous layer and y is the output of the RBF, the calculation of the RBF output is:

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/81.png)

The value of the above formula w_ij is determined by the bitmap encoding of i, where i ranges from 0 to 9, and j ranges from 0 to 7 * 12-1. The closer the value of the RBF output is to 0, the closer it is to i, that is, the closer to the ASCII encoding figure of i, it means that the recognition result input by the current network is the character i. This layer has 84x10 = 840 parameters and connections.

![lenet1](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/lenet/82.png)


**Summary**


* LeNet-5 is a very efficient convolutional neural network for handwritten character recognition.
* Convolutional neural networks can make good use of the structural information of images.
* The convolutional layer has fewer parameters, which is also determined by the main characteristics of the convolutional layer, that is, local connection and shared weights.








## Alexnet:-




## ➡️Day-51:-


### VGG -16:-
```bash
* All Convulational Layer have filter sizes is (3,3).
* Very depth to the Architecture.
* There Was No Overlapping.
* Remove LRN


Conv 1-1
Conv 1-2
Padding


Conv 2-1
Conv 2-2
Padding


Conv 3-1
Conv 3-2
Conv 3-3
Padding


Conv 4-1
Conv 4-2
Conv 4-3
Padding


Conv 5-1
Conv 5-2
Conv 5-3
Padding



Dense
Dense
Dense

```


### VGG -19:-



### ReseNet:-


### InceptionNet:-


## ➡️Day-52:-
```bash



# ➡️R-CNN:-
* Regions Proposal
* Warping and Resize
* Pretrained CNN ---> Alexnet , VGG
* pretrained SVM 
* CleanUp
* Bouding Box

# RCNN
* Regions Proposal
* Warping and Resize
* Pretrained CNN ---> Alexnet , VGG
* pretrained SVM 
* CleanUp
* Bouding Box
```

## 1. Introduction
The CNN based objection detection techniques have improved dramatically over the last few years. The journey starts with R-CNN followed by Fast R-CNN, Faster R-CNN, mask R-CNN and YOLO. These are all very simple, very intuitive and easy to implement algorithms. Personally I have found them very fascinating. I intend to write medium stories for all of them……

R-CNN is the first in the family. Understanding R-CNN is crucial as it will lay foundation to understand subsequent algorithms.


## 2. First look at RCNN


![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*lW4453vRf1gERyRotAAQZQ.jpeg)


- The regions that are extracted from an input image are called region proposals.
- RCNN extracts only around 2000 region proposals from an input image. (All 2000 images will not actually contain objects of our interest)
- As the CNN can only accept inputs with fixed size, all the extracted region proposals are first converted to a fixed size of 227 x 227 pixels. This is called image warping.
- These fixed size region proposals are then fed to a Large convolutional neural network consisting of five convolutional layers and two fully connected layers to get a fixed length features vector for each region proposal.
- These feature maps are then passed to a set of linear SVMs to predict the actual objects in corresponding region proposals. The number of SVMs are equal to the number of classes in dataset plus 1.
- For example if the dataset contains 200 classes, then 201 linear SVMs are used in last stage. 1 extra class is for background. The background of the image is treated as one class.
- Thus each SVM corresponds to one class. So each class specific SVM will predict if the region proposal contains corresponding object or not.
- After that, A bounding box regressor uses a linear regression model to predict more accurate bounding boxes in terms of location.
The above steps are summarized in Figure 5 below.


![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*JjAXZCJJR0n8TOnk.png)


## 3. More insights into R-CNN


According to Wikipedia

Given an input image, R-CNN begins by applying a mechanism called Selective Search to extract regions of interest (ROI), where each ROI is a rectangle that may represent the boundary of an object in image. Depending on the scenario, there may be as many as two thousand ROIs. After that, each ROI is fed through a neural network to produce output features. For each ROI’s output features, a collection of support-vector machine classifiers is used to determine what type of object (if any) is contained within the ROI.

Ross Girshick et al. introduced R-CNN in November 2013. Object detection has come a long way since then. The more recent algorithms are based on foundations laid by R-CNN. Hence it is crucial for aspiring computer vision engineers to understand R-CNN.


### 3.1 How region proposals are generated?

As a very first step of R-CNN, we have to generate region proposals from an image, which can then be warped and fed to CNN for further processing. R-CNN is agnostic to region proposal methods. Which means we can use any method to generate region proposals. The authors of R-CNN have used Selective Search. The corresponding research paper by J.R.R. Uijlings et. al. gives the details of selective search.

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*Yh_zicid04eOpJWJn-VtSg.jpeg)


The criterion used to differentiate a region proposals from rest of the image are worth giving a thought.

- Image (c) in Figure 6contains a chameleon whose color is matching a lot with its surrounding. So we have to use a criterion of texture to differentiate and extract chameleon from rest of the image.
- Image (b) in Figure 6contains two cats whose texture is same. So we have to use a criterion of color.
- In image (d), the wheel of car have different color and texture from car and we may by mistake declare it as separate region. Images are intrinsically hierarchical. Hence wheels and rest of the car should merge into one object.
- On the contrary, in image (a), spoon is inside the bowl and the bowl stands on the table. But we may want to declare spoon and bowl as separate objects instead of merging them into table and declaring them as one object.


The bottom-line here is , there do not exit a single strategy for generating region proposals.

Selective search algorithm presents a variety of diversification strategies to deal with as many image conditions as possible.


![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*FgmQHR6CoLgNubUAle9MLw.jpeg)


The process of selective search can be explained in the following steps with the help of Figure.

- A set of small starting regions which ideally do not span multiple objects is created as shown in first column of Figure 7.
- Similarities between all the adjacent regions are found and two most similar regions are grouped together.
- Again similarities are found and grouping is done. This process is repeated as shown Figure 7.


Three types of diversification strategies are used.

- Variety of color spaces with increasing degree of invariance in terms of light intensity, shadow/shading, highlights.
- By using different similarity measures like color similarity, texture similarity, encouraging small regions to merge early and measuring how well two regions fit into each other.
- Varying the complimentary starting regions.

Around 2000 region proposals thus created are warped and fed to CNN as shown in Figure


## 3.2 The need of bounding box regressor

This is a refinement step. A bounding box given by selective search is represented using [x,y,w,h], where x, y are the coordinates of top left corner of region proposal and w,h are width and height of region proposal. This bounding box given by selective search is further refined by bounding box regressor. Here, A linear regression model is trained to predict a modified window. This way localization error is further reduced and mAP is improved by 3 to 4points.


## 3.3 Training and evaluation of R-CNN

R-CNN is trained on ILSVRC2013 dataset. ILSVRC stands for ImageNet Large Scale Visual Recognition Challenge. The dataset is split into train(395918 images), val(20121 images) and test(40152 images) set.

Three types of training occurs in R-CNN. 1) CNN fine tuning 2) SVM training 3) bounding box regressor training.

At test time, we again obtain 2K region proposals for every image, warp them, feed them to CNN, get their score from SVMs and then R-CNN uses something called as NMS (Non-maximum supression) to reject unwanted region proposals. A object may have been detected by more than one region proposals. NMS will consider only those proposals that have higher SVM score than its learned threshold. NMS will also reject a region if it has overlap(IoU) with another region having higher SVM score. This way we get the best region proposal for a given object.


## 3.4 Results


![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*BZozuKSIBSwV3ArnciEFVw.png)

Figure shows mAP comparison with various other techniques present prior to R-CNN. Note that methods preceded by * in Figure use outside training data in test set. BB stands for bounding box. As it is very clear from figure that R-CNN outperformed all other techniques on ILSVRC2013 dataset.


## 3.5 Drawbacks of R-CNN

- It takes more than 40 seconds to detect the objects in a test image which makes it unsuitable for real time applications.
- The CNN has to run for every region proposals. There is no weight sharing.


## Paper
[Link](https://arxiv.org/pdf/1311.2524.pdf)




# ➡️Fast RCNN:-

## Intuition of Fast RCNN
What else can we do to reduce the computation time an RCNN algorithm typically takes? Instead of running a CNN 2,000 times per image, we can run it just once per image and get all the regions of interest (regions containing some object).

Ross Girshick, the author of RCNN, came up with the idea of running the CNN just once per image and then finding a way to share that computation across the 2,000 regions. In Fast RCNN, we feed the input image to the CNN, which in turn generates the convolutional feature maps. Using these maps, the regions of proposals are extracted. We then use an RoI pooling layer to reshape all the proposed regions into a fixed size, so that they can be fed into a fully connected network.

Let’s break this down into steps to simplify the concept:

- As with the earlier two techniques, we take an image as an input.
- This image is passed to a ConvNet which in turn generates the Regions of Interest.
- An RoI pooling layer is applied to all of these regions to reshape them as per the input of the ConvNet. Then, each region is passed on to a fully connected network.
- A softmax layer is used on top of the fully connected network to output classes. Along with the softmax layer, a linear regression layer is also used parallel to output bounding box coordinates for predicted classes.

So, instead of using three different models (like in RCNN), Fast RCNN uses a single model which extracts features from the regions, divides them into different classes, and returns the boundary boxes for the identified classes simultaneously.

To break this down even further, I’ll visualize each step to add a practical angle to the explanation.

- We follow the now well-known step of taking an image as input:


![](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/fast-rcnn/image-10.png)

- This image is passed to a ConvNet which returns the region of interests accordingly:

![](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/fast-rcnn/image-11.png)

- Then we apply the RoI pooling layer to the extracted regions of interest to make sure all the regions are of the same size:

![](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/fast-rcnn/image-14.png)

- Finally, these regions are passed on to a fully connected network which classifies them, as well as returns the bounding boxes using softmax and linear regression layers simultaneously:

![](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/fast-rcnn/image-13.png)

This is how Fast RCNN resolves two major issues of RCNN, i.e., passing one instead of 2,000 regions per image to the ConvNet, and using one instead of three different models for extracting features, classification, and generating bounding boxes.


## Problems with Fast RCNN
But even Fast RCNN has certain problem areas. It also uses selective search as a proposed method to find the Regions of Interest, which is a slow and time-consuming process. It takes around 2 seconds per image to detect objects, which is much better compared to RCNN. But when we consider large real-life datasets, then even a Fast RCNN doesn’t look so fast anymore.

But there’s yet another object detection algorithm that trumps Fast RCNN. And something tells me you won’t be surprised by its name.

## Paper
[Link](https://arxiv.org/pdf/1504.08083.pdf)





# ➡️Faster RCNN:-





Faster RCNN : <a href="https://arxiv.org/abs/1506.01497" target="_blank">Paper address </a>

Faster-rcnn is one of the most classic algorithms in the field of object detection. It mainly consists of two parts. One is a deep full convolutional network for generating candidate area frames, and the other is a Fast R-CNN detection model. The two share parameters during training.



Faster R-CNN can solve the problem that Fast RCNN uses the third-party tool selective search to extract the region proposal. It uses RPN instead of selective search to make the entire target detection function into a unified network. Faster RCNN uses RPN to make the calculation of region proposals more elegant and efficient. RPN is a full convolutional network. Candidate region generation and target detection share convolutional features. Attention mechanism is used . RPN will tell the network where to focus.

![title](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/faster-rcnn/fast2.png)

### RPN (Region Proposal network)

RPN is the core of faster rcnn. Its essence is a classless object detector based on sliding windows. There are multiple types of anchor boxes (region proposals) at each position of the image. Faster rcnn is trained with these region proposals. Classification and box regression pass Gradient descent backpropagation adjusts network parameters, regenerates the region proposal, and then continues training faster rcnn, repeating this process continuously.

### Structure

![title](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/faster-rcnn/fast1.png)

1. Conv layers: It is mainly composed of the basic conv + relu + pooling layers, which are used to extract the feature map in the image. Used for later shared RPN layers and fully connected layers.
2. region proposal networks (RPN): mainly used to generate region proposals. Use softmax to classify the candidate box (whether the background image is positive or negative), and use bbox to perform regression correction on the candidate box to obtain the proposals.
3.RoI pooling: Collect feature maps and proposals, extract the proposal feature map, and send it to the subsequent fully connected layer to determine the target category.
4.classification: Use the proposal feature map to calculate the proposal category, and bbox regression again to obtain a more accurate positioning.

VGG16-fasterrcnn is shown in Figure 2. It can be seen that the algorithm steps of the model are:
(1). Reshape a P × Q network of any size into M × N, and then send it to the network.
(2). Use vgg16 network to extract the features of the image: feature map.
(3). The RPN layer undergoes a 3 × 3 convolution to generate the positive anchor and bbox regression offsets, and calculates the proposals.
(4). The RoI layer uses the proposals to extract the proposals feature from the feature map and sends them to the subsequent full connection and softmax network for bbox_pre and classification.


Conv layers
As shown in Figure 2, using the VGG16 model as the network infrastructure, Conv layers has 13 conv layers, 13 relu layers, and 4 pooling layers. Here, the convolution operation has a general formula that gives the input image X × X. If kernel_size, padding, and stride are all given, then the dimension of the output is:


![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast3.webp)

X = \ lfloor \ frac {X + 2padding-kernelsize} {stride} \ rfloor+ 1
where, as shown in the figure Calculation process:

Therefore, an M × N proof can be changed to (M / 16) × (N / 16), so that the feature map generated by the conv layers can correspond to the original image.

### RPN

The classical detection methods are very time-consuming. Faster rcnn can use RPN to automatically generate candidate frames, which greatly improves the speed of generating candidate frames.

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast4.webp)

Figure 4 is the RPN structure diagram. It can be seen that RPN actually has two lines. The above is to obtain positive and negative anchors using softmax classification. The following is to calculate the offset of bbox and correct the position. The final layer of the proposal is responsible for synthesizing the positive anchors corresponding to the bbox regression offset to obtain the proposals, while deleting the proposals that are too small and exceed the boundary. To the proposal layer, the function of target positioning is completed.

。
### Multi-channel image convolution basics

For multi-channel multi-convolution kernels to do convolution, the calculation method is as follows:

Input 3 channels and 2 convolution kernels at the same time. For each convolution kernel, first input 3 channels for convolution, and then add the results of the 3 channels to obtain the convolution output.
For multi-channel 1 × 1 convolution, multiplying each channel of the input image by a convolution coefficient and adding them together is equivalent to “linking together” the original independent channels.

### Anchors

Anchors primarily used to represent the position of the candidate box ( , , , ) for the upper left corner and lower left coordinates. There are three types of aspect ratio: {1: 1,2: 1,1: 2}. As shown in Figure 6, through the introduction of commonly used multi-scale methods by anchors, anchors can basically cover all scales and shapes.

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast5.webp)

What do these 9 anchors do? As shown in Figure 7, each point of the feature maps is conveniently calculated by Conv layers, and is equipped with 9 kinds of initial detection frames. There are two bbox regressions to get the position of the modified candidate box.

![title](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/faster-rcnn/fast6.png)

Explain the numbers in Figure 7:

1. The original uses the ZF model. The last conv5 layer generates num_output = 256, corresponding to 256 feature maps, so each point has 256 dimensions.

2. After conv5, do rpn_conv / 3 3 convolution and nun_ouput = 256, which is equivalent to fusing the surrounding 3 3 spatial information at each point , which is equivalent to fusing the surrounding 3 × 3 information, which is more robust. The red boxes of Figures 4 and 7.

3. Assume that each point in the conv feature map has k anchors, and each anchor is divided into positive and negative, so each point is converted from 256d feature to cls = 2k scores; each anchor has (x, y, w , h) corresponds to 4 offsets, so reg = 4k position.

4. All anchors take too much training. The training will randomly select 128 positive anchors and 128 negative anchors in the verified anchors for training.

In fact, the RPN is added with many candidate box anchors in the original picture. Then use cnn to determine which anchors have a positive anchor in the target and which negative anchors do not have a target, so it is only a two-class classification.

So how many anchors are there? Assuming the original image is 800 × 600, VGG is down-sampled 16 times, and 9 anchors are set for each point of the feature map, so:
ceil (800/16) × ceil (600/16) × 9 = 50 × 38 × 9 = 17100



![title](https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/faster-rcnn/fast7.png)

Using softmax to determine positive and negative
After the MxN-sized image is sent to the Faster RCNN network, the RPN network becomes (M / 16) x (N / 16). It is better to set W = M / 16 and H = N / 16. Before entering reshape and softmax, do a 1x1 convolution, as shown in Figure 9

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast8.webp)

The output image after convolution is W × H × 18. There are exactly 9 anchors for each point in the feature maps. At the same time, each anchor may be positive and negative. All this information is stored in a W × H × (9 × 2) size matrix. Why did you do this? Later, the softmax classifies the positive anchors, that is, the box (in the positive anchors) of the preliminary detection target area is initially extracted.
Why connect a reshape layer before and after softmax? In fact, it is just for the convenience of softmax classification. Corresponding to the above matrix holding positive / negative anchors, its storage form in caffe blob is [1, 2x9, H, W]. In the softmax classification, a positive / negative binary classification is required, so the reshape layer will change it to a size of [1, 2, 9xH, W], that is, a dimension is vacated separately for the softmax classification, and then the reshape returns to its original state.
In summary, the RPN network uses anchors and softmax to initially extract positive anchors as candidate frames.


### BoundingBox Regression principle

As shown in Figure 10, the green frame is the Ground Truth (GT) of the aircraft, and the red is the extracted positive anchors. Even if the red frame is recognized by the classifier as an aircraft, but the red frame is not positioned correctly, this picture is equivalent to no The aircraft was correctly detected. So we hope to use a method to fine-tune the red box to make the positive anchors and GT closer.

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast8.webp)

For windows, use the representation, which represents the center coordinates and width and height, respectively. For Figure 11, the red box A represents the original positive anchors, and the green box G represents the target GT. Our goal is to find a relationship so that after inputting the original A, a box G` and G are very close.`

### BoundingBox Regression on proposals


![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast10.webp)

After this convolution, the output image is W × H × 36, and the storage form is [1,4 × 9, H, W]. Each point here has 9 anchors, and each anchor has four regression variables:
in FIG. 8, VGG output 50 38 is feature 256, provided corresponding to 50 38 is K th anchors, RPN output:

1. the size of 50 38 is positive / negative classification characteristic matrix 2k

2. the size of 50 38 is regression regression matrix coordinates 4k


### Proposal layer
This layer is responsible for synthesizing all the transform amounts and positive anchors, calculating accurate proposals, and inputting them to the subsequent ROI Pooling Layer. He has three inputs: the classification results of positive negative anchors, the corresponding bbox reg transformation amounts, rpn_bbox_pred and im_info, and feat_stride = 16.
As shown in Figure 13, im_info = [M, N, scale_factor = 1/16] holds all the scaling information for calculating the offset of the anchor.


The order of the proposal layer forward is:

1. Generate anchors, and use bbox regression for all anchors. (Generating anchors is exactly the same as training)

2. Sort the anchors in descending order according to the input positive scores, and extract the topN anchors, that is, extract the positive anchors after the correction position.

3. Limit the image positive to the boundary of the image.

4. Remove very small (definite length and width) positive anchors

5. Do NMS for the remaining positives

6. The proposals layer has three inputs: the classification results of positive and negative anchors, and the corresponding bbox reg results as the proper input.

The subsequent output is proposal = [x1, y2, x2, y2]. The output here corresponds to the scale of M * N. The detection ends here.
To summarize, RPN is to
generate anchors-> softmax classifier to extract positive anchors-> bbox reg regression to positive anchors-> proposal layer to generate proposals


### RoI pooling

RoI pooling is responsible for generating and collecting the proposal, and calculating the proposal feature maps, and sending it to the subsequent network. From Figure 2 we can see that RoI pooling has two inputs:
1. Original feature maps
2. Proposal boxes output by RPN (not the same size !!!)

#### Why do RoI pooling
For traditional CNN (VGG, ResNet), when the network is trained, the input image size must be a fixed value, and the network output is also a fixed-size vector. If the input dimensions of the images are not the same, it becomes very troublesome. There are two methods to solve:

1. Crop part from the image and transfer it to the network

2. Warp the image to the required size


It can be seen that no matter which method is adopted, either the complete structure of the image is destroyed after crop, or the original shape information of the image is destroyed by warp. RoI pooling is to solve the problem of how to deal with different sizes.

### RoI pooling principle

RoI works as follows:

Since the proposal corresponds to the M * N size, it is first mapped back to the size of the feature map (1/16) using the spatial_scale parameter.
The feature map area corresponding to each proposal is divided into a grid -max_pooling is performed on each part of the grid.

After this processing, the output results of the proposals even if the size is different are fixed. Figure 15 shows the implementation of fixed-length output.



![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast11.webp)

#### Classification
The input of the Classification part is the proposal feature maps. Through the full connect layer and softmax, calculate which category (person car television) each proposal belongs to, and output the cls_prob probability vector. At the same time, use bbox regression again to obtain the position offset bbox_pred of each proposal. Return to a more accurate detection frame. The classification network diagram is shown below

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast12.webp)

After getting 7 × 7 = 49 size feature feature maps from RoI pooling and sending it to the subsequent network, you can see that two things have been done:
1. classify the properties by full connection and softmax 2. perform bbox regression on the properties again, Get more accurate rect box
here to see the whole schematic view of the connection layer 17

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast13.webp)

Calculated as follows:

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast14.webp)

W and b are both pre-trained and the size is fixed. Of course, X and Y are fixed. Therefore, the need for RoI pooling is confirmed here.


### Faster RCNN training

Faster rcnn continues to train on the basis of already trained models (VGG, resnet). In fact, the training process has the following 6 steps:

1. On the trained model, train the RPN network, corresponding to stage1_rpn_train.pt

2. Use the RPN network trained in step 1, collect proposals, corresponding to rpn_test.pt

3. First Train the Fast RCNN network twice, corresponding to stage1_fast_rcnn_train.pt

4. Train the RPN network twice, corresponding to stage2_rpn_train.pt

5. Use the RPN network trained in step 4 to collect the proposals, corresponding to rpn_test.pt

6. Train the Fast RCNN the second time Network, corresponding to stage2_fast_rcnn_train.pt The
training process is similar to "iteration", and it is looped twice. "A similar alternating training can be run for more iterations, but we have observed negligible improvements". Next, explain these six training processes, as shown in Figure 18.


### Training the RPN Network

VGG is pre-trained and features are extracted. All layers in the Conv layers are drawn together (VGG / ResNet), shown in red circle.

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast15.webp)

The Loss of the entire network is as follows: The

above formula represents the anchors index, the positive softmax probability, and the GT predict probability (when IoU of the i-th anchor and GT is greater than 0.7, the anchor is considered positive,
= 1, and IoU <0.3 is considered to be negative, = 0, 0.3 ~ 0.7 do not participate in training). t represents a predict bounding box, and represents a corresponding GT box. As you can see, Loss is divided into two parts:
1. cls losss oftmax network, used to classify anchors as positive and negative networks.
2.Reg loss The L1 loss calculated by the rpnlossbbox layer is used for bbox regression network training. I multiplied it because I only care about the positive anchor, not the negative.
Because the two are very far apart, use parameter balancing, such as: ,, settings. Here, smooth L1 loss is used, and the calculation formula is as follows:

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast16.webp)

After understanding the mathematical principles, look at Figure 18 in reverse:
1. In the RPN training phase, the rpn-data layer will generate anchors for training in exactly the same manner as the proposal layer in the test phase.
2. For rpn_loss_cls, the input scores and
labels are 3. For rpn_loss_bbox, the input rpn_bbox_pred and rpn_bbox_target respectively correspond to and rpn_bbox_inside_weight.
The order of training and detection to generate storage anchors is exactly the same, so that the results can be used for detection.

Collecting Proposals Through a Trained RPN Network

The trained RPN network is used to obtain the Proposal RoI and obtain the positive softmax probability at the same time. As shown in Figure 20, the obtained information is stored in pickle. This network is essentially the same as the RPN network under test.

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast17.webp)

Training Faster RCNN Network

Read the previous pickle file to get the proposals and positive probability. The data layer is input to the network, and then:
1. The extracted proposals are transferred to the network as roi, as shown in the basket
2. Calculate bbox_inside_weights + bbox_outside_weights, the role is the same as RPN, and pass in the soomth_L1_loss layer, as shown in the green box in Figure 21

![title](https://github.com/entbappy/Branching-tutorial/raw/master/faster-rcnn/fast18.webp)

This will train the final softmax and the final bbox regression




# ➡️Day-53:-


## IOU, Mean Average Precision ,Non Maximum Suppression:-


## YOLO V1:-
# What is YOLO?

YOLO is an abbreviation for the term ‘You Only Look Once’. This is an algorithm that detects and recognizes various objects in a picture (in real-time). Object detection in YOLO is done as a regression problem and provides the class probabilities of the detected images.

YOLO algorithm employs convolutional neural networks (CNN) to detect objects in real-time. As the name suggests, the algorithm requires only a single forward propagation through a neural network to detect objects.

This means that prediction in the entire image is done in a single algorithm run. The CNN is used to predict various class probabilities and bounding boxes simultaneously.

The YOLO algorithm consists of various variants. Some of the common ones include tiny YOLO and YOLOv3.

## Why the YOLO algorithm is important

YOLO algorithm is important because of the following reasons:

- Speed: This algorithm improves the speed of detection because it can predict objects in real-time.
- High accuracy: YOLO is a predictive technique that provides accurate results with minimal background errors.
- Learning capabilities: The algorithm has excellent learning capabilities that enable it to learn the representations of objects and apply them in object detection.

<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/yolodetectionsystem.png">


### Model

YOLO regards target detection as a regression problem. It divides the image into S * S grids. If the center of the object falls into a grid, then this grid is responsible for detecting the object and the positions of these bounding boxes, Confidence, category probability . Confidence reflects how confident the model is about the presence of objects in the boxes and the accuracy of the predictions. Confidence level is defined as:

<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/Confidencelevel.png">

if the object does not mesh, the confidence is defined as 0, otherwise the confidence is equal to the predicted block and the real deposit and the ratio of the frame. Each bounding box contains 5 prediction values: x, y, w, h, and confidence, where x and y represent the center of the prediction box relative to the grid boundary, w and h are the width and height of the box, and confidence represents the prediction. The intersection of box and real box is better than IoU. The prediction result can be expressed by SxSx (B * 5 + C) parameters. Running YOLO on PASCAL VOC, S = 7, each grid predicts B = 2 objects, PASCAL VOC has 20 categories, so the number of categories is C = 20, and our prediction result is a 7x7x30 tensor.

<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/finaldetection.png">


Each grid also detects conditional category probabilities as: <img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/probclass.png">
This is the probability that a certain category of objects is contained in a grid. No matter how many boxes are contained in the grid, we only predict a set of class probabilities for each grid. When testing, we multiply the conditional class probability and the confidence of the prediction box to indicate that each box contains the confidence of a certain type of object. This score can represent the category probability and prediction accuracy of the box at the same time.
<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/probclass1.png">


### 2. Network Structure Design-GoogLe Net

The convolutional layer of the network is used to extract image features, while the fully connected layer predicts class possibilities and target locations.

The network uses GoogLe Net for image classification. There are 24 convolutional layers + 2 fully connected layers. However, instead of using GoogLe Net's inception module, 1 * 1 filters are used instead (reducing the number of parameters in the previous layer). ) + 3 * 3 convolution layer. The classification network is pre-trained on ImageNet with 224 * 224, and the target detection input image is twice the size of the classification network (448 * 448). The network structure is shown in the figure:
<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/architechtureyolo01.png">

We also trained a Fast YOLO to accelerate the prediction of target detection boundaries. It uses a neural network with only a few convolutional layers and a few filters. Other parameters are consistent with YOLO.


### 3. Training

First, the classification network is pre-trained on ImageNet containing 1000 classes. For pre-training, the first 20 convolutional layers are followed by an average pooling layer and a fully connected layer. This model is then applied to the target detection network. Four new convolutional layers and two fully connected layers are added, and the weights are randomly initialized. Object detection usually requires finer-grained visualization information, so the resolution of the input image is increased from 224 * 224 to 448 * 448. The last layer predicts both the class likelihood and the position of the bounding box. Normalize the width and height of the bounding box so that they are distributed in the 0-1 interval. The x and y parameters are the offsets of the prediction box from the grid position and are also limited to 0-1. The last layer uses a linear activation function, while all other layers use Leaky ReLU activation functions, as follows:

<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/Trainingyolo1.png">


### 4. Loss function

Optimize the output using square sum loss because it is easier to manipulate, but:

(1) It considers that the positioning error and the classification error have the same weight, and in each image, many grids do not contain any objects, which will make these grids have a confidence of 0, overriding the gradient of those grids that contain objects Causes model instability. To solve this problem, we increase the loss of box regression prediction, reduce the loss of those boxes without objects , use 2 parameters <img src =  "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/a.png"> and <img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/b.png">  adjust it, where <img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/coord.png"> and <img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/noobj.png">



(2) It thinks that the losses of large boxes and small boxes have the same weight. In our grid design, it is obvious that the losses of large boxes are more important than the losses of small boxes . To solve this problem, when predicting the bounding box, instead of directly using width / height, use the square root of width / height .

Each grid can predict multiple bounding boxes. During training, a predictor with the highest IoU and true value is designated to predict this goal . This will make each predictor predict a specific size, aspect ratio, and object category. Do better.

The loss function is defined as ( x, y loss at the center of the prediction box + loss w, h of the prediction box width and loss + confidence loss + classification loss ):

Not all outputs of the network need to be calculated for loss:

* There is a cell falling into the center of the object, and the classification loss needs to be calculated.
* Both predictors have to calculate the confidence loss,
* The predictor with the larger bounding box and greater truth IOU needs to calculate the xywh loss.
* The most critical part is that there is no cell falling into the center of the object, and only the loss of confidence needs to be calculated.

<img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/lossyolo1.png">

* $S^2$ represents the number of grids, which is 7x7 in the text. B represents the number of prediction frames for each grid, which is 2 in the text.

* <img src = "https://raw.githubusercontent.com/entbappy/Branching-tutorial/master/yolo/iob.png">Values are 0 and 1, indicating whether there are targets in the cell.

* λcoord = 5, λnoobj = 0.5. It is a balance factor that balances the box coordinate loss and the box loss without objects.

* The first line uses the sum of squares error as the loss function for the center position prediction.

* The second line uses the square root sum error as a loss function for width and height.

* The third and fourth lines use the sum of squares error as a loss function for confidence.

* The fifth line uses the sum of squares error as a loss function for the category probability.

* Finally, several loss functions are added together as the loss function of yolo v1.


### 5. Hyperparameter setting

batch_size = 64, momentum = 0.9, weight decay = 0.0005

The first epochs and learning rate slowly increase from 0.001 to 0.01. If starting from a high learning rate, the gradient may be unstable, which may cause model divisions. Then train 75 iterations with a learning rate of 0.01, 30 iterations with 0.001, and 30 iterations with 0.0001.

In order to prevent overfitting, dropout and data enhancement are used, and the dropout ratio is 0.5


### 6.NMS

Some large targets may be located by multiple grids at the same time. NMS can solve this multiple prediction problem.


### 7. YOLO advantages

(1) Fast. Because we regard it as a regression problem, without the need for complex pipelines , when testing, we only need to put the new image into the neural network and run it. It can achieve real-time effects, and mAP is higher.

(2) Have a global understanding of the image. Unlike the technology based on sliding window and region proposal, YOLO implicitly encodes the context information of the target's category and its appearance, while Fast RCNN cannot see the larger context information. YOLO uses the characteristics of the entire image to predict each bounding box , and simultaneously predicts all categories of bounding boxes in the image, that is, it has a global understanding of the image.

(3) The learning of goals is more general.

(4) High accuracy and can quickly locate the target and position in the image, even small targets.

(5) The design of the grid unit can alleviate the problem of detecting the same object multiple times.

(6) Provides fewer bounding boxes, only 98 images per image , and about 2000 selective search.

(7) Combine these separate components into a single joint optimization model.

(8) YOLO is a more versatile detector that can detect multiple objects simultaneously


### 8.Flaws of YOLO

(1) Since each grid only predicts 2 bounding boxes, this limits the number of objects that the model can predict

(2) Downsampling is used many times, so the bounding box of the prediction model uses relatively rough features.



## Paper
[Link](https://arxiv.org/pdf/1506.02640.pdf)


## YOLO V2:-


# YOLOv2 Model Architecture

YOLO (You Only Look Once) is a state-of-the-art real-time object detection system. YOLOv2 is an improvement over the original YOLO model, offering better accuracy and speed.

![YOLOv2 Architecture](https://www.researchgate.net/publication/336177198/figure/fig4/AS:809235726229506@1569948240717/The-architecture-of-YOLOv2.ppm)
## Overview

YOLOv2 works by dividing the input image into an SxS grid. Each grid cell predicts multiple bounding boxes and their corresponding class probabilities. YOLOv2 utilizes a single convolutional network to predict the bounding boxes and class probabilities directly from full images in one evaluation.

## Key Components

### Darknet-19

YOLOv2 uses a variant of the Darknet architecture called Darknet-19. It consists of 19 convolutional layers followed by 5 max-pooling layers. Darknet-19 serves as the feature extractor for YOLOv2.

### Convolutional Layers

The convolutional layers in YOLOv2 extract features from the input image. These layers are responsible for detecting various patterns and objects in the image.

### Bounding Box Prediction

Each grid cell predicts multiple bounding boxes along with their corresponding confidence scores and class probabilities. YOLOv2 refines these bounding boxes using techniques like anchor boxes and intersection over union (IoU).

### Training

YOLOv2 is trained end-to-end on a large dataset of labeled images. It optimizes a loss function that combines localization error, classification error, and confidence error. Training YOLOv2 requires significant computational resources due to its deep architecture.

## Performance

YOLOv2 achieves state-of-the-art performance in terms of both accuracy and speed. It can detect a wide range of objects in real-time, making it suitable for applications like autonomous driving, surveillance, and robotics.

## Citation

If you find YOLOv2 useful in your research or project, please consider citing the original paper:



## ➡️Day-54:-

### YOLO V3:-



### YOLO V4:-

### YOLO V4 Part -2:-

### YOLO V5:-
 
### YOLO V6:-




### YOLO V7:-



## ➡️Day-55:-
```bash

Facial Recognition:-

```
### Siamese Neural Network:-

A Siamese neural network (SNN) is a type of artificial neural network that uses the same weights to calculate similar output vectors from two different input vectors. SNNs are made up of two or more identical sub-networks, each with the same configuration, parameters, and weights. SNNs are used to compute similarity functions and identify if two data points are dissimilar.


## Loss Function in Siamese Neural Network:-

* Triplet Loss.
* Contrastive Loss.


### Triplet Loss:-

![Screenshot 2024-05-04 201719.png](<attachment:Screenshot 2024-05-04 201719.png>)

### Contrastive Loss:-
![Screenshot 2024-05-04 201508.png](<attachment:Screenshot 2024-05-04 201508.png>)




## ➡️Day-55:-
```bash

* GAN:-


* DCGAN:-
* STYLE GAN:-
* W GAN:-

* DC Gan Practical Implimentation:-
This tutorial has shown the complete code necessary to write and train a GAN. As a next step, you might like to experiment with a different dataset, for example the Large-scale Celeb Faces Attributes (CelebA) dataset [available on Kaggle](https://www.kaggle.com/jessicali9530/celeba-dataset). To learn more about GANs see the [NIPS 2016 Tutorial: Generative Adversarial Networks](https://arxiv.org/abs/1701.00160).



```