########################################################################
#
#       License: BSD
#       Created: August 15, 2012
#       Author:  Francesc Alted - francesc@blosc.io
#
########################################################################


import tempfile
import os
import os.path
import sys
import glob
import shutil
if sys.version < "2.7":
    import unittest2 as unittest
    from unittest2 import TestCase, skipUnless
else:
    import unittest
    from unittest import TestCase, skipUnless


# Global variables for the tests
verbose = False
heavy = False


# Useful superclass for disk-based tests
class MayBeDiskTest():

    disk = False

    def setUp(self):
        if self.disk:
            prefix = 'bcolz-' + self.__class__.__name__
            self.rootdir = tempfile.mkdtemp(prefix=prefix)
            os.rmdir(self.rootdir)  # tests needs this cleared
        else:
            self.rootdir = None

    def tearDown(self):
        if self.disk:
            # Remove every directory starting with rootdir
            for dir_ in glob.glob(self.rootdir+'*'):
                shutil.rmtree(dir_)

