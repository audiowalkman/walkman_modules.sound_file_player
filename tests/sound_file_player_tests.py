import typing

import walkman
from walkman_modules import sound_file_players


class SoundFilePlayerTest(walkman.unit_tests.ModuleTestCase):
    def get_module_class(self) -> typing.Type[walkman.Module]:
        return sound_file_players.SoundFilePlayer

    def get_module_instance(
        self,
        module_class: typing.Optional[typing.Type[walkman.Module]] = None,
        **kwargs
    ) -> walkman.Module:
        return super().get_module_instance(
            module_class=module_class,
            default_dict={"path": "tests/test.wav"},
            **kwargs
        )
