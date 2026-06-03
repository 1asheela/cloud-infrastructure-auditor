from cli.commands import run_scan
def test_scan():
    result = run_scan()
    assert result is not None