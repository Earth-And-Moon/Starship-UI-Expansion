//core:part:getmodule("KosProcessor"):doevent("Open Terminal").

core:doevent("Open Terminal").

print "Rec".

runpath("0:/boot/starship-cmn.ks").

runpath("0:/kslib/lib_navball.ks").

function getshipname {
	set parentname to choose core:part:parent:name if core:part:hasparent else "".
	if parentname:contains("BOOSTER") {
		return "BOOSTER".
	} else {
		return "SHIP".
	}

}

function logmsg {
	parameter msg.



	if getshipname() = "BOOSTER" {
		log msg to "0:/data/booster.txt".
	}
	if getshipname() = "SHIP" {
		log msg to "0:/data/ship.txt".
	}

}

wait until ship:unpacked.

set launchsite to ship:geoposition.

set deg2m to 40070000/360.
set m2deg to 1/deg2m.

set body_earth to Earth.

set atm to body_earth:atm.

logmsg("---NEW ATTEMPT---").

logmsg(list(launchsite:lat, launchsite:lng):join(" ")).

logmsg("iter int, downrange m, altitude m, north m, lat d, lng d, airq, srf_vel, orb_vel, pressure, temp, engs, ch4pc, loxpc, pitch, heading, roll, shipsep, boostersep, hsrsep").

set itera to 0.

set englist to list(0). // 0 to prevent the list from being empty and resulting in an empty value/string

set senglist to list(0). // 0 to prevent the list from being empty and resulting in an empty value/string

set dt to 0.1.
lock cond to ship:status = "landed" or ship:status = "splashed" or ship:isdead.

set condtrue to false.

set t_end to 1000000000000000000000000000000000000000000000000000000000000.0.



set t_engstart to 5476866868687896894789.0.


lock t_liftoff to min(max(time:seconds-t_engstart,-2),86400.0*365*10).




when throttle >= 0.01 then {
	set t_engstart to time:seconds.
}









function bool2str {
	parameter x.
	return choose "true" if x else "false".
}

until false {
	set vsl to getshipname.
	set englist to list(0).
	set senglist to list(0).
	set itera to itera+dt.	//1.
	set geolng to ship:geoposition:lng. // geopos
	set geolat to ship:geoposition:lat.

	set poslng to (geolng-launchsite:lng)*(deg2m*abs(cos(geolat))).
	set poslat to (geolat-launchsite:lat)*deg2m.

	set altitu to ship:altitude.	

	set airq to ship:q.

	set srf_vel to ship:velocity:surface:mag.

	set orb_vel to ship:velocity:orbit:mag.

	set atmpressure to atm:altitudepressure(altitu).

	set atmtemp to atm:alttemp(altitu).

	set i to 0.

	if vsl = "BOOSTER" {
	for eng in ship:partstaggedpattern("E[0-9]+") {
		set i to i+1.
		if eng:thrust >= 10 { // and seng:ignition	 availablethrust	  2 and (not eng:flameout)  3 and eng:ignition     1 eng:thrust >= 0.01*100 and 
			englist:add(i).
		}
	}
	}

	set i to 0.

	if vsl = "SHIP" {
	for seng in ship:partstaggedpattern("ES[0-9]+") {
		set i to i+1.
		if seng:thrust >= 10 { // and seng:ignition availablethrust	  2 and (not eng:flameout)  3 and eng:ignition     1 eng:thrust >= 0.01*100 and 
			senglist:add(i).
		}
	}
	}

	set engs to englist:join("-").
	set sengs to senglist:join("-").

	
	set ch4pc to choose GetBoosterCH4PC() if vsl = "BOOSTER" else GetShipCH4PC().
	set loxpc to choose GetBoosterLOXPC() if vsl = "BOOSTER" else GetShipLOXPC().

	set vpitch to pitch_for(ship).
	set vhdg to compass_for(ship).
	set vroll to roll_for(ship).

	set shipsep to bool2str(ShipSeparated()).
	set boostersep to bool2str(BoosterSeparated()).
	set hsrsep to bool2str(HSRSeparated()).

	// 0: itera

	set engis to engs.

	if vsl = "SHIP" {
		set engis to sengs.
	}

	set datalist to list(t_liftoff, poslng, altitu, poslat, geolat, geolng, airq, srf_vel, orb_vel, atmpressure, atmtemp, engis, ch4pc, loxpc, vpitch, vhdg, vroll, shipsep, boostersep, hsrsep).

	logmsg(datalist:join(", ")).

	if cond and not condtrue {
		set condtrue to true.
		set t_end to time:seconds + 5.
	}

	if time:seconds >= t_end {
		break.
	}

	wait dt.	//1.
}












