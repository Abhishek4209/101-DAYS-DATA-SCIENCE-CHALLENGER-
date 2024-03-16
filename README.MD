# **101-DAYS-DATA-SCIENCE-CHALLENGER**


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