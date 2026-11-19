@echo off
rem Runs click_next.py. Installs uv (which fetches Python and Playwright) on first run.
cd /d "%~dp0"
where uv >nul 2>&1
if errorlevel 1 (
  powershell -NoProfile -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
  set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)
uv run click_next.py %*
pause
