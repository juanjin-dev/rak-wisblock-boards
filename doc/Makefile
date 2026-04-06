# ------------------------------------------------------------------------------
# Minimal Zephyr-style documentation build
# SPDX-License-Identifier: Apache-2.0

SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build
SPHINXOPTS ?= -j auto -W --keep-going

.PHONY: sync html clean

sync:
	python3 _scripts/sync_doc_sources.py

html: sync
	$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

clean:
	rm -rf $(BUILDDIR)
