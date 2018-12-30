x = -1:1:1;
y = abs(x);
xx = -1:1/10:1;
 
yy = interp1(x,y,xx,'linear');

plot(xx, yy)