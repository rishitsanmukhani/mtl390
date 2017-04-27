% Importing regression data
data = importdata('regression_data.csv');
data = data.data;

% Dependent variables and independent variables
Y = data(:, 1);
X = data(:, 2:end);
[m,n] = size(X);

X = [ones(m,1), X];

% Analytical solution
theta = inv(X'*X)*(X'*Y);
fprintf('Intercept: %f\n', theta(1));
fprintf('Point Estimates: %f %f\n', theta(2), theta(3));

% Plotting the data
[X1_grid, X2_grid] = meshgrid(-3:0.1:3, -3:0.1:3);
Y_grid = theta(1) + theta(2)*X1_grid + theta(3)*X2_grid;
mesh(X1_grid, X2_grid, Y_grid);
hold on;
scatter3(X(:,2), X(:, 3), Y, 'filled');

% Estimation of variance, R-square, adjusted R-square
Yp = X*theta;
SSE = sum((Y - Yp).^2);
MSE = SSE/(m-n-1);
SST = sum((Y - mean(Y)).^2);
MST = SST/(m-1);

variance = MSE;
R_sq = 1 - (SSE/SST);
R_sq_adj = 1 - (MSE/MST);
fprintf('\n\nVariance: %e\nR-square: %e\nAdjusted R-square: %e\n', variance, R_sq, R_sq_adj);

% t-test
C = variance*inv(X'*X);
t1 = theta(2)/sqrt(C(2, 2)); 
t2 = theta(3)/sqrt(C(3,3));
fprintf('\n\nt1 = %e\n', t1);
fprintf('t2 = %e\n', t2);

% F-test
f = (MST - MSE)/MSE;
fprintf('\n\nf = %e\n', f);
