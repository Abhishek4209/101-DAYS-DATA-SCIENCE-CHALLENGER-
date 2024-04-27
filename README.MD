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

