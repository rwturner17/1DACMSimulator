# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:46:12 2013

@author: Will
"""

from acwires import HWire, VWire, NWire


from AtomChip import *

## Wire definition

# Horizontal Wires
hwires = []
vwires = []
nwires = []

hwires.append(HWire('Central Trapping Macrowire', l_trap, w_rad, h_rad, I_in, 
                    -l_trap / 2, -w_rad/2, -h_rad))


hwires.append(HWire('Left Central Trapping Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    I_in, -25e-3, -w_rad/2, -2.1e-3))


hwires.append(HWire('Right Central Trapping Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    I_in, 6.75e-3, -w_rad/2, -2.1e-3))


hwires.append(HWire('Upper Bias Macrowire', 
                    l_trap, w_rad, h_rad, 
                    I_in, -l_trap/2, -w_rad/2, -h_rad))

hwires.append(HWire('Right Upper Bias Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    -I_out, 6.75e-3, a-w_rad/2, -2.1e-3))


hwires.append(HWire('Left Upper Bias Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    -I_out, -25e-3, a-w_rad/2, -2.1e-3))


hwires.append(HWire('Lower Bias Macrowire', 
                    l_trap, w_rad, h_rad, 
                    -I_out, -l_trap/2, -a-w_rad/2, -h_rad))


hwires.append(HWire('Right Lower Bias Macrowire Lead', 
                    33.25e-3, w_rad, 2e-3, 
                    -I_out, 6.75e-3,-a-w_rad/2, -2.1e-3))


hwires.append(HWire('Left Lower Bias Macrowire Lead', 
                    33.25e-3, w_rad, 2e-3, 
                    -I_out, -40e-3,-a-w_rad/2, -2.1e-3))


hwires.append(HWire('Central Microwire', 
                    4e-3, w_micro, h_micro, 
                    I_micro_trap, -2e-3, -w_micro/2, chip_height))


hwires.append(HWire('Left Central Lead Microwire', 
                    3e-3, w_micro_lead, h_micro, 
                    I_micro_trap, -5e-3, -w_micro_lead/2, chip_height))


hwires.append(HWire('Left Central Thick Lead Microwire', 
                    7.5e-3, w_micro_thlead, h_micro, 
                    I_micro_trap, -12.5e-3, -w_micro_thlead/2, chip_height))


hwires.append(HWire('Right Central Lead Microwire', 
                    3e-3, w_micro_lead, h_micro, 
                    I_micro_trap, 2e-3, -w_micro_lead/2, chip_height))


hwires.append(HWire('Right Central Thick Lead Microwire', 
                    7.5e-3, w_micro_thlead, h_micro, 
                    I_micro_trap, 5e-3, -w_micro_thlead/2, chip_height))


hwires.append(HWire('Left Arm Microwire', 
                    1e-3-w_micro/2, w_micro, h_micro, 
                    -I_micro_arm, -2e-3, -1.5*w_micro - sp, chip_height))


hwires.append(HWire('Left Arm Lead Microwire', 
                    3e-3, w_micro_lead, h_micro,  
                    -I_micro_arm, 
                    -5e-3, -1.5*w_micro_lead - sp, chip_height))

hwires.append(HWire('Left Arm Thick Lead Microwire', 
                    6.5e-3, w_micro_thlead, h_micro, 
                    -I_micro_arm, 
                    -11.5e-3, -1.5*w_micro_thlead - sp, chip_height))


hwires.append(HWire('Left Arm Return Microwire', 
                    4e-3-w_micro/2, w_micro_lead, h_micro,  
                    I_micro_arm, 
                    -5e-3, -5e-3, chip_height))


hwires.append(HWire('Left Arm Thick Return Microwire', 
                    4e-3, w_micro_thlead, h_micro,  
                    I_micro_arm, -9.5e-3, -5e-3, chip_height))


hwires.append(HWire('Right Arm Microwire', 
                    1e-3-w_micro/2, w_micro, h_micro, 
                    -I_micro_arm, 
                    l_med/2 + w_micro/2, sp+w_micro/2, chip_height))


hwires.append(HWire('Right Arm Lead Microwire', 
                    3e-3-w_micro/2,w_micro_lead, h_micro, 
                    -I_micro_arm, 
                    2e-3, w_micro_lead/2 + sp, chip_height))


hwires.append(HWire( 'Right Arm Thick Lead Microwire',  
                    6.5e-3-w_micro/2,  w_micro_thlead,  h_micro,  
                    -I_micro_arm,   
                    2e-3,  w_micro_thlead/2 + sp,  chip_height))

hwires.append(HWire( 'Right Arm Return Microwire',  
                    4e-3,  w_micro_lead,  h_micro,  
                    I_micro_arm,   
                    l_med/2 + w_micro/2,  4.5e-3,  chip_height))

hwires.append(HWire( 'Right Arm Thick Return Microwire',  
                    15.75e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    5e-3,  3.5e-3,  chip_height))


hwires.append(HWire( 'Dimple Microwire',  
                    (l_micro - w_micro)/2 ,  w_micro,  h_micro,  
                    -I_micro_dimple,   
                    -l_micro/2,  w_micro/2 + sp,  chip_height))

hwires.append(HWire( 'Left Axial Lead Macrowire',  
                    19.25e-3 ,  0, 0,  
                    I_ax,  
                    -25e-3,  -25e-3,  0))

hwires.append(HWire( 'Right Axial Lead Macrowire',  
                    19.25e-3 ,  0, 0,  
                    -I_ax,   
                    5.75e-3,  -25e-3,  0))


# Vertical Wires

vwires.append(VWire( 'Left Axial Bias Macrowire',  
                    l_ax,  w_ax,  h_ax,  
                    I_ax,   
                    -a_ax/2-w_ax/2,  
                    -l_ax/2,  -sub - h_ax/2))


vwires.append(VWire( 'Left Axial Bias Lead Macrowire',  
                    20e-3,  w_ax,  3e-3,  
                    I_ax,   
                    -a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Right Axial Bias Macrowire',  
                    l_ax,  w_ax,  h_ax,  
                    I_ax,   
                    a_ax/2-w_ax/2,  -l_ax/2,  -sub - h_ax/2))

vwires.append(VWire( 'Right Axial Bias Lead Macrowire',  
                    20e-3,  w_ax,  3e-3,  
                    I_ax,  
                    a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Axial Dimple Macrowire',  
                    l_ax,  w_dimple,  h_dimple,  
                    I_dimple,   
                    -w_dimple/2,  -l_ax/2,  -sub - h_dimple/2))

vwires.append(VWire( 'Axial Dimple Lead Macrowire',  
                    20e-3,  w_dimple,  3e-3,  
                    I_dimple,   
                    -w_dimple/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Left Bias Lead Macrowire',  
                    2.75e-3,  w_rad,  h_ax,  
                    -I_out,   
                    -24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VWire( 'Right Bias Lead Macrowire',  
                    2.75e-3,  w_rad,  h_ax,  
                    I_out,   
                    24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VWire( 'Left Central Lead Macrowire', 
                    13e-3,  w_rad,  3e-3,  
                    I_in,   
                    -24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VWire( 'Right Central Lead Macrowire',  
                    13e-3,  w_rad,  3e-3,  
                    -I_in,   
                    24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VWire( 'Left Central Thick Lead Microwire',  
                    11.5e-3,  w_micro_thlead,  h_micro,  
                    I_micro_trap,   
                    -12.75e-3,  -11e-3,  chip_height))

vwires.append(VWire( 'Right Central Thick Lead Microwire',  
                    11.5e-3,  w_micro_thlead,  h_micro,  
                    -I_micro_trap,   
                    11.75e-3,  -11e-3,  chip_height))

vwires.append(VWire( 'Left Arm Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro, 
                    I_micro_arm,   
                    -l_med/2 - w_micro/2,  -l_arms,  chip_height))

vwires.append(VWire( 'Left Arm Thick Lead Microwire',  
                    12.5e-3,  w_micro_thlead,  h_micro, 
                    -I_micro_arm,   
                    -11.75e-3,  -13e-3,  chip_height))

vwires.append(VWire( 'Left Arm Thick Return Microwire',  
                    12e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    -10e-3,  -16e-3,  chip_height))

vwires.append(VWire( 'Right Arm Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  
                    I_micro_arm,   
                    l_med/2 - w_micro/2,  w_micro/2 + sp,  chip_height))

vwires.append(VWire( 'Right Arm Thick Lead Microwire',  
                    12.5e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    12.75e-3,  -13e-3,  chip_height))

vwires.append(VWire( 'Right Arm Thick Return Microwire',  
                    10e-3,  w_micro_thlead,  h_micro,  
                    -I_micro_arm,   
                    15e-3,  -6e-3,  chip_height))

vwires.append(VWire( 'Dimple Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  
                    -I_micro_dimple,   
                    -w_micro/2,  w_micro/2 + sp,  chip_height))

nwires.append(NWire( 'Left Upper Bias Lead Rod', 
                    40e-2,  0,  0,  
                    -I_out,  
                    -40e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Upper Bias Lead Rod', 
                    40e-2,  0,  0,  
                    I_out,   
                    40e-3,  0,  -40e-2))

nwires.append(NWire( 'Left Lower Bias Lead Rod', 
                    390e-3,  0,  0,  
                    -I_out,  
                    -30e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Lower Bias Lead Rod', 
                    390e-3,  0,  0,  
                    I_out,  
                    30e-3,  0,  -40e-2))

allwires = hwires + vwires + nwires