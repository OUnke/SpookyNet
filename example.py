from ase import Atoms
from spookynet import SpookyNetCalculator

# create ASE Atoms object for carbene
carbene = Atoms('CH2', positions=[
	( 0.000,  0.000,  0.000), 
	(-0.865, -0.584,  0.000), 
	( 0.865, -0.584,  0.000), 
])

# magmom is the number of unpaired electrons, i.e. 0 means singlet
carbene.set_calculator(SpookyNetCalculator(load_from="parameters.pth", charge=0, magmom=0))
print("singlet energy")
print(carbene.get_potential_energy())

# magmom=2 means 2 unpaired electrons => triplet state
carbene.set_calculator(SpookyNetCalculator(load_from="parameters.pth", charge=0, magmom=2))
print("triplet energy")
print(carbene.get_potential_energy())