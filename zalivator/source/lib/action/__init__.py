# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

import os
import glob
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
