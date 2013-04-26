kivy-multilingual
=================

Towards a Kivy Example for gettext Multilingual Support

My goal is to make a Kivy app with translated/localized text based on the language/locale chosen in the F1 settings menu.

So far this works, but I have to have each piece of text that will need translation defined as a StringProperty in my main.py file and then reference it in the .kv file as root.myStringProperty

I want to be able to put "text: _('Hello!')" under the label section in my .kv file rather than needing "text: root.greeting"