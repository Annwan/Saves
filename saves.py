# -*- coding: utf-8 -*-
"""
    Copyright © 2018 Antoine COMBET

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this module.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import os

class SaveManagerBase(object):
    """
    Base class containing all the functions of the module
    Usable as this or as base for a more specific save system
    Keys are always converted to string to match JSON rules
    """

    def __init__(self, save_path, file_indent = None):
        try:
            fi = open(save_path,'r')
            fi.close()
        except FileNotFoundError:
            fi = open(save_path, 'w')
            fi.close()
        self.save_file = save_path
        self.indent = file_indent

    def write_key(self, key, value=None):
        """
    Changes the value of the key `key` to `value` (`None` by default).
    If the key `key` doesn't exist, creates and assign it to `value`.
    Returns `value`
        """
        save={}
        with open(self.save_file, 'r') as fi:
            try:
                save = json.load(fi)
            except:
                pass
                
            
        save[str(key)] = value
        with open(self.save_file, 'w') as fi:
            json.dump(save, fi, indent=self.indent)
            
        return value
        
    def get_value(self, key):
        """
    Returns the value stored at the key `key`
    If the key `key` doesn't exist, raises ValueError
        """
        save={}
        with open(self.save_file, 'r') as fi:
            save = json.load(fi)
            
        if str(key) in save.keys():
            return save[str(key)]
            
        else:
            raise ValueError("Key '" + str(key) + "' doesn't exist")
            
    def set_save_file(self, new_save):
        self.save_file = new_save
    
    
        