#!/bin/bash
###############################################################################
## Run this script from the directory containing the LaTeX source to compile ##
## all presentation materials.                                               ##
###############################################################################

# initial compilation
pdflatex -jobname 2015-12-14-wysocki-gr-spherical-stars \
         '\def\notes{}\input{2015-12-14-wysocki-gr-spherical-stars}'

# compile references
biber 2015-12-14-wysocki-gr-spherical-stars

# recompile with updated references
pdflatex -jobname 2015-12-14-wysocki-gr-spherical-stars \
         '\def\notes{}\input{2015-12-14-wysocki-gr-spherical-stars}'

mv 2015-12-14-wysocki-gr-spherical-stars.pdf \
   2015-12-14-wysocki-gr-spherical-stars--with-notes.pdf

pdflatex -jobname 2015-12-14-wysocki-gr-spherical-stars \
         '\input{2015-12-14-wysocki-gr-spherical-stars}'

mv 2015-12-14-wysocki-gr-spherical-stars.pdf \
   2015-12-14-wysocki-gr-spherical-stars--without-notes.pdf
