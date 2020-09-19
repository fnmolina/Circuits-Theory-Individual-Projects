import matplotlib.pyplot as plt
import numpy as np



def transferInversor(R1, R2, frange, k, wb):
    Vin = [((9*R1)/R2)*(np.sqrt((((2*np.pi)/wb)**2)*(i**2) + 1)) for i in frange]

    return Vin

def transferNoInversor(R1, R2, R4, q1, q2, wb, frange):
    Vin = [(9/(100000*(R1+R2)*R4))*(np.sqrt((((2*np.pi*q1)/wb)**2)*(i**2) + q2**2)) for i in frange]

    return Vin

frange = np.arange(10e1,1e6, 10)

#### Inversor ###
"""
Vin1 = transferInversor(2700, 27000, frange, 21, 57143)
Vin2 = transferInversor(2700, 2700, frange, 3, 400000)
Vin3 = transferInversor(27000, 2700, frange, 1.2, 1000000)
""" 
### No inversor ###

Vin1 = transferNoInversor(2700, 27000,10000, 377190000, 3.42904E+12, 12, frange)
Vin2 = transferNoInversor(2700, 2700, 10000, 68580000, 3.42904E+12, 12, frange)
Vin3 = transferNoInversor(27000, 2700, 100000, 3771900000, 3.42904E+14, 12, frange)


plt.semilogx(frange, Vin1, label = 'Caso 1')
plt.semilogx(frange, Vin2, label = 'Caso 2', )
plt.semilogx(frange, Vin3, label = 'Caso 3')
plt.xlabel('f [Hz]')
plt.ylabel('Vin max') 
plt.grid(True, which="both")
plt.legend()
plt.show()
