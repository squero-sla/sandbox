import pytest
import my_lib

# Start all methods with `test_` to announce them to test collector


def test_demo():
    demo = my_lib.Demo()
    assert demo.hello_world() == "Hello World"
    assert demo.class_parameter == "top-level class parameter"
    assert demo.hello_lib() == "Hello Demo"


# def test_real_world_usage():
#     demo = my_lib.Demo()
#     params = {a}
#     reult = demo.do_something(params)
#     print(result)
