########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.24.December.2015
# v1.0
########################################################################
#
# Display screen resolution
#
########################################################################
#
# imports
#
import Tkinter
import ctypes
root=Tkinter.Tk()
user32=ctypes.windll.user32
#
########################################################################
#
#
#
#######
def screen_res():
#######
#
# pixels
#
    width_px=root.winfo_screenwidth()
    height_px=root.winfo_screenheight() 
#
#######
#
# mm
#
    width_mm=root.winfo_screenmmwidth()
    height_mm=root.winfo_screenmmheight() 
#
#######
#
# inches
#
    width_in=width_mm/25.4
    height_in=height_mm/25.4
#
#######
#
# dpi
#
    width_dpi=width_px/width_in
    height_dpi=height_px/height_in
#
#
# get system metrics
#
    user32.SetProcessDPIAware()
    [width,height] = [user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)]
    current_dpi = width*96/width_px
#
#######
#
# output
#
    print('width: %i px, height: %i px'%(width_px,height_px))
    print('width: %i mm, height: %i mm'%(width_mm,height_mm))
    print('width: %0.f in, height: %0.f in'%(width_in,height_in))
    print('width: %0.f dpi, height: %0.f dpi'%(width_dpi,height_dpi))
    print('size is %0.f %0.f'%(width,height))
    print('current DPI is %0.f' % (current_dpi))    
#
#######
#
    return(width,height,current_dpi)
#
########################################################################
#
# EOF
#
########################################################################
