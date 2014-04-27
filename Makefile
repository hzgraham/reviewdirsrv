#!/usr/bin/make

install: setup.py
	python setup.py install

rpm: rpmcommon
	@rpmbuild --define "_topdir %(pwd)/rpm-build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_specdir $(RPMSPECDIR)" \
        --define "_sourcedir %{_topdir}" \
        -ba $(RPMSPEC)
