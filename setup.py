from distutils.core import setup
setup(
  name = 'uproxy',
  packages = ['uproxy'],
  version = '0.3.99.9',
  description = 'An ipv4/ipv6 suppported http proxy server',
  long_description = open('readme.rst').read(), # need to close?
  author = 'Cong Zhang',
  author_email = 'congzhangzh@gmail.com',
  url = 'https://github.com/medlab/u-proxy',
  keywords = ['http','https', 'ipv4/ipv6', 'proxy'],
  classifiers=[
    'License :: OSI Approved :: BSD License',
    'Development Status :: 6 - Mature',
    'Environment :: Console',
    'Topic :: Utilities',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)