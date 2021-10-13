
# pip install wikipedia
# pip install gTTS

# very very very very simple

import wikipedia

from gtts import gTTS
from wikipedia.wikipedia import languages


summaryWiki = 'Soda Stereo'
language   = 'es'

wikipedia.set_lang(language)

result = wikipedia.summary(summaryWiki)

tts = gTTS(result,lang=language)

tts.save(summaryWiki + '.mp3')





