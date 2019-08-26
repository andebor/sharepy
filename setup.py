from setuptools import setup


setup(name='sharepy',
      version='1.3.0',
      description='Simple SharePoint Online authentication for Python',
      url='https://github.com/JonathonHolvey/sharepy',
      author='Jonathon Holvey',
      author_email='jonathan.holvey@outlook.com',
      license='GPLv3',
      packages=['sharepy'],
      zip_safe=False,
      include_package_data=True,
      package_data={"sharepy": ["saml-templates/*.xml"]})
