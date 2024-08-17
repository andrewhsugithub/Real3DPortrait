# Installation issues
1. when installing pyaudio, portaudio.h not found
solution: https://stackoverflow.com/a/51992497
```bash
conda config --add channels conda-forge 
conda install pyaudio
```
2. ERROR: CMake must be installed to build dlib
solution: https://github.com/davisking/dlib/issues/2943#issuecomment-2080361339
```bash
pip install cmake==3.25.2
pip install dlib==19.24.2
```

3. ERROR: pip's dependency resolver does not currently take into account all the packages that are installed.
```bash
pip install <package_name> --use-deprecated=legacy-resolver
```