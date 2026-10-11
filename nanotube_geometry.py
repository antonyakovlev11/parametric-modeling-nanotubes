"""Geometric diameter through carbon atom centers, not free inner aperture."""
import csv
import math
from pathlib import Path
def diameter(n, m, lattice_nm=0.246):
    if n < 0 or m < 0 or n+m == 0 or lattice_nm <= 0:
        raise ValueError('Require nonnegative nonzero indices and positive lattice constant')
    return lattice_nm / math.pi * math.sqrt(n*n+n*m+m*m)
if __name__ == '__main__':
    with (Path(__file__).parent / 'nanotube-diameters.csv').open('w', encoding='utf-8', newline='') as f:
        w=csv.writer(f);w.writerow(['family','n','m','diameter_nm'])
        for n in range(10,19):
            for family,m in [('zigzag',0),('armchair',n)]:
                w.writerow([family,n,m,diameter(n,m)])
    for n,m in [(12,0),(13,0),(14,0),(8,8)]:
        print(f'({n},{m}): {diameter(n,m):.6f} nm')
