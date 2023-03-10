#!/usr/bin/env python3
# -*- coding: utf-8 -*-


job_data = [
   ('121', 'Yates', 'NY', 5094),
   ('122', 'Wyoming', 'NY', 8722),
   ('001', 'Albany', 'NY', 162692),
   ('003', 'Allegany', 'NY', 11986),
   ]

print()
print(job_data)

# standard sort
job_data.sort()
print()
print(job_data)

# sort by key
def by_state(a):
    return a[1]

job_data.sort(key=by_state)
print()
print(job_data)
