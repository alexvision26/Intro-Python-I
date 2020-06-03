# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

wp1 = LatLon("River", 46, -120)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(name, lat, lon)
    def __str__(self):
        return f"'%s,', %.5f, %.5f" % (self.name, self.lat, self.lon)

# wp2 = Waypoint("Mountain", 50.52331, 125.76435)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(LatLon):
    def __init__(self, name, lat, lon, diff, size):
        self.diff = diff
        self.size = size
        super().__init__(name, lat, lon)
    def __str__(self):
        return f"'%s,', %.5f, %.5f" % (self.name, self.lat, self.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

cata = Waypoint("Catacombs", 41.70505, -121.51521)



# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(cata)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

nbv = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(nbv)
