import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

# Import the module containing the functions to be tested.
# 테스트할 함수를 포함하는 모듈을 불러옵니다.
try:
    import my_code_here as mch
except ImportError as e:
    pytest.fail(
        f"Error importing 'my_code_here': {e}"
        f"'my_code_here'를 불러오는 중 오류가 발생했습니다. {e}"
    )

# Write your test functions here.
# 각 테스트 함수는 'test_'로 시작해야 합니다.

# Pytest will automatically discover and run these test functions.
# Pytest 가 그러한 함수를 자동으로 찾아 실행할 것입니다.

# Example test function:
# 시험 함수 예
def test_example():
    input_value = 'Please set input arguments.\n입력 매개변수를 정하기 바랍니다.'
    result = mch.some_function(input_value)
    expected_output = 'Please set expected results.\n예상 결과를 정하기 바랍니다.'
    assert result == expected_output, (
        f"Input arguments: {input_value}\n"
        f"입력 매개변수 : {input_value}\n"
        f"Expected: {expected_output}\n"
        f"예상 결과: {expected_output}\n"
        f"Got: {result}\n"
        f"실제 결과: {result}"
    )


# Test another function from the 'my_code_here' module.
# 다른 함수를 시험하는 예
def test_another_example():
    input_value1 = 'Please set input arguments.\n입력 매개변수를 정하기 바랍니다.'
    input_value2 = 'Please set input arguments.\n입력 매개변수를 정하기 바랍니다.'
    result = mch.another_function(input_value1, input_value2)
    expected_output = 'Please set expected results.\n예상 결과를 정하기 바랍니다.'
    assert result == expected_output, (
        f"Input arguments: {input_value1}, {input_value2}\n"
        f"입력 매개변수 : {input_value1}, {input_value2}\n"
        f"Expected: {expected_output}\n"
        f"예상 결과: {expected_output}\n"
        f"Got: {result}\n"
        f"실제 결과: {result}"
    )


if __name__ == "__main__":
    pytest.main([__file__])
