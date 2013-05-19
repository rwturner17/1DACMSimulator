# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:38:52 2013

@author: Will
"""

from acmconstants import G1, ALPHA, D12, G2, C, HBAR, OMEGA_RES, LINEWIDTH_RES
from math import pi
#import ImagingBeam
import numpy as np
import AtomImage

def gH(omega, omega_resonance, linewidth):
    return linewidth/(2*pi*((omega - omega_resonance)**2 + 0.25*linewidth**2))
    
def atom_light_interaction(imaging_beam, atom_density):
    '''notation taken from "Atomic Physics" by Christopher Foot
    Produces image from atom density
    need to account for polarization!!'''
    #Isat = (pi*h*c)/(3*img_lambda**2*tau) #on resonance value
    A21 = (G1*4*ALPHA*(2*pi*imaging_beam.omega)**3*D12**2)/(G2*3/C**2)
    
    abs_x_section = (2*pi**2*C**2*A21*gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES))
    
    I_sat = (HBAR*imaging_beam.omega*A21)/(2*abs_x_section)
    
    I_0 = imaging_beam.get_slice(0)
    
#    abs_x_section_eff = abs_x_section/(1 + imaging_beam.intensity/I_sat) #actually varies in space
    abs_x_section_eff = np.array([abs_x_section/(1 + I/I_sat) for I in I_0])
    #now exponentiate and multiply this by atom_density and imaging_beam to make a new image
    optical_density = abs_x_section_eff * atom_density.get_density()
    I_f = I_0 * np.exp(-1*optical_density)
    atom_image = AtomImage.AtomImage(I_f, imaging_beam)
    return atom_image