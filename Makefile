.PHONY: biuld clean test

build:
	bundle exec jekyll build --drafts

start:
	bundle exec jekyll s --drafts --livereload

test: build
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

# _tools
tools:

toolstest:
	$(MAKE) -C _tools/test test

clean:
	-rm -rf _site
