import pytest
import my_lib

# Start all methods with `test_` to announce them to test collector

def test_demo():
    demo = my_lib.Demo()
    assert demo.hello_world() == 'Hello World'
    assert demo.class_parameter == 'top-level class parameter'

