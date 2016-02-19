INSTALL_DIR  ?= /usr/local/altschool/django-softdelete

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(patsubst %/,%,$(dir $(mkfile_path)))

define header
	@tput setaf 6
	@echo "* $1"
	@tput sgr0
endef

# Build/install the app
# Runs on every command
install: $(INSTALL_DIR)
	$(call header,"Installing")
	@. $(INSTALL_DIR)/bin/activate; python setup.py -q install

# Install/update dependencies
# Runs whenever the requirements.txt file changes
$(INSTALL_DIR): $(INSTALL_DIR)/bin/activate
$(INSTALL_DIR)/bin/activate: requirements.txt
	$(call header,"Updating dependencies")
	@test -d $(INSTALL_DIR) || virtualenv $(INSTALL_DIR)
	@. $(INSTALL_DIR)/bin/activate; pip install -q --upgrade pip
	@. $(INSTALL_DIR)/bin/activate; pip install -Ur requirements.txt
	@touch $(INSTALL_DIR)/bin/activate

test: install
	$(call header,"Running unit tests")
	@. $(INSTALL_DIR)/bin/activate; django-admin.py test softdelete --settings="softdelete.settings" --pythonpath=$(current_dir)

test_migrations: install
	$(call header,"Making migrations for test app")
	@. $(INSTALL_DIR)/bin/activate; django-admin.py makemigrations --settings="softdelete.settings" --pythonpath=$(current_dir)/tests test_softdelete_app
	@. $(INSTALL_DIR)/bin/activate; django-admin.py migrate --settings="softdelete.settings" --pythonpath=$(current_dir)/tests test_softdelete_app
	@. $(INSTALL_DIR)/bin/activate; django-admin.py test softdelete --settings="softdelete.settings" --pythonpath=$(current_dir)

clean:
	@rm -rf $(INSTALL_DIR)
	@rm -rf ./build ./dist ./*.egg-info
	@find . -type f -name '*.pyc' -exec rm -rf {} \;
