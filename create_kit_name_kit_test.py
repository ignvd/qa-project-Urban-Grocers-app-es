import pytest
from data import KIT_BODIES
from sender_stand_request import create_user, create_kit

def positive_assert(kit_body):
    token = create_user()
    response = create_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    token = create_user()
    response = create_kit(kit_body, token)
    assert response.status_code == 400

def test_valid_min_length():
    positive_assert(KIT_BODIES["valid_min_length"])

def test_valid_max_length():
    positive_assert(KIT_BODIES["valid_max_length"])

def test_too_short():
    negative_assert_code_400(KIT_BODIES["too_short"])

def test_too_long():
    negative_assert_code_400(KIT_BODIES["too_long"])

def test_special_chars():
    positive_assert(KIT_BODIES["special_chars"])

def test_spaces():
    positive_assert(KIT_BODIES["spaces"])

def test_numbers():
    positive_assert(KIT_BODIES["numbers"])

def test_missing_name():
    negative_assert_code_400(KIT_BODIES["missing_name"])
