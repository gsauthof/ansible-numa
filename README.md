This repository contains a small Ansible module and filter plugin
for dealing with NUMA CPUs and CPU masks.

In detail:

- a fact gathering module that lists the CPU ids in consecutive NUMA order
- a filter plugin that provides a filter for creating CPU masks
  and mapping (CPU) indices

2020, Georg Sauthoff <mail@gms.tf>
