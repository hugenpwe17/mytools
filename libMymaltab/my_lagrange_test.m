clc
clear
close all

x0 = linspace(0,2*pi,10);
y0 = sin(x0);
plot(x0,y0);
hold on

x = linspace(0,2*pi,100);
y = my_lagrange(x0,y0,x);
y_real = sin(x);
plot(x,y);
plot(x,y_real);

legend('origin','interp','real');