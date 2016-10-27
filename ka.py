from numpy import *
import matplotlib.pyplot as plt

pHs = [3.82, 4.05, 4.25, 4.61, 4.81, 5.07]

vols = [60.0, 65.0, 70.0, 80.0, 85.0, 90.0]
ohvols = [10.0, 15.0, 20.0, 30.0, 35.0, 40.0]

def cvcv(c1, v1, v2):
    return (c1 * v1) / v2

x_conc = []
hx_conc = []

for (vol, oh) in zip(vols, ohvols):
    oh_i = cvcv(0.1, oh, vol)
    hx_i = cvcv(0.1, 50.0, vol)

    x_conc.append(oh_i) 
    hx_conc.append(hx_i - oh_i)

h_conc = list(map(lambda x: 10**(-x), pHs))

ka = []
for (h, x, hx) in zip(h_conc, x_conc, hx_conc):
    ka.append(h * x / hx)

x_over_hx = []
for (x, hx) in zip(x_conc, hx_conc):
    x_over_hx.append(log10(x/hx))

pKa = list(map(lambda x: -log10(x), ka))

print(x_conc)
print(hx_conc)
print(h_conc)
print(ka)
print(pKa)
print(x_over_hx)
print(mean(pKa))

m, b = polyfit(pHs, x_over_hx, 1)
print(b)

plt.xlabel('pH')
plt.ylabel('log([X]/[HX])')
plt.plot(pHs, x_over_hx, 'bo')
plt.plot(pHs, list(map(lambda x: m*x + b, pHs)), '-')
plt.show()
