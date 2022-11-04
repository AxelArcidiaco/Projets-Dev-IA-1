# Importation
import spaceship
import constant

# Test importation
print(constant.EARTH_GRAV)

s1 = spaceship.Spaceship(1000, 10, False)
print(s1.colonists, s1.probes, s1.warpdrive)
print(s1.__str__())