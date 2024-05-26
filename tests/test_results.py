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
def test_linear_damping_force(linear_damping_params: Tuple[float, float, float]):
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


# Parametrized test cases without a fixture
@pytest.mark.parametrize("c, v, expected_force", [
    (1.0, 2.0, 1.0),
    (0.5, -3.0, -0.5),
    (2.5, 0.0, 0.0),
    (1.2, -0.8, -1.2),
])
def test_nonlinear_damping_force(c:float, v:float, expected_force:float):
    calculated_force = mch.nonlinear_damping_force(c, v)

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

    # Check if sign of the calculated force matches the sign of velocity
    assert np.sign(calculated_force) == np.sign(v) or (v == 0 and calculated_force == 0), (
        f"{msg_arg}Force should have same sign as velocity (or be zero if v = 0)\n"
        f"힘은 속도와 같은 부호를 가져야 합니다 (v=0이면 0)"
    )

    # Check if magnitude of the force is constant (equal to c)
    assert (
        np.isclose(abs(calculated_force), abs(expected_force), rtol=1e-6)
        or (v == 0 and calculated_force == 0)
    ), (
        f"{msg_arg}Please check the magnitude of force.\n"
        f"힘의 크기를 확인 바랍니다."
        f"{msg_arg}"
        f"Expected: {expected_force}\n"
        f"예상 결과 : {expected_force}\n"
        f"Got: {calculated_force}\n"
        f"반환값: {calculated_force}\n"
    )


@pytest.mark.parametrize(
    "t, x, v, m, c, k, expected_dxdt, expected_dvdt",
    [
        (0.0, 1.0, 2.0, 1.0, 0.5, 10.0, 2.0, -11.0),
        (2.5, -0.5, -1.0, 2.0, 1.5, 5.0, -1.0, 2.0),
        (1.0, 0.0, 0.0, 0.8, 0.2, 8.0, 0.0, 0.0),
        (5.0, 3.0, 0.1, 0.5, 1.2, 6.0, 0.1, -36.24),
    ],
)
def test_linear_slope(
    t: float, x: float, v: float, m: float, c: float, k: float,
    expected_dxdt: float, expected_dvdt: float,
):
    xv = np.array([x, v])
    calculated_slopes = mch.linear_slope(t, xv, m, c, k)

    # Assert the results (with input arguments in message)
    msg_arg = f"Input: t={t}, x={x}, v={v}, m={m}, c={c}, k={k}\n"

    assert isinstance(calculated_slopes, np.ndarray), (
        f"{msg_arg}"
        "Expected type: numpy.ndarray\n"
        "예상 자료형: numpy.ndarray\n"
        f"Got type: {type(calculated_slopes)}\n"
        f"받은 자료형: {type(calculated_slopes)}\n"
    )

    assert calculated_slopes.shape == (2,), (
        f"{msg_arg}"
        "Expected shape: (2,)\n"
        "예상 행렬 수: (2,)\n"  # Corrected translation for "shape"
        f"Got shape: {calculated_slopes.shape}\n"
        f"받은 행렬 수: {calculated_slopes.shape}\n"
    )

    assert np.allclose(
        calculated_slopes, np.array([expected_dxdt, expected_dvdt]), rtol=1e-6
    ), (
        f"{msg_arg}"
        f"Expected: dx/dt={expected_dxdt}, dv/dt={expected_dvdt}\n"
        f"예상 결과: dx/dt={expected_dxdt}, dv/dt={expected_dvdt}\n"
        f"Got: dx/dt={calculated_slopes[0]}, dv/dt={calculated_slopes[1]}\n"
        f"반환된 값: dx/dt={calculated_slopes[0]}, dv/dt={calculated_slopes[1]}"
    )


if __name__ == "__main__":
    pytest.main([__file__])
