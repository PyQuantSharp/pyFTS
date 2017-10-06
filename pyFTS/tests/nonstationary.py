import os
import numpy as np
from pyFTS.common import Membership
from pyFTS.nonstationary import common,perturbation,util,nsfts
from pyFTS.partitioners import Grid
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("/home/petronio/Dropbox/Doutorado/Codigos/")

"""
def generate_heteroskedastic_linear(mu_ini, sigma_ini, mu_inc, sigma_inc, it=10, num=35):
    mu = mu_ini
    sigma = sigma_ini
    ret = []
    for k in np.arange(0,it):
        ret.extend(np.random.normal(mu, sigma, num))
        mu += mu_inc
        sigma += sigma_inc
    return ret


lmv1 = generate_heteroskedastic_linear(1,0.1,1,0.3)
#lmv1 = generate_heteroskedastic_linear(5,0.1,0,0.2)
#lmv1 = generate_heteroskedastic_linear(1,0.3,1,0)

ns = 5 #number of fuzzy sets
ts = 200
train = lmv1[:ts]
test = lmv1[ts:]
w = 25
deg = 4

tmp_fs = Grid.GridPartitioner(train[:35], 10)

fs = common.PolynomialNonStationaryPartitioner(train, tmp_fs, window_size=35, degree=1)

nsfts1 = nsfts.NonStationaryFTS("", partitioner=fs)

nsfts1.train(train[:100])

print(fs)

print(nsfts1)

tmp = nsfts1.forecast(test[:10], time_displacement=200)

print(tmp)
"""

passengers = pd.read_csv("DataSets/AirPassengers.csv", sep=",")
passengers = np.array(passengers["Passengers"])

ts = 80

trainp = passengers[:ts]
testp = passengers[ts:]

tmp_fsp = Grid.GridPartitioner(trainp[:50], 10)

fsp = common.PolynomialNonStationaryPartitioner(trainp, tmp_fsp, window_size=20, degree=1)

nsftsp = nsfts.NonStationaryFTS("", partitioner=fsp)

nsftsp.train(trainp[:50])

print(fsp)

print(nsftsp)

tmpp = nsftsp.forecast(testp, time_displacement=ts)

print(testp)
print(tmpp)

#fig, axes = plt.subplots(nrows=1, ncols=1, figsize=[15,5])

"""
axes.plot(testp, label="Original")
#axes.plot(tmpp, label="NSFTS")

handles0, labels0 = axes.get_legend_handles_labels()
lgd = axes.legend(handles0, labels0, loc=2)
"""