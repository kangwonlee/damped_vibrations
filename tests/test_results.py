import pathlib
import sys


import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))


# Import the functions under testing from the assignment module
# 과제 모듈에서 테스트할 함수들을 불러옵니다
import my_code_here as mch


# please implement your test code here
# 시험 함수를 여기에 구현 바랍니다


if "__main__" == __name__:
    pytest.main([__file__])
