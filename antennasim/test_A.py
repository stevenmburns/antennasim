import pytest

def test_dipole():

    n = 5
    wavelength = 20 # meters
    wirelength = wavelength/2

    freq = 14.1 # MHz

    nodes = [wirelength*i/n for i in range(n+1)]

    filaments = list(zip(nodes[:-1],nodes[1:]))

    center_filament = filaments[n//2]

    print(nodes, filaments, center_filament)
