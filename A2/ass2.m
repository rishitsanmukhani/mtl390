% U(5,14)
data = load('2013CS10255_SANMUKHANI RISHIT GOPAL.csv');

% Estimating a = min(x_i)
% U(5, 14) -> U(0,9)
data = data - 5;

% Values
n = size(data,1);
m = max(data);
mu = mean(data);
std_dev = std(data);

% Methods of moment estimate
mom_estimate = 2*mu;
mle_estimate = m;
umvue_estimate = m + m/n;

% Interval Estimate
z_005 = 2.57;
z_025 = 1.96;
z_05 = 1.65;

conf_interval_1 = [mu - z_005*(std_dev/sqrt(n)), mu + z_005*(std_dev/sqrt(n))];
conf_interval_2 = [mu - z_025*(std_dev/sqrt(n)), mu + z_025*(std_dev/sqrt(n))];
conf_interval_3 = [mu - z_05*(std_dev/sqrt(n)), mu + z_05*(std_dev/sqrt(n))];

theta_1 = 2*conf_interval_1;
theta_2 = 2*conf_interval_2;
theta_3 = 2*conf_interval_3;
