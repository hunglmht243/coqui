from viphoneme import vi2IPA

def vietnamese_text_to_phonemes(text: str) -> str:
    phoneme = vi2IPA(text)
    return phoneme
