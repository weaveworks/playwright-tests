CURRENT_DIR := $(shell pwd)

# had to test
eneko-setup:
	brew install python
	pip3 install -U pytest
	pip3 install pytest-playwright
	playwright install

setup:
	bash -x  ./utils/scripts/mgmt-cluster-setup.sh kind  $(CURRENT_DIR) playwright-mgmt-kind

test:
	pytest test_weave_gitops_enterprise/explorer