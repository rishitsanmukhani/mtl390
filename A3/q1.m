data = load('data.csv');

fprintf('size = %d\n', size(data, 1));
fprintf('mean = %f\n', mean(data));
fprintf('std  = %f\n', std(data));
fprintf('var  = %f\n', var(data));

H = histogram(data, 5:14)
[D, PD] = allfitdist(data, 'PDF')
[D, PD] = allfitdist(data, 'CDF')