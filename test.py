from TTS.tts.utils.text.phonemizers.multi_phonemizer import MultiPhonemizer

if __name__ == "__main__":
    texts = {
        "tr": "Merhaba, bu Türkçe bit örnek!",
        "en-us": "Hello, this is English example!",
        "de": "Hallo, das ist ein Deutches Beipiel!",
        "zh-cn": "这是中国的例子",
    }
    phonemes = {}
    ph = MultiPhonemizer({"tr": "espeak", "en-us": "", "de": "gruut", "zh-cn": ""})
    for lang, text in texts.items():
        phoneme = ph.phonemize(text=text, language=lang)
        phonemes[lang] = phoneme
    print(phonemes)