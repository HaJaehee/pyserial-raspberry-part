#!/usr/bin/env python

l = [15, 18, 2, 36, 12, 78, 5, 6, 9]

#import numpy as np
#print np.mean(l)

#print sum(l) / float(len(l))

print reduce(lambda x, y: x + y, l) / len(l)
