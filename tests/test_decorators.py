from src.decorators import log
import pytest


@log()
def add(a, b):
    return a + b


@log(filename="test_log.txt")
def divide(a, b):
    return a / b


def test_add_ok(capsys):
    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_add_error(capsys):
    with pytest.raises(TypeError):
        add(2, "3")
    captured = capsys.readouterr()
    assert "add error:" in captured.out
    assert "Inputs: (2, '3'), {}" in captured.out


def test_divide_ok():
    result = divide(6, 3)
    assert result == 2.0
    with open("test_log.txt", "r") as f:
        logs = f.read()
    assert "divide ok" in logs


def test_divide_error():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
    with open("test_log.txt", "r") as f:
        logs = f.read()
    assert "divide error: division by zero" in logs
    assert "Inputs: (6, 0), {}" in logs


# Cleanup log file after tests
def teardown_module(module):
    import os
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
