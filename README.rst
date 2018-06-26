uproxy
=======

The only perfect python based proxy server with both IPV6/IPV4 supported
for you!

You can start a server and setup proxy on a browser even on your mobile
device, then you may found some bad software is sending you private data
out, if it’s http based, you may even see all the detail on your running
Python console!

When you debug your web related software or try to monitor your device
network activity, you will found a simple and clear http proxy server is
your Swiss Army Knife, the best friend of engineer and hacks! That’s why
I develop u-proxy which for detected bad software on my phone!

What you need to type is simple
*if you get code from github, you can run with full path*

**./UProxy.py**

**don’t forgot chmod +x UProxy.py to make UProxy.py runable**

or

**./UProxy.py [port] [accept client ip address]**

The most powerful function is conjunction with ssh like

**ssh -L 8000:127.0.0.1:8000 someone@somehost**

and you run UProxy on somehost with

**./UProxy 8000 127.0.0.1**

**It’s safe and powerfull!**

*if you install by pip3 install u-proxy *

*You need run by module like python3 -m uproxy.UProxy

Any pull request is welcome.

Love My Software: https://www.paypal.me/medlab :)

Release Workflow
=========================
1. python setup.py sdist
2. python -m twine upload dist/*

ref:
https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
https://packaging.python.org/guides/migrating-to-pypi-org/

Why I love uproxy more even it's a little slow than others
===========================================================================
1. DNS configure is not always allowed, but proxy is most of time!
2. Https is auto supported because HTTP CONNECT is supported
3. Safe from DNS cache poisoning
4. Easy to deploy on gateway to just serve for lan client

Fast Config a server to server just for lan
===========================================================================
1. pip install uproxy?
2. Create a start script in some place(like ~/bin/start_uproxy), like

.. code-block:: bash

  #!/bin/bash
  python -m uproxy -b [lan address like 192.168.1.1]

3. Auto run by cron after reboot (create job by crontab -e),

  @reboot /sbin/start-stop-daemon -S -x ~/bin/start_uproxy -b

3. Lan client config http proxy by [lan address like 192.168.1.1]:[port num like 8000]