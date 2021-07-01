import pytest

def test_load_jarvis_modules():
    from jarvis import Jarvis

    module_src = "tests/"
    jarvis = Jarvis(module_src)

    assert len(jarvis.modules) == 1
    assert len(jarvis.command_dict) == 1

    assert list(jarvis.command_dict.keys())[0] == "test"

