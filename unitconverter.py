#!/bin/python3
def unit_converter(unit_from,unit_to,value):
    cm_relations = { "cm": 1, "m": 100, "km" : 100000, "mile" : 160000, "yard" : 96 }
    return value*cm_relations[unit_from]/cm_relations[unit_to]
