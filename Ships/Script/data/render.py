booster = []
ship = []

with open("booster.txt") as f:
	booster = [x.split(",") for x in f.read().split("---NEW ATTEMPT---")[-1].splitlines()[3:]]

with open("ship.txt") as f:
	ship = [x.split(",") for x in f.read().split("---NEW ATTEMPT---")[-1].splitlines()[3:]]

#print(booster)

from ursina import *
from ursina import Vec3




boosterpos = [
	Vec3(
		float(v[1].strip()),
		float(v[2].strip()),
		float(v[3].strip())
	) for v in booster
]

shippos = [
	Vec3(
		float(v[1].strip()),
		float(v[2].strip()),
		float(v[3].strip())
	) for v in ship
]

noy = Vec3(1,0,1)

boosterdots = []
shipdots = []

boosterdotsground = []
shipdotsground = []

window.borderless = False

app = Ursina()

for i in shippos:
	shipdots.append(Entity(model="sphere",scale=100*2.5/2/2, color=color.blue, position=i))

for i in boosterpos:
	boosterdots.append(Entity(model="sphere",scale=100*2.5/2/2, color=color.red, position=i))

print(boosterpos)







cam = EditorCamera()

camera.clip_plane_far *= 100






# Booster trajectory

boostertraj = Entity(model=Mesh(vertices=boosterpos, mode='line'), color=color.red)

# Ship trajectory

shiptraj = Entity(model=Mesh(vertices=shippos, mode='line'), color=color.blue)

# Booster ground trajectory path

boostertrajground = Entity(model=Mesh(vertices=[i*noy for i in boosterpos], mode='line'), color=color.red*0.5)

# Ship ground trajectory path

shiptrajground = Entity(model=Mesh(vertices=[i*noy for i in shippos], mode='line'), color=color.blue*0.5)

# Ground, 100x100 km, 50 km in each direction

ground = Entity(model="plane", scale=100000, alpha=0.5)

# 100x100 km plane whose normal vector is north/south, 50 km in each direction

northplane = Entity(model="plane", scale=100000, rotation=Vec3(90,0,0), double_sided=True, alpha=0.5)











app.run()







