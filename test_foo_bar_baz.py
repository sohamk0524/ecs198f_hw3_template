import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here
def test_div_by_3():
	from foo_bar_baz import foo_bar_baz

	assert("1 2 Foo" == foo_bar_baz(3))

def test_div_by_5():
	from foo_bar_baz import foo_bar_baz

	assert("1 2 Foo 4 Bar" == foo_bar_baz(5))

def test_div_by_both():
	from foo_bar_baz import foo_bar_baz

	assert("1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz" == foo_bar_baz(15))

def test_negative_input():
	from foo_bar_baz import foo_bar_baz

	assert("" == foo_bar_baz(-1))
