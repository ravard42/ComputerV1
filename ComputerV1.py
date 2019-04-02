import sys
import matplotlib.pyplot as plt


def printGraph(coef):
	axes = plt.gca()
	
	axes.set_xlim(-10, 10)
	plt.plot([-10, 10], [0, 0], c='black')
	
	ylim = max([f(x, coef) for x in range(-10, 11)])
	axes.set_ylim(-ylim, ylim)
	plt.plot([0, 0], [-ylim, ylim], c='black')
	
	plt.plot([x for x in range(-10, 11)], [f(x, coef) for x in range(-10, 11)], c='lime')
	plt.show()

def delta(coef):
	return (coef[1]**2 - 4*coef[2]*coef[0])

def f(x, coef):
	return coef[2] * x ** 2 + coef[1] * x + coef[0]


if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("usage: python ComputerV1.py 'd * X^0 + e * X^1 + f * X^2 = g * X^0 + h * X^1 + i * X^2'")	
	else:
		left = [int(tab.split("*")[0]) for tab in sys.argv[1].split("=")[0].split('+')]
		right = [int(tab.split("*")[0]) for tab in sys.argv[1].split("=")[1].split('+')]
		coef = [left[0] - right[0], left[1] - right[1], left[2] - right[2]]


		print('La forme reduite de l\'equation est la suivante: {} * X^0 + {} * X^1 + {} * X^2 = 0'.format(coef[0], coef[1], coef[2]))

		if (coef[2] != 0):
			degree = 2
		else:
			if (coef[1] != 0):
				degree = 1
			else:
				degree = 0

		print('Polynomial degree:', degree)
		if (degree == 2):
			print('discriminant:', delta(coef))
		printGraph(coef)
