# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:11:01 2016

@author: Tmn07
"""

from x.p1 import *
print "from x.p1 import *"
print 'a,b=',
print a,
print b

fg()

import p1
print 'import p1'
print 'p1.a,p1.b=',
print p1.a,
print p1.b

print 'a,b=',
print a,
print b

p1.fg()
from p1 import *
print "from p1 import *"
print 'a,b=',
print a,
print b