# -*- coding: utf-8 -*-
"""
Created on Wed May 20 06:44:45 2020

@author: Narendra Chowdary
"""


import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from IPython.display import HTML
import numpy as np

t = np.arange(0,15,.05)
g = 9.8 #m/s**2
# print(t.shape)
# print(t)
#(300,)

ini_posi =100 
b1_z =ini_posi + -1/2 *g*t**2
b1_z = b1_z.astype(int)
print(b1_z)
b1_z_posi0_ind = np.where(b1_z==0)[0][0]
print(b1_z_posi0_ind)
b1_z_posi0_ind
#90
print(b1_z[b1_z_posi0_ind:])
b1_z

array=([100,  99,  99,  99,  99,  99,  99,  99,  99,  99,  98,  98,  98,
        97,  97,  97,  96,  96,  96,  95,  95,  94,  94,  93,  92,  92,
        91,  91,  90,  89,  88,  88,  87,  86,  85,  84,  84,  83,  82,
        81,  80,  79,  78,  77,  76,  75,  74,  72,  71,  70,  69,  68,
        66,  65,  64,  62,  61,  60,  58,  57,  55,  54,  52,  51,  49,
        48,  46,  45,  43,  41,  39,  38,  36,  34,  32,  31,  29,  27,
        25,  23,  21,  19,  17,  15,  13,  11,   9,   7,   5,   2,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
         0])


v1=-g*t
v1_posi0 = v1[b1_z_posi0_ind]
v1_posi0
#-44.1

v2_posi0=2*v1_posi0
v2_posi0
#-88.2

b2_z = -v2_posi0*t - 1/2*g*t**2
b2_z = b2_z.astype(int)
b2_z_ = np.concatenate([b1_z[:b1_z_posi0_ind], b2_z])[:t.shape[0]]
b2_z_
print(b2_z_)

# array=([100,  99,  99,  99,  99,  99,  99,  99,  99,  99,  98,  98,  98,
#         97,  97,  97,  96,  96,  96,  95,  95,  94,  94,  93,  92,  92,
#         91,  91,  90,  89,  88,  88,  87,  86,  85,  84,  84,  83,  82,
#         81,  80,  79,  78,  77,  76,  75,  74,  72,  71,  70,  69,  68,
#         66,  65,  64,  62,  61,  60,  58,  57,  55,  54,  52,  51,  49,
#         48,  46,  45,  43,  41,  39,  38,  36,  34,  32,  31,  29,  27,
#         25,  23,  21,  19,  17,  15,  13,  11,   9,   7,   5,   2,   0,
#          4,   8,  13,  17,  21,  26,  30,  34,  38,  42,  47,  51,  55,
#         59,  63,  67,  71,  75,  79,  83,  87,  91,  94,  98, 102, 106,
#        110, 113, 117, 121, 124, 128, 132, 135, 139, 142, 146, 149, 153,
#        156, 160, 163, 166, 170, 173, 176, 180, 183, 186, 189, 193, 196,
#        199, 202, 205, 208, 211, 214, 217, 220, 223, 226, 229, 232, 234,
#        237, 240, 243, 245, 248, 251, 254, 256, 259, 261, 264, 266, 269,
#        271, 274, 276, 279, 281, 284, 286, 288, 290, 293, 295, 297, 299,
#        302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326,
#        327, 329, 331, 333, 335, 336, 338, 340, 341, 343, 345, 346, 348,
#        349, 351, 352, 354, 355, 357, 358, 359, 361, 362, 363, 365, 366,
#        367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380,
#        381, 381, 382, 383, 384, 385, 385, 386, 387, 387, 388, 389, 389,
#        390, 390, 391, 392, 392, 392, 393, 393, 394, 394, 394, 395, 395,
#        395, 395, 396, 396, 396, 396, 396, 396, 396, 396, 396, 396, 396,
#        396, 396, 396, 396, 396, 396, 395, 395, 395, 395, 394, 394, 394,
#        393, 393, 392, 392, 391, 391, 390, 390, 389, 389, 388, 387, 387,
#        386]) 


#position changeの図
plt.plot(b1_z,label='under ball')
plt.plot(b2_z_,label='upper ball')
plt.xlabel('time')
plt.ylabel('position')
plt.legend()
plt.savefig('suttovi1.png',dpi=100)
plt.show()

#slide balls for animation
b1_z_ = b1_z+40
b2_z__ = b2_z_+20

#show ball
fig,ax = plt.subplots(figsize=(6,4))
ax.plot(0,b1_z_[0],'o',ms=15)
ax.plot(0,b2_z__[0],'o',ms=15)
ax.plot(0,b1_z_.min(),'o',ms=15)
ax.plot(0,b2_z__.min(),'o',ms=15)
ax.plot(0,b2_z__.max(),'o',ms=15)
ax.hlines(0,-.25,.25)
ax.set_xticks([])
ax.set_ylim(-10,b2_z__.max()+20)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.savefig('suttovi2.png',dpi=100)
# plt.show()


#animation
fig,ax = plt.subplots(figsize=(6,4))

ball1, = ax.plot(0,b1_z_[0],'o',ms=15)
ball2, = ax.plot(0,b2_z__[0],'o',ms=15)
ax.hlines(0,-.25,.25)
ax.set_ylim(-10,b2_z__.max()+20)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
def update(num):
    ball1.set_ydata(b1_z_[num])
    ball2.set_ydata(b2_z__[num])    
    print(b1_z_[num])
    print(b2_z_[num])
ani = animation.FuncAnimation(fig, update, 300, interval=2,repeat=True)
plt.show()