.PHONY: all clean clobber

all: pdf/gr-notes.pdf

# this target needs to be fixed to work in all
# it only works when explicitly called for some reason,
# i.e. I cannot put the % in all, I have to list each one
pdf/gr-ch%-notes.pdf: tex/gr-ch%-notes.tex py/gr-ch%-exercises.py pdf
	python3 $(word 2,$^) img/ eps
	pdflatex -output-directory pdf $< && \
	pdflatex -output-directory pdf $<

pdf/gr-notes.pdf: gr-notes.tex pdf
	pdflatex -output-directory pdf $< && \
	pdflatex -output-directory pdf $<

pdf:
	mkdir pdf

clean:
	rm -rf pdf/*.aux pdf/*.log pdf/*.toc

clobber: clean
	rm -rf pdf
