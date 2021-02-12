# copied from
# https://github.com/infrawatch/tripleo-qdr-ansible-role/commit/4897cb6a09fd83c12b8d7a578c845471afe68dbc
import re


def filter_snake_case(camel_case_string):
    camel_case_string = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2',
                               camel_case_string)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case_string).lower()


class FilterModule(object):
    def filters(self):
        return {'snake_case': filter_snake_case}
