#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#
# File: a.py
# Author: suweiyue(suweiyue@baidu.com)
# Date: 2021/04/13 21:58:37
#
########################################################################
"""
    Comment.
"""

import numpy as np
import pickle
from tqdm import tqdm


train_hrt = np.load("./dataset/wikikg90m_kddcup2021/processed/train_hrt.npy", mmap_mode="r")

data = dict()

for h, r, t in tqdm(train_hrt):
    if h not in data:
        data[h] = dict()
    if not r in data[h]:
        data[h][r] = 1
    else:
        data[h][r] += 1

del train_hrt

for h in data:
    h_sum = sum(data[h].values())
    for r in data[h]:
        data[h][r] /= h_sum

pickle.dump(data, open("feature_output/h2r_prob2.pkl", "wb"))
