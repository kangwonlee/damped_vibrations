import ast
import logging
import pathlib
import sys

from typing import Tuple

import pytest

file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()

sys.path.insert(0, str(proj_folder))

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


def test_syntax_validity(py_file:pathlib.Path):

    code = py_file.read_text(encoding="utf-8")

    try:
        ast.parse(code)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in file: {py_file.relative_to(proj_folder)}\n{e}")


@pytest.fixture(scope="session")  # Session scope to share the allowed modules across tests
def allowed_modules() -> Tuple[str]:
    return ("math",)


def test_allowed_imports(py_file:pathlib.Path, allowed_modules:Tuple[str]):

    code = py_file.read_text(encoding="utf-8")

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module_name = node.module if isinstance(node, ast.ImportFrom) else node.names[0].name
            if module_name not in allowed_modules:
                pytest.fail(
                    f"Import of disallowed module '{module_name}' in {py_file}\n"
                    f"{py_file.relative_to(proj_folder)} 파일에서 '{module_name}' 모듈을 import 않기 바랍니다."
                )


def test_importable():
    import my_code_here
    assert my_code_here is not None


if __name__ == "__main__":
    pytest.main([__file__])
