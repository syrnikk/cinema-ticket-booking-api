from functional_tests.logging_in_and_data_check import LoggingInAndDataCheck
from functional_tests.edit_data import DataEditing
from functional_tests.register import Register

if __name__ == "__main__":
    sel1 = LoggingInAndDataCheck()
    sel1.setup_method()
    sel1.test()
    sel1.teardown_method()

    sel2 = DataEditing()
    sel2.setup_method()
    sel2.test()
    sel2.teardown_method()

    sel3 = Register()
    sel3.setup_method()
    sel3.test()
    sel3.teardown_method()