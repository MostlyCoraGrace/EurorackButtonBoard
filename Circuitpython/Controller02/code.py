import board  # type: ignore (this is a CircuitPython built-in)

from joystick_xl.inputs import Axis, Button, Hat
from joystick_xl.joystick import Joystick

joystick = Joystick()

joystick.add_input(
    Axis(board.A0), # Large Slider A
    Axis(board.A1), # Large Slider B
    Axis(board.A2), # Large 4x Knob A
    Axis(board.A3), # Large 4x Knob B
    Axis(board.A4), # Large 4x Knob C
#   Axis(board.A5), # Large 4x Knob D, but this one doesnt work :(
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
    Button(), # These buttons all come from the Neokey matrix
)

#Set up the NeoKey matrix
import keypad

COLUMNS = 2
ROWS = 5

keys = keypad.KeyMatrix(
    row_pins=(
        board.SCK,
        board.MOSI,
        board.MISO,
        board.D2,
        board.D13
    ),
    column_pins=(
        board.D12,
        board.D11,
    ),
    columns_to_anodes=False,
)

while True:

    # The Neokey matrix sends events that we can react to.
    key_event = keys.events.get()
    if key_event:
        
        # Whenever there is an event for the key,
        # whether that be it being pressed or un-pressed,
        # we send the corresponding action to the joystick.
        joystick.button[key_event.key_number].source_value = 0 if key_event.pressed else 1

    joystick.update()
