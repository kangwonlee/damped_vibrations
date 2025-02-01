import pathlib
import random
import sys
from typing import Tuple


import matplotlib.pyplot as plt
import numpy as np
import pytest


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))


# Import the module containing the functions to be tested.
# 테스트할 함수를 포함하는 모듈을 불러옵니다.
try:
    import exercise
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
    calculated_force = exercise.linear_damping_force(c, v)

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
    calculated_slopes = exercise.linear_slope(t, xv, m, c, k)

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


@pytest.fixture
def exact_linear(m_c_k_xv0_t_array: Tuple[float, float, float, np.ndarray, np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    m, c, k, xv0, t_array = m_c_k_xv0_t_array

    x0, v0 = xv0

    A = (c*x0 + 2*m*v0 + x0 * (c**2 - 4 * k * m)**0.5) / (2 * (c**2 - 4 * k * m)**0.5)
    B = (-c*x0 + (-2)*m*v0 + x0 * (c**2 - 4 * k * m)**0.5) / (2 * (c**2 - 4 * k * m)**0.5)

    expA = t_array * (-c+(c**2 - 4*k*m)**0.5)/(2*m)
    expB = (-1.0) * t_array * (c+(c**2 - 4*k*m)**0.5)/(2*m)

    exact = A * np.exp(expA) + B * np.exp(expB)

    return exact


def test_linear_solution(
        m_c_k_xv0_t_array: Tuple[float, float, float, np.ndarray, np.ndarray],
        exact_linear: np.ndarray):

    m, c, k, xv0, t_array = m_c_k_xv0_t_array

    result = exercise.linear_solution(t_array, xv0, m, c, k)

    # Basic checks
    assert isinstance(result, dict), "Return value should be a dictionary"
    assert set(result.keys()) == {"t_array", "n", "xv_array"}, "Dictionary keys are incorrect"
    assert result["n"] == len(t_array), "n should be the length of t_array"
    assert result["xv_array"].shape == (2, len(t_array)), "xv_array shape is incorrect"

    # Assert the results (with input arguments in message)
    msg_arg = (
        f"Input: t={t_array.min()} ~ {t_array.max()}, xv0={xv0}, m={m}, c={c}, k={k}\n"  # Input args here
    )

    # Check if solution exhibits expected behavior
    x, v = result["xv_array"]

    # 1. Initial conditions are met
    assert np.allclose(x[0], xv0[0], rtol=1e-6), (
        f"{msg_arg}"
        "Initial position is incorrect\n"
        "초기 위치 확인 바랍니다\n"
        f"Expected: ={xv0[0]}\n"
        f"예상 결과: {xv0[0]}\n"
        f"Got: {x[0]}\n"
        f"반환된 값: {x[0]}"
    )
    assert np.allclose(v[0], xv0[1], rtol=1e-6), (
        f"{msg_arg}"
        "Initial velocity is incorrect\n"
        "초기 속도 확인 바랍니다\n"
        f"Expected: ={xv0[0]}\n"
        f"예상 결과: {xv0[0]}\n"
        f"Got: {x[0]}\n"
        f"반환된 값: {x[0]}"
    )

    # 2. Check if t_array has the same values as input
    assert np.allclose(result["t_array"], t_array), (
        f"{msg_arg}"
        "t_array should have the same value as input time array"
        "t_array는 입력 시간 배열과 동일한 값을 가져야 합니다"
    )

    i_larger = np.where(abs(exact_linear) > 1e-3)

    t_large = t_array[i_larger]
    exact_large = exact_linear[i_larger]
    x_large = x[i_larger]

    # 3. Solution should be close to exact solution
    if not np.allclose(exact_large, x_large, rtol=1e-1, atol=1e-3):
        plt.subplot(3, 1, 1)
        plt.plot(t_array, x, label="Solution")
        plt.plot(t_array, exact_linear, label="Exact solution")

        i_far = np.where(np.isclose(exact_large, x_large, rtol=1e-3, atol=1e-3))

        plt.scatter(t_large[i_far], x_large[i_far], label="Far from exact solution", color="red")

        plt.xlabel("Time [s]")
        plt.ylabel("Position [m]")
        plt.legend(loc=0)
        plt.title("Linear solution outside the tolerance")

        plt.subplot(3, 1, 2)
        plt.semilogy(t_large, abs((x_large-exact_large)), label="Error")
        plt.xlabel("Time [s]")
        plt.ylabel("abs Error")
        plt.legend(loc=0)
        plt.grid(True)

        plt.subplot(3, 1, 3)
        plt.semilogy(t_large, abs((x_large-exact_large)/exact_large), label="Error")
        plt.xlabel("Time [s]")
        plt.ylabel("Relative Error")
        plt.legend(loc=0)
        plt.grid(True)

        plt.savefig(f"linear_solution_envelopes_{m}.png")
        plt.close()

        pytest.fail(
            f"{msg_arg}"
            "Solution does not match the exact solution within the tolerance\n"
            "해답이 허용 오차를 벗어났습니다\n"
            "Please check the solution\n"
            "해답을 확인 바랍니다"
        )


if __name__ == "__main__":
    pytest.main([__file__])
