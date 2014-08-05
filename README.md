tvw.buildout
============

buildout for tvw relaunch

## Get started

In order to make the most out of this slightly enhanced buildout setup, you
should follow this rough guidelines.

Use a virtualenv that excludes setuptools/distribute and let buildout handle
the installation for you:

```bash
/path/to/virtualenv-2.7 --no-setuptools tvw
New python executable in tvw/bin/python2.7
Also creating executable in tvw/bin/python
cd tvw
git clone git@github.com:vwc/tvw.buildout.git buildout.tvw
cd buildout.tvw
../bin/python bootstrap.py -c development.cfg
```


