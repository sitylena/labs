from scipy.stats import norm, expon, uniform
import matplotlib.pyplot as plt
import numpy

# my_norm = norm(5, 1)
# viborka = my_norm.rvs(size=1000)
# print(viborka)

my_exp = expon(0.2)
viborka = my_exp.rvs(size=1000)
# print(viborka)

my_uni = uniform(3, 7)
viborka = my_uni.rvs(size=1000)
# print(viborka)

x = numpy.linspace(0, 4, 100)
pdf = my_exp.pdf(x)

x = numpy.linspace(0, 4, 100)
cdf = norm.cdf(x)

plt.plot(x, cdf)
plt.step(x, cdf)
plt.ylabel('$f(x)$')

plt.xlabel('$x$')
plt.show()

