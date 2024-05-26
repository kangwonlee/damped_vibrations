

# Investigating Linear and Nonlinear Damping in Oscillatory Systems<br>선형 비선형 감쇠진동 시스템 조사

This project explores the behavior of oscillating systems under the influence of two types of damping:<br>이 과제는 아래 두 종류의 감쇠에 영향을 받는 진동 시스템의 행동을 알아보고자 합니다:

1. Linear Damping: The damping force is directly proportional to the velocity of the oscillating object.<br>선형 감쇠 : 감쇠력은 진동하는 물체의 속도에 정확히 선형적으로 비례합니다.
1. Nonlinear Damping: The damping force is not linearly related to the velocity and often exhibits more complex behavior.<br>비선형 감쇠 : 감쇠력은 속도와 선형적으로 비례하지 않으며 많은 경우 더 복잡한 행동을 보입니다.

## Problem Description<br>문제 설명

We will model two scenarios involving an oscillating system (like a mass on a spring):<br>임의의 진동계 (스프링과 연결된 질량 같은) 에 관한 두 가지 시나리오를 살펴보겠습니다.

1. Scenario 1: Linear damping where the damping force is proportional to the velocity.<br>시나리오 1: 감쇠력이 속도에 선형적으로 비례하는 선형 감쇠일 것이다.
1. Scenario 2: Nonlinear damping where the damping force is proportional to the sign of the velocity.<br>시나리오 2: 감쇠력이 속도의 **부호**에 비례하는 비선형 감쇠일 것이다.

Our goal is to use numerical methods to solve the ordinary differential equations (ODEs) that describe these systems and analyze the resulting motion.<br>우리의 목표는 이러한 시스템을 묘사하는 상미분 방정식(ODEs)의 해를 수치적인 방법으로 구하고, 그 결과로 나타나는 거동을 분석하는 것입니다.

## Implementations<br>구현 사항

1. Implement Damping Functions:<br>감쇠 함수 구현:

    * Write a function `linear_damping_force(v, c)` that returns the linear damping force `c*v`, where `v` is the velocity and `c` is the damping coefficient.<br>`linear_damping_force(v, c)`: 선형 감쇠력 `c * v` 를 반환하는 함수 (`v`는 속도, `c`는 감쇠 계수).
    * Write a function `nonlinear_damping_force(v, c)` that returns the nonlinear damping force `c*sign(v)`, where `sign(v)` is the signum function (`-1` for negative `v`, `0` for zero `v`, and `1` for positive `v`).<br>`nonlinear_damping_force(v, c)`: 비선형 감쇠력 `c * sign(v)`를 반환하는 함수 (`sign(v)`는 부호 함수)

1. Define ODE Slopes (Derivatives):<br>상미분 방정식의 기울기 함수 구현:

    * Write a function `linear_slope(t, xv, m, c, k)` that returns the derivatives of position and velocity for the linear damping scenario. The input `xv` is an array containing the position and velocity at time `t`.<br>`linear_slope(t, xv, m, c, k)`: 선형 감쇠 시나리오에 대한 위치와 속도의 미분을 반환하는 함수. 입력 `xv`는 시간 `t`에서의 위치와 속도를 담은 배열.
    * WWrite a function `nonlinear_damping_solution(t_eval, m, k, c, x0, v0)` that does the same for the nonlinear damping scenario.<br>`nonlinear_damping_solution(t_eval, m, k, c, x0, v0)`: 비선형 감쇠 시나리오에 대한 위치와 속도의 미분을 반환하는 함수.

1. Solve the ODEs:<br>ODE의 해 곡선:

    * Write a function `linear_damping_solution(t_eval, m, k, c, x0, v0)` that uses `solve_ivp` from `SciPy` to solve the ODE for Scenario 1 (linear damping) and returns the solution at specified time points t_eval.<br>`linear_damping_solution(t_eval, m, k, c, x0, v0)`: `SciPy`의 `solve_ivp`를 사용하여 시나리오 1 (선형 감쇠)에 대한 상미분방정식의 해를 구하고 지정된 시점 `t_eval`에서의 해를 반환합니다.
    * WWrite a function `nonlinear_damping_solution(t_eval, m, k, c, x0, v0)` that does the same for Scenario 2 (nonlinear damping).<br>`nonlinear_damping_solution(t_eval, m, k, c, x0, v0)`: 시나리오 2 (비선형 감쇠)에 대한 해를 반환하는 함수.

1. Analysis and Visualization:<br>분석과 시각화:

    * Plot and compare the displacement $x(t)$ and velocity $\frac{d}{dt}x(t)$ for both scenarios over a suitable time interval.<br>두 시나리오에 대한 변위 $x(t)$와 속도 $\frac{d}{dt}x(t)$를 그래프로 나타내고 비교 분석합시다.
    * Compare and contrast the behavior of the two systems. How does the damping affect the amplitude and frequency of the oscillations?<br>두 시스템의 행동을 비교 분석합니다. 감쇠가 진동의 진폭과 주파수에 어떤 영향을 미치는지 설명해 봅시다.

### File Table<br>파일 목록

| File or Folder<br>파일 또는 폴더 | Type<br>형식 | Purpose<br>목적 | Description<br>설명 | Permission<br>권한 |
|-----------------------|----------|---------------------------|-------------------------------------------------------------------------------------|:-------------:|
| `my_code_here.py`    | Python   | Main Script<br>주 파일 | Write your code to solve the assignment problem in this file.<br>이 파일에 과제 코드를 작성.  | Modify<br>수정 |
| `sample.py`           | Python   | Example Usage<br>사용 예 | This file demonstrates how to use the assignment code.<br>과제 코드 사용 예. | Read-Only<br>읽기 전용 |
| `.github/workflows/` | YAML     | CI/CD Configuration<br>연속 통합/배포 설정 | Defines automated workflows for testing and deployment.<br>시험 배포 자동화 절차 설정. | Read-Only<br>읽기 전용 |
| `tests/`              | Python   | Test Cases<br>시험 파일 | Tests to check the correctness of your code.<br>코드가 맞는지 시험. | Read-Only<br>읽기 전용 |

### Function Table<br>함수 목록

* Description of the function(s) of the `my_code_here.py` file.<br>`my_code_here.py` 파일의 함수에 대한 설명입니다.

| function<br>함수 | return type<br>반환 형 | return unit<br>반환값 단위 | return value<br>반환값 |
|:--------:|:-----------:|:-----------:|:-----------:|
| `linear_damping_force(c, v)` | `float` | $N$ | Linear damping force.<br> 선형 감쇠력. |
| `nonlinear_damping_force(c, v)` | `float` | $N$ | Nonlinear damping force.<br> 비선형 감쇠력. |
| `linear_slope(t, xv, m, c, k)` | `numpy.ndarray` | $m/s$, $m/s/s$ | Callback function for the linear system.<br> 선형 진동계 콜백 함수. |
| `nonlinear_slope(t, xv, m, c, k)` | `numpy.ndarray` | $m/s$, $m/s/s$ | Callback function for the nonlinear system.<br> 비선형 진동계 콜백 함수. |
| `linear_solution(t_array, xv0, m, c, k)` | - | $s$, $m$, $m/s$ | Solution curve for the linear system.<br> 선형 진동계 해 곡선 계산. |
| `nonlinear_solution(t_array, xv0, m, c, k)` | - | $s$, $m$, $m/s$ | Solution curve for the nonlinear system.<br> 비선형 진동계 해 곡선 계산. |

* Write all your code within the function(s) in `my_code_here.py`, but feel free to add comments outside the functions to explain your work.<br>`my_code_here.py` 의 모든 코드는 함수 안에 작성되어야 함. 예외로 설명을 위한 주석문은 함수 밖에 자유로이 추가할 수 있음.

### Argument Table<br>매개변수 목록

| argument<br>매개변수 | return type<br>반환 형 | unit<br>단위 | return value<br>반환값 |
|:--------:|:-----------:|:-----------:|:-----------:|
| `t` | `float` | $sec$ | Time.<br> 시간. |
| `t_array` | `numpy.ndarray` | $sec$ | Time array.<br> 시간 배열. |
| `m` | `float` | $kg$ | Mass.<br> 질량. |
| `c` | `float` | $N/(m/s)$ | Damping coefficient.<br> 감쇠 계수. |
| `k` | `float` | $N/m$ | Spring coefficient.<br> 스프링 상수. |
| `x` | `float` | $m$ | Position.<br> 위치. |
| `v` | `float` | $m/s$ | derivative of the position.<br> 위치의 미분. |
| `xv` | `numpy.ndarray` | $m$, $m/s$ | array containing the position and the speed.<br> 위치와 속도를 담은 배열. |
| `xv0` | `numpy.ndarray` | $m$, $m/s$ | array containing the initial values.<br> 초기값 배열. |


### Return Value Key Table<br>매개변수 키 목록

* `linear_solution()` and `nonlinear_solution()` functions are expected to return a `dict` of following keys.<br>과제 함수 중 `linear_solution()` 와(과) `nonlinear_solution()`는 아래 key를 담은 `dict`를 반환하시오.

| return value key<br>반환값 key | type<br>형 |unit<br>단위 | value |
|:--------:|:-----------:|:-----------:|:-----------:|
| `'t_array'` | `numpy.ndarray` | $sec$ | Time array. <br>시간 배열. |
| `'n'` | `int` | - | Length of the time array.<br>시간 배열의 길이. |
| `'xv_array'` | `numpy.ndarray` | $m$, $m/s$ | Position and velocity array of dimension $2 \times n$. <br>크기 $2 \times n$ 인 위치, 속도 배열. |

### Allowed Modules<br>허용 모듈 목록

* In the `my_code_here.py` file, please `import` these modules only.<br>`my_code_here.py` 파일에서는 아래 모듈만 `import` 바랍니다.

| module<br>모듈 | description<br>설명 |
|:--------:|:-----------:|
| `numpy` | numpy |
| `scipy.integrate` | numerical solver<br>수치 해법 |

## Grading<br>채점 기준 (총 5점)

* Description of the grading.<br>평가에 대한 설명입니다.

| Criteria<br>기준	| Points<br>배점 |
|:---------:|:------:|
| Python Grammar<br>Python 문법	| 1 |
| Coding Style<br>모든 코드는 함수 안에	| 1 |
| Linear Results<br>선형 감쇠 결과	| 2 |
| Nonlinear Results<br>비선형 감쇠 결과	| 1 |


## Example<br>예

* Please run `sample.py` file to see an example of how to use the functions and visualize the results. <br>해당 함수들의 사용법과 해당 결과를 시각화 하는 법에 대해서는 `sample.py` 를 실행시켜 보기 바랍니다.

## References<br>참고문헌

* Harmonic oscillator / Damped harmonic oscillator [[wiki](https://en.wikipedia.org/wiki/Harmonic_oscillator#Damped_harmonic_oscillator)]<br>조화진동자 / 감쇠진동 [[wiki](https://ko.wikipedia.org/wiki/조화_진동자#감쇠_진동)]
* scipy.integrate.solve_ivp() [[link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)].

## Notes

* This assignment was developed with the assistance of an AI language model for creative inspiration and guidance, demonstrating the potential of AI as a tool to enhance learning and problem-solving.  Students are encouraged to use AI responsibly and ethically, always prioritizing their own understanding and critical thinking.

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다. (교육 도구 개발 및 개선, 연구, 테스트 케이스 및 교육용 데이터셋 생성 등).

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.
