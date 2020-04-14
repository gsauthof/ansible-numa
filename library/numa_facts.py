#!/usr/bin/python
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: © 2020 Georg Sauthoff <mail@gms.tf>
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function, unicode_literals

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: numa_facts

short_description: Collects NUMA facts

version_added: "2.9"

description:
    - collects a mapping

options:

author:
    - Georg Sauthoff (@gsauthof)
'''

EXAMPLES = '''
# Just gather facts
- name: gather NUMA facts
  numa_facts:

'''

RETURN = '''
ansible_facts:
  description: facts to add to ansible_facts
  returned: always
  type: complex
  contains:
    conrep:
      description:
        - Dictonary of NUMA facts
      type: dict
      sample: { "numa_cores": [  [0, 1, 6, 7], [2, 3, 4, 5] ] }
'''

from ansible.module_utils.basic import AnsibleModule

import glob

def get_numa_cores():
    xs = []
    nodes = glob.glob('/sys/devices/system/node/node*')
    def f(x):
        i = x.rindex('node')+4
        return x[:i], int(x[i:])
    nodes.sort(key=f)
    for node in nodes:
        with open(node + '/cpumap') as f:
            m = f.read()
        for i, x in enumerate(reversed( bin(int(m, 16))[2:] )):
            if x == '1':
                xs.append(i)
    return xs

def run_module():
    module_args = dict()

    result = dict(
        changed       = False,
        ansible_facts = dict(),
    )

    module = AnsibleModule(
        argument_spec       = module_args,
        supports_check_mode = True
    )
    # debug = module._verbosity >= 3

    result['ansible_facts']['numa_cores'] = get_numa_cores()


    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()


