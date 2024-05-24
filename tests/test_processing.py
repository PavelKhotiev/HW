import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize(
    "state, expected_output",
    [
        ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
        ("PENDING", [{"id": 2, "state": "PENDING"}]),
        ("FAILED", [{"id": 4, "state": "FAILED"}]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(sample_data, state, expected_output):
    assert filter_by_state(sample_data, state) == expected_output


def test_filter_by_state_default(sample_data):
    expected_output = [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]
    assert filter_by_state(sample_data) == expected_output


def test_filter_by_state_empty_data():
    data = []
    assert filter_by_state(data) == []


def test_filter_by_state_no_matching_states():
    data = [
        {"id": 1, "state": "PENDING"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "FAILED"},
        {"id": 4, "state": "FAILED"},
    ]
    assert filter_by_state(data) == []


def test_filter_by_state_no_matching_custom_state():
    data = [
        {"id": 1, "state": "PENDING"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "FAILED"},
        {"id": 4, "state": "FAILED"},
    ]
    assert filter_by_state(data, state="EXECUTING") == []
