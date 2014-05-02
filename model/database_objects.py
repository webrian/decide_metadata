#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "Adrian Weber, Centre for Development and Environment, University of Bern"
__date__ = "$Apr 17, 2014 11:09:03 AM$"

import hashlib

from .meta import Base
from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {"schema": 'metadata'}
    gid = Column(Integer, primary_key=True)
    name_en = Column(String(256), nullable=False)
    name_lo = Column(String(256), nullable=False)
    order = Column(Integer, nullable=False)

class Privilege(Base):
    __tablename__ = 'privileges'
    __table_args__ = {"schema": "metadata"}
    gid = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String(256))

class Source(Base):
    __tablename__ = 'sources'
    __table_args__ = {"schema": 'metadata'}
    gid = Column(Integer, primary_key=True)
    description_en = Column(String(256), nullable=False)
    description_lo = Column(String(256), nullable=False)

class Owner(Base):
    __tablename__ = 'owners'
    __table_args__ = {"schema": 'metadata'}
    gid = Column(Integer, primary_key=True)
    name_en = Column(String(256), nullable=False)
    name_lo = Column(String(256), nullable=False)

class Datatype(Base):
    __tablename__ = "datatypes"
    __table_args__ = {"schema": "metadata"}
    gid = Column(Integer, primary_key=True)
    type = Column(String(256))

class AdminLevel(Base):
    __tablename__ = 'administrative_levels'
    __table_args__ = {"schema": 'metadata'}
    gid = Column(Integer, primary_key=True)
    name_en = Column(String(256), nullable=False)
    name_lo = Column(String(256), nullable=False)

variables_layers = Table('variables_layers', Base.metadata,
                         Column('gid', Integer, primary_key=True),
                         Column('fk_variable', Integer, ForeignKey('metadata.variables.gid'), nullable=False),
                         Column('fk_layer', Integer, ForeignKey('metadata.layers.gid'), nullable=False),
                         schema='metadata'
                         )

class Layer(Base):
    __tablename__ = "layers"
    __table_args__ = {"schema": "metadata"}
    gid = Column(Integer, primary_key=True)
    url = Column(String(256), nullable=False)
    layername = Column(String(256), nullable=False)
    name_en = Column(String(256), nullable=False)
    name_lo = Column(String(256), nullable=False)
    description_en = Column(String(256))
    description_lo = Column(String(256))
    type = Column(String(256))
    fk_privilege = Column(Integer, ForeignKey('metadata.privileges.gid'))
    privilege = relationship("Privilege")
    fk_category = Column(Integer, ForeignKey('metadata.categories.gid'))
    variables = relationship('Variable', secondary=variables_layers)

class Variable(Base):
    __tablename__ = "variables"
    __table_args__ = {"schema": "metadata"}
    gid = Column(Integer, primary_key=True)
    code = Column(String(256), nullable=False)
    short_label = Column(String(256), nullable=False)
    label_en = Column(String(256), nullable=False)
    label_lo = Column(String(256), nullable=False)
    description_en = Column(String(256))
    description_lo = Column(String(256), nullable=False)
    is_in_statable = Column(Boolean)
    is_in_gis_downloadable = Column(Boolean)
    fk_privilege = Column(Integer, ForeignKey('metadata.privileges.gid'))
    privilege = relationship("Privilege")
    fk_category = Column(Integer, ForeignKey('metadata.categories.gid'))
    fk_source = Column(Integer, ForeignKey('metadata.sources.gid'))
    fk_owner = Column(Integer, ForeignKey('metadata.owners.gid'))
    fk_datatype = Column(Integer, ForeignKey('metadata.datatypes.gid'))
    datatype = relationship("Datatype")
    fk_administrative_level = Column(Integer, ForeignKey('metadata.administrative_levels.gid'))