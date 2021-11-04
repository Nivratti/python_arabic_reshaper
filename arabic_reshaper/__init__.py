import os

from .arabic_reshaper import reshape, default_reshaper, ArabicReshaper, reverse_reshape
from .reshaper_config import (config_for_true_type_font,
                              ENABLE_NO_LIGATURES,
                              ENABLE_SENTENCES_LIGATURES,
                              ENABLE_WORDS_LIGATURES,
                              ENABLE_LETTERS_LIGATURES,
                              ENABLE_ALL_LIGATURES)


__version__ = '2.2.3'
