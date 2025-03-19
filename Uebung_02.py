class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.z}"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z,)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z,)
    
    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z,)
    
    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other,)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)
    
    def normalize(self):
        magnitude = (self.x**2 + self.y**2 + self.z**2) ** 0.5
        if magnitude == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)


a = Vector3(3,4,2)
b = Vector3(2,1,0)
c = a * b       # Komponentenweise Multiplikation
print(c)
d = a.dot(b)    # Skalarprodukt
print(d)
e = a.cross(b)  # Kreuzprodukt
print(e)
f = a.normalize()
print(f)
