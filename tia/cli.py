from enum import IntEnum
from pathlib import Path
from sys import stderr

import click

from tia.cov import get_context_table, get_file_table, get_line_table
from tia.maps import get_impact_map

class ExitCode(IntEnum):
    ok = 0
    not_ok = 1


@click.group()
@click.option('-v', '--verbose', is_flag=True, help='Enables debug output on stdout.')
@click.option(
    '--config-file',
    '-c',
    type=click.Path(resolve_path=True),
    default='tia.yml',
    help='Configuration file (default: tia.yml).',
)
@click.version_option()
@click.pass_context
def cli(ctx, verbose, config_file):
    ctx.obj = {
        'verbose': verbose,
    }
    if verbose:
        print('Configuration file: {}'.format(click.format_filename(config_file)))
    config_file_path = Path(config_file)
    # validation of config file path
    if not config_file_path.is_file():
        click.echo('Configuration file {} is not existing.'.format(config_file_path), err=True)
        exit(ExitCode.not_ok)
    if config_file_path.suffix not in ['.yaml', '.yml']:
        print('Configuration file {} is no YAML file.'.format(config_file_path))
        exit(ExitCode.not_ok)


@cli.command(help='Discover impact of production code on tests. \
Specify production code file or files with [FILES]. The corresponding \
tests are provided via stdout. For impacted tests on a per file basis \
use the verbose output (option -v/--verbose).')
@click.argument('files', nargs=-1, required=False, type=click.Path(resolve_path=True), default=None)
@click.option(
    '--coverage-database',
    '-d',
    type=click.Path(resolve_path=True),
    default='.coverage',
    help='Which coverage database shall be used? (Default: .coverage)')
@click.pass_context
def impact(ctx, files, coverage_database):
    import pprint
    verbose = ctx.obj['verbose']  # get options from parent command context
    if verbose:
        if files:
            print('Production code file(s):')
            pprint.pprint(files)
        print('Coverage database:')
        print(coverage_database)
    coverage_database_path = Path(coverage_database)
    if not coverage_database_path.is_file():
        print('Database file {} is not existing.'.format(coverage_database_path), file=stderr)
        exit(ExitCode.not_ok)
    # validation if coverage database file path is a sqlite3 database later
    file_table = get_file_table(coverage_database)
    line_table = get_line_table(coverage_database)
    context_table = get_context_table(coverage_database)
    impact_map = get_impact_map(file_table, line_table, context_table, iter(files))
    if verbose:
        # impact map output on a per file basis
        print('Impact Map:')
        pprint.pprint(impact_map)
    else:
        tests = impact_map.map(lambda x: x.tests).flatten().sorted()
        print(tests)
