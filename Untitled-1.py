import numpy as np
import matplotlib.pyplot as plt

g = 9.81
#t = np.arrange(0,11,1)
t = np.linspace(0,100,1001)

s = 0.5*g*t**2

plt.figure()
plt.title('draha')
plt.plot(t,s)
plt.xlabel('cas t[s]')
plt.ylabel('draha s[m]')
plt.legend('a =g')
plt.grid(True)
plt.show ()


#doinstalovat do terminalu ve vsc 
#python -m pip install notebook
#python -m pip install numpy
#python -m pip install matplotlib