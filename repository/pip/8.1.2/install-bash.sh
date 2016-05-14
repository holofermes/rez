#!/bin/bash

srcpath=$1
destpath=$2
destRelative=`python -c "import os.path; print os.path.relpath('${destpath}', '${srcpath}')"`
pypath=${destpath}/lib/site-packages

/usr/bin/mkdir -p ${pypath}


cd ${srcpath}
PYTHONPATH=$PYTHONPATH:${pypath} python setup.py install --prefix=${destRelative} --old-and-unmanageable

/usr/bin/mkdir -p ${destpath}/python
/usr/bin/cp -rf ${pypath}/* ${destpath}/python/
/usr/bin/rm -rf ${destpath}/lib
