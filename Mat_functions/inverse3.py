# Crystal Plasticity Code.

import math,sys

################# inverse 3by3 matrix ######################
def matinv3(a):
    a_inv = [[0.0 for i in range(3)] for j in range(3)]
    
    det = a[0][0]*a[1][1]*a[2][2]-a[0][0]*a[1][2]*a[2][1]-a[1][0]*a[0][1]\
              *a[2][2]+a[1][0]*a[0][2]*a[2][1]+a[2][0]*a[0][1]*a[1][2]-a[2][0]\
              *a[0][2]*a[1][1]
    
    a_inv[0][0] =  ( a[1][1]*a[2][2]-a[1][2]*a[2][1])/det
    a_inv[0][1] = -( a[0][1]*a[2][2]-a[0][2]*a[2][1])/det
    a_inv[0][2] = -(-a[0][1]*a[1][2]+a[0][2]*a[1][1])/det
    a_inv[1][0] = -( a[1][0]*a[2][2]-a[1][2]*a[2][0])/det
    a_inv[1][1] =  ( a[0][0]*a[2][2]-a[0][2]*a[2][0])/det
    a_inv[1][2] = -( a[0][0]*a[1][2]-a[0][2]*a[1][0])/det
    a_inv[2][0] =  ( a[1][0]*a[2][1]-a[1][1]*a[2][0])/det
    a_inv[2][1] = -( a[0][0]*a[2][1]-a[0][1]*a[2][0])/det
    a_inv[2][2] =  ( a[0][0]*a[1][1]-a[0][1]*a[1][0])/det
      
    return a_inv,det

################# end of inverse 3by3 matrix ######################
       
