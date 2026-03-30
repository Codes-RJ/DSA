#!/usr/bin/env python3
"""
Setup script for DSA Repository
This script helps set up the development environment for the DSA repository.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def setup_virtual_environment():
    """Create and activate virtual environment."""
    venv_path = Path("venv")
    
    if not venv_path.exists():
        print("📦 Creating virtual environment...")
        if not run_command(f"{sys.executable} -m venv venv", "Virtual environment creation"):
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Determine activation script
    if os.name == 'nt':  # Windows
        activate_script = venv_path / "Scripts" / "activate"
        pip_command = venv_path / "Scripts" / "pip"
    else:  # Unix-based
        activate_script = venv_path / "bin" / "activate"
        pip_command = venv_path / "bin" / "pip"
    
    print(f"📝 To activate the virtual environment, run:")
    if os.name == 'nt':
        print(f"   venv\\Scripts\\activate")
    else:
        print(f"   source venv/bin/activate")
    
    return str(pip_command)


def install_dependencies(pip_command):
    """Install Python dependencies."""
    print("📚 Installing Python dependencies...")
    
    # Upgrade pip first
    if not run_command(f"{pip_command} install --upgrade pip", "Pip upgrade"):
        return False
    
    # Install requirements
    if not run_command(f"{pip_command} install -r requirements.txt", "Dependencies installation"):
        return False
    
    return True


def setup_git_hooks():
    """Set up git hooks for pre-commit."""
    print("🪝 Setting up git hooks...")
    
    # Install pre-commit hooks if pre-commit is available
    if run_command("pre-commit --version", "Check pre-commit"):
        return run_command("pre-commit install", "Pre-commit hooks installation")
    else:
        print("⚠️  Pre-commit not available. Install with: pip install pre-commit")
        return True


def setup_documentation():
    """Set up MkDocs documentation."""
    print("📖 Setting up documentation...")
    
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("❌ docs directory not found")
        return False
    
    # Change to docs directory and setup
    original_dir = os.getcwd()
    try:
        os.chdir(docs_dir)
        
        # Install docs requirements
        if not run_command("pip install -r requirements.txt", "Docs dependencies"):
            return False
        
        # Build documentation to verify setup
        if not run_command("mkdocs build", "Documentation build"):
            return False
        
        print("🌐 Documentation setup completed!")
        print("   To serve documentation locally: cd docs && mkdocs serve")
        print("   Documentation will be available at: http://127.0.0.1:8000")
        
        return True
        
    finally:
        os.chdir(original_dir)


def verify_installations():
    """Verify that key tools are installed."""
    print("🔍 Verifying installations...")
    
    tools = [
        ("g++", "C++ compiler"),
        ("javac", "Java compiler"),
        ("python", "Python interpreter"),
        ("pip", "Python package manager"),
    ]
    
    all_good = True
    for tool, description in tools:
        if run_command(f"{tool} --version", f"Check {description}"):
            print(f"✅ {description} is available")
        else:
            print(f"⚠️  {description} may not be installed or not in PATH")
            all_good = False
    
    return all_good


def main():
    """Main setup function."""
    print("🚀 DSA Repository Setup Script")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup virtual environment
    pip_command = setup_virtual_environment()
    if not pip_command:
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies(pip_command):
        sys.exit(1)
    
    # Setup git hooks
    setup_git_hooks()
    
    # Setup documentation
    setup_documentation()
    
    # Verify installations
    verify_installations()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Start exploring the repository")
    print("3. For documentation: cd docs && mkdocs serve")
    print("4. Happy coding! 🚀")


if __name__ == "__main__":
    main()
