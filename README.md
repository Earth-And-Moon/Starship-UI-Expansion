# Starship UI Expansion

Starship UI Expansion is a KSP utility to log data from Starship flights and optionally display it in an external Telemetry UI window.

## Installation

### Dependencies

The Python scripts (made for and in Python 3.11.1) require the Ursina package to be installed. It is used to create the shapes and text in the telemetry UI and for the rendering of the data.
The kOS scripts require Starship Expansion Project and, obviously, kOS.

### Installation itself

1. Click Code > Download ZIP
2. Open the zip and go into the folder that contains the readme
3. Drag and drop the Ships folder into your KSP folder
4. Done

## Setup

In the KSP Editor, build a normal Starship stack with the following:

- 33 individual Raptor engines on the booster, each with a kOS name tags from E1 to E33
- 6 Raptors on the ship, with kOS name tags from ES1 to ES6
- two external kOS processors: one mounted to the Booster Core, one to the Ship Main Tanks, both should have the file sue-rec.ks as their boot file

It is also possible to create ship or booster only (as in high altitude test flights). However, the scripts have not been tested for this, but based on how the script is made, it should work.

## How to use

### Configure the recorder script to your KSP installation

Open Ships/Script/boot/starship-cmn.ks in a text editor. The file is ripped from my own undisclosed launch script. It contains some customization options.

### Telemetry UI

Run Ships/Script/sue-telemetry.py while flying or before launch or in the VAB.
It is recommended to use OBS or other video recording/editing software to overlay the telemetry onto KSP and to make it transparent.

### Telemetry Data

The recording scripts create or append data to the ship.txt and booster.txt files in Ships/Script/data. Each flight is separated by the line **---NEW ATTEMPT---**.
Render.py in thet folder will render the data in 3D. For rendering customizations, open the file in Notepad or a different editor and scroll down.

### Features

- Telemetry is designed to be identical to the one used on Flights 1 to 8.
- somewhat customizable (fuel resource name, etc.)
- if (contact with) a vehicle stage is lost, it will grey out the corresponding telemetry shortly after.





