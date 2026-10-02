"""Refresh provider."""

import xbmcaddon
import xbmcvfs
from lib.providers.abstract_orange_provider import AbstractOrangeProvider

profile_path = xbmcaddon.Addon().getAddonInfo("profile")
pinia_file = f"{profile_path}__pinia.json"
config_file = f"{profile_path}__config.json"
xbmcvfs.delete(pinia_file)
xbmcvfs.delete(config_file)
AbstractOrangeProvider()
