default:
	cat makefile

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
