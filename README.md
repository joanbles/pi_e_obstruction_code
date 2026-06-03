# pi_e_obstruction_code

Numerical verification scripts accompanying the research paper:

"Obstructions to the Algebraic Independence of π and e: Mixed D-Modules, Exponential Motives and the Regular–Irregular Barrier"

## Description

This repository contains reproducible numerical experiments related to the computation of the Stokes constant

C_Stokes = ∫₀¹ ₂F₁(1/2,1/2;1;t)eᵗ dt

and integer relation searches using the PSLQ algorithm.

## Files

C_Stokes_PSLQ_verification.py

Computes:

- The Stokes constant C_Stokes
- The Legendre period Ω₁
- The constants e and π

and performs a PSLQ search for integer relations among

{1, C_Stokes, Ω₁, e, π, C_StokesΩ₁, C_Stokese, Ω₁e}

using arbitrary-precision arithmetic.

requirements.txt

Python dependencies required to run the scripts.

## Requirements

- Python 3
- mpmath

Install:

pip install -r requirements.txt

Current Numerical Test

Precision:

300 decimal digits

PSLQ parameters:

- tolerance = 1e-50
- maxcoeff = 10000

Expected output:

PSLQ: None

indicating that no integer relation was detected within the tested bounds.

License

MIT License.
