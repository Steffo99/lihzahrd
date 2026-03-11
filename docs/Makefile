export SPHINXOPTS    =
export SPHINXBUILD   = "sphinx-build"
export SOURCEDIR     = "."
export BUILDDIR      = "_build"

export AUTOBUILD     = "sphinx-autobuild"
export AUTOOPTS      = --watch='../src'

export LATEXMKOPTS   ?= ""
export LATEXOPTS     ?= "-interaction=nonstopmode"

.PHONY: help dev html clear Makefile

help:
	uv run $(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

dev:
	uv run $(AUTOBUILD) $(SOURCEDIR) $(BUILDDIR) $(AUTOOPTS) $(O)

html:
	uv run $(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

clean:
	uv run $(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
