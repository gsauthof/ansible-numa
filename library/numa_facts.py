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
      sample: { "numa_cores": [  0, 1, 6, 7, 2, 3, 4, 5 ] }
'''

from ansible.module_utils.basic import AnsibleModule

def get_numa_cores():
    xs = []
    i = 0
    try:
        while True:
            with open('/sys/devices/system/node/node{}/cpulist'.format(i)) as f:
                m = f.read()
            ys = sum(([list(range(int(x), int(y)+1))
                         for (x, y) in (z.split('-'),)][0] if '-' in z
                             else [int(z)] for z in m.split(',')), [])
            xs.extend(ys)
            i += 1
    except IOError:
        pass
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


