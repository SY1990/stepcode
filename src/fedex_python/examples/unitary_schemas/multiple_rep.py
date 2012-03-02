# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Expr import *
from SCL.Builtin import *
from SCL.Rules import *

schema_name = 'multiple_rep'

schema_scope = sys.modules[__name__]

text = STRING
representation_context = STRING
identifier = STRING
shape_definition = STRING
transformation = STRING
representation_item = STRING
characterized_product_definition = STRING
# SELECT TYPE characterized_definition
characterized_definition = SELECT(
	'characterized_object',
	'characterized_product_definition',
	'shape_definition',
	scope = schema_scope)
label = STRING
characterized_object = STRING

####################
 # ENTITY representation_relationship #
####################
class representation_relationship(BaseEntityClass):
	'''Entity representation_relationship definition.

	:param name
	:type name:STRING

	:param rep_1
	:type rep_1:representation

	:param rep_2
	:type rep_2:representation
	'''
	def __init__( self , name,rep_1,rep_2, ):
		self.name = name
		self.rep_1 = rep_1
		self.rep_2 = rep_2

	@apply
	def name():
		def fget( self ):
			return self._name
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument name is mantatory and can not be set to None')
			if not check_type(value,STRING):
				self._name = STRING(value)
			else:
				self._name = value
		return property(**locals())

	@apply
	def rep_1():
		def fget( self ):
			return self._rep_1
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument rep_1 is mantatory and can not be set to None')
			if not check_type(value,representation):
				self._rep_1 = representation(value)
			else:
				self._rep_1 = value
		return property(**locals())

	@apply
	def rep_2():
		def fget( self ):
			return self._rep_2
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument rep_2 is mantatory and can not be set to None')
			if not check_type(value,representation):
				self._rep_2 = representation(value)
			else:
				self._rep_2 = value
		return property(**locals())

####################
 # ENTITY shape_representation_relationship #
####################
class shape_representation_relationship(representation_relationship):
	'''Entity shape_representation_relationship definition.
	'''
	def __init__( self , representation_relationship__name , representation_relationship__rep_1 , representation_relationship__rep_2 ,  ):
		representation_relationship.__init__(self , representation_relationship__name , representation_relationship__rep_1 , representation_relationship__rep_2 , )

####################
 # ENTITY representation #
####################
class representation(BaseEntityClass):
	'''Entity representation definition.

	:param name
	:type name:STRING

	:param items
	:type items:SET(1,None,'STRING', scope = schema_scope)

	:param context_of_items
	:type context_of_items:STRING
	'''
	def __init__( self , name,items,context_of_items, ):
		self.name = name
		self.items = items
		self.context_of_items = context_of_items

	@apply
	def name():
		def fget( self ):
			return self._name
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument name is mantatory and can not be set to None')
			if not check_type(value,STRING):
				self._name = STRING(value)
			else:
				self._name = value
		return property(**locals())

	@apply
	def items():
		def fget( self ):
			return self._items
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument items is mantatory and can not be set to None')
			if not check_type(value,SET(1,None,'STRING', scope = schema_scope)):
				self._items = SET(value)
			else:
				self._items = value
		return property(**locals())

	@apply
	def context_of_items():
		def fget( self ):
			return self._context_of_items
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument context_of_items is mantatory and can not be set to None')
			if not check_type(value,STRING):
				self._context_of_items = STRING(value)
			else:
				self._context_of_items = value
		return property(**locals())

####################
 # ENTITY property_definition #
####################
class property_definition(BaseEntityClass):
	'''Entity property_definition definition.

	:param name
	:type name:STRING

	:param definition
	:type definition:characterized_definition
	'''
	def __init__( self , name,definition, ):
		self.name = name
		self.definition = definition

	@apply
	def name():
		def fget( self ):
			return self._name
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument name is mantatory and can not be set to None')
			if not check_type(value,STRING):
				self._name = STRING(value)
			else:
				self._name = value
		return property(**locals())

	@apply
	def definition():
		def fget( self ):
			return self._definition
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument definition is mantatory and can not be set to None')
			if not check_type(value,characterized_definition):
				self._definition = characterized_definition(value)
			else:
				self._definition = value
		return property(**locals())

####################
 # ENTITY context_dependent_shape_representation #
####################
class context_dependent_shape_representation(BaseEntityClass):
	'''Entity context_dependent_shape_representation definition.

	:param representation_relation
	:type representation_relation:shape_representation_relationship
	'''
	def __init__( self , representation_relation, ):
		self.representation_relation = representation_relation

	@apply
	def representation_relation():
		def fget( self ):
			return self._representation_relation
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument representation_relation is mantatory and can not be set to None')
			if not check_type(value,shape_representation_relationship):
				self._representation_relation = shape_representation_relationship(value)
			else:
				self._representation_relation = value
		return property(**locals())

####################
 # ENTITY definitional_representation_relationship #
####################
class definitional_representation_relationship(representation_relationship):
	'''Entity definitional_representation_relationship definition.
	'''
	def __init__( self , representation_relationship__name , representation_relationship__rep_1 , representation_relationship__rep_2 ,  ):
		representation_relationship.__init__(self , representation_relationship__name , representation_relationship__rep_1 , representation_relationship__rep_2 , )

####################
 # ENTITY component_2d_location #
####################
class component_2d_location(context_dependent_shape_representation,shape_representation_relationship,definitional_representation_relationship):
	'''Entity component_2d_location definition.

	:param context_dependent_shape_representation_representation_relation
	:type context_dependent_shape_representation_representation_relation:component_2d_location
	'''
	def __init__( self , context_dependent_shape_representation__representation_relation ,  ):
		context_dependent_shape_representation.__init__(self , context_dependent_shape_representation__representation_relation , )
		shape_representation_relationship.__init__(self , )
		definitional_representation_relationship.__init__(self , )

	@apply
	def context_dependent_shape_representation_representation_relation():
		def fget( self ):
			return EvalDerivedAttribute(self,'''SELF''')
		def fset( self, value ):
		# DERIVED argument
			raise AssertionError('Argument context_dependent_shape_representation_representation_relation is DERIVED. It is computed and can not be set to any value')
		return property(**locals())
