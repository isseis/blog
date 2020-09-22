#! /bin/sh

bundle_cmd="bundle"
if [ -x /usr/bin/bundle2.7 ]; then
	bundle_cmd="/usr/bin/bundle2.7"
fi

if [ ! -d ./_site ]; then
	echo "_site directory not found. Need to run jekyll build first." >&2
	exit 1;
fi

# Run HTMLProofer
exec ${bundle_cmd} exec htmlproofer ./_site \
	--disable-external --empty-alt-ignore --allow-hash-href
