.PHONY: test check_geotag_test

test: check_geotag_test

check_geotag_test:
	# type check
	mypy _tools/check_geotag.py
	# unit test
	_tools/test/check_geotag_test.py -v
	# command test
	_tools/check_geotag.py _tools/test/nogeotagged.jpg
	! _tools/check_geotag.py _tools/test/geotagged.jpg > /dev/null
