---
title: Notes
---

{% assign chapters = "1,2" | split: "," %}
{% assign types = "PDF,TeX" | split: "," %}

# Chapters from Textbook

The textbook used in this course is "Dynamics and Evolution of Galactic Nuclei" by David Merritt. The following sections contain my personal notes on each chapter of the book.

## Complete Notes

[PDF](notes/textbook/pdf/gr-notes.pdf)

[TeX](notes/textbook/gr-notes.tex)


{% for chapter in {{chapters}} %}
## Chapter {{chapter}}

{% for type in {{types}} %}
{% assign typeid = {{type | downcase}} %}
[{{type}}](notes/textbook/{{typeid}}/gr-ch{{chapter}}-notes.{{typeid}})

{% endfor %}
{% endfor %}
