#!/usr/bin/python

# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: © 2020 Georg Sauthoff <mail@gms.tf>
# SPDX-License-Identifier: GPL-3.0-or-later

def cpumask(cores, fmt='hex'):
    r = 0
    for x in cores:
        r |= 1 << x
    if fmt == 'hex':
        return hex(r)
    else:
        return str(r)

def mapidx(xs, ys):
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
