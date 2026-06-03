import mpmath
mpmath.mp.dps = 300  # 300 dígitos de precisión

# Cálculo de C_Stokes
def integrando(t):
    return mpmath.hyp2f1(0.5, 0.5, 1.0, t) * mpmath.exp(t)

C = mpmath.quad(integrando, [0, 1], maxdegree=10)
print(f"C_Stokes = {C}")

# Valores de referencia
Omega1 = mpmath.gamma(mpmath.mpf('1')/4)**2 / (2 * mpmath.sqrt(2*mpmath.pi))
e_val  = mpmath.e
pi_val = mpmath.pi
# Test PSLQ: buscar relación entera entre
# [1, C, Omega1, e, pi, C*Omega1, C*e, Omega1*e]
nums = [mpmath.mpf(1), C, Omega1, e_val, pi_val,
        C*Omega1, C*e_val, Omega1*e_val]
result = mpmath.pslq(nums, tol=1e-50, maxcoeff=10000)
print(f"PSLQ: {result}")
# Resultado esperado: None (sin relación encontrada)