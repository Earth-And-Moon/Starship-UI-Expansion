print "Cmn Script Running".

wait until ship:unpacked.







// Fuel. Adjust this based on your installation by (un)commenting the respective line! Despite their names, do not rename the variables.
// The script was originally made for RO.

// Stock

set CooledLqdMethane to "LiquidFuel".
set CooledLqdOxygen to "Oxidizer".

// Community Resource Pack

//set CooledLqdMethane to "LqdMethane".
//set CooledLqdOxygen to "Oxidizer".

// RO

//set CooledLqdMethane to "CooledLqdMethane".
//set CooledLqdOxygen to "CooledLqdOxygen".












wait 5.






//wait until ag10.


// Config

set pi to 3.14159265358979323.

set deg2m to 40070000/360.

set m2deg to 1/deg2m.

set deg2rad to pi/180.

set rad2deg to 180/pi.


//randomseed(time:seconds).





set TgtApoapsis to 250000.



set AscentMode to "new".	// "old": heat shield south (Flight 1-3), "new": heat shield north (since Flight 4), "0": heat shield down (not recommended)


set RollTo0At30km to true.


set SeparateHSR to false. //true. // True/Flase: True: HSR is installed and should be separated, False: HSR is not installed or should not be separated.

set BoosterFlipDir to random()*360.	//	stress: -90.	//round(random())*180.	//random()*360.	//120.	//-20. //0. // in degrees relative to Ship/Booster QD side, towards the right side of ship/booster, in degrees.

set LaunchSite to ship:geoposition.

set CatchSite to LaunchSite.

set PreCatchSite to latlng(LaunchSite:lat, LaunchSite:lng+500*m2deg).

set PreCatchSite2 to latlng(LaunchSite:lat, LaunchSite:lng+(100-100)*m2deg).

set OffShoreSite to latlng(LaunchSite:lat, LaunchSite:lng+35000*m2deg).

set PreOffShoreSite to latlng(LaunchSite:lat, LaunchSite:lng+(35000+400)*m2deg).

//set TowerSite to latlng(LaunchSite:lat, LaunchSite:lng-30*m2deg).







//set AscentRollFactor to //choose 1 if AscentMode = "new"


set AscentRollFactor to 1.


set Roll30Factor to 1.


if AscentMode = "old" {
	set AscentRollFactor to -1.
}
else if AscentMode = "new" {
	set AscentRollFactor to 1.
}
else if AscentMode = "0" {
	set AscentRollFactor to 0.
}
else {
	set AscentRollFactor to 1.
}



if RollTo0At30km {
	set Roll30Factor to 0.
}













// AGs

// AG1-3: Booster Engine Rings
// AG4-5: Ship Engine Rings
// AG6: Ship SL Engine Actuate Out
// Abort: Toggle Flaps/Grid fins
// Brakes: Vent fuel




//for p in ship:parts {
//	print p:name.
//}





// Part Names

//set BOOSTER_CORE to "SEP.23.BOOSTER.INTEGRATED".

//set BOOSTER_HSR to "SEP.23.BOOSTER.HSR".

set SHIP_CORE to "SEP.24.SHIP.CORE".

set SHIP_HEADER to "SEP.24.SHIP.HEADER".

//set BOOSTER_GRIDFIN to "SEP.23.BOOSTER.GRIDFIN".

set BOOSTER_CORE to "SEP.25.BOOSTER.CORE".

set BOOSTER_HSR to "SEP.25.BOOSTER.HSR".

set BOOSTER_GRIDFIN to "SEP.25.BOOSTER.GRIDFIN".



set BOOSTER_GRIDFIN_MODULE to "ModuleControlSurface".

set BOOSTER_GRIDFIN_AUTH to "authority limiter".



set TOWER_OLM to "SLE.SS.OLM".

set TOWER_MZ to "SLE.SS.OLIT.MZ".

set TOWER_BASE to "SLE.SS.OLIT.Base".

// Parts

set TowerOlm to ship:partsnamed(TOWER_OLM)[0].

set TowerBase to ship:partsnamed(TOWER_BASE)[0].

set Mechazilla to ship:partsnamed(TOWER_MZ)[0].

set BoosterCore to ship:partsnamed(BOOSTER_CORE)[0].

set ShipCore to ship:partsnamed(SHIP_CORE)[0].

set GridFins to ship:partsnamed(BOOSTER_GRIDFIN).

set HSR to choose ship:partsnamed(BOOSTER_HSR)[0] if SeparateHSR else 0.


set OLMSite to Earth:geopositionof(TowerOLM:position).
set TowerSite to Earth:geopositionof(TowerBase:position).


// Conditions & States

function ShipSeparated {
	return ship:partsnamed(SHIP_CORE):length = 0.
}

function BoosterSeparated {
	return ship:partsnamed(BOOSTER_CORE):length = 0.
}

function HSRSeparated {
	return choose ship:partsnamed(BOOSTER_HSR):length = 0 if SeparateHSR else true. // If no HSR is installed or it shouldn't be jettisoned, pretend it to be already "jettisoned".
}



// Functions

function GetResource {
	parameter prt, res.

	set ress to prt:resources.

	for re in ress {
		if re:name = res {
			return re.
		}
	}
	return 0.
}

function GetBoosterLOXPC {
	set rex to GetResource(BoosterCore, CooledLqdOxygen).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}

function GetBoosterCH4PC {
	set rex to GetResource(BoosterCore, CooledLqdMethane).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}


function GetShipLOXPC {
	set rex to GetResource(ShipCore, CooledLqdOxygen).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}

function GetShipCH4PC {
	set rex to GetResource(ShipCore, CooledLqdMethane).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}



function GetShipHeaderLOXPC {
	set rex to GetResource(ShipHeader, CooledLqdOxygen).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}

function GetShipHeaderCH4PC {
	set rex to GetResource(ShipHeader, CooledLqdMethane).

	if rex = 0 {
		return 0.
	}

	return rex:amount/rex:capacity.

}


function VentFuel {
	parameter onoff is true.
	if onfoff = true {
		brakes on.
		return onoff.
	}
	brakes off.
	return onoff.
}

function sgn {
	parameter x.
	return choose 1 if x >= 0 else -1.
}

function clamp {
	parameter x,m,n.

	if x <= m { return m. }
	if x >= n { return n. }
	return x.
}


set lastimppos to latlng(0,0).



function getimppos {
	//wait 0.
	if ADDONS:TR:AVAILABLE {
		if ADDONS:TR:HASIMPACT {
			wait 0.
			set iii to ADDONS:TR:IMPACTPOS.
			//clearscreen.
			//print "Landing prediction:".
			//print iii.
			global lastimppos is iii.
			return iii.
		} else {
		return lastimppos.
		}
	} else {
		return lastimppos.	//print 1/0. // TR not available.
	}
}

function print0 {
	parameter x.

	print x.

	return 0.

}


function interpolate {
	parameter x_0, x_1, y_0, y_1, x.

	return (y_0*(x_1-x)+y_1*(x-x_0))/(x_1-x_0).

}

function angle180 {
	parameter x.
	if x <= -180 {
		return x+360.
	}

	if x > 180 {
		return x+360.
	}

	return x.



}


function activateengs {
	parameter x.
	for y in x {
		set id to "E" + y:tostring.
		set z to ship:partstagged(id).

		// if z:length <= 0.9
		//{
			print("ID:").
			print(id).
			print("z:").
			print(z).
			print("--").
			//print("p": "

			if z:length >= 1 {
				z[0]:activate.
				if z[0]:hasgimbal {
					set z[0]:gimbal:pitch to true.
					set z[0]:gimbal:yaw to true.
					set z[0]:gimbal:roll to true.
				}
			}
		//}


	}
}

function deactivateengs {
	parameter x.
	for y in x {
		set id to "E" + y:tostring.
		set z to ship:partstagged(id).
		if z:length >= 1 {
			z[0]:shutdown.
			if z[0]:hasgimbal {
				set z[0]:gimbal:pitch to false.
				set z[0]:gimbal:yaw to false.
				set z[0]:gimbal:roll to false.
			}
		}


	}
}

function bool2int {
	parameter x.
	return choose 1 if x else 0.
}

// abbreviations

set engs_33 to list(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33).

set engs_13 to list(1,2,3,4,5,6,7,8,9,10,11,12,13).

set engsouter20 to list(14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33).






