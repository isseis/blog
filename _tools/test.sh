#! /bin/sh

if [ ! -d ./_site ]; then
	echo "_site directory not found. Need to run jekyll build first." >&2
	exit 1;
fi

# Run HTMLProofer
exec builde exec htmlproofer ./_site \
	--disable-external --empty-alt-ignore --allow-hash-href
