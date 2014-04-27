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

import sys, os, subprocess

"""
need to differentiate between IPA and a stand alone 389 Directory Server
"""

'''
if len(args) != 1:
    parser.error("Incorrect number of arguments")
else:

pathname = sys.arg[1]
print pathname
'''

class analyze:

    def __init__(self, args):
        
        self.args = args
        self.hostname = self.readhostname() 
        variables = analyze()
        self.dirsrvpath = /etc/dirsrv


    def _env_settings()
        

    def readhostname():
        try:
            hostname = os.path.join(self.pathname,'hostname')
            hstnm = open('hostname', 'r')
            name = hstnm.read()
            print "the hostname is = %s" % name

    def check_logs()
       subprocess.cal(["logconv.pl","-V","" % instance
       logs = subprocess.Popen(["logvonv.pl", "-V", "/etc/dirsrv/%s" % instance ], stdout=subprocess.PIPE)
       output,  = logs.communicate()
       return logs

    def get_instance()                   
        """need to determine the instance name either through input or code"""
        os.path
        for each in d = listdir(dirsvpath
        glob.glob   
        isdir(join(dirsrvpath,d))


