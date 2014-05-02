#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Adrian Weber, Centre for Development and Environment, University of Bern"
__date__ ="$Apr 17, 2014 11:06:43 AM$"

"""SQLAlchemy Metadata and Session object"""
from sqlalchemy.ext.declarative import declarative_base

__all__ = ['Base']

# The declarative Base
Base = declarative_base()
