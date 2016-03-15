########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.22.December.2015
########################################################################
# 
# Print partial table 210 from BURN card for time and burnup 
# Pulled from the MCNP output and written to a new file
# Run in directory with the raw MCNP output files
# Create a new directory for the burnup v time data files
#
########################################################################
#
#
#
####### 
#
# imports
#
import os
from sys import argv
script,mcnpx_output=argv
#
########################################################################
#
#
#
#######
#
# open mcnpx output file
#
mcnpx_file=open(mcnpx_output,'r').readlines()
#
#######
# 
# prepare output files 
#
mcnpx_output_temp=os.path.splitext(mcnpx_output)[0] #separates filename.suffix, keeps filename
mcnpx_output_file=os.path.splitext(mcnpx_output_temp)[0]+'_burn.card.out' #same thing, these particular files were filename.suffix1.suffix2
#
#######
# 
# open the tally file for writing
#
os.chdir('/media/sf_home/usr/borrelli/mcnpx.decks/thorium.uranium.fuel/homogenous.th.u.mixture/output/burn.card/15.00mm_pitch/1500D/')
time_burnup_file=open(mcnpx_output_file,'w+')
#
#######
#
# set time steps on BURN card +1 for TIME=0
#
time_steps=151
#
#######
#
# initialize the counter
# 
i=0
#
####### 
#
# search the file
# line will write the current line
# mcnpx_file[i] writes the next line, etc.
# need to know how many time steps have been written
#
for line in mcnpx_file:
  i=i+1
  if ' neutronics and burnup data' in line:
    for j in range(0,time_steps):
	time_burnup_file.write(mcnpx_file[j+(i+3)])
# end j
# end if
# end line 
#
#######
# 
# close files
#
time_burnup_file.close()
#
########################################################################
#
# EOF
#
########################################################################
