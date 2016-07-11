#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  db_conns.py
#  sql-sanity-checker
#

import yaml
import MySQLdb
import MySQLdb.cursors

class DBConnections(object):
    connections = {}

    def __init__(self, config_file):
        with open(config_file) as istream:
            configs = yaml.safe_load_all(istream)
            for config in configs:
                db_name = config['name']
                del config['name']
                self.connections[db_name] = MySQLdb.connect(cursorclass=MySQLdb.cursors.DictCursor, **config)

