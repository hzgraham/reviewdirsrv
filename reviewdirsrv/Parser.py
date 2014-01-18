#!/usr/bin/env python
# Copyright (c) 2014 Henry Graham <hgraham@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse

class Parser()
    def __init__(self)
        self.parser = argparse.ArguementParser(description='analyse sosreport')
        self.parser.add_arguements('--path', help='path to extracted sosreport')
