import os
import sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))

from course import course_details




def payment_details():
    print("this is the payment file")

course_details.course_detail()