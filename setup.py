#!/usr/bin/env python3

from setuptools import setup


LONG_DESCRIPTION = '''
Imgs2AsciiAnimation

convert jpgs to ascii animation

将图片转换为字符动画

Bugs
====
Send a PR.

'''

setup(name='imgs2asciianimation',
      version='1.0',
      description='jpg图片转字符动画!',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='efvhi',
      author_email='efvhi.github.io',
      url='https://github.com/efvhi/imgs2asciianimation/',
      scripts=['imgs2asciianimation'],
     )