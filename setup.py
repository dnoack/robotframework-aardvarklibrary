#!/usr/bin/env python

from setuptools import setup, Command
import sys
import os
import subprocess
sys.path.insert(0, 'src')

version_py = os.path.join(os.path.dirname(__file__), 'src', 'AardvarkLibrary',
        'version.py')
try:
    version = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--dirty'],
            stderr=subprocess.STDOUT).rstrip()
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (IOError, subprocess.CalledProcessError) as e:
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f, d)
            version = d['__version__']
    except IOError:
        version = 'unknown'

with open('README.rst') as f:
    readme = f.read()

class run_build_libdoc(Command):
    description = "Build Robot Framework library documentation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import robot.libdoc
        except ImportError:
            print "build_libdoc requires the Robot Framework package."
            sys.exit(-1)
        robot.libdoc.libdoc('AardvarkLibrary', 'docs/AardvarkLibrary.html')

def main():
    setup(name = 'robotframework-aardvarklibrary',
            version = version,
            description = 'Aardvark Library for Robot Framework',
            long_description = readme,
            author_email = 'michael.walle@kontron.com',
            package_dir = { '' : 'src' },
            license = 'Apache License 2.0',
            classifiers = [
                'Development Status :: 4 - Beta',
                'License :: OSI Approved :: Apache Software License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Testing',
            ],
            packages = [ 'AardvarkLibrary' ],
            install_requires = [
                'robotframework',
                'pyaardvark >= 0.2',
            ],
            cmdclass = {
                'build_libdoc': run_build_libdoc,
            },
    )

if __name__ == '__main__':
    main()
