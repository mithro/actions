#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from __future__ import print_function

import pprint
import urllib
import urllib.request
import os
import os.path
import sys

from pkg_resources import get_distribution

module_name = os.environ['PYTHON_MODULE']

# Download pytest.ini
if not os.path.exists('pytest.ini'):
    dry_run = os.environ.get('CI') != 'true'
    repo = os.environ['GITHUB_REPOSITORY']
    sha = os.environ['GITHUB_SHA']
    url = 'https://raw.githubusercontent.com/{repo}/{sha}/pytest.ini'.format(**locals())
    print('Downloading', url)

    data = urllib.request.urlopen(url).read().decode('utf-8')
    print('Got following data')
    print('-'*75)
    pprint.pprint(data.splitlines())
    print('-'*75)

    with open('pytest.ini', 'w') as f:
        f.write(data)

# Print info about installed module
module = get_distribution(module_name)
version = '.'.join(module.version.split('.'))
print()
print(module_name, 'version:', version)
print(module_name, 'location:', module.location)
print()

sys.stdout.flush()
sys.stderr.flush()
# Run pytest against the library
import pytest
sys.exit(pytest.main())
