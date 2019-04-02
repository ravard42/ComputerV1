import sys
import matplotlib.pyplot as plt

#On considèrera toujours que l’entrée est bien formatée,
#ie:
#Tous les termes sont de la forme ap * x^p. 
#Les puissances sont bien ordonnées et toutes présentes

def printGraph(coef):
	axes = plt.gca()
	
	axes.set_xlim(-10, 10)
	plt.plot([-10, 10], [0, 0], c='black')
	
	ylim = max([f(x, coef) for x in range(-10, 11)])
	ylim = max(ylim, 10)
	axes.set_ylim(-ylim, ylim)
	plt.plot([0, 0], [-ylim, ylim], c='black')
	
	plt.plot([x for x in range(-10, 11)], [f(x, coef) for x in range(-10, 11)], c='lime')
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
		if (coef[i].is_integer()):
			print('{} * X^{}'.format(abs(int(coef[i])), i), end=end)
		else:
			print('{} * X^{}'.format(abs(coef[i]), i), end=end)

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
	print_forme_reduite(coef)
	degree = len(coef) - 1
	print('Degré du polynôme:', degree)
	if (degree == 2):
		print('discriminant:', delta(coef))
	printGraph(coef)
