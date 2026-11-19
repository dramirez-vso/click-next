# click-next

Opens a web page in Microsoft Edge and clicks the dark (enabled) **NEXT >** button,
ignoring the light-gray (disabled) one.

## Use (Windows)

1. Download: **Code > Download ZIP**, then extract it.
2. Double-click `run.bat` and enter the page URL when asked.
   Or from a terminal: `run.bat https://example.com/page`

The first run installs [uv](https://docs.astral.sh/uv/), which downloads Python and
Playwright. Later runs start immediately. The browser used is the Edge already on Windows.
