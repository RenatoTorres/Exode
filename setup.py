from distutils.core import setup
setup(
  name = 'Exode',
  packages = ['Exode'],
  package_data={'Exode': ['Object/*.py','Core/*.py','Core/Instructions/*.py','UI/*.py']},
  install_requires=['pyserial'],
  version = '1.0.6',
  description = 'Exode is a Pythons library for communication between Arduino microcontroller boards and a connected computer.',
  author = 'Renato Torres',
  author_email = 'renatoveigatorres@gmail.com',
  url = 'https://github.com/RenatoTorres/Exode',
  download_url = 'https://github.com/RenatoTorres/Exode/tarball/1.0.6',
  license='APACHE 2.0'
)

# python setup.py register
# python python setup.py sdist upload
# http://peterdowns.com/posts/first-time-with-pypi.html
