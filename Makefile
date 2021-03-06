# Copyright (C) 2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

# Set up a Python environment to run the actions_include tool on.
ENV_DIR = venv
PYTHON = $(ENV_DIR)/bin/python3
ACTIVATE = source $(ENV_DIR)/bin/activate;

env: requirements.txt
	rm -rf $(ENV_DIR)
	virtualenv --copies $(ENV_DIR)
	$(ACTIVATE) pip install -r $<
	touch --reference=$< $(PYTHON)

.PHONY: env

$(PYTHON): requirements.txt
	make env

enter: | $(PYTHON)
	$(ACTIVATE) bash

# Generate the output files
SRC_YAML = $(wildcard workflows/*.yml)

build: | $(PYTHON)
	@true

info:
	@echo 'Output files: $(OUT_YAML)'

.PHONY: info
