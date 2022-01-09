class TestExample:

    def test_check_math(self):
        a = 5
        b = 5
        expected_sum = 10
        assert a + b == expected_sum, f"Sum of variables a and b is not equal {expected_sum}"

    def test_check_letters(self):
        a = "a"
        b = "b"
        expected_sum = "ab"
        assert a + b == expected_sum, f"String is not equal {expected_sum}"

# python -m pytest test_example.py -k "test_check_math"

#  -m  command line option, module, which searches sys.path for the module and then runs it.

#  -k  Run tests by keyword expressions (Ключевое слово).
#  This will run tests which contain names that match the given string expression (case-insensitive),
#  which can include Python operators that use filenames, class names and function names as variables.

