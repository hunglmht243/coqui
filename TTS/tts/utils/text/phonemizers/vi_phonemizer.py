from typing import Dict

from TTS.tts.utils.text.vietnamese.phonemizer import vietnamese_text_to_phonemes
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_JA_PUNCS = "、.,[]()?!〽~『』「」【】"

_TRANS_TABLE = {"、": ","}


def trans(text):
    for i, j in _TRANS_TABLE.items():
        text = text.replace(i, j)
    return text


class VI_Phonemizer(BasePhonemizer):
    """🐸TTS Ja-Jp phonemizer using functions in `TTS.tts.utils.text.japanese.phonemizer`

    TODO: someone with JA knowledge should check this implementation

    Example:

        >>> from TTS.tts.utils.text.phonemizers import JA_JP_Phonemizer
        >>> phonemizer = JA_JP_Phonemizer()
        >>> phonemizer.phonemize("どちらに行きますか？", separator="|")
        'd|o|c|h|i|r|a|n|i|i|k|i|m|a|s|u|k|a|?'

    """

    language = "vi"

    def __init__(self, punctuations=_DEF_JA_PUNCS, keep_puncs=True, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "vi_phonemizer"

    def _phonemize(self, text: str, separator: str = "|") -> str:
        ph = vietnamese_text_to_phonemes(text)
        if separator is not None or separator != "":
            return separator.join(ph)
        return ph

    def phonemize(self, text: str, separator="|", language=None) -> str:
        """Custom phonemize for JP_JA

        Skip pre-post processing steps used by the other phonemizers.
        """
        return self._phonemize(text, separator)

    @staticmethod
    def supported_languages() -> Dict:
        return {"vi": "Vietnamese (Vietnam)"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True


if __name__ == "__main__":
    text = "hôm nay trời đẹp vãi lồn"
    e = VI_Phonemizer()
    print(e.supported_languages())
    print(e.version())
    print(e.language)
    print(e.name())
    print(e.is_available())
    print(e.phonemize(text))
