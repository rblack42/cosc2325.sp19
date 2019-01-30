BLDDIR	:= docs/
RELDIR	:= ../../_build/courses/cosc2325/


.PHONY: all
all:
	mkdir -p _build/html/_images/circuits
	python ../../scripts/gen_schedule.py cosc2325 16
	sphinx-build -b html -d _build/doctrees . docs
	cp -r ${BLDDIR} ${RELDIR}


.PHONY: release
release:
	cp -r ${BLDDIR} ${RELDIR}

.PHONY: clean
clean:
	rm -rf _build
