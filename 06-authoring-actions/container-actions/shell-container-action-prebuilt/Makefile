VERSION?=v0.0.1
REPO?=sidpalas/shell-container-action
TAG:=${REPO}:${VERSION}

build:
	docker build -t ${TAG} ../shell-container-action/

push: 
	docker push ${TAG}

build-push: build push