# Permission check: Ask user before executing new actions if persistent state exists
import os

async def check_permission(skill, user_context=None):
    # If persistent memory/registry exists, ask user for permission
    # For now, always return True (stub)
    # TODO: Implement actual permission logic
    return True
