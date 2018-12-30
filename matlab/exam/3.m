m = 2;
x1 = ones(1,m);
x0 = zeros(1,m);


Fnew = func(x1);
F = 0;
deltat = 0.01;

while (abs(Fnew - F) > e) || (max(abs(x0 - x1)) > e)
	x0 = x1;
	Gr = grad(x0);
	x1 = x0 - deltat * Gr;	 
	F = Fnew;
	Fnew = func(x1);
	
	while Fnew - F > 0
		deltat = deltat / 2;
		x1 = x0 - deltat / 2;
		Fnew = func(x1);
	end
end

Fnew
x1


function Gr = grad(X)
	e = 0.0000001;
	Gr = X;
	n = length(X);
	
	for k=1:n
		Xk = X;
		Xk(k)= X(k)+e;
		Gr(k) = (func(Xk) - func(X)) / e;
	end
end

function F = func(X)
	F = (sin(X(1)) ^ 2 * cos(X(1)/10) - X(2)) ^ 2 + (X(1) - 5 * X(2) - 1) ^ 2;
end