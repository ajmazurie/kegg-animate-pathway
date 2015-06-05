#!/usr/bin/env python

# 'version' follows https://www.python.org/dev/peps/pep-0440/

import setuptools
import json
import glob

_SETUP = json.load(open("setup.json", "rU"))
_VERSION = json.load(open("VERSION", "rU"))
_REQUIREMENTS = filter(
    lambda line: line.strip() != '',
    open("REQUIREMENTS", "rU").readlines())

setuptools.setup(
    name = _SETUP["project_name"],
    description = _SETUP.get("project_description", _SETUP["project_name"]),
    author = _SETUP["project_author"],

    version = "%s%s%s" % (
        _VERSION["changeset_latest_tag"],
        {
            # development version
            "DEVELOPMENT": "dev",
            # pre-release versions
            "ALPHA": "a",
            "BETA": "b",
            # release candidate
            "RELEASE_CANDIDATE": "rc",
            # final release
            None: '',
        }[_SETUP.get("project_status")],
        _VERSION["changeset_local_revision"]),

    requires = _REQUIREMENTS,
    scripts = glob.glob("bin/*"),
)
