#!/bin/bash
###############################################################################
## Run this script from the directory containing the LaTeX source to create  ##
## archives of all source materials in zip and tar.gz formats                ##
###############################################################################

filelist="2015-12-14-wysocki-gr-spherical-stars.tex \
          bibliography.bib \
          aas_macros.sty \
          build.sh \
          img/*"



zip 2015-12-14-wysocki-gr-spherical-stars.zip $filelist
tar -zvcf 2015-12-14-wysocki-gr-spherical-stars.tar.gz $filelist
