# click-next

Clicks the dark (enabled) **NEXT >** button on a web page, ignoring the light-gray
(disabled) one.

## Bookmarklet (no install)

Waits for the Next button to turn dark, clicks it once, and changes the tab title to
**CLICKED NEXT**.

1. In Edge press **Ctrl+Shift+O**, then **Add favorite**. Name it `Click Next` and paste
   the code below as the URL.
2. On the page with the gray Next button, click the favorite. The tab title changes to
   **Watching for Next...**
3. If clicking Next loads a new page, click the favorite again there.

```
javascript:(()=>{const f=()=>{const ds=[document];for(const i of document.querySelectorAll('iframe'))try{if(i.contentDocument)ds.push(i.contentDocument)}catch(x){}for(const d of ds)for(const e of d.querySelectorAll('button,a,[role="button"]')){if(!/^\s*next\s*[>\u203a]?\s*$/i.test(e.textContent)||e.disabled||e.getAttribute('aria-disabled')==='true')continue;const[r,g,b]=d.defaultView.getComputedStyle(e).color.match(/\d+/g).map(Number);if((r*299+g*587+b*114)/1000<140)return e}};const t=setInterval(()=>{const e=f();if(e){clearInterval(t);e.click();document.title='CLICKED NEXT'}},1000);document.title='Watching for Next...'})()
```

If favorites can't run scripts, press **F12**, open **Console**, and paste the code
without the leading `javascript:`.

## Playwright script (Windows, needs install rights)

1. Download: **Code > Download ZIP**, then extract it.
2. Double-click `run.bat` and enter the page URL when asked.
   Or from a terminal: `run.bat https://example.com/page`

The first run installs [uv](https://docs.astral.sh/uv/), which downloads Python and
Playwright. The browser used is the Edge already on Windows. Machines that block `.bat`
files or user-installed programs can't run this; use the bookmarklet instead.
