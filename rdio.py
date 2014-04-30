'''
Rdio - Sublime Text Plugin

Provides a convenient way to pause, play, go to next/previous track,
and get current track information in the Rdio Mac application.
'''


import sublime
import sublime_plugin
import subprocess


class Rdio():
  commands = {
    'play': 'play',
    'pause': 'pause',
    'next': 'next track',
    'previous': 'previous track',
    'toggle': 'playpause'
  }


  getters = {
    'artist': 'artist',
    'album': 'album',
    'track': 'name'
  }


  def run_applescript(script):
    osa = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return osa.communicate(bytes(script, 'UTF-8'))[0].decode('UTF-8')


  def execute(action):
    if action in Rdio.commands.keys():
      script = 'if application "Rdio" is running then tell application "Rdio" to {0}'.format(Rdio.commands[action])
      return Rdio.run_applescript(script).strip()
    elif action in Rdio.getters.keys():
      script = 'if application "Rdio" is running then tell application "Rdio" to get the {0} of the current track'.format(Rdio.getters[action])
      return Rdio.run_applescript(script).strip()


class RdioPlayCommand(sublime_plugin.WindowCommand):

  def run(self):
    Rdio.execute('play')
    track = Rdio.execute('track')
    status = 'Play: {0}'.format(track)
    sublime.status_message(status)


class RdioPauseCommand(sublime_plugin.WindowCommand):

  def run(self):
    Rdio.execute('pause')
    track = Rdio.execute('track')
    status = 'Pause: {0}'.format(track)
    sublime.status_message(status)


class RdioToggleCommand(sublime_plugin.WindowCommand):

  def run(self):
    Rdio.execute('toggle')
    track = Rdio.execute('track')
    status = 'Toggle: {0}'.format(track)
    sublime.status_message(status)


class RdioNextCommand(sublime_plugin.WindowCommand):

  def run(self):
    Rdio.execute('next')
    track = Rdio.execute('track')
    status = 'Next: {0}'.format(track)
    sublime.status_message(status)


class RdioPreviousCommand(sublime_plugin.WindowCommand):

  def run(self):
    Rdio.execute('previous')
    track = Rdio.execute('track')
    status = 'Previous: {0}'.format(track)
    sublime.status_message(status)


class RdioTrackCommand(sublime_plugin.WindowCommand):

  def run(self):
    track = 'Current Track: {0} - {1} ({2})'.format(Rdio.execute('artist'), Rdio.execute('track'), Rdio.execute('album'))
    sublime.status_message(track)

