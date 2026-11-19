# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright>=1.40"]
# ///
"""Open a page in Microsoft Edge and click the dark (enabled) "NEXT >" button,
skipping the light-gray (disabled) one."""
import sys

from playwright.sync_api import sync_playwright

# Text brightness below this counts as "dark" (0 = black, 255 = white).
# The dark button is roughly #555, the light one roughly #bbb.
DARK_THRESHOLD = 140

# Runs in the page: finds a dark, enabled element whose text is "Next" and tags it.
FIND_DARK_NEXT = """(threshold) => {
  for (const el of document.querySelectorAll('button, a, [role="button"]')) {
    if (!/^\\s*next\\s*[>\\u203a]?\\s*$/i.test(el.textContent)) continue;
    if (el.disabled || el.getAttribute('aria-disabled') === 'true') continue;
    const [r, g, b] = getComputedStyle(el).color.match(/\\d+/g).map(Number);
    if ((r * 299 + g * 587 + b * 114) / 1000 < threshold) {
      el.setAttribute('data-pw-dark-next', '');
      return true;
    }
  }
  return false;
}"""


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else input("Page URL: ").strip()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
        page.goto(url)

        # Wait up to 30s for the dark Next button to appear, then click it.
        page.wait_for_function(FIND_DARK_NEXT, arg=DARK_THRESHOLD, timeout=30_000)
        page.click("[data-pw-dark-next]")
        input("Clicked the dark Next button. Press Enter to close the browser.")
        browser.close()


if __name__ == "__main__":
    main()
