import matplotlib.pyplot as plt
import numpy as np

import my_code_here as mch


def sample_main():
    # This is a sample main function
    # 이것은 샘플 메인 함수입니다.
    m_kg = 1.0
    c_Npmps = 0.5
    k_Npm = 10.0

    t_sec = 0.0

    t_array_sec = np.linspace(0.0, 10.0, 101)

    v_mps = 1.0
    x_m = 0.1

    xv = np.array([x_m, v_mps])
    xv0 = np.array([x_m, 0.0])

    print(
        f"linear damping force example = {mch.linear_damping_force(c_Npmps, v_mps)}[N]\n"
        f"nonlinear damping force example = {mch.nonlinear_damping_force(c_Npmps, v_mps)}[N]\n"
    )
    
    print(
        f"linear slope example = {mch.linear_slope(t_sec, xv, m_kg, c_Npmps, k_Npm)}[N]\n"
        f"nonlinear slope example = {mch.nonlinear_slope(t_sec, xv, m_kg, c_Npmps, k_Npm)}[N]\n"
    )

    d_linear = mch.linear_solution(t_array_sec, xv0, m_kg, c_Npmps, k_Npm)
    d_nonlinear = mch.nonlinear_solution(t_array_sec, xv0, m_kg, c_Npmps, k_Npm)

    xv_linear = d_linear['xv_array']
    xv_nonlinear = d_nonlinear['xv_array']

    assert max(xv_linear.shape) == len(t_array_sec)
    assert max(xv_nonlinear.shape) == len(t_array_sec)

    # plot time vs {x, v}
    plt.clf()
    _, axs = plt.subplots(2, 1)
    for k in range(2):
        axs[k].plot(t_array_sec, xv_linear[k, :], label="linear")
        axs[k].plot(t_array_sec, xv_nonlinear[k, :], label="nonlinear")
        axs[k].set_xlabel("time [s]")
        axs[k].legend(loc=0)
        axs[k].grid(True)

    axs[0].set_ylabel("x[m]")
    axs[1].set_ylabel("v[m/s]")
    plt.savefig("sample.png")


if "__main__" == __name__:
    sample_main()
