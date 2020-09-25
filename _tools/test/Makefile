.PHONY: test check_geotag_test

test: check_geotag_test

check_geotag_test:
	# type check
	mypy ../check_geotag.py
	# unit test
	PYTHONPATH=.. \
	./check_geotag_test.py -v
	# command test
	../check_geotag.py nogeotagged.jpg
	! ../check_geotag.py geotagged.jpg > /dev/null
