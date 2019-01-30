#!/bin/sh

make clean
cat > outline.rst << END
Course Outline
==============
END
sphinx-build -b rst . _build/rst

