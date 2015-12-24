########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.24.December.2015
########################################################################
# 
# Pulls the keff and burnup from the partial table 210 from BURN card
# Run mcnpx_general.burnup first
# Writes a new file with content, keff, and burnup
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
mcnpx_output_file=os.path.splitext(mcnpx_output_temp)[0]+'_time.v.burnup.out' #same thing, these particular files were filename.suffix1.suffix2.
#
#######
# 
# open the tally file for writing
#
os.chdir('../burnup')
time_burnup_file=open(mcnpx_output_file,'w+')
#
#######
#
# set time steps on BURN card +1 for TIME=0
#
time_steps=21
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
# end for j
# end if
# end for line 
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
