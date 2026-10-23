

def tube_cross_section(d_out, d_in):
    import math
    r_out = d_out / 2
    r_in = d_in / 2
    S = math.pi * (r_out**2 - r_in**2)
    return S
def tube_mass(d_out, d_in, length, density=7850):
    area = tube_cross_section(d_out, d_in)
    mass = area * length * density
    return mass

print(tube_mass(0.060, 0.050, 6,))
print(tube_mass(0.060, 0.050, 6, density=2700))