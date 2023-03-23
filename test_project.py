import pytest
import project
from termcolor import colored

def test_error_messege():
    assert project.error_messege(*["C", "S", "5", "0", "P"]) == "Please insert [C] [S] [5] [0] [P] "
    assert project.error_messege(*["1", "2", "\"", "*", "!"]) == "Please insert [1] [2] [\"] [*] [!] "


def test_Quit():
    with pytest.raises(SystemExit):
        project.Quit("q")

def test_divider():
    assert project.divider(10, "red") == colored("==========", "red")
