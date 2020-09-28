TESTDIR        = tests
SCRIPTDIR      = scripts

default:
	echo "Welcome to M05 mini project"

.PHONY: loadData
loadData:
	# todo

.PHONY: unitTests
unitTests: cleanTests
	nosetests --nocapture -v "$(TESTDIR)/test.py"

.PHONY: cleanTests
cleanTests:
	rm -rf "$(TESTDIR)/output"

.PHONY: doc
doc:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html