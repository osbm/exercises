# import math module and calculate the cumulative disribution function of normal distribution
import math


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# calculate the probability of normal distribution
def normal_pdf(x, mu=0, sigma=1):
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / math.sqrt(2 * math.pi * sigma ** 2)

# chi-squared cdf distribution
def chi_squared_cdf(x, k):
    return math.gamma((k + 1) / 2) / (math.gamma(k / 2) * math.sqrt(k * math.pi)) * (1 + x / k) ** (-(k + 1) / 2)
    
# t-distribution
def t_cdf(x, k):
    return 1 - math.erf(x / math.sqrt(k))
from scipy import stats
print(stats.t.cdf(2.086,20))

print(t_cdf(2.086,20))

#print(chi_squared_cdf(2.447, 6))

print("---------")
print(normal_cdf(1.282))
print(normal_cdf(1.333))
print(normal_cdf(1.645))
print(normal_cdf(1.960))
print("---------")
print(stats.norm.cdf(1.282))
print(stats.norm.cdf(1.333))
print(stats.norm.cdf(1.645))
print(stats.norm.cdf(1.960))


