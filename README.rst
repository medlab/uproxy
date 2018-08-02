uproxy
============================================================================
A perfect python based proxy server with both IPV6/IPV4 support

Quick start
==========================================================================
1. pip install uproxy
2. python -m uproxy.UProxy
3. config your proxy client with server:8000

Why I love uproxy more even it's a little slow than others
===========================================================================
1. DNS configure is not always allowed, but proxy is most of time!
2. Https is auto supported because HTTP CONNECT is supported
3. Safe from DNS cache poisoning
4. Easy to deploy on gateway to just serve for lan client

Quick Config a server just server for lan
===========================================================================
1. pip install uproxy?
2. Create a start script in some place(like ~/bin/start_uproxy), like

.. code-block:: bash

  #!/bin/bash
  python -m uproxy -b [lan address like 192.168.1.1 or 127.0.0.1]

3. Auto run by cron after reboot (create job by crontab -e),

  @reboot /sbin/start-stop-daemon -S -x ~/bin/start_uproxy -b

4. Lan client config http proxy by [lan address like 192.168.1.1]:[port num like 8000]

Combine with ssh port forward
============================================================================
ssh -L 8000:127.0.0.1:8000 remoter_user@remotehost

Release Workflow
=========================
1. python setup.py sdist
2. python -m twine upload dist/*

ref:
https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
https://packaging.python.org/guides/migrating-to-pypi-org/

Welcome to contribute
===================================
Any pull request is welcome.

Love My Software: https://www.paypal.me/medlab :)
