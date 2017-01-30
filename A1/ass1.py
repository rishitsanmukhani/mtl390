import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# Reading data
data = np.genfromtxt('2013CS10255_SANMUKHANI RISHIT GOPAL.csv')

# Generating frequency table
def frequency_table(x, nbins):
  print("Frequency Table:")
  hist, bins = np.histogram(x, nbins)
  for idx in range(0, nbins):
    print("{} - {} = {}".format(bins[idx], bins[idx+1], hist[idx]))
  print("\n")

# Generating histogram plot
def histogram_plot(x, nbins):
  print("Generating histogram plot...")
  plt.hist(x, nbins)
  plt.title("Histogram Plot")
  plt.xlabel("Value")
  plt.ylabel("Frequency")
  plt.tight_layout()
  plt.savefig("histogram.png")
  plt.close()  
  print("Done\n")

# Generating bar plot
def bar_plot(x,nbins):
  print("Generating bar plot...")
  plt.hist(x, nbins, histtype='bar', rwidth=0.4)
  plt.title("Bar Plot")
  plt.ylabel("Frequency")

  # Adding the labels to each bar
  # The labes represent the interval
  hist, bins = np.histogram(x, nbins)
  bins = bins + ((bins[1]-bins[0])/2)
  labels = ['']*nbins
  for idx in range(0, nbins):
    labels[idx] = '{:.2f}-{:.2f}'.format(bins[idx], bins[idx+1])

  plt.xticks(bins, labels, rotation=45)
  plt.tight_layout()
  plt.savefig("bar_plot.png")
  plt.close()
  print("Done\n")

# Generating box plot
def box_plot(x):
  print("Generating box plot...")
  plt.boxplot(x)
  plt.title("Box Plot")
  plt.ylabel("Value")
  plt.savefig("box.png")
  plt.close()
  print("Done\n")

# Calculating the measures using scipy.stats
def measures(x):
  q75, q25 = np.percentile(x,[75, 25])
  print("Mean                     : {}".format(np.mean(x)))
  print("Median                   : {}".format(np.median(x)))
  print("Coefficient of variation : {}".format(st.variation(x)))
  print("Coefficient of skewness  : {}".format(st.skew(x)))
  print("Coefficient of kurtosis  : {}".format(st.kurtosis(x)))
  print("Inter-quartile range     : {}".format(q75 - q25))
  print("\n")

frequency_table(data, 20)
histogram_plot(data, 20)
bar_plot(data, 20)
box_plot(data)
measures(data)