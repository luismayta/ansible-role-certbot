Ansible Role Certbot
====================

|Build Status| |Ansible Galaxy| |GitHub issues| |GitHub license|

:Version: 0.0.0
:Web: https://github.com/hadenlabs/ansible-role-certbot
:Download: http://github.com/hadenlabs/ansible-role-certbot
:Source: http://github.com/hadenlabs/ansible-role-certbot
:Keywords: ansible-role-certbot

.. contents:: Table of Contents:
    :local:

Ansible Galaxy role for `Certbot`_.

Requirements:
-------------

List of applications:

- `Pyenv`_
- `Docker`_

Install
-------

Install it with the following command:

.. code-block:: bash

    $ ansible-galaxy install hadenlabs.certbot

Role Variables
--------------

The default role variables in ``defaults/main.yml`` are:

.. code-block:: yaml

    certbot_create_if_missing: false
    certbot_create_method: standalone
    certbot_admin_email: email@gmail.com
    certbot_create_standalone_stop_services:
    - nginx
    certbot_vhosts:
        - {servername: "abcyourdomain.com", documentroot: "/var/www/abcyourdomain.com"}
        - {servername: "abcyourdomain1.com", documentroot: "/var/www/abcyourdomain1.com"}

Dependencies
------------

None

License
-------

The code in this repository is licensed under the Apache unless
otherwise noted.

Please see LICENSE_ for details.

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
============

Please see `CONTRIBUTING`_ for details.


Versioning
----------

Releases are managed using bitbucket release feature. We use [Semantic Versioning](http://semver.org) for all
the releases. Every change made to the code base will be referred to in the release notes (except for
cleanups and refactorings).

Credits
-------

-  `author`_
-  `contributors`_

Made with :heart: :coffee: and :pizza: by `author`_ and `company`_.

.. Badges:

.. |Build Status| image:: https://travis-ci.org/hadenlabs/ansible-role-certbot.svg
   :target: https://travis-ci.org/hadenlabs/ansible-role-certbot
.. |Ansible Galaxy| image:: https://img.shields.io/badge/galaxy-hadenlabs.certbot-blue.svg
   :target: https://galaxy.ansible.com/hadenlabs/ansible-role-certbot/
.. |GitHub issues| image:: https://img.shields.io/github/issues/hadenlabs/ansible-role-certbot.svg
   :target: https://github.com/hadenlabs/ansible-role-certbot/issues
.. |GitHub license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
   :target: LICENSE

.. Links
.. _`changelog`: CHANGELOG.rst
.. _`contributors`: AUTHORS
.. _`contributing`: docs/source/CONTRIBUTING.rst
.. _`LICENSE`: LICENSE

.. _`company`: https://github.com/hadenlabs
.. _`author`: https://github.com/luismayta

.. dependences
.. _Certbot: https://certbot.eff.org/
.. _Pyenv: https://github.com/pyenv/pyenv
.. _Docker: https://www.docker.com/
