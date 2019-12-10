# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner
from hamcrest import assert_that, equal_to


USERNAME: str = "root"

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host) -> None:
    filename = host.file("/etc/hosts")

    assert_that(filename.exists, equal_to(True))
    assert_that(filename.host, equal_to("root"))
    assert_that(filename.group, equal_to("root"))
