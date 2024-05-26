import pathlib
import random
import sys
from typing import Tuple

import numpy as np
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

# Fixture to provide test cases
@pytest.fixture(params=[
    (2.0, 2.0),
    (-1.5, -3.0),
    (0.0, 0.0),
])
def linear_damping_params(request) -> Tuple[float, float, float]:
    force, velocity = request.param
    damping_coefficient = force / velocity if velocity != 0 else 1.0  # Handle division by zero
    return damping_coefficient, velocity, force


# Test function to check linear damping force calculation
def test_linear_damping_force(linear_damping_params):
    c, v, expected_force = linear_damping_params
    calculated_force = mch.linear_damping_force(c, v)

    msg_arg = (
        f"input arguments: c = {c:g}, v = {v:g}\n"
        f"입력 매개변수: c = {c:g}, v = {v:g}\n"
    )

    assert isinstance(calculated_force, float),(
        f"{msg_arg}Expected type: float\n"
        f"예상 자료형: float\n"
        f"Got type: {type(calculated_force)}\n"
        f"받은 자료형: {type(calculated_force)}\n"
    )

    # Use np.isclose for floating-point comparisons
    assert np.isclose(calculated_force, expected_force, rtol=1e-6), (
        f"{msg_arg}Expected: {expected_force:g}\n"
        f"예상값: {expected_force:g}\n"
        f"Got: {calculated_force:g}\n"
        f"받은 값: {calculated_force:g}\n"
    )


# Fixture to provide test cases
@pytest.fixture(params=[
    (1.0, 2.0),   # c = 1.0, v = 2.0
    (0.5, -3.0),  # c = 0.5, v = -3.0
    (2.5, 0.0),   # c = 2.5, v = 0.0
    (1.2, -0.8),
])
def nonlinear_damping_test_case(request):
    return request.param

# Test function to check nonlinear damping force calculation
def test_nonlinear_damping_force(nonlinear_damping_test_case):
    c, v = nonlinear_damping_test_case

    calculated_force = mch.nonlinear_damping_force(c, v)

    msg_arg = (
        f"input arguments: c = {c:g}, v = {v:g}\n"
        f"입력 매개변수: c = {c:g}, v = {v:g}\n"
    )

    # Check if sign of the calculated force matches the sign of velocity
    assert np.sign(calculated_force) == np.sign(v) or (v == 0 and calculated_force == 0), (
        f"{msg_arg}Force should have same sign as velocity (or be zero if v = 0)\n"
        f"힘은 속도와 같은 부호를 가져야 합니다 (v=0이면 0)"
    )

    # Check if magnitude of the force is constant (equal to c)
    assert (
            np.isclose(abs(calculated_force), c, rtol=1e-6) 
            or (v == 0 and calculated_force == 0)), (
        f"{msg_arg}Magnitude of force should be equal to c\n"
        f"힘의 크기는 c와 같아야 합니다")


if __name__ == "__main__":
    pytest.main([__file__])
