"""System entity module test code feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from Module.regex import regex
import pytest


@scenario('tc.feature', 'Test case')
def test_case():
    """Test case."""
    pass

@given(parsers.parse("input_sentence is {now_input}"), target_fixture = 'context')
def input_sentence(now_input):
    """context."""
    now = regex(now_input)

    return now
    # raise NotImplementedError

@when('starting module', target_fixture = 'context2')
def starting_module(context):
    """starting module."""
    
    context.find_loop()
    context.get_tagged_sentence()

    return context

    
@then(parsers.parse("entity_name is {result_entity_name}"))
def entity_name_is(context2, result_entity_name):
    """entity_name is."""

    result_entity_name = result_entity_name.split(', ')

    assert context2.get_entity_name() == result_entity_name


@then(parsers.parse("value is {result_value}"))
def value_is(context2, result_value):
    """value is."""
    
    result_value = result_value.split(', ')

    assert context2.get_value() == result_value


@then(parsers.parse("start_idx is {result_start_idx}"))
def start_idx_is(context2, result_start_idx):
    """start_idx is."""

    result_start_idx = result_start_idx.split(', ')
    result_start_idx = list(map(int, result_start_idx))

    assert context2.get_start_idx() == result_start_idx


@then(parsers.parse("end_idx is {result_end_idx}"))
def end_idx_is(context2, result_end_idx):
    """end_idx is."""

    result_end_idx = result_end_idx.split(', ')
    result_end_idx = list(map(int, result_end_idx))
    
    assert context2.get_end_idx() == result_end_idx


@then(parsers.parse("get_tagged_sentence is {result_tagged_sentence}"))
def get_tagged_sentence_is(context2, result_tagged_sentence):
    """get_tagged_sentence is."""

    assert context2.get_tagged_sentence() == result_tagged_sentence