from nonebot.plugin import PluginMetadata
from nonebot.plugin.manager import PluginLoader

if isinstance(globals()["__loader__"], PluginLoader):
    from .utils import on_startup

    on_startup()

    from . import plugins  # noqa: F401

from .version import VERSION, __version__  # noqa: F401

__plugin_meta__ = PluginMetadata(
    name="haruka_bot_re",
    description="将B站UP主的动态和直播信息推送至QQ",
    usage="https://github.com/GrandDuke1106/HarukaBot-Re",
    homepage="https://github.com/GrandDuke1106/HarukaBot-Re",
    type="application",
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "GrandDuke1106",
        "version": __version__,
        "priority": 1,
    },
)
