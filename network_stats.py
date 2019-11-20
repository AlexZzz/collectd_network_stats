#!/usr/bin/python

import collectd
import json
from subprocess import check_output

def get_nstat():
        return check_output(['nstat','-azj'])

def read_func():
        val = collectd.Values(type='gauge')
        val.plugin = 'nstat'
        for k, v in json.loads(get_nstat()).get('kernel').items():
                val.plugin_instance=k
                val.dispatch(values=[v])

collectd.register_read(read_func)
