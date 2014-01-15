#!/usr/bin/env python
# Copyright (c) 2014 Henry Graham <hgraham@redhat.com>
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, subprocess

"""
need to differentiate between IPA and a stand alone 389 Directory Server
"""


if len(args) != 1:
    parser.error("Incorrect number of arguments")
else:

pathname = sys.arg[1]
print pathname

def usage():
    print """Usage: sumarize [--init, -i|--check, -ch|--clean, -cl]
    --init, -i          

    Examples:

       Initialize:

"""
class analyze:

    def __init__(self, xsos):
        self.xsos = xsos
        variables = analyze()
        self.dirsrvpath = /etc/dirsrv


    def readhostname()
        hostname = os.path.join(self.path,'hostname')
        hstnm = open('hostname', 'r')
        name = hstnm.read()
        print "the hostname is = %s" % name

    def check_logs()
       subprocess.cal(["logconv.pl","-V","" % instance


    def get_instance()                   
        """need to determine the instance name either through input or code"""
        os.path
        for each in d = listdir(dirsvpath
        glob.glob   
        isdir(join(dirsrvpath,d))



import subprocess
p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "Today is", output

import subprocess
p = subprocess.Popen(["ls", "-l", "/etc/resolv.conf"], stdout=subprocess.PIPE)
output, err = p.communicate()
print "*** Running ls -l command ***\n", output
