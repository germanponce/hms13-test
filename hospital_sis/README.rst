=========================================
Sistema de Información Hospitalario SIS-1
=========================================

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |tech-docs| |odoo13-docs| |help|
    * - tests
      - | |python37| |odoo13| |travis| |coverall|
    * - license
      - |github-license|
    * - contribute
      - |github-issues| |github-forks| |github-contributors|
    * - share
      - |share-twitter| |github-stars|

.. |tech-docs| image:: http://img.shields.io/badge/tutorial-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.youtube.com/watch?v=ibwZs-dL5H8
    :alt: Documentation Source

.. |odoo13-docs| image:: http://img.shields.io/badge/13.0-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/documentation/13.0/index.html
    :alt: Odoo 13 Documentation

.. |help| image:: http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/forum/help-1
    :alt: Odoo Help

.. |share-twitter| image:: https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmacagua%2Fhospital_sis
    :target: https://twitter.com/intent/tweet?text=Download%20and%20use%20%27hospital_sis%27%20package%20for%20doing%20Python%20trainings%20in%20Venezuela%20%F0%9F%87%BB%F0%9F%87%AA%20https://github.com/macagua/hospital_sis
    :alt: Share at Twitter

.. |github-contributors| image:: https://img.shields.io/github/contributors/macagua/hospital_sis.svg
    :target: https://github.com/macagua/hospital_sis/graphs/contributors
    :alt: Github Contributors

.. |github-license| image:: https://img.shields.io/github/license/macagua/hospital_sis.svg
    :target: https://github.com/macagua/hospital_sis/blob/master/LICENSE
    :alt: Github License

.. |github-issues| image:: https://img.shields.io/github/issues/macagua/hospital_sis
    :target: https://github.com/macagua/hospital_sis/issues
    :alt: Github Issues

.. |github-forks| image:: https://img.shields.io/github/forks/macagua/hospital_sis
    :target: https://github.com/macagua/hospital_sis/network/members
    :alt: Github Forks

.. |github-stars| image:: https://img.shields.io/github/stars/macagua/hospital_sis
    :target: https://github.com/macagua/hospital_sis/stargazers
    :alt: Github Favorites

.. |python37| image:: https://img.shields.io/badge/Python-3.7-blue
    :target: https://www.python.org/downloads/release/python-375/
    :alt: Python 3.7.5 version

.. |odoo13| image:: https://img.shields.io/badge/Odoo-13-blue
    :target: https://github.com/odoo/odoo/tree/13.0
    :alt: Odoo 13 version

.. |travis| image:: https://travis-ci.org/macagua/hospital_sis.svg?branch=master
    :target: https://travis-ci.org/macagua/hospital_sis
    :alt: Travis-CI Build Status

.. |coverall| image:: https://coveralls.io/repos/github/macagua/hospital_sis/badge.svg?branch=master
    :target: https://coveralls.io/github/macagua/hospital_sis?branch=master
    :alt: Coveralls Checkout Status

.. end-badges

About
=====

Sistema de Información Hospitalario SIS-1, is an Odoo 13 module to ease the
management of hospitals, you can manage registration of patients and her
medical appointments, etc.

This Odoo module let you manage:

- manage hospitals.

- manage specialties.

- manage medical appointments.

- manage patients using 'res_company' model overriding with new fields added.


Features
========

This Odoo 13 module include the follow technical features included:

- Data demonstration support.

- Internationalisation (i18n) support.

- Tests units support.

- ACL and security rules customs support.


Dependencies
============

This module requires the following dependencies:

- odoo 13 > https://github.com/odoo/odoo


Install
=======

Download the source code:

::

    $ git clone https://github.com/macagua/hospital_sis.git


Move ``hospital_sis`` folder into ``extra-addons`` Odoo directory:

::

    $ mv hospital_sis /full/path/to/extra-addons/


Restart the Odoo instance server, login and got to **Apps** > **Sistema de Información Hospitalario SIS-1** > **Install**

.. figure:: https://raw.githubusercontent.com/macagua/hospital_sis/master/static/description/install_module.png
    :align: center
    :width: 70%
    :alt: Install 'Sistema de Información Hospitalario SIS-1' Module

    Install 'Sistema de Información Hospitalario SIS-1' Module

Then go to Main menu at left top corner and click to **Hospital**.

.. figure:: https://raw.githubusercontent.com/macagua/hospital_sis/master/static/description/manage_app.png
    :align: center
    :width: 70%
    :alt: Access to 'Hospital' Menu

    Access to 'Hospital' Menu


Testing
=======

For run the module tests, with the following command:

::

    $ /full/path/to/odoo-bin --addons-path=/full/path/to/addons,/full/path/to/extra-addons \
      -d t -i hospital_sis --test-enable --stop-after-init --log-level=test


Contribute
==========

- Issue Tracker: https://github.com/macagua/hospital_sis/issues

- Source Code: https://github.com/macagua/hospital_sis


License
=======

- The project is licensed under the AGPL-3.


References
==========

The followings are the links using as references for development this Odoo 13 module:

Development
-----------

- `Curso de programación en Odoo: Clase 05 Crear un Sistema Hospitalario - Chile - Youtube <https://www.youtube.com/watch?v=ibwZs-dL5H8>`_.


Quality assurance
-----------------

- `Automated testing in Odoo <https://www.surekhatech.com/blog/automated-testing-in-odoo>`_.

- `Odoo Experience 2018 - Improve the Quality of Your Modules with Automated Tests <https://www.youtube.com/watch?v=jZddEWFdUcM>`_.


Translations
------------

- `Language Translation in Odoo 12 <https://www.cybrosys.com/blog/language-translation-odoo-12>`_.

- `How to load translations in Odoo <https://www.youtube.com/watch?v=ce5zMG7EGtE>`_.
