default:
	cat makefile

install:
	dnf -y install pytest

test:
	pytest-3