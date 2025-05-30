






"""
telem = [None,

#3
True,
True,
True,

#13
True,
False,
True,
False,
True,
False,
True,
False,
True,
#False,

#20

False,
False,
False,

False,
False,
False,

False,
False,
False,
False,

False,
False,
False,

False,
False,
False,

False,
False,
False,
False
]"""


telem = [None]*34

dist3 = 0.2
dist13 = 0.6
dist33 = 1

radius = 0.2+0.15-0.05

from math import radians as rad
from ursina import *

#import krpc, time, os
#conn = krpc.connect()

window.borderless = False

#window.position = Vec2(0,-100)

window.always_on_top = True

#x = Entity
#x.i = 0

#window.fps_counter = x

#window.title = "Starship Telemetry"



app = Ursina(size=Vec2(1600+20,250), title="Starship Telemetry")

window.fps_counter.visible = False




 #.color=color.black #.visible = False		# .position = Vec3(32757345735,34565646546,6546649798)	#.enabled = False
sky = Sky(color=color.black)

engs = [None]

sengs = [None]

engcircleradiusadd = 0.1/2/2	#0.01

fullang = 360

engcircles = [None]



ui_booster_engs = Entity(position=(-7.25,0,0))

ui_ship_engs = Entity(position=(7.25,0,0))












for i in range(3):

	ang = 360/3*i

	x = sin(rad(ang))*dist3

	y = cos(rad(ang))*dist3

	engs.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius, position=Vec3(x,y,0)))

	engcircles.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius+engcircleradiusadd, position=Vec3(x,y,10), color=color.gray*1.5))

for i in range(10):

	ang = 360/10*i

	x = sin(rad(ang))*dist13

	y = cos(rad(ang))*dist13

	engs.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius, position=Vec3(x,y,0)))

	engcircles.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius+engcircleradiusadd, position=Vec3(x,y,10), color=color.gray*1.5))

for i in range(20):

	ang = 360/20*i + (1/40*360)

	x = sin(rad(ang))*dist33

	y = cos(rad(ang))*dist33

	engs.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius, position=Vec3(x,y,0)))

	engcircles.append(Entity(parent=ui_booster_engs, model="sphere", scale=radius+engcircleradiusadd, position=Vec3(x,y,10), color=color.gray*1.5))






for i in range(3):

	ang = 360/3*i

	x = sin(rad(ang))*dist3

	y = cos(rad(ang))*dist3

	sengs.append(Entity(parent=ui_ship_engs, model="sphere", scale=radius, position=Vec3(x,y,0)))

	engcircles.append(Entity(parent=ui_ship_engs, model="sphere", scale=radius+engcircleradiusadd, position=Vec3(x,y,10), color=color.gray*1.5))


for i in range(3):

	ang = 360/3*i + 60

	x = sin(rad(ang))*dist13

	y = cos(rad(ang))*dist13

	sengs.append(Entity(parent=ui_ship_engs, model="sphere", scale=radius*2, position=Vec3(x,y,0)))

	engcircles.append(Entity(parent=ui_ship_engs, model="sphere", scale=radius*2+engcircleradiusadd, position=Vec3(x,y,10), color=color.gray*1.5))









#cam = EditorCamera()

camera.fov /= 3
# persp
#camera.fov *= 2/2*5

# ortho
camera.fov /= 5*1.5
camera.fov *= 1.5 #*1.5 #*2

camera.orthographic = True


font = "fonts/consolab.ttf"

#"fonts/consolab.ttf"

#r"C:\WINDOWS\Fonts\CONSOLAB.TTF"

#r"C:\Windows\Fonts\Consolas.ttf"

#r //

#"Consolas"

#"fonts/Courier New.ttf"

# , font="fonts/Courier New.ttf"

# , font = font

speed = Text(text="SPEED", position=Vec3(-2.25,0.25,0), color=color.white, scale=4, font = font) #, resolution=100  *Text.size

alt = Text(text="ALTITUDE", position=Vec3(-2.25,0.1,0), color=color.white, scale=4, font = font)

loxt = Text(text="LOX", position=Vec3(-2.25,-0.05,0), color=color.white, scale=4, font = font)

ch4t = Text(text="CH4", position=Vec3(-2.25,-0.2,0), color=color.white, scale=4, font = font)






sspeed = Text(text="SPEED", position=Vec3(1.25,0.25,0), color=color.white, scale=4, font = font) #, resolution=100  *Text.size

salt = Text(text="ALTITUDE", position=Vec3(1.25,0.1,0), color=color.white, scale=4, font = font)

sloxt = Text(text="LOX", position=Vec3(1.25,-0.05,0), color=color.white, scale=4, font = font)

sch4t = Text(text="CH4", position=Vec3(1.25,-0.2,0), color=color.white, scale=4, font = font)



tplus = Text(text="T-00:00:00", position=Vec3(0,0,0), color=color.white, scale=6, font = font, origin=(0,0,0)) #, resolution=100  *Text.size

tsub = Text(text="STARSHIP FLIGHT TEST", position=Vec3(0,-0.1,0), color=color.white, scale=3, font = font, origin=(0,0,0)) #, resolution=100  *Text.size

#tplus.position.x = -tplus.width/2





Texture.default_filtering = "mipmap"

tex_boosterwithhsr = Texture("img/boosterwithhsr.png")

#tex_boosterwithhsr.filtering = "mipmap"


tex_booster = Texture("img/booster.png")

tex_ship = Texture("img/ship.png")

tex_stack = Texture("img/stack.png")

#tex_booster.filtering = "mipmap"


boosterwithhsrt = Entity(model="quad", position=Vec3(-2, 0, 0), texture=tex_boosterwithhsr, scale=Vec3(1,tex_boosterwithhsr.height/tex_boosterwithhsr.width,1)*0.33)

boostert = Entity(model="quad", position=Vec3(-2, 0, 0), texture=tex_booster, scale=Vec3(1,tex_booster.height/tex_booster.width,1)*0.33)

#boostert = Entity(model="quad", position=Vec3(-2, 0, 0), texture=tex_boosterwithhsr, scale=Vec3(1,tex_boosterwithhsr.height/tex_boosterwithhsr.width,1)*0.33)

stackt = Entity(model="quad", position=Vec3(-2, 0, 0), texture=tex_stack, scale=Vec3(1,tex_stack.height/tex_stack.width,1)*0.25)





#boosterhider = Entity(model="quad", position=Vec3(-6.5, 0, -1), color=color.black*0.75, scale=Vec3(5*2,2*1.25,1))


boosterhider = Entity(parent=camera.ui, model="quad", position=Vec3(-2, 0, -1), color=color.black*0.75, scale=Vec3(3,1,1), visible=False)

shiphider = Entity(parent=camera.ui, model="quad", position=Vec3(2, 0, -1), color=color.black*0.75, scale=Vec3(3,1,1), visible=False)

#cam = EditorCamera()

shipt = Entity(model="quad", position=Vec3(2, 0, 0), texture=tex_ship, scale=Vec3(1,tex_ship.height/tex_ship.width,1)*0.25*1.75)


#tplus = Entity(model="quad", position=Vec3(2, 0, 0), texture=tex_ship, scale=Vec3(1,tex_ship.height/tex_ship.width,1)*0.25*1.75)


#boostert.scale.y = boostert.texture.height/boostert.texture.width



#speed = Text(text="1000", position=Vec3(-1.45-1.5*0*0.25,0.25,0), color=color.white, scale=4, font = font) #origin=(1,0.5), 

#alt = Text(text=" 150", position=Vec3(-1.45-1.5*0*0.25,0.1,0), color=color.white, scale=4, font = font) # origin=(1,0.5),

#Text(text="KMH", position=Vec3(-1.5,0.25,0), color=color.white, scale=4, font = font)

#Text(text="KM", position=Vec3(-1.5,0.1,0), color=color.white, scale=4, font = font)

def str2bool(x):
	return str(x).lower() == "true"

def setspeedalt(v=0,h=0,ch4=0,lox=0, which=1):
	# v in m/s, h in m
	v = str(round(v*3.6))
	h = str(round(h/1000))
	m = str(round(ch4*100*10)/10)
	l = str(round(lox*100*10)/10)
	
	strv = " "*(5-len(v)) + v
	strh = " "*(5-len(h)) + h
	strm = " "*(5-len(m)) + m
	strl = " "*(5-len(l)) + l

	#print(ch4)

	if which == 1:

		speed.text = f"SPEED      {strv} KMH"
		alt.text =   f"ALTITUDE   {strh} KM"
		loxt.text =   f"LOX        {strl} %"
		ch4t.text =   f"CH4        {strm} %"
	elif which == 2:
		sspeed.text = f"SPEED      {strv} KMH"
		salt.text =   f"ALTITUDE   {strh} KM"
		sloxt.text =   f"LOX        {strl} %"
		sch4t.text =   f"CH4        {strm} %"


"""

		parts = vessel.parts

		engines = parts.with_name("SEP.23.RAPTOR2.SL.RC")

		innerengines = vessel = parts.with_tag("BoosterInner3")


		for engine in engines:
			if hasattr(engine, "engine"):
				if engine.engine.active:
					enginesrunning.append(engine)

		for engine in innerengines:
			if hasattr(engine, "engine"):
				if engine.engine.active:
					innerrunning.append(engine)

"""

partlist = [None] + [None]*33



def settplus(t):

	if t <= 0:
		#            "T-00:00:00"
		tplus.text = "T- S O O N"
	else:
		#m = int(t/60)

		#h = int(m/60)

		#s = int(m/60)

		h = str(int(t/3600))

		if len(h) <= 1:
			h = "0" + h
			if len(h) <= 1:
				h = "0" + h

		u = time.strftime('%M:%S', time.gmtime(t))

		v = f"T+{h}:{u}"

		#print(f"T+{h}:{u}")

		#print(h,m,s)

		tplus.text = v


#settplus(56)
#settplus(340)
#settplus(86400*10)

#1/0

def engineon(x):
	#try:
		if x in (None, []):
			return False

		if x.active and x.has_fuel and x.throttle >= 0.01 and x.available_thrust >= 0.1 and x.thrust >= 0.1:
			return True

		return False

	#except Exception as e:
	#	print(e)
	#	return False


def getcolor(x):
	if x:
		return color.white

	else:
		#return color.gray*0.5 #*0.25
		return rgb(0.1,0.1,0.1)





#sc = conn.space_center


streams = [None]

firstrun = True

import traceback



"""
while True:
	try:
		v = sc.active_vessel

		if firstrun:

			firstrun = False

			for i in range(1,33+1):
				streams.append(conn.add_stream(v.parts.with_tag, "E"+str(i)))

			#parts = 

		for i in range(1,33+1):
			id = "E"+str(i)
			wt = []
			try:
				#wt = v.parts.with_tag(id)	#vessel.
				wt = streams[i]()
			except Exception as e:
				print("Inner",e)
				wt = []

			partlist[i] = wt[0].engine if len(wt) >= 1 else None

		for i in range(1,33+1):

			telem[i] = engineon(partlist[i])

		for i in range(1,33+1):


			engs[i].color = getcolor(telem[i])

		app.step()

		time.sleep(1/60)

	except Exception as e:
		print("Outer",e)
		#print(traceback.format_exc())
		firstrun = True
		pass
"""


def angle180(x):
	if x <= -180:
		return x+360
	elif x >= 180:
		return x-360
	return x

def sgn(x):
	return 1 if x >= 0 else -1

def telemangle(pitch, heading):
	heading = angle180(heading)
	pitch = angle180(pitch)

	#return pitch * sgn(heading)

	#x = 90-pitch

	#a = pitch

	#if heading < 0:
	#	a += 2*x

	a = (90-pitch)*sgn(heading)

	print(heading)

	return a

#cam = EditorCamera()

while True:
#def update():



	# .earthandmoon. is the original author of this addon. If you downloaded it somewhere else, you have found a ripped or illegaly redistributed version.





	s = ""

	ship = ""

	#if 1 == 1:

	try:
		with open("data/booster.txt") as f:
			s = f.read()
	except:
		continue

	try:
		with open("data/ship.txt") as f:
			ship = f.read()
	except:
		continue

	l = s.splitlines()[-1]

	l2 = ship.splitlines()[-1]

	if "," not in l or "engs" in l or len(l) <= 50:
		continue # not a data line but heading/new attempt etc.

	if "," not in l2 or "engs" in l2 or len(l2) <= 50:
		continue # not a data line but heading/new attempt etc.

	m = [n.strip() for n in l.split(",")]

	m2 = [n2.strip() for n2 in l2.split(",")]


	time1 = float(m[0])
	time2 = float(m2[0])

	boosterlost = False
	shiplost = False


	shipsep = str2bool(m[17])
	boostersep = str2bool(m2[18])
	hsrsep = str2bool(m[19])



	if time1 + 3 < time2:
		boosterlost = True

	if time2 + 3 < time1	or	not shipsep:
		shiplost = True


	if boosterlost:
		boosterhider.visible = True
	else:
		boosterhider.visible = False


	if shiplost:
		shiphider.visible = True
	else:
		shiphider.visible = False



	tp = max(time1,time2)

	settplus(tp)


	vpitch = float(m[14])
	vhdg = float(m[15])
	vroll = float(m[16])

	spitch = float(m2[14])
	shdg = float(m2[15])
	sroll = float(m2[16])


	#print(m)

	o = [int(p.strip()) for p in m[11].split("-")]

	o2 = [int(p2.strip()) for p2 in m2[11].split("-")]

	#for q in o:
	#	if q != 0:
	#		

	for q in range(1,33+1):
		r = q in o
		engs[q].color = getcolor(r)


	for q2 in range(1,6+1):
		r = q2 in o2
		sengs[q2].color = getcolor(r)


	alti = float(m[2])

	speedi = float(m[7])

	ch4i = float(m[12])

	loxi = float(m[13])


	salti = float(m2[2])

	sspeedi = float(m2[7])

	sch4i = float(m2[12])

	sloxi = float(m2[13])

	setspeedalt(speedi, alti, ch4i, loxi)

	setspeedalt(sspeedi, salti, sch4i, sloxi, which=2)

	#boostert.rotation_x = 2

	#print(boostert.rotation)

	print(window.windowed_position)

	#boostert.rotation_z += 2
	#boosterwithhsrt.rotation_z += 2
	#stackt.rotation_z = 2

	telang = telemangle(vpitch, vhdg)

	telang2 = telemangle(spitch, shdg)

	boostert.rotation_z = telang #90-telang
	boosterwithhsrt.rotation_z = telang #90-telang
	stackt.rotation_z = telang #90-telang

	shipt.rotation_z = telang2 #90-telang

	if shipsep:
		stackt.visible = False
		if hsrsep:
			boostert.visible = True
			boosterwithhsrt.visible = False
		else:
			boostert.visible = False
			boosterwithhsrt.visible = True
	else:
		stackt.visible = True
		boosterwithhsrt.visible = False
		boostert.visible = False

	app.step()

	time.sleep(1/10)

#app.run()


#app.run()














