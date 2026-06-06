import mpmath

# ============================================================

# Parámetros declarados en el manuscrito

# ============================================================

mpmath.mp.dps = 600       # 600 dígitos decimales de precisión
TOL = mpmath.mpf('1e-50')
MAXCOEFF = 10_000         # Cota sobre |n_i| en la búsqueda PSLQ

# ============================================================

# Cálculo de C_Stokes

# ============================================================

def integrando(t):
    return (
        mpmath.hyp2f1(
            mpmath.mpf('1') / 2,
            mpmath.mpf('1') / 2,
            mpmath.mpf(1),
            t
        )
        * mpmath.exp(t)
    )

C = mpmath.quad(integrando, [0, 1], maxdegree=20)

# Mostrar primeros 60 dígitos en pantalla

print(f"C_Stokes = {mpmath.nstr(C, 60)}")

# Guardar 600 dígitos en archivo

with open("C_Stokes_600digits.txt", "w", encoding="utf-8") as f:
    f.write(mpmath.nstr(C, 600))

print("✓ Archivo C_Stokes_600digits.txt generado correctamente.")

# ============================================================

# Valores de referencia

# ============================================================

Omega1 = (
    mpmath.gamma(mpmath.mpf(1) / 4) ** 2
    / (2 * mpmath.sqrt(2 * mpmath.pi))
)

e_val = mpmath.e
pi_val = mpmath.pi

# ============================================================

# Test PSLQ

# Vector:

# (1, C, Omega1, e, pi, C*Omega1, C*e, Omega1*e)

# ============================================================

nums = [
    mpmath.mpf(1),
    C,
    Omega1,
    e_val,
    pi_val,
    C * Omega1,
    C * e_val,
    Omega1 * e_val
]

result = mpmath.pslq(
    nums,
    tol=TOL,
    maxcoeff=MAXCOEFF
)

print(f"PSLQ (maxcoeff={MAXCOEFF}, tol={TOL}) = {result}")

print()
print("=" * 60)
print("VERIFICACIÓN COMPLETADA")
print("=" * 60)
print("Archivo generado: C_Stokes_600digits.txt")
print(f"PSLQ resultado: {result}")
print("=" * 60)

# Resultado esperado:

# PSLQ (maxcoeff=10000, tol=1e-50) = None

