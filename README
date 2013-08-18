About
=====

Extra testing goodies for ``nose.tools``. 

Adds an ``issues_warnings`` decorator, where tests must issue one of the
expected warnings to pass (similar to ``nose.tools.raises`` for exceptions).

If installed on Python < 2.7 backports the new ``unittest.TestCase.assert*``
methods, and converts them to ``nose`` style assertions (spelled in PEP 8
fashion, so ``assert_equal`` rather than ``assertEqual``):

    * ``assert_greater`` / ``assert_less`` / ``assert_greater_equal`` /
      ``assert_less_equal``
      
    * ``assert_regexp_matches`` / ``assert_not_regexp_matches``
    
    * ``assert_in`` / ``assert_not_in``
    
    * ``assert_is`` / ``assert_is_not``
    
    * ``assert_is_none`` / ``assert_is_not_none``
    
    * ``assert_dict_contains_subset``
    
    * and `more...`_. 

.. _`more...`: http://docs.python.org/2.7/whatsnew/2.7.html#updated-module-unittest


Installation
============

To install ``nose_extra_tools`` run::

    $ pip install nose_extra_tools


Usage examples
==============

::

    from nose_extra_tools import assert_in, issues_warnings
    
    @issues_warnings(UserWarning, DeprecationWarning)
    def test_issues_deprecation_warning():
        import warnings
        warnings.warn('This test passes')
    
    @issues_warnings(Warning)
    def test_forgot_to_issue_warning():
        pass
    
    def test_backported_assert_in():
        assert_in(10, range(5))


Contribute
==========

If you find any bugs, or wish to propose new features `please let me know`_. 

If you'd like to contribute, simply fork `the repository`_, commit your changes
and send a pull request. Make sure you add yourself to `AUTHORS`_.

.. _`please let me know`: https://bitbucket.org/petar/nose_extra_tools/issues/new
.. _`the repository`: http://bitbucket.org/petar/nose_extra_tools
.. _`AUTHORS`: https://bitbucket.org/petar/nose_extra_tools/src/default/AUTHORS
