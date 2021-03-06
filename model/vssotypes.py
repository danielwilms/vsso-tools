# (C) 2021 BMW Group - All rights reserved.
# AUTHOR: Daniel Wilms BMW Group

from enum import Enum
from rdflib import XSD, URIRef

class VssoConcepts (Enum):
    
    EMPTY =             ""
    BELONGS_TO =        "belongsToVehicleComponent"
    HOLDS_VALUE =       "holdsState"
    HAS_SIGNAL =        "hasDynamicVehicleProperty"
    HAS_ATTRIBUTE =     "hasStaticVehicleProperty"
    PART_OF =           "partOf"
    HAS_COMP_INST =     "hasInstance"
    VEHICLE =           "Vehicle"
    VEHICLE_SIGNAL =    "ObservableVehicleProperty"
    VEHICLE_ACT =       "ActuatableVehicleProperty"
    VEHICLE_COMP =      "VehicleComponent"
    VEHICLE_PROP =      "DynamicVehicleProperty"

    def __init__ (self, vsso_name):
        self.ns = "https://github.com/danielwilms/vsso-demo/"
        self.vsso_name = vsso_name

    @property
    def uri(self):
        return URIRef(f'{self.ns}{self.value}')

    @property
    def uri_string(self):
        return f'{self.ns}{self.value}'



DataTypes = {'UInt8': XSD.unsignedByte,
    'Int8': XSD.byte,
    'UInt16': XSD.unsignedShort,
    'Int16': XSD.short,
    'UInt32': XSD.unsignedInt,
    'Int32': XSD.int,
    'UInt64': XSD.unsignedLong,
    'Int64': XSD.long,
    'Boolean': XSD.boolean,
    'Float': XSD.float,
    'Double': XSD.double,
    'String': XSD.string
}
    
Namespaces = {
    'qudt': "http://qudt.org/schema/qudt/",
    'cdt': "http://w3id.org/lindt/custom_datatypes#"
}
DataUnits = {    
    'N.m': URIRef(Namespaces["cdt"]+'ucum'),
    'cm3': URIRef(Namespaces["cdt"]+'volume'),
    'cm^3': URIRef(Namespaces["cdt"]+'volume'),
    'kw': URIRef(Namespaces["cdt"]+'power'),
    'l': URIRef(Namespaces["cdt"]+'volume'),
    'mm': URIRef(Namespaces["cdt"]+'length'),
    'kg': URIRef(Namespaces["cdt"]+'mass'),
    'inch': URIRef(Namespaces["cdt"]+'length'),
    'A': URIRef(Namespaces["qudt"]+'ElectricCurrentUnit'),
    'Nm': URIRef(Namespaces["qudt"]+'BendingMomentOrTorqueUnit'),
    'N.m': URIRef(Namespaces["qudt"]+'BendingMomentOrTorqueUnit'),
    'V': URIRef(Namespaces["qudt"]+'EnergyPerElectricChargeUnit'),
    'celsius': URIRef(Namespaces["qudt"]+'TemperatureUnit'),
    'cm/s': URIRef(Namespaces["qudt"]+'LinearVelocityUnit'),
    'degree': URIRef(Namespaces["qudt"]+'AngleUnit'),
    'degrees': URIRef(Namespaces["qudt"]+'AngleUnit'),
    'degrees/s': URIRef(Namespaces["qudt"]+'AngularVelocityUnit'),
    'g/s': URIRef(Namespaces["qudt"]+'MassPerTimeUnit'),
    'inch': URIRef(Namespaces["qudt"]+'LengthUnit'),
    'kW': URIRef(Namespaces["qudt"]+'PowerUnit'),
    'kilometer': URIRef(Namespaces["qudt"]+'LengthUnit'),
    'km': URIRef(Namespaces["qudt"]+'LengthUnit'),
    'km/h': URIRef(Namespaces["qudt"]+'LinearVelocityUnit'),
    'kpa': URIRef(Namespaces["qudt"]+'PressureOrStressUnit'),
    'kPa': URIRef(Namespaces["qudt"]+'PressureOrStressUnit'),
    'l': URIRef(Namespaces["qudt"]+'VolumeUnit'),
    'l/h': URIRef(Namespaces["qudt"]+'VolumePerTimeUnit'),
    'm': URIRef(Namespaces["qudt"]+'LengthUnit'),
    'm/s': URIRef(Namespaces["qudt"]+'LinearVelocityUnit'),
    'm/s2': URIRef(Namespaces["qudt"]+'LinearAccelerationUnit'),
    'm/s^2': URIRef(Namespaces["qudt"]+'LinearAccelerationUnit'),
    'mbar': URIRef(Namespaces["qudt"]+'PressureOrStressUnit'),
    'min': URIRef(Namespaces["qudt"]+'TimeUnit'),
    'ml': URIRef(Namespaces["qudt"]+'VolumeUnit'),
    'mm': URIRef(Namespaces["qudt"]+'LengthUnit'),
    'pa': URIRef(Namespaces["qudt"]+'PressureOrStressUnit'),
    'Pa': URIRef(Namespaces["qudt"]+'PressureOrStressUnit'),
    'percent': URIRef(Namespaces["qudt"]+'DimensionlessUnit'),
    'percentage': URIRef(Namespaces["qudt"]+'DimensionlessUnit'),
    'ratio': URIRef(Namespaces["qudt"]+'DimensionlessUnit'),
    'rpm': URIRef(Namespaces["qudt"]+'AngularVelocityUnit'),
    's': URIRef(Namespaces["qudt"]+'TimeUnit')
}
