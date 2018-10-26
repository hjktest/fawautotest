#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/14 13:18
# software: PymCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts=ts.cumsum()
test=ts.plot()
