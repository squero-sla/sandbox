
venv:
	python3 -m venv .venv
	@echo "Virtual environment created. Now run 'source venv/bin/activate' to activate it."

install:
	pip install -r requirements.txt
install-dev: install
	pip install -r requirements-dev.txt

test:
	pytest -v
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc
