from viphoneme import vi2IPA
from unidecode import unidecode

def vietnamese_text_to_phonemes(text: str) -> str:
    text=unidecode(text)
    phoneme = vi2IPA(text)
    
    return phoneme
