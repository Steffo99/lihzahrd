export SPHINXOPTS    =
export SPHINXBUILD   = "sphinx-build"
export SOURCEDIR     = "."
export BUILDDIR      = "_build"

export LATEXMKOPTS   ?= ""
export LATEXOPTS     ?= "-interaction=nonstopmode"

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
