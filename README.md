pi_e_obstruction_code

Numerical verification scripts accompanying the research paper:

"Obstructions to the Algebraic Independence of π and e: Mixed D-Modules, Exponential Motives and the Regular–Irregular Barrier"

Description

This repository contains reproducible numerical experiments related to the computation of the Stokes constant

[
C_{\mathrm{Stokes}}

\int_0^1
{}_2F_1
!\left(
\frac12,
\frac12;
1;
t
\right)
e^t,dt
]

and PSLQ integer relation searches involving the quantities

[
(1,,
C_{\mathrm{Stokes}},,
\Omega_1,,
e,,
\pi,,
C_{\mathrm{Stokes}}\Omega_1,,
C_{\mathrm{Stokes}}e,,
\Omega_1e).
]

The goal is not to prove algebraic independence, but to provide reproducible computational evidence and numerical experiments related to the obstruction program developed in the associated manuscript.

---

Repository Contents

C_Stokes_PSLQ_verification.py

Computes:

- The Stokes constant C_{\mathrm{Stokes}}
- The Legendre period \Omega_1
- The constants e and \pi

and performs a PSLQ search for integer relations among the selected quantities.

requirements.txt

Python dependencies required to run the numerical experiments.

CITATION.cff

Citation metadata for the repository.

results/

Contains saved outputs from numerical verification runs.

Current result file:

- "C_Stokes600PSLQ-None.txt"

---

Requirements

- Python 3
- mpmath

Install dependencies:

pip install -r requirements.txt

Run:

python C_Stokes_PSLQ_verification.py

---

Computational Parameters

The numerical results reported in manuscript v2 were obtained using the following settings:

Parameter| Value| Matches manuscript v2
mp.dps| 600| ✓ Abstract, §7, Appendix A
tol| 1e-50| ✓ Abstract, §7, Appendix A
maxcoeff| 10000| ✓ Abstract, §7, Appendix A
maxdegree| 10| ✓ Numerical quadrature

---

Current Strongest Verification

The strongest numerical verification currently available in this repository used:

- 600 decimal digits of precision
- PSLQ tolerance = 1e-50
- Maximum coefficient bound = 10000

Result:

PSLQ: None

No integer relation was detected within the explored PSLQ search bounds.

Execution environment:

- Python + mpmath
- Verified using Pydroid 3 (Android)
- Runtime approximately 33 minutes

---

Numerical Result

C_Stokes ≈
2.31485069088088081326758073486432396399554898386717...

Full numerical output is available in:

results/C_Stokes600PSLQ-None.txt

---

Interpretation

A negative PSLQ result does not prove algebraic independence.

It only indicates that no integer relation was found among the tested quantities within the specified search bounds and numerical precision.

The computational evidence is therefore exploratory and supportive rather than conclusive.

---

Citation

If you use this repository in research, please cite it using the metadata provided in:

CITATION.cff

---

License

MIT License.
