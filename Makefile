.PHONY: unittest
unittest:
	uv run python -m unittest python

.PHONY: texttest
texttest:
	uv run python python/texttest_fixture.py 100

.PHONY: approvaltests
approvaltests:
	uv run python python/tests/test_gilded_rose_approvals.py

tests:
	uv run pytest python/tests

ruff:
	uv run ruff format .