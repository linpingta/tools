#-*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :


""" Element With Business Logic"""
__author__ = "chutong"


from abc import ABCMeta, abstractmethod
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class BaseRender(object):
	"""
	Base data render class
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def run(self, dataframe, dimensions, metrics, logger):
		""" Render data to output"""
		pass


class LinePlotter(BaseRender):
	""" 
	Plot line for data
	"""
	def __init__(self):
		self._name = None

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	def run(self, dataframe, dimensions, metrics, handler, logger):
		assert self._name
		if len(dimensions) == 1:
			plt.figure()
			dataframe.plot(x=dataframe[dimensions[0]], y=metrics)
			plt.title(self._name)
			handler.savefig()
			plt.close()
		else:
			raise Exception('dimensions len[%d] and metrics len[%d] illegal' % (len(dimensions), len(metrics)))


class RenderFactory(object):
	"""
	Build render or plotter
	"""
	@classmethod
	def build(cls, type):
		if type == 'line':
			return LinePlotter()
		else:
			raise TypeError("type %s not defined for render" % type)
