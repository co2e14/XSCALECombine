#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: christianorr
"""
import subprocess
import time
import sys

inpnumber = input("How many datasets are there? ")
inpnumberstatic = inpnumber
inpnumberstaticint = int(inpnumber)
inpnumber = int(inpnumber)
inpnumberline = inpnumber
inpline = ("INPUT_FILE=")

if (inpnumber > 1):
    print("")
else:
    sys.exit()

defaults = ("OUTPUT_FILE=XSCALE.HKL",
"RESOLUTION_SHELLS=10 5 4 3.6 3.4 3.2 3 2.8 2.6 2.5 2.4 2.3 2.2 2.1 2 1.9 1.8 1.7",
"!INCLUDE_RESOLUTION_RANGE=",
"!MERGE=TRUE",
"!FRIEDEL'S_LAW=FALSE",
"!REFLECTIONS/CORRECTION_FACTOR=50",
"!STRICT_ABSORPTION_CORRECTION=TRUE")

xscaleinp = open("XSCALE.INP","w")
    
for line in defaults:
    xscaleinp.write(line)
    xscaleinp.write("\n")
xscaleinp.close()

xscaleinp = open("XSCALE.INP","a")

while (inpnumberline > 0):
    inpnumberline = inpnumberline - 1
    dataline = input("Enter dataset: ")
    xscaleinp = open("XSCALE.INP","a")
    xscaleinp.write(inpline)
    xscaleinp.write(dataline)
    xscaleinp.write("\n")
    xscaleinp.close()
else:
    print("done")
    
#for i in range(inpnumber):
#    xscaleinp.write(inpline)
#    xscaleinp.write("\n")
#xscaleinp.close()

print("Check XSCALE.INP...")

cont = input("Okay to continue? (y/n): ")
if cont == "y":
    print("Moving on...")
else:
    sys.exit()

count = 1
while (inpnumber > 0):
    inpnumber = inpnumber - 1
    print("placeholder for xscale_par")
    #subprocess.run(["xscale_par"])
    time.sleep(3)
    count = count + 1
    counter = count - 1
    counter = str(counter)
    if (count <= inpnumberstaticint):    
        print(counter + " of " + inpnumberstatic) 
    else:
        print("XSCALE complete")
else:
    print("Processing finished")
    
