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

    # Sets the number of colonists aboard the ship
    def setColonits(self, colonists):
        self.colonists = colonists

    # Sets the number of probes aboard the ship
    def setProbes(self, probes):
        self.probes = probes
        
    # Sets the presence of a warpdrive aboard the ship
    def setWarpdrive(self, warpdrive):
        self.warpdrive = warpdrive

    # Sets the state of the technological database inside the ship's computers
    def setTechbaseState(self, techbase_state):
        self.techbase_state = techbase_state

    # Sets the state of the cultural database inside the ship's computers
    def setCulturalbaseState(self, culturalbase_state):
        self.culturebase_state = culturalbase_state

    # =========================== toString  =========================== #
    def __str__(self):
        s = "There are "
        s += str(self.colonists) + " colonists aboard the ship held in cryosleep.\n"
        s += "There are " + str(self.probes) + " probes left in storage.\n"
        if self.warpdrive:
            s += "The ship is equipped with an Alcubierre Warp Drive.\n"
        else:
            s += "The ship isn't equipped with an Alcubierre Warp Drive.\n"
        s += "The technological database integrity is " + str(self.techbase_state) + "%"
        
        return s
    
    # =========================== Functions =========================== #
    # Returns a string that contains the technological level of the colonists based on the technological database state.
    # The ages are: 
    # - Interstellar = Antimatter for energy & propulsion, Alcubierre Warp Drive for near Lightspeed
    # - Late Interplanetary = Nuclear Fusion for energy & propulsion, Fusion rocket are efficient enough to allow for continuous 1g burns for days to weeks
    # - Early Interplanetary = Nuclear Fusion for energy & propulsion, Fusion rocket aren't efficient enough to allow for continuous 1g burns for days to weeks
    # - Information = Tech level of Earth during the 21st century
    # - Atomic = Tech level of Earth's between the end of World War 2 and the beginning of of the 21st century
    # - Industrial = Tech level comparable to Earth's between the beginning of the industrial revolution and the end of World War 2
    # - Renaissance = Tech level comparable to Earth's between the 16th and beginning of the 19th centuries
    # - Middle Ages = Tech level comparable to Earth's between the end of the 5th and 15th centuries
    # - Iron Age / Late Antiquity = Tech level comparable to the Roman Republic/Empire
    # - Bronze Age / Early Antiquity = Tech level comparable to Ancient Egypts
    # - Stone Age = Tech level comparable to hunters/gatherers society and/or early sendentary culture
    def getTechLevel(self):
        s = ""
        if self.techbase_state == 100 :
            s = "Interstellar Age giving the colonist access to antimatter-based technologies for energy production and propulsion "
            s += "as well as Alcubierre Warp Drive for near lightspeed travel amongst other technologies."
        elif self.techbase_state > 0 and self.techbase_state <= 10:
            s = ""
        return s