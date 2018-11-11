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

class SaveManagerBase(object):

    def __init__(self, save_path, file_indent = None):
        self.save_file = save_path
        self.indent = file_indent

    def create_key(self, key_name, key_value=None):
        save = {}
        with open(self.save_file, 'r') as fi:
            save = json.load(fi)
            
        if not save.has_key(str(key_name)):
            save[str(key_name)] = key_value
            
        else:
            raise ValueError("Key already exists")
            
        with open(self.save_file, 'w') as fi:
            json.dump(save, self.save_file, indent=self.indent)
        
        return 0
    
    def edit_key(self, key_name, key_value=None):
        save={}
        with open(self.save_file, 'r') as fi:
            save = json.load(fi)
            
        if save.has_key(str(key_name)):
            save[str(key_name)] = key_value
            
        else:
            raise ValueError("Key doesn't exists")
            
        with open(self.save_file, 'w') as fi:
            json.dump(save, fi, indent=self.indent)
            
        return 0
        
    def get_value(self, key_name):
        save={}
        with open(self.save_file, 'r') as fi:
            save = json.load(fi)
            
        if save.has_key(str(key_name)):
            return save[str(key_name)]
            
        else:
            raise ValueError("Key doesn't exists")
            
    def set_save_file(self, new_save):
        self.save_file = new_save
    
    
        