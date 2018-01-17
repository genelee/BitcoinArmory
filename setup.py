#! /usr/bin/python
from distutils.core import setup


opts = {}

setup( options = opts, windows = [
                        {
                            "script": "../../ArmoryQt.py",
                            "icon_resources": [(1, "../../img/armory256x256.ico"),
                                               (1, "../../img/armory64x64.ico"),
                                               (1, "../../img/armory48x48.ico")]
                        }
                ]
    )


