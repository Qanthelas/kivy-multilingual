import kivy
kivy.require('1.5.1')
 
import gettext
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
#from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
import os
 
# Set up message catalog access
dir = os.path.dirname(__file__)
languagePath = os.path.join(dir, 'language')
gettext.bindtextdomain('multilingual', languagePath)
 
class Multilingual(BoxLayout):
    '''Basics for widget where we select and then test a language preference.
    '''
    label_language = ObjectProperty()
    greeting = StringProperty()
    testtext = StringProperty()
    
    def myfunction(self, text):
        self.result = text + ' this is a test'
        #self.testtext = self.result
        return self.result
 
def _(*args):
  return App.get_running_app().get_text(*args)
 
class MultilingualApp(App):
    def build(self):
        self.set_language('en_US')
        self.root = Multilingual(greeting='Translated Message Will Be Here')

        #self.root.myfunction('blah')
      
    def set_language(self,selectedLanguage):
        self.t = gettext.translation('multilingual', languagePath, languages=[selectedLanguage], fallback=True)
        _ = self.t.ugettext #The 'u' in 'ugettext' is for Unicode - use this to keep Unicode from breaking the app
        #self.root.greeting = _('Hello!')
 
    def get_text(self, *args):
        return self.t.ugettext(*args)
    
    def build_config(self, config):
        config.add_section('localization')
        config.set('localization', 'language', 'en_US')
    
    def build_settings(self, settings):
        settings.add_json_panel('Multilingual', self.config, data='''[
            { "type": "title", "title": "Language Settings" },
            { "type": "options", "title": "Language",
              "desc": "Choose which language to translate the text of this app into",
              "section": "localization", "key": "language",
              "options": ["en_US", "de", "fr", "es"]}
        ]''')
 
    def on_config_change(self, config, section, key, value):
        if config is not self.config:
            return
        token = (section, key)
        if token == ('localization', 'language'):
            self.set_language(value)
        print "Language is now", value
 
if __name__ == '__main__':
    MultilingualApp().run()