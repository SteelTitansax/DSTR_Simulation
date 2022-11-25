# Equation design of an DSTR
# -------------------------

# Libraries
# -------------------------
from scipy.integrate import quad

# Variable declarations
# ---------------------

k = 0.3  # 1/min
Ca0 = 10  # mol/l
X =0.8

# Kinetics
# --------
def rA(X):
    Ca = Ca0 * (1 - X)
    return k * Ca

def integral(X):
    return X / rA(X)


IntergerResult, err = quad(integral, 0, X)
T = Ca0 * IntergerResult
print("Volumen : " + str(T))