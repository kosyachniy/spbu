load('datatx4.mat');

p1 = polyfit(t, xx, 2);
p2 = polyfit(t, yy, 4);
appr1 = polyval(p1, t);
appr2 = polyval(p2, t);

p1
p2

er1 = (appr1 ./ xx) - 1;
er2 = (appr2 ./ yy) - 1;

hold on;
grid on;
plot(t, xx, 'b');
plot(t, appr1, 'c');
plot(t, yy, 'r');
plot(t, appr2, 'm');

hold off;
figure;
plot(t, er1, 'b');

hold on;
grid on;
plot(t, er2, 'r');
hold off;