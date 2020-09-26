TESTDIR        = tests
SCRIPTDIR      = scripts

default:
	echo "Welcome to M05 mini project"

.PHONY: loadData
loadData:
	# todo

.PHONY: unitests
unitests: cleantests
	nosetests -v "$(TESTDIR)/test.py"

.PHONY: cleantests
cleantests:
	rm -rf "$(TESTDIR)/output"