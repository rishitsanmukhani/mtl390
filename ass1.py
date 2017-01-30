import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

data = np.genfromtxt('2013CS10255_SANMUKHANI RISHIT GOPAL.csv')

def frequency_table(x, nbins):
  print("Frequency Table:")
  hist, bins = np.histogram(x, nbins)
  for idx in range(0, nbins):
    print("{} - {} = {}".format(bins[idx], bins[idx+1], hist[idx]))
  print("\n")

def histogram_plot(x, nbins):
  print("Generating histogram plot...")
  plt.hist(x, nbins)
  plt.title("Histogram Plot")
  plt.savefig("histogram.png")
  plt.close()
  print("Done\n")

def bar_plot(x):
  print("Generating bar plot...")
  freq = [1]*len(x)
  for idx in range(0,len(x)):
    freq[idx]=idx
  x = np.sort(x)
  plt.bar(freq, x)
  plt.title("Bar Plot")
  plt.savefig("bar.png")
  plt.close()
  print("Done\n")

def box_plot(x):
  print("Generating box plot...")
  plt.boxplot(x)
  plt.savefig("box.png")
  plt.title("Box Plot")
  plt.close()
  print("Done\n")

def measures(x):
  q75, q25 = np.percentile(x,[75, 25])
  print("Mean                     : {}".format(np.mean(x)))
  print("Median                   : {}".format(np.median(x)))
  print("Coefficient of variation : {}".format(st.variation(x)))
  print("Coefficient of skewness  : {}".format(st.skew(x)))
  print("Coefficient of kurtosis  : {}".format(st.kurtosis(x)))
  print("Inter-quartile range     : {}".format(q75 - q25))   

frequency_table(data, 10)
histogram_plot(data, 10)
bar_plot(data)
box_plot(data)
measures(data)
