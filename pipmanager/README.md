# `pipmanager`

**`pipmanager`** is a Python library and command-line tool that simplifies managing Python packages using `pip`. It allows you to list installed packages, check for outdated ones, install or uninstall packages, and upgrade all outdated packages.

## Features

- **List Installed Packages**: Quickly view all installed Python packages.
- **Check for Outdated Packages**: Identify which packages have updates available.
- **Install a Package**: Easily install any Python package by name.
- **Uninstall a Package**: Remove any installed package with a single command.
- **Upgrade All Outdated Packages**: Automatically upgrade all outdated packages in one go.
- **Command-Line Interface (CLI)**: Manage packages directly from your terminal.
- **Library for Automation**: Use it programmatically in Python scripts.

## Setting Up a Virtual Environment

Using a virtual environment is recommended to isolate project dependencies and avoid conflicts.

### Steps:

1. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

   This creates a directory named `venv` that contains the virtual environment.

2. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install All Dependencies**:
   Install both runtime and development dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Verify the Setup**:
   Ensure all dependencies are installed:
   ```bash
   pip list
   ```

### Requirements Files

Include the following requirements files for runtime and development dependencies.

#### **`requirements.txt`** (Runtime Dependencies)

```plaintext
click==8.1.3
```

#### **`requirements-dev.txt`** (Development Dependencies)

```plaintext
pytest==7.4.0
pytest-mock==3.10.0
pylint==2.17.5
```

## Installation

### From PyPI

To install the latest version from PyPI:

```bash
pip install pipmanager
```

### From Source

If you're working with the source code, navigate to the project directory and install it locally:

```bash
pip install .
```

## Usage

### Command-Line Interface (CLI)

Once installed, you can use the `pipmanager` command directly from your terminal.

#### Commands:

1. **List Installed Packages**

   ```bash
   pipmanager list
   ```

   Displays all currently installed Python packages.

2. **Check for Outdated Packages**

   ```bash
   pipmanager outdated
   ```

   Lists all packages with available updates.

3. **Install a Package**

   ```bash
   pipmanager install --package <package_name>
   ```

   Example:

   ```bash
   pipmanager install --package requests
   ```

   Installs the `requests` package.

4. **Uninstall a Package**

   ```bash
   pipmanager uninstall --package <package_name>
   ```

   Example:

   ```bash
   pipmanager uninstall --package requests
   ```

   Uninstalls the `requests` package.

5. **Upgrade All Outdated Packages**
   ```bash
   pipmanager upgrade-all
   ```
   Upgrades all outdated packages to their latest versions.

### Library Usage

You can also use `pipmanager` programmatically in your Python scripts:

#### Example Script:

```python
from pipmanager import PipManager

# List installed packages
PipManager.list_packages()

# Check for outdated packages
PipManager.check_updates()

# Install a specific package
PipManager.install_package("numpy")

# Uninstall a specific package
PipManager.uninstall_package("numpy")

# Upgrade all outdated packages
PipManager.upgrade_all()
```

## How It Works

- `pipmanager` uses Python’s `subprocess` module to run `pip` commands behind the scenes.
- Output from commands is displayed in the terminal, ensuring a user-friendly experience.

## Error Handling

- If you provide an invalid package name, `pipmanager` will display an error message.
- The library ensures that all commands are safe and idempotent:
  - Reinstalling an already installed package won't cause issues.
  - Uninstalling a non-existent package will return a clear error.

## Contributing

We welcome contributions to `pipmanager`! Follow these steps to contribute:

1. Fork the repository on GitHub.
2. Clone your fork:

   ```bash
   git clone https://github.com/HamadMulti/devops-lab.git
   ```

3. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
6. Make changes and write tests.
7. Push your branch:
   ```bash
   git push origin feature/your-feature
   ```
8. Open a pull request on the main repository.

## Testing

To run the tests, use the following command:

```bash
pytest tests/
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Examples

### CLI Example

```bash
# Check installed packages
pipmanager list

# Check outdated packages
pipmanager outdated

# Install Flask
pipmanager install --package flask

# Uninstall Flask
pipmanager uninstall --package flask

# Upgrade all outdated packages
pipmanager upgrade-all
```

### Python Script Example

```python
from pipmanager import PipManager

# Check for updates
PipManager.check_updates()

# Install Flask
PipManager.install_package("flask")

# Upgrade all outdated packages
PipManager.upgrade_all()
```

## Release Workflow

The `main` branch always contains the production-ready code. Releases follow this workflow:

1. Create a release branch from `master`:
   ```bash
   git checkout -b release/<version-number> master
   ```
2. Finalize release details (update version, changelog, etc.).
3. Merge the release branch into `main` and tag it:
   ```bash
   git checkout main
   git merge release/<version-number>
   git tag -a v<version-number> -m "Release <version-number>"
   git push origin main --tags
   ```
4. Merge the release branch back into `master`:
   ```bash
   git checkout develop
   git merge release/<version-number>
   git push origin develop
   ```

## Future Enhancements

- Add support for virtual environments.
- Enable rollback of package changes.
- Improve support for dependency resolution.

## Support

For any questions or issues, feel free to:

- Open a GitHub issue in the repository.
- Contact the maintainers directly.
