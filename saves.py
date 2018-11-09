# -*- coding: utf-8 -*-
"""

"""

from __future__ import unicode_litterals
from codecs import open

import json

def create_key(save_file, key_name, key_value=None,indent=None):
    save = {}
    with open(save_file, 'r') as fi:
        save = json.load(fi)
        
    if not save.has_key(str(key_name)):
        save[str(key_name)] = key_value
        
    else:
        raise ValueError("key already exists")
        
    with open(save_file, 'w') as fi:
        json.dump(save, save_file, indent=indent)
    
    return 0

def edit_key(save_file, key_name, key_value=None,indent=None):
    save={}
    with open(save_file, 'r') as fi:
        save = json.load(fi)
        
    if save.has_key(str(key_name)):
        save[str(key_name)] = key_value
        
    else:
        raise ValueError("key doesn't exists")
        
    with open(save_file, 'w') as fi:
        json.dump(save, save_file, indent=indent)
        
    return 0
    
def get_value(save_file, key_name):
    save={}
    with open(save_file, 'r') as fi:
        save = json.load(fi)
        
    if save.has_key(str(key_name)):
        return save[str(key_name)]
        
    else:
        raise ValueError("key doesn't exists")
    