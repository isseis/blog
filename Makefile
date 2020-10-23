.PHONY: biuld clean start fulltest js test tools tooltest

INSTALL_CMD=	/usr/bin/install
INSTALL_DATA=	$(INSTALL_CMD) -m644

build: js
	bundle exec jekyll build --drafts

start:
	bundle exec jekyll s --drafts --livereload

test: clean
	bundle exec jekyll build
	bundle exec htmlproofer ./_site \
		--disable-external --empty-alt-ignore --allow-hash-href

fulltest: build
	bundle exec htmlproofer ./_site \
		--empty-alt-ignore --allow-hash-href

full: 
	$(MAKE) clean
	$(MAKE) tools
	$(MAKE) build
	$(MAKE) toolstest test

js: assets/js/medium-zoom.min.js

assets/js/medium-zoom.min.js: node_modules/medium-zoom/dist/medium-zoom.min.js
	$(INSTALL_DATA) $< $@

# _tools
tools:

toolstest:
	$(MAKE) -C _tools/test test

clean:
	-rm -rf _site .jekyll-cache .jekyll-metadata
