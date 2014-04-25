#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Adrian Weber, Centre for Development and Environment, University of Bern"
__date__ ="$Apr 17, 2014 11:07:49 AM$"

from decide_metadata.model.meta import MetadataSession

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    MetadataSession.configure(bind=engine)