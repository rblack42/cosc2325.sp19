BLDDIR	:= _build/html/
RELDIR	:= ../../_build/courses/cosc2325/


.PHONY: all
all:
	mkdir -p _build/html/_images/circuits
	sphinx-build -b html -d _build/doctrees . _build/html


.PHONY: release
release:
	cp -r ${BLDDIR} ${RELDIR}

.PHONY: clean
clean:
	rm -rf _build
