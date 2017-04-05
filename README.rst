.. image:: https://travis-ci.org/emulbreh/pyffx.svg?branch=master
    :target: https://travis-ci.org/emulbreh/pyffx


pyffx
=====

pyffx is a pure Python implementation of *Format-preserving, Feistel-based encryption* (FFX).

* `The FFX Mode of Operation for Format-Preserving Encryption`_
* `Addendum to “The FFX Mode of Operation for Format-Preserving Encryption”`_

Only method 2 is implemented.

See also `libffx`_

Usage
-----

.. code-block:: python

    >>> import pyffx
    >>> e = pyffx.Integer(b'secret-key', length=4)
    >>> e.encrypt(1234)
    6103
    >>> e.decrypt(6103)
    1234
    >>> e = pyffx.String(b'secret-key', alphabet='abc', length=6)
    >>> e.encrypt('aaabbb')
    'acbacc'
    >>> e.decrypt('acbacc')
    'aaabbb'

.. _The FFX Mode of Operation for Format-Preserving Encryption: http://csrc.nist.gov/groups/ST/toolkit/BCM/documents/proposedmodes/ffx/ffx-spec.pdf
.. _Addendum to “The FFX Mode of Operation for Format-Preserving Encryption”: http://csrc.nist.gov/groups/ST/toolkit/BCM/documents/proposedmodes/ffx/ffx-spec2.pdf
.. _libffx: https://github.com/kpdyer/libffx
