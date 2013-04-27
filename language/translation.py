from os.path import join, dirname
import gettext

def set_language(self,selectedLanguage):
    self.t = gettext.translation('multilingual', languagePath, languages=[selectedLanguage], fallback=True)
    _ = self.t.ugettext #The 'u' in 'ugettext' is for Unicode - use this to keep Unicode from breaking the app
    return _
lang = str()
_ = setlanguage(lang)