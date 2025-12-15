# Changelog
All notable changes to this project will be documented in this file.

The format is based on *Keep a Changelog*  
and this project follows *Semantic Versioning*.

---

## [0.2.0-beta] – 2025-12-15

### Added
- Colorized terminal output using ANSI escape codes (INFO, WARN, ERROR)
- Helper functions for formatted output (`INFO()`, `WARN()`, `ERROR()`)
- Sample file (`samplefile.txt`) to detect encryption/decryption state
- Case-insensitive username check to support Windows domain accounts
- Cross-platform path handling using `os.path.join()`
- Automatic creation of `Locker` directory if missing

### Changed
- Replaced recursive main menu calls with a `while True` loop
- Improved menu structure and option handling
- Refactored locker file listing into `list_locker()`
- User authentication now uses `getpass.getuser()` instead of `os.getlogin()`
- Improved error messages for encryption/decryption failures
- Standardized log output format across the program

### Fixed
- Potential recursion overflow caused by self-calling menu functions
- Duplicate file listing caused by not clearing `Locker_directory_files`
- Platform-dependent directory creation using `os.system`
- Path handling issues on non-Windows systems

### Security
- Prevented accidental double encryption/decryption by adding state checks
- Improved handling of permission-related file access errors

### Known Issues
- Encryption and decryption logic contains duplicated code
- Files are overwritten directly without temporary backup
- Encryption state detection depends on `samplefile.txt`
- Global variables are still used throughout the codebase

---

## [0.1.0-alpha] – Initial Release

### Added
- Basic file encryption and decryption using Fernet (symmetric encryption)
- User-based execution restriction
- Key generation and keyfile support
- Automatic locker directory scanning
- Interactive command-line interface

### Notes
- Early alpha release intended for learning and testing purposes only
- Not recommended for use on important data
