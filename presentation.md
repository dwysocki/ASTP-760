---
title: Presentation
---

# Summary

This is my final presentation for the course, on spherical solutions for stars in GR.


# Downloads

My slides can be downloaded in PDF format

- [with notes]({{site.baseurl}}/presentation/2015-12-14-wysocki-gr-spherical-stars--with-notes.pdf)
    - best viewed on a PDF viewer with split-screen presentation support,
      such as [pdfpc](https://davvil.github.io/pdfpc/)
- [without notes]({{site.baseurl}}/presentation/2015-12-14-wysocki-gr-spherical-stars--without-notes.pdf)

or as <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> source code

- [zip](
    {{site.baseurl}}/presentation/2015-12-14-wysocki-gr-spherical-stars.zip)
- [tar.gz](
    {{site.baseurl}}/presentation/2015-12-14-wysocki-gr-spherical-stars.tar.gz)


To compile the <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span>, run [`build.sh`]({{site.baseurl}}/presentation/build.sh) inside the unpacked archive. Alternatively, if you don't want the notes, just run

{% highlight bash %}
$ pdflatex 2015-12-14-wysocki-gr-spherical-stars.tex
$ biber 2015-12-14-wysocki-gr-spherical-stars
$ pdflatex 2015-12-14-wysocki-gr-spherical-stars.tex
{% endhighlight %}
