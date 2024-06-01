default:
	cat makefile

install:
	dnf -y install pytest

inst:
	python3 -m venv venv
	. ./venv/bin/activate && pip3 install pytest
	@echo '. ./venv/bin/activate'

test:
	python3 -m unittest discover tests/ "test_*.py"

act:
	act --container-architecture linux/amd64

update:
	make test
	git status
	sleep 3
	git add .
	git commit -am 'update'
	git push
