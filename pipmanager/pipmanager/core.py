import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipManager:
    @staticmethod
    def list_packages():
        """List all installed pip packages."""
        logging.info("Fetching the list of installed packages...")
        subprocess.run([sys.executable, "-m", "pip", "list"])

    @staticmethod
    def check_updates():
        """Check for outdated pip packages."""
        logging.info("Checking for outdated packages...")
        subprocess.run([sys.executable, "-m", "pip", "list", "--outdated"])

    @staticmethod
    def install_package(package_name):
        """Install a package using pip."""
        logging.info(f"Installing package: {package_name}")
        result = subprocess.run([sys.executable, "-m", "pip", "install", package_name], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Successfully installed {package_name}.")
        else:
            logging.error(f"Failed to install {package_name}.\nError: {result.stderr}")

    @staticmethod
    def uninstall_package(package_name):
        """Uninstall a package using pip."""
        logging.info(f"Uninstalling package: {package_name}")
        result = subprocess.run([sys.executable, "-m", "pip", "uninstall", package_name, "-y"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Successfully uninstalled {package_name}.")
        else:
            logging.error(f"Failed to uninstall {package_name}.\nError: {result.stderr}")

    @staticmethod
    def upgrade_all():
        """Upgrade all outdated packages."""
        logging.info("Upgrading all outdated packages...")
        result = subprocess.run([sys.executable, "-m", "pip", "list", "--outdated", "--format=freeze"], capture_output=True, text=True)
        outdated = result.stdout.splitlines()

        if not outdated:
            logging.info("All packages are up to date.")
            return

        for line in outdated:
            package = line.split("==")[0]
            logging.info(f"Upgrading {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package])
