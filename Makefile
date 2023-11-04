.PHONY: clean devserver install pep8 pin_requirements \
		test hooks

# Project constants
PROJECT = game
POETRY = poetry
PYTEST = pytest
PYTHON = python
MANAGE_PY = $(PYTHON) manage.py
PIP = pip
PIP_INSTALL = $(PIP) install

# SemVer variables
VERSION = $(shell cat VERSION)
BUILD_NUM ?= 0

hooks:
	pre-commit install --hook-type pre-commit --hook-type pre-push

pep8:
	flake8 --statistics $(PROJECT)/

pin_requirements:
	$(POETRY) update -v --lock

clean:
	find . -name "*.pyc" -delete

install: clean
	$(PIP_INSTALL) poetry
	$(POETRY) install

test:
	$(POETRY) run pytest
