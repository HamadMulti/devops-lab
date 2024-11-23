import argparse
from pipmanager import PipManager

def main():
    parser = argparse.ArgumentParser(description="A tool to manage pip packages.")
    parser.add_argument("command", choices=["list", "outdated", "install", "uninstall", "upgrade-all"],
                        help="Command to execute")
    parser.add_argument("--package", "-p", help="Package name (for install/uninstall commands)")
    
    args = parser.parse_args()
    manager = PipManager()

    if args.command == "list":
        manager.list_packages()
    elif args.command == "outdated":
        manager.check_updates()
    elif args.command == "install":
        if not args.package:
            print("Error: --package is required for install command.")
        else:
            manager.install_package(args.package)
    elif args.command == "uninstall":
        if not args.package:
            print("Error: --package is required for uninstall command.")
        else:
            manager.uninstall_package(args.package)
    elif args.command == "upgrade-all":
        manager.upgrade_all()

if __name__ == "__main__":
    main()
