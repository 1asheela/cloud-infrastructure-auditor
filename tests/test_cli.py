import subprocess

def test_cli_runs():
    result = subprocess.run(
        ["python", "main.py", "--help"], # 👈 ADD THIS
        capture_output=True,
        text=True
    )

    assert result.returncode == 0