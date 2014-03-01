
import math

from timeit import default_timer as timer

import numpy as np
import matplotlib.pyplot as plt

def juliaop(z, c, px):
	if px==-1:
		return z*z+c
	else:
		return 0+0j

def burningshipop(z, c, px):
	if px==-1:
		return complex(math.fabs(z.real),math.fabs(z.imag))**2+c
	else:
		return 0+0j

def condition(z,px,limit,i):
	if px==-1:
		if z.real**2 + z.imag**2 >= limit:
			return i
		return -1
	else:
		return px

def fractalfunc(func, z, c, limit, width, height, realrange, imagrange, maxiter):
	im = np.ones((height,width), dtype=int)
	im *= -1

	op = np.vectorize(func)
	img = np.vectorize(condition)

	start = timer()
	for i in range(maxiter):
		z = op(z,c,im)
		im = img(z,im,limit,i)
	dt = timer() - start
	print 'fractal time:', dt
	return im

def julia(c, width, height, realrange, imagrange, maxiter):
	z = np.zeros((height,width), dtype=complex)
	pixel_size_real = float(realrange[1] - realrange[0])/float(width)
	pixel_size_imag = float(imagrange[1] - imagrange[0])/float(height)
	for imag in range(height):
		for real in range(width):
			z[imag,real] = complex(realrange[0]+real*pixel_size_real,imagrange[0]+imag*pixel_size_imag)
	R = (1+np.sqrt(1+4*np.sqrt(c.real**2+c.imag**2)))/2.0
	limit = R**2
	return fractalfunc(juliaop,z,c, limit, width, height, realrange, imagrange, maxiter)

def mandelbrot(width, height, realrange, imagrange, maxiter):
	z = np.zeros((height,width), dtype=complex)
	c = np.zeros((height,width), dtype=complex)
	pixel_size_real = float(realrange[1] - realrange[0])/float(width)
	pixel_size_imag = float(imagrange[1] - imagrange[0])/float(height)
	for imag in range(height):
		for real in range(width):
			c[imag,real] = complex(realrange[0]+real*pixel_size_real,imagrange[0]+imag*pixel_size_imag)
	return fractalfunc(juliaop,z,c,4,width, height, realrange, imagrange, maxiter)

def burningship(width, height, realrange, imagrange, maxiter):
	z = np.zeros((height,width), dtype=complex)
	c = np.zeros((height,width), dtype=complex)
	pixel_size_real = float(realrange[1] - realrange[0])/float(width)
	pixel_size_imag = float(imagrange[1] - imagrange[0])/float(height)
	for imag in range(height):
		for real in range(width):
			c[imag,real] = complex(realrange[0]+real*pixel_size_real,imagrange[0]+imag*pixel_size_imag)
	return fractalfunc(burningshipop,z,c,4,width, height, realrange, imagrange, maxiter)


def newtonop(z, px):
	if px==-1:
		return z
	else:
		return 1+0j

def newtoncond(z, eps, px, i):
	if px==-1:
		if np.abs(z) <= eps:
			return i
		return -1
	else:
		return px	

def newtonfractalfunc(z, p, a, eps, width, height, realrange, imagrange, maxiter):
	im = np.ones((height,width), dtype=int)
	im *= -1
	
	p = np.poly1d(p)
	pd = np.polyder(p)

	op = np.vectorize(newtonop)
	img = np.vectorize(newtoncond)

	start = timer()
	for i in range(maxiter):
		zp = z - (a*p(z))/pd(z)
		#im = img(z,zp,eps,im,i)
		im = img(p(zp),eps,im,i)
		z = op(zp,im)
	dt = timer() - start
	print 'fractal time:', dt
	print im
	return im

def newton(p, a, eps, width, height, realrange, imagrange, maxiter):
	
	z = np.zeros((height,width), dtype=complex)
	pixel_size_real = float(realrange[1] - realrange[0])/float(width)
	pixel_size_imag = float(imagrange[1] - imagrange[0])/float(height)
	for imag in range(height):
		for real in range(width):
			z[imag,real] = complex(realrange[0]+real*pixel_size_real,imagrange[0]+imag*pixel_size_imag)

	return newtonfractalfunc(z,p, a, eps, width, height, realrange, imagrange, maxiter)

width=800
height=600
maxiter = 100
realrange = (-2.0, 0.7)
imagrange = (-1.3, 1.3)
c = 0+1j

#start = timer()
#im = julia(c=0+1j,width, height, realrange, imagrange, maxiter)
#dt = timer() - start
#print 'total time:', dt

start = timer()
#im = burningship(width, height, realrange=(-1.9,1.2), imagrange=(-1.9,0.6), maxiter=100)
#plt.imshow(im, extent=[-1.9,1.2,0.6,-1.9])

im = burningship(width, height, realrange=(-1.8,-1.7), imagrange=(-0.085,0.02), maxiter=500)
plt.imshow(im, extent=[-1.8,-1.7,0.02,-0.085], cmap='flag')
#plt.hot()
#plt.jet()
#autumn
#bone
#cool
#copper
#flag #**
#gray
#hot
#hsv #**
#jet
#pink
#prism
#spring
#summer
#winter
#spectral

dt = timer() - start
print 'total time:', dt

#start = timer()
#im = mandelbrot(width=800, height=600, realrange=(-2.0, 0.7), imagrange=(-1.3, 1.3), maxiter=100)
#plt.imshow(im, extent=[-2.0, 0.7,1.3, -1.3], cmap='flag')
#im = mandelbrot(width=800, height=600, realrange=(-1.79, -1.74), imagrange=(-0.03, 0.03), maxiter=100)
#plt.imshow(im, extent=[-1.79, -1.74,-0.03, 0.03])
#dt = timer() - start
#print 'total time:', dt

#start = timer()
#im = newton([1, 0, 0, -1], 1, 1e-3, width, height, (-1.0, 1.0), (-1.0, 1.0), maxiter)
#im = newton([1, 0, -2, 2], 1, 1e-3, width, height, (-3.0, 3.0), (-3.0, 3.0), maxiter)
#im = newton([1, 0, 0, 0, 15, 0, 0, 0, -16], 1, 1e-3, width, height, (-3.0, 3.0), (-3.0, 3.0), maxiter)
#im = newton([1, 0, -3j, -5-2j, 3, 1], 1, 1e-2, width, height, (-3.0, 3.0), (-3.0, 3.0), maxiter)
#im = newton([1, 0, 0, -1], -0.5, 0.5, width, height, (-2.0, 2.0), (-2.0, 2.0), maxiter)
#dt = timer() - start
#print 'total time:', dt

#

#plt.xlim((-3,3))
#plt.ylim((-3,3))
#plt.xticks(range(10), [-3+i*0.1*6 for i in range(10)])
plt.show()