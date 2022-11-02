# A list of constants for the game

# Constants for Earth
EARTH_GRAV = EG = 9.807 # in m/s²
EARTH_MASS = EM = 5.9722e24 # in kg
EARTH_RADIUS = ER  = 6371 # in km

# Constants for Luna / the Moon
LUNA_GRAV = LG = 1.62 # in m/s²
LUNA_MASS = LM = 7.34767309e22 # in kg
LUNA_RADIUS = LR = 1737.4 # in km

# Constants for Jupiter
JUPITER_GRAV = JG = 24.79 # in m/s²
JUPITER_MASS = JM = 1.898e27 # in kg
JUPITER_RADIUS = JR = 69911 # in km

# Constants for the Sun
SOL_GRAV = SG = 274 #in m/s²
SOL_MASS = SM = 1.98847e30 # in kg
SOL_RADIUS = SR = 696340 # in km
SOL_LUMINOSITY = 1
SOL_TEMP = 5778 # in Kelvin

# Astronomical constants
ASTRONOMICAL_UNIT = AU = 149597871 # in km
LIGHT_SPEED = LS = 299792458 # in m/s
LIGHT_YEAR = LY = 9460730472580800 # in km

# Star Type according to the Hardvard Classification
O_TYPE = "O-type star" # also known as O-type main-sequence star, Blue giant, and Blue supergiant
B_TYPE = "B-type star" # also known as B-type main-sequence star, Blue giant, and Blue supergiant
A_TYPE = "A-type star" # also known as A-type main-sequence star
F_TYPE = "F-type star" # also known as F-type main-sequence star
G_TYPE = "G-type star" # also known as G-type main-sequence star, Yellow supergiant, and Yellow hypergiant
K_TYPE = "K-type star" # also known as K-type main-sequence star
M_TYPE = "M-type star" # also known as M-type main-sequence star, Red dwarf, Red giant, and Red supergiant
L_TYPE = T_TYPE = Y_TYPE = "Brown dwarf"
D_TYPE = "White dwarf"

# Star type temperature in Kelvin
O_MIN_TEMP = 30000
B_MAX_TEMP = 30000
B_MIN_TEMP = 10000
A_MAX_TEMP = 10000
A_MIN_TEMP = 7500
F_MAX_TEMP = 7500
F_MIN_TEMP = 6000
G_MAX_TEMP = 6000
G_MIN_TEMP = 5200
K_MAX_TEMP = 5200
K_MIN_TEMP = 3700
M_MAX_TEMP = 3700
M_MIN_TEMP = 2400

# Star type color
O_COLOR = "Blue"
B_COLOR = "Blue white"
A_COLOR = "White"
F_COLOR = "Yellow white"
G_COLOR = "Yellow"
K_COLOR = "Orange"
M_COLOR = "Red"

# Other type of stellar object not in the Harvard Classification
N_TYPE = "Neutron Star"
BD_TYPE = "Black dwarf"
BH_TYPE = "Black hole"
SBH_TYPE = "Supermassive black hole"
Q_TYPE = "Quasar"
PS_TYPE = "Proto-star"