
# coding: utf-8


import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

def demodFM(fase,cuadratura):
	dFase=np.diff(fase)
	dCuadratura=np.diff(cuadratura)
	n=len(dFase)
	deltaTheta=np.zeros(n)
	for i in range(n):
		deltaTheta[i]=(fase[i]*dCuadratura[i]-cuadratura[i]*dFase[i])/(fase[i]**2+cuadratura[i]**2)
	return deltaTheta