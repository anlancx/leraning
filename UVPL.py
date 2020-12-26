import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

UV_date = pd.read_csv(r'D:\CCM003-UV.csv')
PL_date = pd.read_excel(r'D:\CCM003-PL.xlsx', header=46)

max_min_scaler = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))

x1 = UV_date['nm']
y1 = UV_date[['Abs']].apply(max_min_scaler)
x2 = PL_date['nm']
y2 = PL_date[['Data']].apply(max_min_scaler)

plt.plot(x1,y1,label='Abs in TOL')
plt.plot(x2,y2,label='PL in TOL')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity (a.u.)')
plt.legend()
plt.show()

