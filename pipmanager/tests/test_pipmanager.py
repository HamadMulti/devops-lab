import subprocess
import pytest
from pipmanager.core import PipManager

@pytest.fixture
def mock_subprocess_run(mocker):
    """Fixture to mock subprocess.run."""
    return mocker.patch("subprocess.run")

def test_list_packages(mock_subprocess_run):
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=["pip", "list"], returncode=0, stdout="package1 1.0.0\npackage2 2.0.0\n"
    )
    result = PipManager.list_packages()
    assert result == "package1 1.0.0\npackage2 2.0.0\n"

def test_check_updates(mock_subprocess_run):
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=["pip", "list", "--outdated"],
        returncode=0,
        stdout="package1 1.0.0 1.1.0\npackage2 2.0.0 2.1.0\n",
    )
    result = PipManager.check_updates()
    assert result == "package1 1.0.0 1.1.0\npackage2 2.0.0 2.1.0\n"

def test_install_package(mock_subprocess_run):
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=["pip", "install", "example-package"],
        returncode=0,
        stdout="Successfully installed example-package",
    )
    result = PipManager.install_package("example-package")
    assert result == "Successfully installed example-package"

def test_uninstall_package(mock_subprocess_run):
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=["pip", "uninstall", "-y", "example-package"],
        returncode=0,
        stdout="Successfully uninstalled example-package",
    )
    result = PipManager.uninstall_package("example-package")
    assert result == "Successfully uninstalled example-package"

def test_upgrade_all(mock_subprocess_run):
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=["pip", "list", "--outdated"],
        returncode=0,
        stdout="package1 1.0.0 1.1.0\npackage2 2.0.0 2.1.0\n",
    )
    mock_subprocess_run.side_effect = [
        subprocess.CompletedProcess(
            args=["pip", "install", "--upgrade", "package1"],
            returncode=0,
            stdout="Successfully upgraded package1",
        ),
        subprocess.CompletedProcess(
            args=["pip", "install", "--upgrade", "package2"],
            returncode=0,
            stdout="Successfully upgraded package2",
        ),
    ]
    result = PipManager.upgrade_all()
    assert result == "Successfully upgraded package1\nSuccessfully upgraded package2"
