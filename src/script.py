#!/usr/bin/python
import urllib, json
import os
import re
import shutil

variable='1'
variable2='100'

for p in range(1,7500,100):

	imagenes=[]
	MeSHes=[]
	imag=[]
	normal=[]
	anormal=[]
	et=[]

	url = "https://openi.nlm.nih.gov/retrieve.php?query=&it=xg&coll=cxr&m="+variable+"&n="+variable2
	response = urllib.urlopen(url)
	data = json.load(response)

	lista=data['list']
	contador=-1
	for l in lista:
		contador=contador+1
		imagen=data['list'][contador]['imgThumb']
		imagen=imagen.replace('.png','')
		imagen=list(imagen)
		posicion=imagen.index('R')
		imagen[0:posicion+1]=[]
		imagen=''.join(imagen)
		MeSH = data['list'][contador]['MeSH']['major']
		imagenes.append(imagen)
		MeSHes.append(MeSH)


	contador=-1
	for j in imagenes:
		contador=contador+1
		im=str(imagenes[contador])
		imag.append(im)

	x=[]
	final=[]
	contador=-1
	for i in MeSHes:
		contador=contador+1
		etiqueta=MeSHes[contador]
		cont=-1
		for j in etiqueta:
			cont=cont+1
			et=etiqueta[cont].split('/')
			et=et+x
			x=et
		final.append(x)
		x=[]

		if 'normal' in final[contador]:
			normal.append(imag[contador]+'.jpg')
		else:
			anormal.append(imag[contador]+'.jpg')

	contador=-1
	for n in normal:
		contador=contador+1
		foto=normal[contador]
		try:
			src="../Desktop/X/%s" %foto
			dst="../Desktop/Normal"
			shutil.move(src,dst)
		except:
			print foto, 'No encontrada\n'
	contador=-1
	for a in anormal:
		contador=contador+1
		foto=anormal[contador]
		try:
			src=".../Desktop/X/%s" %foto
			dst=".../Desktop/Anormal"
			shutil.move(src,dst)
		except:
			print foto, 'No encontrada\n'

	variable=int(variable)+100
	variable=str(variable)
	variable2=int(variable2)+100
	variable2=str(variable2)
