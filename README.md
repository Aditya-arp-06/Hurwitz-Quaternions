# Hurwitz Goldbach — verification code

Companion code for *On the Additive Properties and Goldbach's Conjecture for Hurwitz Quaternions* (Aditya Patil).

All arithmetic is exact integer arithmetic on doubled coordinates: a+bi+cj+dk is stored as (2a,2b,2c,2d).

## What this repository actually verifies

| Script | What it does |
| --- | --- |
| run_experiments.py | Goldbach sweep, 2 ≤ N ≤ 40: 15,912 targets; 14,865,240 ordered decompositions; min R=8; max R=2602 |
| extended_experiment.py | Smaller prime census, 2 ≤ N ≤ 150: 166800 / 56136 / 624 for primes 2, 3, 5; total 223560 |
| inspect_stats.py | min/max/mean R by norm |
| verify_added_theorems.py | R=8 on the norm-2 shell; 24 σ_odd(2m) at norms 18m |
| verify_examples.py | 13 explicit decompositions |
| verify_new_theorems.py | Real axis n=2..120; twin family |
| verify_n450.py | Norms 2, 3, 5 blocked for one target of norm 450 |
| count_lattice.py | 39,476,352 = number of Hurwitz integers with 2 ≤ N ≤ 2000 |

Terminal transcripts: `outputs/`.

## What this repository does not contain

There is no M=2000 Goldbach sweep. 39,476,352 is
#{α in O : 2 ≤ N(α) ≤ 2000} = C(2000)−1−24,
not the size of a completed Goldbach search.

- `run_experiments.py` only does 2 ≤ N ≤ 40 (15,912 targets, 14,865,240 decompositions).
- `extended_experiment.py` is the smaller-prime census to N=150.
- The number 39,476,352 is C(2000)−1−24 = size of the Hurwitz ball, NOT a Goldbach search.
- There is no M=2000 decompose script.

## Run

```
pip install -r requirements.txt
python run_experiments.py
python extended_experiment.py
python verify_new_theorems.py
python verify_added_theorems.py
python verify_examples.py
python verify_n450.py
python inspect_stats.py
python count_lattice.py
```
