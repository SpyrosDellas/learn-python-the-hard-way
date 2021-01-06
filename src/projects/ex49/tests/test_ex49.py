from nose.tools import *
import ex49.parser as ps

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_peek():
    assert_equal(ps.peek([]), None)
    assert_equal(ps.peek([('noun', 'princess')]), 'noun')

def test_match():
    assert_equal(ps.match([], 'noun'), None)
    assert_equal(ps.match([('noun', 'princess')], 'noun'), ('noun', 'princess'))
    assert_equal(ps.match([('noun', 'princess')], 'verb'), None)

def test_skip():
    assert_equal(ps.skip([], 'noun'), None)
    assert_equal(ps.skip([('noun', 'princess')], 'noun'), None)

def test_parse_verb():
    assert_raises(ps.ParserError, ps.parse_verb, [])
    result = ps.parse_verb([('stop', 'in'), ('verb', 'go')])
    assert_equal(result, ('verb', 'go'))

def test_parse_object():
    assert_raises(ps.ParserError, ps.parse_object, [])
    result = ps.parse_object([('stop', 'in'), ('noun', 'princess')])
    assert_equal(result, ('noun', 'princess'))
    result = ps.parse_object([('stop', 'in'), ('direction', 'north')])
    assert_equal(result, ('direction', 'north'))

def test_parse_subject():
    assert_raises(ps.ParserError, ps.parse_subject, [], ('noun', 'door'))
    result = ps.parse_subject([('stop', 'in'), ('verb', 'go'),
                               ('stop', 'in'), ('direction', 'east')],
                               ('noun', 'door'))
    assert_equal(result.subject, 'door')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'east')

def test_parse_sentence():
    assert_raises(ps.ParserError, ps.parse_sentence, [])
    result = ps.parse_sentence([('stop', 'in'), ('verb', 'go'),
                               ('stop', 'in'), ('direction', 'east')])
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'east')
