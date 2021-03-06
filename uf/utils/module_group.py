#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2017, UFactory, Inc.
# All rights reserved.
#
# Author: Duke Fong <duke@ufactory.cc>


class ModuleGroup():
    def __init__(self, ufc, node, iomap, **kwargs):
        self.nodes = {}
        for n in self.__class__.sub_nodes:
            args = {}
            if 'args' in n.keys():
                for k in n['args']:
                    args[k] = kwargs[k]
            for io in list(n['iomap']):
                t, p = n['iomap'][io].split(': ', 1)
                if t == 'outer':
                    if p in iomap.keys():
                        n['iomap'][io] = iomap[p]
                    else:
                        del n['iomap'][io]
                elif t == 'inner':
                    n['iomap'][io] = node + '/' + p
            self.nodes[n['node']] = n['module'](ufc, node + '/' + n['node'], n['iomap'], **args)


