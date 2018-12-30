x1 = ones(1, 2);
x0 = zeros(1, 2);
f = func(x1);
F = 0;
delt = 0.01;

while (abs(f - F) > eps) || (max(abs(x0 - x1)) > eps)
	x0 = x1;
	gra = gradient(x0);
	x1 = x0 - delt * gra;	 
	F = f;
	f = func(x1);
	
	while f - F > 0
		delt = delt / 2;
		x1 = x0 - delt / 2;
		f = func(x1);
	end
end

f
x1


function res = gradient(X)
	eps = 0.0000001;
	res = X;
	n = length(X);
	
	for k=1:n
		Xk = X;
		Xk(k)= X(k) + eps;
		res(k) = (func(Xk) - func(X)) / eps;
	end
end

function F = func(X)
	F = ((sin(X(1)) ^ 2) * cos(X(1)/10) - X(2)) ^ 2 + (X(1) - 5 * X(2) - 1) ^ 2;
end