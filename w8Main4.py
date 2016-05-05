import math

myLocation=list()
Locations=list()
distances=list()

myLocation=[(37.575869, 126.976637)]
Locations=[(37.576549, 126.985520),(37.570426, 126.992118),(37.570175, 126.982998),(37.571618, 126.976551)]

for i in range(0,len(Locations)):
    distances.append(math.sqrt((myLocation[0][0]-Locations[i][0])**2+(myLocation[0][1]-Locations[i][1])**2))

print distances

print min(distances)

raw_input()