import subprocess
import os

class BaseSkill:
    """
    Base class for skills.  This is a placeholder and you should replace it 
    with your actual base class if you have one.
    """
    async def run(self, **kwargs):
        raise NotImplementedError


class Skill_open_discord(BaseSkill):
    """
    Opens Discord.
    """
    async def run(self, **kwargs):
        """
        Opens Discord using the default application.

        Returns:
            bool: True if Discord was successfully opened, False otherwise.
        """
        try:
            #Attempt to find Discord in common locations
            discord_path = None
            if os.name == 'nt': #Windows
                discord_path =  subprocess.check_output(['where', 'discord']).decode().strip()
            elif os.name == 'posix': #Linux/macOS
                discord_path = subprocess.check_output(['which', 'discord']).decode().strip()

            if discord_path:
                subprocess.Popen([discord_path])
                return True
            else:
                #Fallback: try to open a URL, less reliable
                import webbrowser
                webbrowser.open("https://discord.com/app")
                return True #Consider this a success even if not opened via app

        except FileNotFoundError:
            return False
        except subprocess.CalledProcessError:
            return False
        except Exception as e: #Catch other potential errors
            print(f"An error occurred while opening Discord: {e}")
            return False
