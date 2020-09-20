#! /bin/sh

bundle_cmd="bundle"
if [ -x /usr/bin/bundle2.7 ]; then
	bundle_cmd="/usr/bin/bundle2.7"
fi

# Start Jekyll server
exec ${bundle_cmd} exec jekyll s --drafts --livereload
