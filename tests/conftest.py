import itertools
import pathlib
import random

from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()



def py_files() -> Tuple[pathlib.Path]:
    return tuple(
        filter(
            lambda s:'sample.py' != s.name,
            proj_folder.glob('*.py')
        )
    )


def pytest_generate_tests(metafunc):
    if "py_file" in metafunc.fixturenames:
        metafunc.parametrize("py_file", py_files())


# =====
import numpy as np

@pytest.fixture(
        params=[(1.0, 0.1, 1.0, np.array([1.0, 0.0]), np.arange(0, 5+1e-7, 1e-3)),
            (2.0, 0.5, 4.0, np.array([0.5, 0.0]), np.arange(0, 10+1e-7, 1e-3)),])
def m_c_k_xv0_t_array(request) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    return request.param
