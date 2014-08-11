# Convert .ui files to .py files using pyuic4 for use with PyQt4
# Use: Put this file in the folder with all your .ui files. Run make from the command line.
# Note: Ensure this file uses tabs for indents, not spaces or it will not work.

UIFILES := $(wildcard *.ui)
PYFILES := $(UIFILES:.ui=.py)

.PHONY: all
all: $(PYFILES)

%.py: %.ui
	pyuic4 $< --output $@