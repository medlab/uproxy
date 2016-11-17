# u-proxy

The only perfect python based proxy server with both IPV6/IPV4 supported for you!

You can start a server and setup proxy on a browser even on your mobile device, then you may found some bad software is sending you private data out, if it's http based, you may even see all the detail on your running Python console!

When you debug your web related software or try to monitor your device network activity, you will found a simple and clear http proxy server is your Swiss Army Knife, the best friend of engineer and hacks! That's why I develop u-proxy which for detected bad software on my phone!

What you need to type is simple

**./u-proxy.py**

**don't forgot chmod +x u-proxy.py to make u-proxy.py runable**

or

**./u-proxy.py [port] [accept client ip address]**

The most powerful function is conjunction with ssh like

**ssh -L 8000:127.0.0.1:8000 someone@somehost**

and you run u-proxy on somehost with

**./u-proxy 8000 127.0.0.1**

**It's safe and powerfull!**

Any pull request is welcome.

Love My Software: https://www.paypal.me/medlab :)
