# Exercise 49. Making Sentences

from nose.tools import *
from ex49 import parser

def test_peek():
    # Nothing to return
    empty_word_list = []
    assert_equal(None, parser.peek(empty_word_list))

    # Return word_list[0][0]
    word_list = [('noun','test'), ('direction', 'north')]
    assert_equal('noun', parser.peek(word_list))
    

def test_match():
    # Nothing to match
    empty_word_list = []
    assert_equal(None, parser.match(empty_word_list, None))

    # word_list[0][0] word type mismatch
    word_list = [('something','test'), ('direction', 'north')]
    assert_equal(None, parser.match(word_list, 'noun'))

    # Right word_list[0][0] word type match
    word_list = [('noun','test'), ('direction', 'north')]
    assert_equal(('noun', 'test'), parser.match(word_list, 'noun'))
    

def test_skip():
    # Pop all the word_list elements
    word_list = [('stop','the'), ('stop', 'of'), ('stop', 'all')]
    parser.skip(word_list, 'stop')
    assert_equal([], word_list)

    # Pop first element
    word_list = [('noun','Test'), ('stop', 'of'), ('direction', 'West')]
    parser.skip(word_list, 'noun')
    assert_equal([('stop', 'of'), ('direction', 'West')], word_list)

    # First element word type can't be popped
    word_list = [('noun','Test'), ('stop', 'of'), ('direction', 'West')]
    parser.skip(word_list, 'stop')
    assert_equal([('noun','Test'), ('stop', 'of'), ('direction', 'West')], word_list)

@raises(parser.ParserException)
def test_parse_verb():
    # First element is a verb
    word_list = [('verb','run'), ('direction', 'west')]
    assert_equal(('verb','run'), parser.parse_verb(word_list))

    # Stop words before the verb detected
    word_list = [('stop', 'to'), ('verb','run'), ('direction', 'west')]
    assert_equal(('verb','run'), parser.parse_verb(word_list))

    # ParserException: verb must come before the direction
    word_list = [('stop','to'), ('direction', 'west'), ('verb','run')]
    assert_equal(('verb','run'), parser.parse_verb(word_list))

@raises(parser.ParserException)
def test_object():
    # Noun as an object 
    word_list = [('noun','force'), ('direction','north')]
    assert_equal(('noun','force'), parser.parse_object(word_list))

    # Direction as an object 
    word_list = [('direction','north'), ('noun','force')]
    assert_equal(('direction','north'), parser.parse_object(word_list))

    # Filter stop words and noun as an object 
    word_list = [('stop','the'), ('noun','force'), ('direction','north')]
    assert_equal(('noun','force'), parser.parse_object(word_list))

    # Verb as an object (Error)
    word_list = [('verb','run')] 
    parser.parse_object(word_list)

@raises(parser.ParserException)
def test_subject():
    # No noun
    word_list = [('verb','run'), ('direction', 'north')]
    assert_equal(('noun','player'), parser.parse_subject(word_list))

    # With noun
    word_list = [('noun', 'Princess'),('verb','run'), ('direction', 'north')]
    assert_equal(('noun','Princess'), parser.parse_subject(word_list))

    # No noun neither verb
    parser.parse_subject(('direction', 'north'))

@raises(parser.ParserException)
def test_sentence():
    # Default subject player 
    sentence = parser.Sentence(('noun','player'), ('verb','run'), ('direction','north'))
    parsed_sentence = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal([sentence.subject, sentence.verb, sentence.object], 
                [parsed_sentence.subject, parsed_sentence.verb, parsed_sentence.object])

    # Filter stop word
    sentence = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), (('noun', 'honey')))
    parsed_sentence = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'),
                                            ('stop', 'the'), ('noun', 'honey')])
    assert_equal([sentence.subject, sentence.verb, sentence.object], 
                [parsed_sentence.subject, parsed_sentence.verb, parsed_sentence.object])

    # Wrong sentence
    parser.parse_sentence([('direction', 'south'), ('verb', 'run')])

    # Wrong sentence
    parser.parse_sentence([('noun', 'The'), ('direction', 'south'), ('verb', 'run')])
    