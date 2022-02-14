import math
# define a function to sum two numbers
def sum(a, b):
    return a + b


# define a function to multiply two numbers
def multiply(a, b):
    return a * b

# define a function to subtract two numbers
def subtract(a, b):
    return a - b

# define a function to divide two numbers
def divide(a, b):
    return a / b
# define a function to square a number
def square(a):
    return a * a
def squareroot(a):
    return a ** 0.5
def cube(a):
    return a * a * a
def cubicroot(a):
    return a ** (1/3)
def power(a,b):
    return a ** b
def log(a):
    return math.log(a)
def ln(a):
    return math.log(a)
def exp(a):
    return math.exp(a)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def arcsin(a):
    return math.asin(a)
def arccos(a):
    return math.acos(a)
def arctan(a):
    return math.atan(a)
def arctan2(a,b):
    return math.atan2(a,b)
def sinh(a):
    return math.sinh(a)
def cosh(a):
    return math.cosh(a)
def tanh(a):
    return math.tanh(a)
def arcsinh(a):
    return math.asinh(a)
def arccosh(a):
    return math.acosh(a)
def arctanh(a):
    return math.atanh(a)
def deg2rad(a):
    return a * math.pi / 180
def rad2deg(a):
    return a * 180 / math.pi
def factorial(a):
    return math.factorial(a)
def gamma(a):
    return math.gamma(a)
def lgamma(a):
    return math.lgamma(a)
def erf(a):
    return math.erf(a)
def erfc(a):
    return math.erfc(a)
def erfinv(a):
    return math.erfinv(a)
def erfcinv(a):
    return math.erfcinv(a)
def gamma_inc(a,b):
    return math.gamma(a+1) * math.exp(-b)
def gamma_inc_inv(a,b):
    return math.gamma_inc(a,1/b)
def gamma_inc_inv_lower(a,b):
    return math.gamma_inc_inv(a,b)
def gamma_inc_inv_upper(a,b):
    return math.gamma_inc_inv(a,b)
def gamma_inc_lower(a,b):
    return math.gamma_inc(a,b)
def gamma_inc_upper(a,b):
    return math.gamma_inc(a,b)
def beta(a,b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a+b)
def beta_inv(a,b):
    return math.gamma_inc_inv(a+b,a)
def beta_inv_lower(a,b):
    return math.gamma_inc_inv_lower(a+b,a)
def beta_inv_upper(a,b):
    return math.gamma_inc_inv_upper(a+b,a)
def beta_lower(a,b):
    return math.gamma_inc_lower(a+b,a)
def beta_upper(a,b):
    return math.gamma_inc_upper(a+b,a)
def digamma(a):
    return math.digamma(a)
def trigamma(a):
    return math.trigamma(a)
def polygamma(a,b):
    return math.polygamma(a,b)
def polygamma_lower(a,b):
    return math.polygamma_lower(a,b)
def polygamma_upper(a,b):
    return math.polygamma_upper(a,b)
def psi(a):
    return math.psi(a)
def zeta(a):
    return math.zeta(a)
def hurwitz_zeta(a,b):
    return math.zeta(a,b)
def dirichlet_eta(a,b):
    return math.zeta(a,b)
def dirichlet_eta_lower(a,b):
    return math.zeta(a,b)
def dirichlet_eta_upper(a,b):
    return math.zeta(a,b)
def dirichlet_eta_star(a,b):
    return math.zeta(a,b)
def dirichlet_eta_star_lower(a,b):
    return math.zeta(a,b)
def dirichlet_eta_star_upper(a,b):
    return math.zeta(a,b)
def dirichlet_beta(a,b):
    return math.beta(a,b)
def dirichlet_beta_lower(a,b):
    return math.beta(a,b)
def dirichlet_beta_upper(a,b):
    return math.beta(a,b)
def dirichlet_beta_star(a,b):
    return math.beta(a,b)
def dirichlet_beta_star_lower(a,b):
    return math.beta(a,b)
def dirichlet_beta_star_upper(a,b):
    return math.beta(a,b)
def dirichlet_gamma(a,b):
    return math.gamma(a,b)
def dirichlet_gamma_lower(a,b):
    return math.gamma(a,b)
def dirichlet_gamma_upper(a,b):
    return math.gamma(a,b)
def dirichlet_gamma_star(a,b):
    return math.gamma(a,b)
def dirichlet_gamma_star_lower(a,b):
    return math.gamma(a,b)
