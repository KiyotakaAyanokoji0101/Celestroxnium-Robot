from os import getenv as _getenv
from dotenv import load_dotenv as _load_dotenv

from Celestroxnium.core.helpers.logging_helper import info as _info, error as _error, warn as _warn

def load_env() -> bool:
    """
    Loads '.env' variables.
    """
    return _load_dotenv()

def get_env_or_default(env: str, is_essential: bool = True, default = None, silence: bool = False):
    """
    If `is_essential` is set to `True` (by default) it will inform and exit the program.
    Otherwise if it is set to `False` it will inform and would return the `default` argument.
    """
    if env_vale := _getenv(env, default):
        if env_vale == default:
            _warn(f"Environment variable '{env}' couldn't be found. Using defaults.", silence = silence)
        else:
            _info(f"Environment variable '{env}' found.", silence = silence)

        return env_vale

    if is_essential:
        if not silence:
            _error(f"Environment variable '{env} couldn't be found. Exitting...")

        quit()

    _warn(f"Environment variable '{env}' couldn't be found. Skipping...", silence = silence)
    return default

def get_env_int_or_None(env: str, is_essential: bool = True, silence: bool = False) -> int|None:
    """
    Returns integer from the environmental variables if valid else, it returns `None`.
    """
    value: str|None = get_env_or_default(env, False, silence = True)

    if value:
        if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
            _info(f"Environment variable '{env}' found.", silence = silence)
            return int(value)

        _warn(f"Environment variable '{env}' isn't numeric. Skipping...", silence = silence)
        return None

    if is_essential:
        _error(f"Environment variable '{env} couldn't be found. Exitting...", silence = silence)
        quit()

def get_env_bool_or_default(env: str, is_essential: bool = True, default: bool = False, silence: bool = False) -> bool:
    """
    Returns boolean `True` or `False`. If `None` then `default` argument is returned.
    """
    if env_value := _getenv(env):
        _info(f"Environment variable '{env}' found.", silence = silence)
        return env_value == "True"

    if is_essential:
       _error(f"Environment variable '{env}' couldn't be found. Exitting...", silence = silence)
       exit()

    return default
