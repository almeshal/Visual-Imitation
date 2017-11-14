#!/usr/bin/env python

import sys

def grabar(nom,posL,posR):
	outfile = open(nom, 'a') # Indicamos el valor 'w'.
	for i in range(len(lpos1)):
		outfile.write(str(lpos1[i]))
		if (i != 6):
			outfile.write(',')
	for i in range(len(lpos1)):
		outfile.write(','+str(lpos1[i]))
	outfile.write('\n')
	outfile.close()

def leer(cosa):
	file=open(cosa,'r')
	data=file.readlines()
	file.close()
	#contador=0
	array=[]
	for linea in data:
	    for numero in linea.split(','):
			array.append(float(numero))

	return array


def mover(array):
	posRecord=[]
	for i in range(0,len(arr),14):
		#print i
		for j in range(14):
			posRecord.append(arr[i+j])
		print posRecord
		posRecord = []
		#mover

lpos1 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 0.09225918246029519]
rpos1 = [1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]

grabar(sys.argv[1],lpos1,rpos1)

arr = leer(sys.argv[1])

mover(arr)
