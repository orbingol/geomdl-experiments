# geomdl-experiments
from setuptools import setup
import os
import re


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Implemented from http://stackoverflow.com/a/41110107
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)


data = dict(
    name='geomdl_exp',
    version=get_property('__version__', 'geomdl_exp'),
    description='Experiments with NURBS-Python (geomdl)',
    author='Onur Rauf Bingol',
    author_email='nurbs-python@googlegroups.com',
    license='MIT',
    url='https://github.com/orbingol/geomdl-experiments',
    packages=['geomdl_exp'],
    install_requires=['geomdl>=4.3.4'],
    long_description=read('README.rst'),
    keywords='NURBS B-Spline curve surface CAD modeling visualization',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    project_urls={
        'Documentation': 'http://nurbs-python.readthedocs.io/',
        'Source': 'https://github.com/orbingol/geomdl-experiments',
        'Tracker': 'https://github.com/orbingol/geomdl-experiments/issues',
    },
)

if __name__ == '__main__':
    setup(**data)