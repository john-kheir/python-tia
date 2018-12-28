import pytest

from tia.cov import (
    ContextTableRow,
    FileTableRow,
    LineTableRow,
    get_context_table,
    get_file_table,
    get_line_table,
)

pytestmark = [pytest.mark.coveragepy, pytest.mark.unit]

# corresponding to the content of tests/data/.coverage
context_table_rows = [
    ContextTableRow(context_id=1, context=''),
    ContextTableRow(context_id=2, context='test_reading_existing_valid_config_file_returns_string'),
    ContextTableRow(context_id=3, context='test_reading_existing_invalid_config_file_raises_error'),
    ContextTableRow(context_id=4, context='test_reading_non_existing_config_file_raises_exception'),
    ContextTableRow(context_id=5, context='test_read_valid_parent_key_config'),
    ContextTableRow(context_id=6, context='test_read_valid_explicit_full_blown_pipelines_config'),
    ContextTableRow(context_id=7, context='test_read_valid_implicit_full_blown_pipelines_config'),
    ContextTableRow(context_id=8, context='test_read_valid_single_pipeline_with_dirs_only_config'),
    ContextTableRow(context_id=9, context='test_read_valid_single_pipeline_with_files_only_config'),
    ContextTableRow(context_id=10, context='test_read_invalid_pipelines_config'),
    ContextTableRow(context_id=11, context='test_is_some_ci'),
    ContextTableRow(context_id=12, context='test_is_no_ci'),
    ContextTableRow(context_id=13, context='testsfailed'),
]

# corresponding to the content of tests/data/.coverage
file_table_rows = [
    FileTableRow(file_id=1, path='/home/fk/github/python-tia/tia/__init__.py'),
    FileTableRow(file_id=2, path='/home/fk/github/python-tia/tia/config.py'),
    FileTableRow(file_id=3, path='/home/fk/github/python-tia/tia/env.py'),
]

# corresponding to the content of tests/data/.coverage
line_table_rows = [
    LineTableRow(file_id=1, context_id=1, lineno=1),
    LineTableRow(file_id=2, context_id=1, lineno=1),
    LineTableRow(file_id=2, context_id=1, lineno=2),
    LineTableRow(file_id=2, context_id=1, lineno=3),
    LineTableRow(file_id=2, context_id=1, lineno=5),
    LineTableRow(file_id=2, context_id=1, lineno=8),
    LineTableRow(file_id=2, context_id=1, lineno=9),
    LineTableRow(file_id=2, context_id=1, lineno=12),
    LineTableRow(file_id=2, context_id=1, lineno=25),
    LineTableRow(file_id=2, context_id=1, lineno=30),
    LineTableRow(file_id=3, context_id=1, lineno=7),
    LineTableRow(file_id=3, context_id=1, lineno=10),
    LineTableRow(file_id=3, context_id=1, lineno=20),
    LineTableRow(file_id=3, context_id=1, lineno=27),
    LineTableRow(file_id=3, context_id=1, lineno=34),
    LineTableRow(file_id=3, context_id=1, lineno=41),
    LineTableRow(file_id=3, context_id=1, lineno=48),
    LineTableRow(file_id=3, context_id=1, lineno=55),
    LineTableRow(file_id=3, context_id=1, lineno=62),
    LineTableRow(file_id=3, context_id=1, lineno=69),
    LineTableRow(file_id=3, context_id=1, lineno=76),
    LineTableRow(file_id=3, context_id=1, lineno=83),
    LineTableRow(file_id=3, context_id=1, lineno=90),
    LineTableRow(file_id=2, context_id=2, lineno=17),
    LineTableRow(file_id=2, context_id=2, lineno=18),
    LineTableRow(file_id=2, context_id=2, lineno=20),
    LineTableRow(file_id=2, context_id=2, lineno=22),
    LineTableRow(file_id=2, context_id=3, lineno=17),
    LineTableRow(file_id=2, context_id=3, lineno=18),
    LineTableRow(file_id=2, context_id=3, lineno=20),
    LineTableRow(file_id=2, context_id=3, lineno=21),
    LineTableRow(file_id=2, context_id=4, lineno=17),
    LineTableRow(file_id=2, context_id=4, lineno=18),
    LineTableRow(file_id=2, context_id=4, lineno=19),
    LineTableRow(file_id=2, context_id=5, lineno=26),
    LineTableRow(file_id=2, context_id=5, lineno=27),
    LineTableRow(file_id=2, context_id=6, lineno=26),
    LineTableRow(file_id=2, context_id=6, lineno=27),
    LineTableRow(file_id=2, context_id=6, lineno=31),
    LineTableRow(file_id=2, context_id=6, lineno=32),
    LineTableRow(file_id=2, context_id=6, lineno=33),
    LineTableRow(file_id=2, context_id=6, lineno=34),
    LineTableRow(file_id=2, context_id=6, lineno=35),
    LineTableRow(file_id=2, context_id=6, lineno=36),
    LineTableRow(file_id=2, context_id=6, lineno=37),
    LineTableRow(file_id=2, context_id=6, lineno=38),
    LineTableRow(file_id=2, context_id=6, lineno=39),
    LineTableRow(file_id=2, context_id=6, lineno=40),
    LineTableRow(file_id=2, context_id=6, lineno=41),
    LineTableRow(file_id=2, context_id=6, lineno=42),
    LineTableRow(file_id=2, context_id=6, lineno=44),
    LineTableRow(file_id=2, context_id=6, lineno=45),
    LineTableRow(file_id=2, context_id=6, lineno=46),
    LineTableRow(file_id=2, context_id=6, lineno=47),
    LineTableRow(file_id=2, context_id=6, lineno=51),
    LineTableRow(file_id=2, context_id=6, lineno=52),
    LineTableRow(file_id=2, context_id=6, lineno=53),
    LineTableRow(file_id=2, context_id=7, lineno=26),
    LineTableRow(file_id=2, context_id=7, lineno=27),
    LineTableRow(file_id=2, context_id=7, lineno=31),
    LineTableRow(file_id=2, context_id=7, lineno=32),
    LineTableRow(file_id=2, context_id=7, lineno=33),
    LineTableRow(file_id=2, context_id=7, lineno=34),
    LineTableRow(file_id=2, context_id=7, lineno=35),
    LineTableRow(file_id=2, context_id=7, lineno=36),
    LineTableRow(file_id=2, context_id=7, lineno=37),
    LineTableRow(file_id=2, context_id=7, lineno=38),
    LineTableRow(file_id=2, context_id=7, lineno=39),
    LineTableRow(file_id=2, context_id=7, lineno=40),
    LineTableRow(file_id=2, context_id=7, lineno=41),
    LineTableRow(file_id=2, context_id=7, lineno=42),
    LineTableRow(file_id=2, context_id=7, lineno=44),
    LineTableRow(file_id=2, context_id=7, lineno=45),
    LineTableRow(file_id=2, context_id=7, lineno=46),
    LineTableRow(file_id=2, context_id=7, lineno=47),
    LineTableRow(file_id=2, context_id=7, lineno=51),
    LineTableRow(file_id=2, context_id=7, lineno=52),
    LineTableRow(file_id=2, context_id=7, lineno=53),
    LineTableRow(file_id=2, context_id=8, lineno=26),
    LineTableRow(file_id=2, context_id=8, lineno=27),
    LineTableRow(file_id=2, context_id=8, lineno=31),
    LineTableRow(file_id=2, context_id=8, lineno=32),
    LineTableRow(file_id=2, context_id=8, lineno=33),
    LineTableRow(file_id=2, context_id=8, lineno=34),
    LineTableRow(file_id=2, context_id=8, lineno=35),
    LineTableRow(file_id=2, context_id=8, lineno=36),
    LineTableRow(file_id=2, context_id=8, lineno=37),
    LineTableRow(file_id=2, context_id=8, lineno=38),
    LineTableRow(file_id=2, context_id=8, lineno=39),
    LineTableRow(file_id=2, context_id=8, lineno=40),
    LineTableRow(file_id=2, context_id=8, lineno=41),
    LineTableRow(file_id=2, context_id=8, lineno=42),
    LineTableRow(file_id=2, context_id=8, lineno=44),
    LineTableRow(file_id=2, context_id=8, lineno=45),
    LineTableRow(file_id=2, context_id=8, lineno=46),
    LineTableRow(file_id=2, context_id=8, lineno=47),
    LineTableRow(file_id=2, context_id=8, lineno=51),
    LineTableRow(file_id=2, context_id=8, lineno=52),
    LineTableRow(file_id=2, context_id=8, lineno=53),
    LineTableRow(file_id=2, context_id=9, lineno=26),
    LineTableRow(file_id=2, context_id=9, lineno=27),
    LineTableRow(file_id=2, context_id=9, lineno=31),
    LineTableRow(file_id=2, context_id=9, lineno=32),
    LineTableRow(file_id=2, context_id=9, lineno=33),
    LineTableRow(file_id=2, context_id=9, lineno=34),
    LineTableRow(file_id=2, context_id=9, lineno=35),
    LineTableRow(file_id=2, context_id=9, lineno=36),
    LineTableRow(file_id=2, context_id=9, lineno=37),
    LineTableRow(file_id=2, context_id=9, lineno=38),
    LineTableRow(file_id=2, context_id=9, lineno=39),
    LineTableRow(file_id=2, context_id=9, lineno=40),
    LineTableRow(file_id=2, context_id=9, lineno=41),
    LineTableRow(file_id=2, context_id=9, lineno=42),
    LineTableRow(file_id=2, context_id=9, lineno=44),
    LineTableRow(file_id=2, context_id=9, lineno=45),
    LineTableRow(file_id=2, context_id=9, lineno=46),
    LineTableRow(file_id=2, context_id=9, lineno=47),
    LineTableRow(file_id=2, context_id=9, lineno=51),
    LineTableRow(file_id=2, context_id=9, lineno=52),
    LineTableRow(file_id=2, context_id=9, lineno=53),
    LineTableRow(file_id=2, context_id=10, lineno=26),
    LineTableRow(file_id=2, context_id=10, lineno=27),
    LineTableRow(file_id=2, context_id=10, lineno=31),
    LineTableRow(file_id=2, context_id=10, lineno=32),
    LineTableRow(file_id=2, context_id=10, lineno=33),
    LineTableRow(file_id=2, context_id=10, lineno=34),
    LineTableRow(file_id=2, context_id=10, lineno=35),
    LineTableRow(file_id=2, context_id=10, lineno=36),
    LineTableRow(file_id=2, context_id=10, lineno=37),
    LineTableRow(file_id=2, context_id=10, lineno=38),
    LineTableRow(file_id=2, context_id=10, lineno=39),
    LineTableRow(file_id=2, context_id=10, lineno=40),
    LineTableRow(file_id=2, context_id=10, lineno=41),
    LineTableRow(file_id=2, context_id=10, lineno=42),
    LineTableRow(file_id=2, context_id=10, lineno=44),
    LineTableRow(file_id=2, context_id=10, lineno=45),
    LineTableRow(file_id=2, context_id=10, lineno=46),
    LineTableRow(file_id=2, context_id=10, lineno=47),
    LineTableRow(file_id=2, context_id=10, lineno=51),
    LineTableRow(file_id=2, context_id=10, lineno=52),
    LineTableRow(file_id=2, context_id=10, lineno=54),
    LineTableRow(file_id=2, context_id=10, lineno=55),
    LineTableRow(file_id=3, context_id=11, lineno=12),
    LineTableRow(file_id=3, context_id=11, lineno=23),
    LineTableRow(file_id=3, context_id=11, lineno=24),
    LineTableRow(file_id=3, context_id=11, lineno=91),
    LineTableRow(file_id=3, context_id=11, lineno=92),
    LineTableRow(file_id=3, context_id=11, lineno=15),
    LineTableRow(file_id=3, context_id=11, lineno=94),
    LineTableRow(file_id=3, context_id=11, lineno=30),
    LineTableRow(file_id=3, context_id=11, lineno=31),
    LineTableRow(file_id=3, context_id=11, lineno=37),
    LineTableRow(file_id=3, context_id=11, lineno=38),
    LineTableRow(file_id=3, context_id=11, lineno=44),
    LineTableRow(file_id=3, context_id=11, lineno=45),
    LineTableRow(file_id=3, context_id=11, lineno=51),
    LineTableRow(file_id=3, context_id=11, lineno=52),
    LineTableRow(file_id=3, context_id=11, lineno=13),
    LineTableRow(file_id=3, context_id=11, lineno=58),
    LineTableRow(file_id=3, context_id=11, lineno=59),
    LineTableRow(file_id=3, context_id=11, lineno=65),
    LineTableRow(file_id=3, context_id=11, lineno=66),
    LineTableRow(file_id=3, context_id=11, lineno=72),
    LineTableRow(file_id=3, context_id=11, lineno=73),
    LineTableRow(file_id=3, context_id=11, lineno=79),
    LineTableRow(file_id=3, context_id=11, lineno=80),
    LineTableRow(file_id=3, context_id=11, lineno=14),
    LineTableRow(file_id=3, context_id=11, lineno=86),
    LineTableRow(file_id=3, context_id=11, lineno=87),
    LineTableRow(file_id=3, context_id=12, lineno=12),
    LineTableRow(file_id=3, context_id=12, lineno=23),
    LineTableRow(file_id=3, context_id=12, lineno=24),
    LineTableRow(file_id=3, context_id=12, lineno=91),
    LineTableRow(file_id=3, context_id=12, lineno=94),
    LineTableRow(file_id=3, context_id=12, lineno=30),
    LineTableRow(file_id=3, context_id=12, lineno=31),
    LineTableRow(file_id=3, context_id=12, lineno=37),
    LineTableRow(file_id=3, context_id=12, lineno=38),
    LineTableRow(file_id=3, context_id=12, lineno=44),
    LineTableRow(file_id=3, context_id=12, lineno=45),
    LineTableRow(file_id=3, context_id=12, lineno=51),
    LineTableRow(file_id=3, context_id=12, lineno=52),
    LineTableRow(file_id=3, context_id=12, lineno=13),
    LineTableRow(file_id=3, context_id=12, lineno=58),
    LineTableRow(file_id=3, context_id=12, lineno=59),
    LineTableRow(file_id=3, context_id=12, lineno=65),
    LineTableRow(file_id=3, context_id=12, lineno=66),
    LineTableRow(file_id=3, context_id=12, lineno=72),
    LineTableRow(file_id=3, context_id=12, lineno=73),
    LineTableRow(file_id=3, context_id=12, lineno=79),
    LineTableRow(file_id=3, context_id=12, lineno=80),
    LineTableRow(file_id=3, context_id=12, lineno=14),
    LineTableRow(file_id=3, context_id=12, lineno=86),
    LineTableRow(file_id=3, context_id=12, lineno=87),
    LineTableRow(file_id=3, context_id=12, lineno=17),
]


def test_get_context_table():
    db_path = 'tests/data/.coverage'
    table_rows_iterator = get_context_table(db_path)
    table_rows = list(table_rows_iterator)
    assert table_rows == context_table_rows


def test_get_file_table():
    db_path = 'tests/data/.coverage'
    table_rows_iterator = get_file_table(db_path)
    table_rows = list(table_rows_iterator)
    assert table_rows == file_table_rows


def test_get_line_table():
    db_path = 'tests/data/.coverage'
    table_rows_iterator = get_line_table(db_path)
    table_rows = list(table_rows_iterator)
    assert table_rows == line_table_rows
