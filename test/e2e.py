import filecmp
import shutil
from contextlib import contextmanager
from pathlib import Path
from tempfile import mkdtemp

from click.testing import CliRunner

import main

test_expected_output_file = str(Path(__file__).parent / 'files' / 'expected_output.yaml')


@contextmanager
def temp_test_output_file(prefix: str = 'pte-') -> str:
    dir_name: str = str()
    inited: bool = False
    try:
        dir_name = mkdtemp(prefix=prefix)
        inited = True
        output_file_name = Path(dir_name).joinpath('output.yaml')
        yield output_file_name
    finally:
        if inited:
            shutil.rmtree(dir_name)


def test_unforced():
    with temp_test_output_file() as test_output_file:
        runner = CliRunner()
        runner.invoke(main.cli, ['unforced', '--file', test_output_file])
        assert filecmp.cmp(test_output_file, test_expected_output_file)


def test_forced():
    with temp_test_output_file() as test_output_file:
        runner = CliRunner()
        runner.invoke(main.cli, ['forced', '--file', test_output_file])
        assert filecmp.cmp(test_output_file, test_expected_output_file)


def test_extraforced():
    with temp_test_output_file() as test_output_file:
        runner = CliRunner()
        runner.invoke(main.cli, ['extraforced', '--file', test_output_file])
        assert filecmp.cmp(test_output_file, test_expected_output_file)
