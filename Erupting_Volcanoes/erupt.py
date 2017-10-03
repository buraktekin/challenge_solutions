# -*- coding: utf-8 -*-
__author__ = "Burak Tekin"

import numpy as np
import time
import sys

class Erupting(object):
	# Colors
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	DANGER = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	DIVIDER = BOLD + "\n{}\n".format('-'*80) + ENDC

	# --------------------------INITIALIZING...--------------------------
	def __init__(self):
		print self.BOLD + "\n{0}\n ERUPTING VOLCANOES SIMULATION \n CREATED BY: Burak TEKIN \n ❤ ❤ ❤ Coded by love ❤ ❤ ❤ \n{0}".format('-'*80) + self.ENDC
		for i in range(20):
			time.sleep(.2)
			sys.stdout.write("\rLoading: [{}]".format("🌋  " * i))
			sys.stdout.flush()
		print self.DIVIDER + self.BOLD + "Following prompt will ask you about the parameters needed to create the simulation.\n" + self.BLUE + "- Have Fun!" + self.ENDC + self.DIVIDER

		self.volcanoes = dict()
		self.n = int(raw_input("give a number n to create an area with the size of nxn: "))
		self.area = np.zeros((self.n, self.n))
		print self.UNDERLINE + self.HEADER + "\nAREA CREATED:\n" + self.ENDC + self.BLUE + str(self.area) + self.ENDC + self.DIVIDER

		self.active_volcanoes = int(raw_input("how many active volcanoes are there in this area:"))
		for volcano in range(self.active_volcanoes):
			current_volcano = dict()
			print "\n{0} Volcano #{1} {0}".format('-'*35, volcano + 1)
			x = self.prompter(self.n, "POSITION-X: ")
			y = self.prompter(self.n, "POSITION-Y: ")
			w = raw_input("POWER: ")
			current_volcano['x'] = x - 1
			current_volcano['y'] = y - 1
			current_volcano['w'] = w
			self.volcanoes["volcano"+str(volcano + 1)] = current_volcano
		self.locate_volcanoes()
	# --------------------------/INITIALIZING --------------------------

	# ----------------------------- METHODS ----------------------------
	def prompter(self, limit, message):
		param = int(raw_input(message))
		if (0 < param <= limit):
			print self.HEADER + str(param) + self.ENDC
		else:
			print self.DANGER + "CUUUUSSS BILADER!!\nThe value given is out of determined area size.\nKeep the value in the range of 1 - {}".format(limit) + self.ENDC
			param = self.prompter(limit, message)
		return param


	def locate_volcanoes(self):
		for volcano in self.volcanoes.values():
			self.area[volcano['x']][volcano['y']] = volcano['w']
			coordinates = [volcano['x'], volcano['y']]
			self.find_neighbours(coordinates, 1)


	def find_neighbours(self, cell, radius):
		traced = list()
		peripheral = list()
		while (radius < self.n):
			temp = list()
			for r in range(cell[0] - radius, cell[0] + radius + 1):
				for c in range(cell[1] - radius, cell[1] + radius + 1):
					if([r,c] != cell and [r,c] not in traced and 0 <= r < self.n and 0 <= c < self.n):
							temp.append([r,c])
							traced.append([r,c])
					
			peripheral.append(temp)
			radius += 1

		self.volcanic_effect(peripheral, cell)


	def volcanic_effect(self, peripheral, cell):
		max_power = int(self.area[cell[0]][cell[1]])
		result = max_power
		for index, peripherals in enumerate(peripheral):
			for per in peripherals:
				value = self.area[per[0]][per[1]]
				new_value = max_power - (index + 1)
				if new_value > 0:
					value += new_value
					result = value if value > result else result
				else:
					value += 0
				self.area[per[0]][per[1]] = value
				# print value, " - ", max_power, " - ", index

		print self.BLUE + str(self.area) + self.ENDC + "\n"
		print "-------------------------------"
		print "{}".format(self.BLUE + "MAX ELEMENT RESULT:" + str(result) + self.ENDC)

	# -------------------------- /METHODS --------------------------

e = Erupting()
