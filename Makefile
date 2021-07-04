all: env
	pip3 install -r requirements.txt

env:
	python3 -m venv env

