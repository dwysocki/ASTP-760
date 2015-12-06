---
title: Notes
---

{% assign chapters = "1,2,3,5,6,7,8" | split: "," %}
{% assign types = "PDF,TeX" | split: "," %}

# Chapters from Textbook

The textbook used in this course is "A First Course in General Relativity" by Bernard Schutz. The following sections contain my personal notes on each chapter of the book, along with my solutions to many of the problems. I make no guarantees to the correctness of the solutions.

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
