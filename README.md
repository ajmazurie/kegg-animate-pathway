kegg-animate-pathway
====================

**kegg-animate-pathway** is a [Python](http:www.python.org)-based command-line utility which interfaces with the [KEGG](http://www.genome.jp/kegg/>) API to produce animated figures of metabolic pathways to reveal activities of its genes and/or compounds.

Here is an example:
![example of animated pathway](https://raw.githubusercontent.com/ajmazurie/kegg-animate-pathway/master/doc/pathway.gif)

The color, size, and bluring of the overlays can be modified at will. For example, here is the same pathway but with the overlays blurred and scaled up:

![example of animated pathway](https://raw.githubusercontent.com/ajmazurie/kegg-animate-pathway/master/doc/pathway+blur+scaling.gif)

Installation
------------

```
$ pip install https://github.com/ajmazurie/kegg-animate-pathway/zipball/master
```

Notes
-----

The use of green for down-regulated and green for up-regulated genes and proteins is a *de facto* standard in the literature. Those colors, however, are difficult to distinguish for most color-blind people.

As discussed at http://jfly.iam.u-tokyo.ac.jp/color/ the following replacements are better options:

- instead of green (0 255 0) and red (255 0 0) you should prefer bluish green (0 158 115) and orange (230 159 0)
- even better, you should prefer sky blue (86 180 233) and yellow (240 228 66); those have a higher contrast than the previous choice
