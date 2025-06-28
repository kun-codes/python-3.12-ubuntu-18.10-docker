# Python 3.12 Ubuntu 18.10 Docker Image with Automated Patch Updates

[![Docker Pulls](https://img.shields.io/docker/pulls/kuncodes/python-3.12-ubuntu-18.10)](https://hub.docker.com/r/kuncodes/python-3.12-ubuntu-18.10)

This repository provides a Dockerfile for building a Python 3.12 environment on Ubuntu 18.10. It also includes automation to keep the Python 3.12 patch version up to date using GitHub Actions.

## Docker Image
The prebuilt image is available on Docker Hub: [kuncodes/python-3.12-ubuntu-18.10](https://hub.docker.com/r/kuncodes/python-3.12-ubuntu-18.10)

Pull it directly with:
```sh
docker pull kuncodes/python-3.12-ubuntu-18.10
```

## Why This Image?
This image is designed for compiling Python binaries with [Nuitka](https://nuitka.net/) on an older Ubuntu base. Using Ubuntu 18.10 ensures compatibility with older versions of glibc, making the resulting binaries runnable on a wider range of Linux distributions, including older ones.

## Features
- **Dockerfile**: Builds Python 3.12 on Ubuntu 18.10.
- **Automated Patch Updates**: A GitHub Actions workflow (`update-python-patch.yml`) runs daily to check for the latest Python 3.12.x patch release and updates the Dockerfile accordingly.
- **Pull Request Automation**: When a new patch is detected, the workflow automatically commits the change and opens a pull request.

## Usage
### Build the Docker Image
```sh
docker build -t python:3.12-ubuntu18.10 .
```

### Run the Docker Image
```sh
docker run -it python:3.12-ubuntu18.10 python --version
```

### Example: Compile with Nuitka for Maximum Compatibility
You can use this image to compile your Python scripts with Nuitka, ensuring the resulting binaries are compatible with older Linux distributions:

```sh
docker run --rm -v "$PWD:/src" -w /src python:3.12-ubuntu18.10 \
    nuitka --onefile your_script.py
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
