VERSION=$(shell cat pyproject.toml| grep version | cut -d '"' -f 2)

pre: format isort ruff

clean:
	rm -rf dist

format:
	pipx run ruff format --line-length 120 .

isort:
	pipx run isort .

ruff:
	pipx run ruff  --line-length 120 .

build: pre
	pipx run build

publish: clean build
	pipx run twine upload dist/*
	
publish-docker:
	docker buildx build --platform linux/amd64,linux/arm64 -t asafamr123/quick-eks-cross-az:$(VERSION) -t asafamr123/quick-eks-cross-az:latest --push . 