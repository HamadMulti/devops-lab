import subprocess
from pipmanager.manager import PipManager
from unittest.mock import patch

class TestPipManager:

    @patch('subprocess.run')
    def test_list_packages(self, mock_subprocess):
        mock_subprocess.return_value.stdout = "package1 1.0.0\npackage2 2.0.0\n"
        result = PipManager.list_packages()
        assert result == "package1 1.0.0\npackage2 2.0.0\n"

    @patch('subprocess.run')
    def test_check_updates(self, mock_subprocess):
        mock_subprocess.return_value.stdout = "package1 1.0.0 1.1.0\npackage2 2.0.0 2.1.0\n"
        result = PipManager.check_updates()
        assert result == "package1 1.0.0 1.1.0\npackage2 2.0.0 2.1.0\n"

    @patch('subprocess.run')
    def test_install_package(self, mock_subprocess):
        mock_subprocess.return_value.stdout = "Successfully installed example-package"
        result = PipManager.install_package("example-package")
        assert result == "Successfully installed example-package"

    @patch('subprocess.run')
    def test_uninstall_package(self, mock_subprocess):
        mock_subprocess.return_value.stdout = "Successfully uninstalled example-package"
        result = PipManager.uninstall_package("example-package")
        assert result == "Successfully uninstalled example-package"

    @patch('subprocess.run')
    def test_upgrade_all(self, mock_subprocess):
        mock_subprocess.side_effect = [
            # First call to list outdated packages
            subprocess.CompletedProcess(args=["pip", "list", "--outdated"], returncode=0, stdout="package1 1.0.0 1.1.0\n"),
            # Next calls for upgrading packages
            subprocess.CompletedProcess(args=["pip", "install", "--upgrade", "package1"], returncode=0, stdout="Successfully upgraded package1")
        ]
        result = PipManager.upgrade_all()
        assert result == "Successfully upgraded package1"
