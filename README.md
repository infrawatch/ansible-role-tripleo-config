# tripleo-collectd-ansible-role

This ansible role is designed to be used with TripleO to deploy the collectd
service using ansible (as opposed to puppet).
This role is called from TripleO at various deploy stages, and will run
main.yml to set up the expected vars, before running a task corresponding to
the current deploy_stage. The current deploy stage is specified using the
deploy_stage variable and is passed by TripleO.

## Adding molecule tests

Molecule tests use a combo of common/verify.yml and a scenario-specific verify.yml.

The playbooks are structured so that each scenario will include
common/verify.yml, and this will import a scenario-specific verify.yml once the
common tests have been run. A typical molecule verify action will run:
* basic checks on the created configs (defined in common/verify.yml)
* stf functional tests against the collectd-test container (common/verify.yml)
* scenario-specific checks defined in scenario_name/verify.yml

To enable the common verify actions in your scenario verify playbook, import
the common playbook:

    ---
    - import_playbook: ../common/verify.yml
