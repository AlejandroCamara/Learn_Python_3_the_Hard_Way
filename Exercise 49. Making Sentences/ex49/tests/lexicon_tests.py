# Exercise 49. Making Sentences

from nose.tools import *
from ex49 import lexicon

def test_directions():
    assert_equal(lexicon.scan("North"), [('direction', 'North')])
    result = lexicon.scan("north sOutH east")
    assert_equal(result, [('direction', 'north'),
                        ('direction', 'sOutH'),
                        ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("GO"), [('verb', 'GO')])
    result = lexicon.scan("go kiLl eat")
    assert_equal(result, [('verb', 'go'),
                        ('verb', 'kiLl'),
                        ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                        ('stop', 'in'),
                        ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear prinCeSs")
    assert_equal(result, [('noun', 'bear'),
                        ('noun', 'prinCeSs')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                        ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"),
                    [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                        ('error', 'IAS'),
                        ('noun', 'princess')])