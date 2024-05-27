docs/requirements.txt: poetry.lock
	poetry export --only docs --format requirements.txt \
	--without-hashes --without-urls | \
	grep -w \
	-e sphinx= \
	-e sphinx-.*= \
	-e furo= \
	-e myst-parser= \
	> docs/requirements.txt
