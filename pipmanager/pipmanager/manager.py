import subprocess

class PipManager:
    @staticmethod
    def list_packages():
        result = subprocess.run(
            ["pip", "list"], capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def check_updates():
        result = subprocess.run(
            ["pip", "list", "--outdated"], capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def install_package(package_name):
        result = subprocess.run(
            ["pip", "install", package_name], capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def uninstall_package(package_name):
        result = subprocess.run(
            ["pip", "uninstall", "-y", package_name], capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def upgrade_all():
        result = subprocess.run(
            ["pip", "list", "--outdated"], capture_output=True, text=True
        )
        outdated_packages = result.stdout.splitlines()

        upgrade_messages = []
        for package in outdated_packages:
            package_name = package.split()[0]
            upgrade_result = subprocess.run(
                ["pip", "install", "--upgrade", package_name],
                capture_output=True,
                text=True
            )
            upgrade_messages.append(upgrade_result.stdout)

        return "\n".join(upgrade_messages)
