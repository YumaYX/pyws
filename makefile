default:
	cat makefile

install:
	dnf -y install pytest

test:
	python3 -m unittest discover tests/ "test_*.py"

update:
	make test
	git status
	sleep 3
	git add .
	git commit -am 'update'
	git push
