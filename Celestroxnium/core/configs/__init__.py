import re

from typing import Optional

from Celestroxnium.core.helpers.regex_helper import str_to_dict
from Celestroxnium.core.helpers.misc_helper import set_to_empty
from Celestroxnium.core.helpers import env_helper as _env_helper, logging_helper as _logging_helper

_env_helper._load_dotenv()

get_env = _env_helper.get_env_or_default
get_env_int = _env_helper.get_env_int_or_None
get_env_bool = _env_helper.get_env_bool_or_default

regex = re.compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*")

### REMOVE UNNCESSARY VARS / ENV CONFIGS!!
### REMOVE UNNCESSARY VARS / ENV CONFIGS!!
### REMOVE UNNCESSARY VARS / ENV CONFIGS!!
### REMOVE UNNCESSARY VARS / ENV CONFIGS!!
### REMOVE UNNCESSARY VARS / ENV CONFIGS!!

class Config:
    """
    Configuartion variables of bot:
        todo
    """

    IS_LOCAL_DEPLOY: bool = get_env_bool("IS_LOCAL_DEPLOY", False)

    MAIN_BOT_TOKEN: Optional[str] = get_env("MAIN_BOT_TOKEN")

    ALIVE_IMAGE: Optional[str] = get_env("ALIVE_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png")
    START_IMAGE: Optional[str] = get_env("START_IMAGE", False, "https://telegra.ph//file/bdacc5cdac69ea353190c.png")

    API_ID: Optional[int] = get_env_int("API_ID")
    API_HASH: Optional[str] = get_env("API_HASH")

    MAIN_SESSION: Optional[str] = get_env("MAIN_SESSION") 

    COMMAND_HANLDER_APP: str = get_env("COMMAND_HANLDER_APP", False, ".") # type: ignore
    COMMAND_HANLDER_BOT: str = get_env("COMMAND_HANLDER_BOT", False, "!") # type: ignore

    TIME_ZONE: Optional[str] = get_env("TIME_ZONE", False, "Asia/Kolkata")

    DB_CHAT_ID: int = get_env_int("DB_CHAT_ID") # type: ignore
    LOG_CHAT_ID: Optional[int] = get_env_int("LOG_CHAT_ID", False)
    START_UP_CHAT_ID: Optional[int] = get_env_int("START_UP_CHAT_ID", False)
    PLUGIN_CHANNEL_CHAT_ID: Optional[int] = get_env_int("PLUGIN_CHANNEL_CHAT_ID", False)

    START_UP_TEXT: str = get_env("START_UP_TEXT", False, "Bot has started!") # type: ignore

    SESSION_STRINGS: list[str] = get_env("SESSION_STRINGS", False, "").split(' ') # type: ignore
    BOT_TOKENS: list[str] = get_env("BOT_TOKENS", False, "").split(' ') # type: ignore
    
    SUDO_USERS: list[int] = [int(i) for i in get_env("SUDO_USERS", False, "").split(' ') if i.isdigit()] # type: ignore
    DISABLE_SUDO_USERS: bool = get_env_bool("DISABLE_SUDO_USERS", False, False)

    MAIN_MODULE_PLUGIN_NO_LOAD_APP: list[str] = get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MAIN_MODULE_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MAIN_MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore

    MODULE_PLUGIN_NO_LOAD_APP: list[str] = get_env("MODULE_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MODULE_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MODULE_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    MAIN_FUNC_PLUGIN_NO_LOAD_APP: list[str] = get_env("MAIN_FUNC_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    MAIN_FUNC_PLUGIN_NO_LOAD_BOT: list[str] = get_env("MAIN_FUNC_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    FUNC_PLUGIN_NO_LOAD_APP: list[str] = get_env("FUNC_PLUGIN_NO_LOAD_APP", False, "").split(' ') # type: ignore
    FUNC_PLUGIN_NO_LOAD_BOT: list[str] = get_env("FUNC_PLUGIN_NO_LOAD_BOT", False, "").split(' ') # type: ignore

    # For developers

    DEBUG: bool = get_env_bool("DEBUG", False)

    FORCE: bool = get_env_bool("FORCE", False)

    CUSTOM_CONFIGS_FORMAT: int = get_env_int("CUSTOM_CONFIGS_FORMAT", False) or 1

    CUSTOM_DIRECTORIES: list[str] = get_env("CUSTOM_DIRECTORIES", False, "").split(' ') # type: ignore
    CUSTOM_CONFIGS: dict[str, str] = str_to_dict(
                                            get_env("CUSTOM_CONFIGS", False, ""), # type: ignore
                                            CUSTOM_CONFIGS_FORMAT
                                        )

    FAST_LOAD: bool = get_env_bool("FAST_LOAD", False, True)

    # Conditional Statements and Fallbacks

    SESSION_STRINGS = set_to_empty(SESSION_STRINGS)
    BOT_TOKENS = set_to_empty(BOT_TOKENS)

    MAIN_MODULE_PLUGIN_NO_LOAD_APP = set_to_empty(MAIN_MODULE_PLUGIN_NO_LOAD_APP)
    MAIN_MODULE_PLUGIN_NO_LOAD_BOT = set_to_empty(MAIN_MODULE_PLUGIN_NO_LOAD_BOT)
    MODULE_PLUGIN_NO_LOAD_APP = set_to_empty(MODULE_PLUGIN_NO_LOAD_APP)
    MODULE_PLUGIN_NO_LOAD_BOT = set_to_empty(MODULE_PLUGIN_NO_LOAD_BOT)
    MAIN_FUNC_PLUGIN_NO_LOAD_APP = set_to_empty(MAIN_FUNC_PLUGIN_NO_LOAD_APP)
    MAIN_FUNC_PLUGIN_NO_LOAD_BOT = set_to_empty(MAIN_FUNC_PLUGIN_NO_LOAD_BOT)
    FUNC_PLUGIN_NO_LOAD_APP = set_to_empty(FUNC_PLUGIN_NO_LOAD_APP)
    FUNC_PLUGIN_NO_LOAD_BOT = set_to_empty(FUNC_PLUGIN_NO_LOAD_BOT)

    CUSTOM_DIRECTORIES = set_to_empty(CUSTOM_DIRECTORIES)

    # Compounds:

    ALL_SESSION_STRINGS: list[str] = [MAIN_SESSION] + SESSION_STRINGS # type: ignore
    ALL_BOT_TOKENS: list[str] = [MAIN_BOT_TOKEN] + BOT_TOKENS # type: ignore

    ALL_MODULE_PLUGIN_NO_LOAD_APP = MAIN_MODULE_PLUGIN_NO_LOAD_APP + MODULE_PLUGIN_NO_LOAD_APP
    ALL_MODULE_PLUGIN_NO_LOAD_BOT = MAIN_MODULE_PLUGIN_NO_LOAD_BOT + MODULE_PLUGIN_NO_LOAD_BOT

    ALL_FUNC_PLUGIN_NO_LOAD_APP = MAIN_FUNC_PLUGIN_NO_LOAD_APP + FUNC_PLUGIN_NO_LOAD_APP
    ALL_FUNC_PLUGIN_NO_LOAD_BOT = MAIN_FUNC_PLUGIN_NO_LOAD_BOT + FUNC_PLUGIN_NO_LOAD_BOT

    # Post Start-Up Variables:

    # TODO = ""?

    # Testing purposes:

    TEST: str = "?"