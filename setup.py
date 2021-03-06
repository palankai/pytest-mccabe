from setuptools import setup

setup(
    name='pytest-mccabe',
    description='pytest plugin to run the mccabe code complexity checker.',
    long_description=open("README.rst").read(),
    license="MIT license",
    version='1.0',
    author='Florian Bruhin',
    author_email='me@the-compiler.org',
    url='https://github.com/The-Compiler/pytest-mccabe',
    py_modules=['pytest_mccabe'],
    entry_points={'pytest11': ['mccabe = pytest_mccabe']},
    install_requires=['pytest>=3.6.0', 'mccabe'],
    zip_safe=True,
    classifiers=[
        'Environment :: Plugins',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    keywords='pytest plugin mccabe complexity',
)
