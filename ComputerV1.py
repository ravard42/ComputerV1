import sys
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#On considèrera toujours que l’entrée est bien formatée,
#ie:
#Tous les termes sont de la forme ap * x^p. 
#Les puissances sont bien ordonnées et toutes présentes

rep_lim = 10

def printGraph(coef):
	axes = plt.gca()
	
	axes.set_xlim(-rep_lim, rep_lim)
	plt.plot([-rep_lim, rep_lim], [0, 0], c='black')
	
	ylim = max([f(x, coef) for x in range(-rep_lim, rep_lim + 1)])
	ylim = max(ylim, rep_lim)
	axes.set_ylim(-ylim, ylim)
	plt.plot([0, 0], [-ylim, ylim], c='black')

	x = np.linspace(-rep_lim, rep_lim, 200)
	plt.plot(x, f(x, coef))	
	plt.show()

def delta(coef):
	return (coef[1]**2 - 4*coef[2]*coef[0])

def f(x, coef):
	ret = 0;
	for i in range(0, len(coef)):
		ret += coef[i] * x ** i
	return ret

def print_forme_reduite(coef):
	print('Forme réduite de l\'équation: ', end='')
	for i in range(0, len(coef)):
		if (i is not len(coef) - 1):
			end = ' + ' if coef[i + 1] >= 0 else ' - '
		else:
			end = " = 0\n"
		tmp = abs(coef[i]) if i != 0 else coef[i]
		if (coef[i].is_integer()):
			print('{} * X^{}'.format(int(tmp), i), end=end)
		else:
			print('{} * X^{}'.format(round(tmp, 3), i), end=end)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		sys.exit("usage: python ComputerV1.py 'a0 * X^0 + a1 * X^1 + a2 * X^2 + ... + an * X^n = b0 * X^0 + b1 * X^1 + b2 * X^2 + ... + bm * X^m'")	

	s = sys.argv[1]
	
	while (1):
		index = s.find('- ')
		if (index == -1):
			break
		s = s[:index] + '+ -' + s[index + 2:]
		
	left = [float(tab.split("*")[0]) for tab in s.split("=")[0].split('+')]
	right = [float(tab.split("*")[0]) for tab in s.split("=")[1].split('+')]
	n = max(len(left), len(right))
	left.extend([0 for i in range(0, n - len(left))])
	right.extend([0 for i in range(0, n - len(right))])
	coef = [left[i] - right[i] for i in range(0, n)]
	while (not coef[-1] and len(coef) > 1):
		del coef[-1]
	print("note: les flottants sont arrondis a 3 chiffres après la virgule")
	print_forme_reduite(coef)
	degree = len(coef) - 1
	print('Degré du polynôme:', degree)
	if (degree > 2):
		print("le degré de l'équation est supérieur à 2, je ne peux pas résoudre...")
	elif (degree == 2):
		d = delta(coef)
		print('discriminant:', round(d, 3))
		if (d > 0):
			x1 = (-coef[1] - sqrt(d)) / (2 * coef[2])
			x1 = int(x1) if x1.is_integer() else round(x1, 3)
			x2 = (-coef[1] + sqrt(d)) / (2 * coef[2])
			x2 = int(x2) if x2.is_integer() else round(x2, 3)
			print("discriminant strictement positif donc 2 solutions sur R\nx1 = {}\nx2 = {}".format(x1, x2))
		elif (d == 0):
			x0 = -coef[1] / (2 * coef[2])
			x0 = int(x0) if x0.is_integer() else round(x0, 3)
			print("Une seule solution -> x0 =", x0)
		elif (d < 0):
			xr = -coef[1] / (2 * coef[2])
			xr = int(xr) if xr.is_integer() else round(xr, 3)
			xi = sqrt(abs(d)) / (2 * coef[2])
			xi = int(xi) if xi.is_integer() else round(xi, 3)
			print("discriminant strictement négatif donc 2 solutions complexes conjuguées :\nx1 = {} - i * {}\nx2 = {} + i * {}".format(xr, xi, xr, xi))
	elif (degree == 1):
		x0 = -coef[0] / coef[1]
		x0 = int(x0) if x0.is_integer() else round(x0, 3)
		print("Une seule solution -> x0 =", x0)
	elif (degree == 0):
		if (coef[0] == 0):
			print("Tous les réels sont solutions")
		else:
			print("Aucune solution")
	printGraph(coef)
