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