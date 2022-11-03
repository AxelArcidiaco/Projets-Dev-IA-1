/**
 * Created 03/11/2022
 * Last modified on 03/11/2022
 */

// A list of constants for the game

// Constants for Earth
const EARTH_GRAV = 9.807 // gravity in m/s²
const EARTH_MASS = 5.9722e24 // mass in kg
const EARTH_RADIUS = 6371 // radius in km

// Constants for Luna / the Moon
const LUNA_GRAV = 1.62; // gravity in m/s²
const LUNA_MASS = 7.34767309e22; // mass in kg
const LUNA_RADIUS = 1737.4; // radius in km

// Constants for Jupiter
const JUPITER_GRAV = 24.79; // gravity in m/s²
const JUPITER_MASS = 1.898e27; // mass in kg
const JUPITER_RADIUS = 69911 // radius in km

// Constants for the Sun
const SOL_GRAV = 274; // gravity in m/s²
const SOL_MASS = 1.98847e30; // mass in kg
const SOL_RADIUS = 696340; // radius in km
const SOL_LUMINOSITY = 1;
const SOL_TEMP = 5778; // Temperature in Kelvin

// Astronomical constants
const ASTRONOMICAL_UNIT = 149597871; // in km
const LIGHT_SPEED = 299792458; // in m/s
const LIGHT_YEAR = 9460730472580800; // in km

// Star Type according to the Hardvard Classification
const O_TYPE = "O-type star"; // also known as O-type main-sequence star, Blue giant, and Blue supergiant
const B_TYPE = "B-type star"; // also known as B-type main-sequence star, Blue giant, and Blue supergiant
const A_TYPE = "A-type star"; // also known as A-type main-sequence star
const F_TYPE = "F-type star"; // also known as F-type main-sequence star
const G_TYPE = "G-type star"; // also known as G-type main-sequence star, Yellow supergiant, and Yellow hypergiant
const K_TYPE = "K-type star"; // also known as K-type main-sequence star
const M_TYPE = "M-type star"; // also known as M-type main-sequence star, Red dwarf, Red giant, and Red supergiant
const L_TYPE = "Brown dwarf";
const T_TYPE = "Brown dwarf";
const Y_TYPE = "Brown dwarf";
const D_TYPE = "White dwarf";

// 'Star type temperature in Kelvin'
const O_MIN_TEMP = 30000;
const B_MAX_TEMP = 30000;
const B_MIN_TEMP = 10000;
const A_MAX_TEMP = 10000;
const A_MIN_TEMP = 7500;
const F_MAX_TEMP = 7500;
const F_MIN_TEMP = 6000;
const G_MAX_TEMP = 6000;
const G_MIN_TEMP = 5200;
const K_MAX_TEMP = 5200;
const K_MIN_TEMP = 3700;
const M_MAX_TEMP = 3700;
const M_MIN_TEMP = 2400;

// Star type color
const O_COLOR = "Blue";
const B_COLOR = "Blue white";
const A_COLOR = "White";
const F_COLOR = "Yellow white";
const G_COLOR = "Yellow";
const K_COLOR = "Orange";
const M_COLOR = "Red";

// Other type of stellar object not in the Harvard Classification
const N_TYPE = "Neutron Star";
const BD_TYPE = "Black dwarf";
const BH_TYPE = "Black hole";
const SBH_TYPE = "Supermassive black hole";
const Q_TYPE = "Quasar";
const PS_TYPE = "Proto-star";