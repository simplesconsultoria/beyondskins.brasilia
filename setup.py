from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='beyondskins.brasilia',
      version=version,
      description="Beyondskins Brasilia Theme for Plone/Diazo powered sites",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone diazo theme beyondskins brasilia cms',
      author='Thiago Tamosauskas',
      author_email='thiago@simplesconsultoria.com.br',
      url='https://github.com/simplesconsultoria/beyondskins.brasilia',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['beyondskins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
