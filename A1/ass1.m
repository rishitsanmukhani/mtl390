data = load('2013CS10255_SANMUKHANI RISHIT GOPAL.csv');

[D, PD] = allfitdist(data, 'PDF')
[D, PD] = allfitdist(data, 'CDF')