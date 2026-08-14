from character import Character
from classesraces import CharRace, race_info
# from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import Label, Static, Button, OptionList, DataTable
from textual.widget import Widget
from textual.screen import Screen
from textual.message import Message
from textual import on
from textual.containers import Horizontal, Vertical

'''
Attributes are generated in the app, and displayed in AttributesTable.
When a race is selected, we need to update the AttributeTable with racial
modifiers.
These updates are temporary and will be finalized (character.set_ATT())
when a finalize button is presed.
'''
races = [race.value for race in CharRace]

class CharacterCreation(Screen):
    def compose(self) -> ComposeResult:
        race_selector = SelectorDescriptor(races, id='select-race')
        yield Static(" Create your advenutrer! ")
        yield Button("Back",id='pop')
        with Horizontal():
            with Vertical(id="left-panel"):
                # yield Static("attributes")
                yield AttributeTable(id='attr-table')
            with Vertical(id="right-panel"):
                yield race_selector
                # yield class_selector
        # yield name_input

    def on_mount(self) -> None:
        self.query_one("#left-panel").styles.width = "40%"

    def on_selector_descriptor_race_selected(self, message) -> None:
        self.app.character.set_race(message.race)
        self.query_one(AttributeTable).update_attributes(message.race)

    @on(Button.Pressed, "#reroll")
    def reroll(self):
        self.query_one(AttributeTable).reroll()



class AttributeTable(Widget):
    def __init__(self, id=None):
        super().__init__(id=id)
        self.attributes = {}
        self.temp_attributes = {}
        self.restrictions = {}
        self.race = None

    def compose(self) -> ComposeResult:
        with Vertical():
            yield DataTable()
            yield Button("Reroll", id='reroll')

    def reroll(self):
        self.app.character.gen_attr()
        self.attributes = self.app.character.attributes

        modifiers = (
            race_info[self.race].attr_modifiers or {}
            if self.race is not None
            else {}
        )

        self.temp_attributes = {
            name: (base, modifiers.get(name, 0))
            for name, base in self.attributes.items()
        }

        self.refresh_table()

    def on_mount(self) -> None:
        self.attributes = self.app.character.attributes
        self.refresh_table()


    def update_attributes(self, race):
        self.race = race
        self.attributes = self.app.character.attributes
        self.restrictions = race_info[race].min_scores or {}

        modifiers = race_info[race].attr_modifiers or {}

        self.temp_attributes = {
            name: (base, modifiers.get(name, 0))
            for name, base in self.attributes.items()
        }

        self.refresh_table()

    def refresh_table(self) -> None:
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns("ATTR", "VALUE", "")
        rows = [
            (name,
             self.color_attr(name, base, modifier, self.restrictions),
             f"[{modifier:+}]" if modifier else None)
            for name, (base, modifier) in self.temp_attributes.items()
        ]
        table.add_rows(rows)

    def color_attr(self, name, base, modifier, restrictions):
        value = base + modifier
        req = restrictions.get(name)
        if req is not None and value < req:
            return f"[red]{value}[/red]"
        return str(value)


class SelectorDescriptor(Widget):
    def __init__(self, options: list, id=None):
        super().__init__(id=id)
        self.options = options
        self.flavor_label = Label("Placeholder", id='race-text')
        self.modifiers_label = Label("Placeholder")
        self.requirements_label = Label("Placeholder")

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="selector"):
                    yield OptionList(*self.options, id='options')
            with Vertical(id="description"):
                yield self.flavor_label
                yield self.modifiers_label
                yield self.requirements_label

    class RaceSelected(Message):
        def __init__(self, race):
            super().__init__()
            self.race = race

    @on(OptionList.OptionHighlighted)
    async def on_option_highlighted(self, event:
                                    OptionList.OptionHighlighted):
        race_value = event.option.prompt
        race = CharRace(race_value)
        if race in race_info:
            flavor = race_info[race].flavor_text
            modifiers = str(race_info[race].attr_modifiers)
            requirements = str(race_info[race].min_scores)
            self.flavor_label.update(flavor)
            self.modifiers_label.update("Modifiers:" + modifiers)
            self.requirements_label.update("Requirements:\n" + requirements)
        self.post_message(self.RaceSelected(race))


class pyOSE(App):
    CSS_PATH = "main.tcss"
    BINDINGS = [
        Binding("ctrl+x", "quit", "Quit"),
    ]
    SCREENS = {
        'character-creation': CharacterCreation,
    }

    def __init__(self):
        super().__init__()
        self.character = Character()
        self.character.gen_attr()

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
