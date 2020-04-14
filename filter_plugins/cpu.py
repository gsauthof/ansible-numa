#!/usr/bin/python
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: © 2020 Georg Sauthoff <mail@gms.tf>
# SPDX-License-Identifier: GPL-3.0-or-later

def cpumask(cores, fmt='hex'):
    r = 0
    if type(cores) is not list:
        cores = [ cores ]
    for x in cores:
        r |= 1 << x
    if fmt == 'hex':
        return hex(r)
    else:
        return str(r)

def mapidx(xs, ys):
    if type(xs) is not list:
        return ys[xs]
    zs = []
    for x in xs:
        zs.append(ys[x])
    return zs

class FilterModule(object):

    def filters(self):
        filters = {
                'cpumask': cpumask,
                'mapidx': mapidx
        }
        return filters
