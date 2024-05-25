
# Breaking News: Dunder Mifflin Plagued by Mysterious Oscillations!<br>속보입니다! 긴급 진동 발생! SNL 수치해석 특별 방송!

"This just in! SNL's top field reporter is live at Dunder Mifflin's Scranton branch, where employees are experiencing a bizarre phenomenon: unexplained oscillations causing chaos throughout the office.  Sources say the vibrations are so intense that Dwight Schrute's bobblehead collection has been knocked off its shelf, and Stanley Hudson's crossword puzzle is now completely illegible. We're here to investigate the source of these oscillations and determine if they're a threat to the company's productivity (and sanity)."

안녕하십니까, 시청자 여러분. 저는 SNL 특파원 주 기자입니다! 지금 막 무한상사에서 긴급 상황이 발생했습니다. 유재석 부장님의 격렬한 춤사위와 정준하 과장님의 폭풍 먹방으로 인해 사무실 전체가 흔들리고 있습니다. 이 엄청난 진동은 마치 지진이라도 난 듯 책상과 의자를 덜덜 떨게 만들고 있습니다.

하지만, 걱정하지 마십시오! 우리에겐 든든한 지원군, 파이썬의 `solve_ivp` 함수가 있습니다. 이 강력한 도구를 활용하면, 이 혼돈 속에서도 진동의 패턴을 분석하고 예측할 수 있습니다.

**지금부터 저와 함께, 무한상사의 진동 현장을 수치해석으로 파헤쳐 봅시다!**

## Problem Description<br>현장 상황

"Our sources have identified two potential culprits behind the Dunder Mifflin mayhem:

1. Kevin's Chili Calamity (Linear Damping): Kevin Malone, the office's resident chili enthusiast, accidentally spilled a massive pot of his famous chili on the breakroom floor. The resulting waves of chili are causing the floor to oscillate, with the linoleum providing a linear damping force.<br>유재석 부장님의 댄스 타임: 유 부장님의 현란한 춤 동작은 책상을 좌우로 흔들리게 만들고 있습니다. 이 움직임은 시간이 지날수록 점차 줄어드는 선형 감쇠 진동으로 볼 수 있습니다. 마치 흥겨운 댄스곡이 끝나고 차분한 음악으로 넘어가는 것처럼 말이죠.
1. Michael's Motivational Mayhem (Nonlinear Damping): Michael Scott, the self-proclaimed "World's Best Boss," has been conducting a series of impromptu motivational speeches and team-building exercises. The resulting chaos and confusion have caused the office to vibrate erratically, with a damping force that seems as unpredictable as Michael himself.<br>정준하 과장님의 먹방 퍼레이드: 정 과장님이 짜장면을 흡입하는 모습은 마치 진공청소기 같습니다. 이 엄청난 먹방은 의자를 앞뒤로 격렬하게 움직이게 만들고 있습니다. 이 움직임은 예측하기 어려운 비선형 감쇠 진동으로, 마치 박명수 차장님의 급발진 잔소리처럼 갑작스럽고 강렬합니다.

Our team of expert analysts will be using Python's `solve_ivp` function to model these scenarios and determine the nature of the damping forces at play. We'll also be interviewing key witnesses (and potential suspects) to get to the bottom of this bizarre situation."
 
**특종! 여러분도 수치해석 전문가가 될 수 있습니다!**

## Tasks<br>미션

1. Field Reporter's Toolkit: Get your Python environment set up with `solve_ivp` ready for action. It's time to channel your inner investigative journalist and uncover the truth behind the Dunder Mifflin oscillations.

1. Implement Damping Functions:<br>감쇠 함수 구현

    * Write a function `linear_damping_force(v, c)` that returns the linear damping force `c*v`, where `v` is the velocity and `c` is the damping coefficient.<br>`linear_damping_force(v, c)`: 선형 감쇠력 `c * v` 를 반환하는 함수 (`v`는 속도, `c`는 감쇠 계수).
    * Write a function `nonlinear_damping_force(v, c)` that returns the nonlinear damping force `c*sign(v)`, where `sign(v)` is the signum function (`-1` for negative `v`, `0` for zero `v`, and `1` for positive `v`).<br>`nonlinear_damping_force(v, c)`: 비선형 감쇠력 `c * sign(v)`를 반환하는 함수 (`sign(v)`는 부호 함수)

1. Solve the ODEs:<br>ODE의 해 곡선:

    * Write a function `linear_damping_solution(t_eval, m, k, c, x0, v0)` that uses `solve_ivp` to solve the ODE for Kevin's chili spill with linear damping and returns the solution at specified time points `t_eval`.
    * Write a function `nonlinear_damping_solution(t_eval, m, k, c, x0, v0)` that does the same for Meredith's office chair race with nonlinear damping.
(Note: `m` is the mass, `k` is the spring constant, `x0` is the initial displacement, and `v0` is the initial velocity.)

1. Breaking News Analysis:<br>결과 분석 및 비교:

    * Plot and compare the displacement $x(t)$ and velocity $\frac{d}{dt}x(t)$ for both scenarios over a suitable time interval.<br>두 시나리오에 대한 변위 $x(t)$와 속도 $\frac{d}{dt}x(t)$를 그래프로 나타내고 비교 분석합니다.
    * Discuss the observed differences and their physical interpretations in the context of "The Office." For example, you could relate the smooth decay of linear damping to Jim's calm demeanor and the erratic behavior of nonlinear damping to Michael's chaotic energy.<br>선형 감쇠와 비선형 감쇠의 차이점을 "무한상사"의 관점에서 이해해봅시다. 예를 들어 선형 감쇠의 부드러운 진폭 감소를 유재석 부장의 차분한 태도와 연결지어 생각해 볼 수 있고, 비선형 감쇠의 불규칙한 행동을 박명수 차장의 에너지 넘친 급발진과 비교해 볼 수도 있을 것입니다.

1. Exclusive Interview (Bonus):  For those who want to go the extra mile, conduct a mock interview with a Dunder Mifflin employee (played by you or a friend). Get their perspective on the oscillations and their potential impact on office productivity. Extra points for incorporating iconic quotes and mannerisms from the show.

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
| `linear_solution(t_array, xv, xv0, m, c, k)` | - | $s$, $m$, $m/s$ | Solution curve for the linear system.<br> 선형 진동계 콜백 함수. |
| `nonlinear_solution(t_array, xv, m, c, k)` | - | $s$, $m$, $m/s$ | Solution curve for the nonlinear system.<br> 비선형 진동계 콜백 함수. |

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

* References for the assignment.<br>과제에 대한 참고문헌입니다.

**시청자 여러분, 감쇠 진동의 세계는 결코 지루하지 않습니다! 여러분의 빛나는 수치해석 실력으로 무한상사의 진동 문제를 해결하고, 숨겨진 진실을 밝혀내세요! 이상, SNL 특파원 주 기자였습니다!**

## Notes

* This assignment was developed with the assistance of an AI language model for creative inspiration and guidance, demonstrating the potential of AI as a tool to enhance learning and problem-solving.  Students are encouraged to use AI responsibly and ethically, always prioritizing their own understanding and critical thinking.

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다. (교육 도구 개발 및 개선, 연구, 테스트 케이스 및 교육용 데이터셋 생성 등).

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.
