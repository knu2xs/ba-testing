:: Variables
SETLOCAL
SET CONDA_DIR="%~dp0env"

:: Jump to command
GOTO %1

:: jupyter lab
:jupyter
    ENDLOCAL & (
        CALL conda run -p %CONDA_DIR% jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token=""
    )
    GOTO end

:: run pytests
:tests
    ENDLOCAL & (
        CALL conda run -p %CONDA_DIR% pytest ./testing
    )
    GOTO end

:end
    EXIT /B