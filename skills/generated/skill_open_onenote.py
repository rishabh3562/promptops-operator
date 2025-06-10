import subprocess
import os

class BaseSkill:  # Dummy BaseSkill class for inheritance
    pass


class Skill_open_onenote(BaseSkill):
    async def run(self, **kwargs):
        """Opens OneNote."""
        try:
            onenote_path = self._find_onenote_path()
            if onenote_path:
                subprocess.Popen([onenote_path])
                return True
            else:
                return False  # OneNote not found
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def _find_onenote_path(self):
        """Attempts to find the OneNote executable path."""
        # Adjust paths as needed for different operating systems
        potential_paths = [
            r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE",  #Example Windows Path. Adjust as needed.
            r"C:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE", #Example Windows Path. Adjust as needed.

            # Add more paths for other locations or operating systems.

        ]
        for path in potential_paths:
            if os.path.exists(path):
                return path
        return None
