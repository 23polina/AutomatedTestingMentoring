import re
from pathlib import Path

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class ScreenshotListener:
    """Takes a screenshot after every keyword that has the 'screenshot' tag"""

    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, tag="screenshot"):
        self.ROBOT_LIBRARY_LISTENER = self
        self.tag = tag.lower()
        self.counter = 0
        logger.console(f"[ScreenshotListener] loaded, tag='{self.tag}'")

    def end_keyword(self, data, result):
        tags = [str(t).lower() for t in result.tags]
        if self.tag not in tags:
            return
        logger.console(f"[ScreenshotListener] screenshot for: {result.name}")
        try:
            builtin = BuiltIn()
            selenium = builtin.get_library_instance("SeleniumLibrary")
            output_dir = Path(builtin.get_variable_value("${OUTPUT DIR}"))
            target_dir = output_dir / "screenshots"
            target_dir.mkdir(parents=True, exist_ok=True)

            self.counter += 1
            safe_name = re.sub(r"[^A-Za-z0-9]+", "_", result.name).strip("_")
            filename = f"{self.counter:03d}_{safe_name}_{result.status}.png"
            selenium.capture_page_screenshot(str(target_dir / filename))
        except Exception as error:
            logger.console(f"[ScreenshotListener] ERROR: {error}")
