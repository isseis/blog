.PHONY: biuld clean start fulltest test tools tooltest

build:
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

# _tools
tools:

toolstest:
	$(MAKE) -C _tools/test test

clean:
	-rm -rf _site .jekyll-cache .jekyll-metadata
