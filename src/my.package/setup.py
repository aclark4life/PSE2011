from setuptools import setup, find_packages

setup (
    name='my.package',
    packages=find_packages(),
    namespace_packages=['my'],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone 
    """
)
