#!/usr/bin/env python
#$changeset_latest_tag$
#$changeset_local_revision$

import glob
import json
import os
import setuptools

_VERSION_SUFFIX = {
    # development version
    "DEVELOPMENT": "dev",
    # pre-release versions
    "ALPHA": "a",
    "BETA": "b",
    # release candidate
    "RELEASE_CANDIDATE": "rc",
    # final release
    None: '.'}

_CWD = os.path.abspath(os.path.dirname(__file__))

def load_txt (fn):
    if (not os.path.exists(os.path.join(_CWD, fn))):
        return
    for line in open(fn, "rU"):
        line = line.strip()
        if (line == ''):
            continue
        if (line[0] == '#'):
            continue
        yield line

def load_ini (fn):
    strip = lambda t: t.strip().strip('"').strip()
    for line in load_txt(fn):
        key, value = line.split('=', 1)
        yield strip(key), strip(value)

_PROJECT = dict(load_ini("PROJECT"))
_CHANGESET = dict(load_ini("CHANGESET"))
_REQUIREMENTS = list(load_txt("REQUIREMENTS"))
_MANIFEST = ["PROJECT", "CHANGESET", "REQUIREMENTS"]

setuptools.setup(
    name = _PROJECT["project_name"],
    description = _PROJECT.get(
        "project_description", _PROJECT["project_name"]),
    author = _PROJECT["project_author"],
    version = "%s%s%s" % (
        _CHANGESET["changeset_latest_tag"],
        _VERSION_SUFFIX[_PROJECT.get("project_status")],
        _CHANGESET["changeset_local_revision"]),
    requires = _REQUIREMENTS,
    scripts = glob.glob("bin/*"),
)
