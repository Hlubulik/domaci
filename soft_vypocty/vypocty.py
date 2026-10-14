
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

#matlab 
    a = 9.81;
t = 0:0.1:5;
s = 0.5 * a * t.^2;
plot(t, s)
xlabel('cas t [s]')
ylabel('draha s [m]')
grid on
hold on
data = table(t', s', 'VariableNames', {'t', 's'});
writetable(data, 'volny_pad.csv');
title('Dráha při volném pádu');
