
pre: format isort ruff

format:
	pipx run ruff format --line-length 120 .

isort:
	pipx run isort .

ruff:
	pipx run ruff  --line-length 120 .

build: pre
	pipx run build

publish: build
	pipx run twine upload dist/*
	