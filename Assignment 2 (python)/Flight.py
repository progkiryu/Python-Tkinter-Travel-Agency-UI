class Flight:
    def __init__(self, airline, flight_no, takeoff, landing, cost):
        self.airline = airline
        self.flight_no = flight_no
        self.takeoff = takeoff
        self.landing = landing
        self.cost = cost
    
    def to_string(self):
        return self.airline + " Flight " + str(self.flight_no) + " from " + self.takeoff + " to " + self.landing + " for " + "{:.2f}".format(float(self.cost))