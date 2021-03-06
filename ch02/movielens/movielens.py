# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:43:49 2016

@author: MKeenan
"""

import pandas as pd
import os
encoding = 'latin1'


upath = os.path.expanduser('/users.dat')
rpath = os.path.expanduser('/ratings.dat')
mpath = os.path.expanduser('/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)
#%%