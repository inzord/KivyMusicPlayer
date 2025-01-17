import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from musicplayer.dir.path_dir import Path

Window.size = (600, 600)
Builder.load_file('box.kv')


class CallScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.music_files = ''
        self.sound = None
        self.current_key = 0
        self.sound_duration = 0

    def play_music(self):
        if self.sound is not None:
            self.sound.volume = self.ids.volume_slider.value
            self.sound.play()
            # self.sound.bind(on_stop=self.skip_next())

    def stop_music(self):
        if self.sound is not None:
            self.sound.stop()

    def set_volume(self, value):
        if self.sound is not None:
            self.sound.volume = value

    def load(self, path, selection):
        self.stop_music()
        self.sound = SoundLoader.load(selection[0])
        self.play_music()
        self.music_files = os.listdir(path)
        self.current_key = self.music_files.index(os.path.split(selection[0])[1])
        # TinyTag.get(selection[0]).duration

    def seek_forward(self, value):
        self.sound_duration = int(self.sound.length)
        if hasattr(self, 'sound_duration'):
            if self.sound is not None:
                self.sound.seek(value)
                print(self.sound_duration)
        return
        # else:
        #     print("Атрибут 'sound_duration' не существует")
        #     self.sound_duration = int(self.sound.length)

    @staticmethod
    def get_dir_path():
        return Path.get_dir_path()

    def skip_next(self):
        if self.music_files:
            self.current_key = (self.current_key + 1) % len(self.music_files)
            next_value = self.music_files[self.current_key]
            next_sound = os.path.join(self.get_dir_path(), next_value)

            self.stop_music()
            self.sound = SoundLoader.load(next_sound)
            self.play_music()
        else:
            return print("No music files loaded")

    def skip_previous(self):
        if self.music_files:
            self.current_key = (self.current_key - 1) % len(self.music_files)
            next_value = self.music_files[self.current_key]
            next_sound = os.path.join(self.get_dir_path(), next_value)

            self.stop_music()
            self.sound = SoundLoader.load(next_sound)
            self.play_music()
        else:
            return print("No music files loaded")

    def get_sound_duration(self):
        print(self.sound_duration)
        # self.sound = SoundLoader.load(self.music_files)
        # self.sound_duration = self.sound.length
        # return self.sound_duration


class SecondScreen(MDScreen):
    pass


class MainApp(MDApp):

    # def build(self):
    #     sm = ScreenManager()
    #     sm.add_widget(CallScreen(name='call_screen'))
    #     sm.add_widget(SecondScreen(name='second_screen'))
    #     return sm
    #
    # def on_start(self):
    #     # Запускаем функцию через 3 секунд после запуска приложения
    #     Clock.schedule_once(self.go_to_second_screen, 3)
    #
    # def go_to_second_screen(self, dt):
    #     self.root.current = 'second_screen'

    def build(self):
        return CallScreen()

    def on_start(self):
        Clock.schedule_once(self.go_to_second_screen, 3)

    def go_to_second_screen(self, dt):
        self.root.current = 'second_screen'

    # def button_skip_next_pressed(self):
    #     print('button_skip_next_pressed')


MainApp().run()
