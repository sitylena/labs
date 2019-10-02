from scipy.stats import norm, expon, uniform, poisson
import matplotlib.pyplot as plt
import numpy

# my_norm = norm(5, 1)
# viborka = my_norm.rvs(size=1000)
# plt.hist(viborka, normed=True, bins=20)
#
# x = numpy.linspace(0, 10, 100)
# pdf = my_norm.pdf(x)
# plt.plot(x, pdf)
#
# plt.show()
#
#
# my_exp = expon(0.2)
# viborka = my_exp.rvs(size=1000)
# plt.hist(viborka, normed=True, bins=20)
#
# x = numpy.linspace(0, 10, 100)
# pdf = my_exp.pdf(x)
# plt.plot(x, pdf)
#
# plt.show()
#
#
# my_uni = uniform(3, 4)
# viborka = my_uni.rvs(size=1000)
# plt.hist(viborka, normed=True, bins=10)
#
# x = numpy.linspace(2, 8, 100)
# pdf = my_uni.pdf(x)
# plt.plot(x, pdf)
#
# plt.show()

my_poisson = poisson(5)
viborka = my_poisson.rvs(size=1000)

x = numpy.linspace(0, 12, 13)

num_in_viborka = []
for x1 in x:
    num_in_viborka.append(len(list(filter(lambda n: n == x1, viborka.tolist())))/1000)
plt.plot(x, num_in_viborka, 'o')
pmf = my_poisson.pmf(x)
plt.plot(x, pmf, 'o')
plt.ylabel('$P(X=x)$')
plt.xlabel('$x$')
plt.show()
