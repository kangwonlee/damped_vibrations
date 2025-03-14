import os
import pathlib
import random
import sys

from typing import Tuple


import matplotlib.pyplot as plt
import numpy as np
import pytest


sys.path.insert(
    0,
    os.getenv(
        'STUDENT_CODE_FOLDER',
        str(
            pathlib.Path(__file__).parent.parent.absolute()
        )
    )
)


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


# Parametrized test cases without a fixture
@pytest.mark.parametrize("c, v, expected_force", [
    (1.0, 2.0, 1.0),
    (0.5, -3.0, -0.5),
    (2.5, 0.0, 0.0),
    (1.2, -0.8, -1.2),
])
def test_nonlinear_damping_force(c:float, v:float, expected_force:float):
    calculated_force = exercise.nonlinear_damping_force(c, v)

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


@pytest.mark.parametrize("t, x, v, m, c, k, expected_dxdt, expected_dvdt", [
    (0.0, 1.0, 2.0, 1.0, 0.5, 10.0, 2.0, -10.5),      
    (2.5, -0.5, -1.0, 2.0, 1.5, 5.0, -1.0, 2.0),    
    (1.0, 0.0, 0.0, 0.8, 0.2, 8.0, 0.0, 0.0),       
    (5.0, 3.0, 0.1, 0.5, 1.2, 6.0, 0.1, -38.4),     
    (2.0, -2.0, -3.0, 1.3, 0.8, 4.0, -3.0, 6.769230769230768) 
])
def test_nonlinear_slope(
        t:float, x:float, v:float, m:float, c:float, k:float,
        expected_dxdt:float, expected_dvdt:float):
    xv = np.array([x, v])
    calculated_slopes = exercise.nonlinear_slope(t, xv, m, c, k)

    # Assert the results (with input arguments in message)
    msg_arg = (
        f"Input: t={t}, x={x}, v={v}, m={m}, c={c}, k={k}\n"  # Input args here
    )

    assert isinstance(calculated_slopes, np.ndarray),(
        f"{msg_arg}Expected type: numpy.ndarray\n"
        f"예상 자료형: numpy.ndarray\n"
        f"Got type: {type(calculated_slopes)}\n"
        f"받은 자료형: {type(calculated_slopes)}\n"
    )

    assert calculated_slopes.shape == (2,), (
        f"{msg_arg}Expected shape: (2,)\n"
        f"예상 행 열 수: (2,)\n"
        f"Got shape: {calculated_slopes.shape}\n"
        f"받은 행 열 수: {calculated_slopes.shape}\n"
    )

    assert np.allclose(calculated_slopes, np.array([expected_dxdt, expected_dvdt]), rtol=1e-6), (
        f"{msg_arg}"
        f"Expected: dx/dt={expected_dxdt}, dv/dt={expected_dvdt}\n"
        f"예상 결과: dx/dt={expected_dxdt}, dv/dt={expected_dvdt}\n"
        f"Got: dx/dt={calculated_slopes[0]}, dv/dt={calculated_slopes[1]}\n"
        f"반환된 값: dx/dt={calculated_slopes[0]}, dv/dt={calculated_slopes[1]}"
    )


def test_nonlinear_solution(
        m_c_k_xv0_t_array: Tuple[float, float, float, np.ndarray, np.ndarray],):

    m, c, k, xv0, t_array = m_c_k_xv0_t_array

    result = exercise.nonlinear_solution(t_array, xv0, m, c, k)

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

    energy = calc_energy(m, k, x, v)
    d_energy = np.diff(energy)

    # 3. Energy should be decreasing
    if not np.all(d_energy <= 1e-2):

        i_where = np.argwhere(d_energy > 0)

        plt.subplot(3, 1, 1)
        plt.plot(t_array, energy, label="energy")

        plt.scatter(t_array[i_where], energy[i_where], color='red', label="Increasing energy")

        plt.xlabel("Time [s]")
        plt.ylabel("Energy [J]")
        plt.legend(loc=0)
        plt.title("Energy should be decreasing")
        plt.grid(True)

        plt.subplot(3, 1, 2)
        plt.plot(t_array, x, label="position")

        plt.scatter(t_array[i_where], x[i_where], color='red', label="Increasing energy")

        plt.xlabel("Time [s]")
        plt.ylabel("x [m]")
        plt.legend(loc=0)
        plt.grid(True)

        plt.subplot(3, 1, 3)
        plt.plot(t_array, v, label="position")

        plt.scatter(t_array[i_where], v[i_where], color='red', label="Increasing energy")

        plt.xlabel("Time [s]")
        plt.ylabel("v [m/s]")
        plt.legend(loc=0)
        plt.grid(True)

        plt.savefig(f"nonlinear_energy_{m}.png")
        plt.close()

        pytest.fail(
            f"{msg_arg}"
            "Energy should be decreasing\n"
            "에너지는 감소해야 합니다"
            f"d_energy.max(): {d_energy.max()} at t = {t_array[np.argmax(d_energy)]}\n"
        )

    # 4. Energy dissipation would be related to the dissipation by damping force

    d_energy_dt = d_energy / t_array[1]

    dissipation = c * np.abs(v)

    delta_dedt_dissp = d_energy_dt + dissipation[:-1]

    if delta_dedt_dissp.max() >= 0.01:

        plt.subplot(2, 1, 1)
        plt.plot(t_array[:-1] , d_energy_dt, label='dE/dt')
        plt.plot(t_array , -dissipation, label='-dissipation')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(t_array[:-1] , delta_dedt_dissp, label='error')
        plt.grid(True)

        plt.savefig(f'de_dt_{m}.png')
        plt.close()

        pytest.fail(
            f"{msg_arg}"
            "Energy rate should be close to the dissipation by the damping\n"
            "에너지 감소율은 감쇠에 의한 소산에 가까와아 합니다"
            f"max error : {delta_dedt_dissp.max()} at t = {t_array[np.argmax(delta_dedt_dissp)]}\n"
        )


def calc_energy(m:float, k:float, x:np.ndarray, v:np.ndarray) -> np.ndarray:
    return 0.5*m*v**2 + 0.5*k*x**2


if __name__ == "__main__":
    pytest.main([__file__])
