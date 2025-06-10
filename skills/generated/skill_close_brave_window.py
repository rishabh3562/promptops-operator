from promptops.skills.base import BaseSkill
import os
import subprocess

class Skill_close_brave_window(BaseSkill):
    async def run(self, **kwargs):
        try:
            # Find Brave windows using wmctrl (requires wmctrl to be installed)
            process = subprocess.run(['wmctrl', '-l'], capture_output=True, text=True, check=True)
            brave_windows = [line.split()[0] for line in process.stdout.splitlines() if "brave" in line.lower()]

            # Close each Brave window
            for window_id in brave_windows:
                subprocess.run(['wmctrl', '-c', window_id], check=True)

            return True
        except FileNotFoundError:
            print("Error: wmctrl not found. Please install it.")
            return False
        except subprocess.CalledProcessError as e:
            print(f"Error closing Brave window: {e}")
            return False
