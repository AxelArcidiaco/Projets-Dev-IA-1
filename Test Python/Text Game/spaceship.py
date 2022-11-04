# Class spaceship defines the spaceship that is controlled by the player.

class Spaceship:
    colonists = 0 # Number of colonists aboard the spaceship
    probes = 0 # Number of probes aboard the spaceship
    techbase_state = 100 # State of the technological database inside the ship's computers
    culturebase_state = 100 # State of the cultural database inside the ship's computers
    warpdrive = False # If a warp drive is present or not
    
    # Class constructor
    def __init__(self, colonists, probes, warpdrive):
        self.colonists = colonists
        self.probes = probes
        self.warpdrive = warpdrive

# =========================== Getter & Setter =========================== #
# Returns the current number of colonists
def getColonists(self):
    return self.colonists

# Returns the number of probes
def getProbes(self):
    return self.probes

# Returns True if a warp drive is present on the ship. By default this function returns False
def getWarpdrive(self):
    return self.warpdrive

# Returns the integrity of the ship's technological database
def getTechbaseState(self):
    return self.techbase_state

# Returns the integrity of the ship's cultural database
def getCulturalbaseState(self):
    return self.culturalbase_state 