from classesraces import CharRace, CharClass, race_info
from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import Label, Static, Button, OptionList
from textual.widget import Widget
from textual.screen import Screen
from textual import events, on
from textual.containers import Horizontal, Vertical, VerticalScroll

races = [race.value for race in CharRace]

class CharacterCreation(Screen):
    def compose(self) -> ComposeResult:
        race_selector = SelectorDescriptor(races)
        yield Static(" Create your advenutrer! ")
        yield Button("Back",id='pop')
        with Horizontal():
            with Vertical(id="left-panel"):
                # yield attribute_table
                yield Static("attributes")
            with Vertical(id="right-panel"):
                yield race_selector
                # yield class_selector
        # yield name_input

class SelectorDescriptor(Widget):
    def __init__(self, options: list):
        super().__init__()
        self.options = options
        self.description_label = Label("Placeholder")

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="selector"):
                    yield OptionList(*self.options)
            with Vertical(id="description"):
                yield self.description_label
                # yield Label("Description placeholder")
    @on(OptionList.OptionHighlighted)
    async def on_option_highlighted(self, event:
                                    OptionList.OptionHighlighted):
        race_value = event.option.prompt
        race = CharRace(race_value)
        if race in race_info:
            description = race_info[race].flavor_text
            self.description_label.update(description)


class pyOSE(App):
    BINDINGS = [
        Binding("ctrl+x", "quit", "Quit"),
    ]
    SCREENS = {
        'character-creation': CharacterCreation,
    }

    def compose(self):
        yield Static(" Welcome to PyOSE! ")
        yield Button("Character creation", id="character-creation")
        yield Button("Combat", id="combat")

    @on(Button.Pressed, "#character-creation, #combat-button")
    def add_screen_to_stack(self, event: Button.Pressed) -> None:
        self.push_screen(event.button.id)

    @on(Button.Pressed, "#pop")
    def pop_screen_from_stack(self, event: Button.Pressed) -> None:
        self.pop_screen()



if __name__ == '__main__':
    OSE = pyOSE()
    OSE.run()
