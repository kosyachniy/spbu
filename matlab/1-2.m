x = -1:1:1;
y = abs(x);
xx = -1:0.1:1;
 
p = polyfit(x, y, 2);
yy = polyval(p, xx);

plot(xx, yy);
plot(x, y);