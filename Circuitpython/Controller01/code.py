import board
import rotaryio
from joystick_xl.inputs import Axis, Button, Hat
from joystick_xl.joystick import Joystick

#Set up the joystick
joystick = Joystick()

joystick.add_input(
    Button(board.D0), # Large momentary switch
    Button(board.D1), # Large two-way momentary switch A
    Button(board.SDA), # Large two-way momentary switch B
    Button(board.SCL), # Large toggle switch
    Button(board.D2), # Small toggle switch
    Button(board.MISO), # Big missile switch
    Axis(board.A0), # Big joystick X axis
    Axis(board.A1), # Big joystick Y axis
    Axis(board.A2), # Little slider axis
    Axis(board.A3), # Large 1x knob Left
    Axis(board.A4), # Large 1x knob right
    Button(board.MOSI), # left Rotary encoder middle click
    Button(), # left Rotary encoder A
    Button(), # left Rotary encoder B
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

# Set up the rotary encoder inputs
ENC_A = board.A5
ENC_B = board.SCK

encoder = rotaryio.IncrementalEncoder(ENC_A, ENC_B)
encoder_pos = encoder.position
last_encoder_pos = encoder.position
encoder_value = 0

#Set up the NeoKey matrix
import keypad

COLUMNS = 2
ROWS = 5

keys = keypad.KeyMatrix(
    row_pins=(
        board.D5,
        board.D7,
        board.D9,
        board.D10,
        board.D11
    ),
    column_pins=(
        board.D12,
        board.D13,
    ),
    columns_to_anodes=False,
)

while True:
    # The encoder needs to be set manually
    encoder_pos = encoder.position # Get the current encoder position
    encoder_value = encoder_pos - last_encoder_pos # how does the encoder position differ
    if not encoder_value == 0:
        if encoder_value > 0:
            joystick.button[7].source_value = 1
            joystick.button[8].source_value = 0
        else:
            joystick.button[7].source_value = 0
            joystick.button[8].source_value = 1
    else:
        joystick.button[7].source_value = 1
        joystick.button[8].source_value = 1
    last_encoder_pos = encoder.position # Store the current encoder position for next time

    # The Neokey matrix sends events that we can react to.
    key_event = keys.events.get()
    if key_event:
        # Whenever there is an event for the key,
        # whether that be it being pressed or un-pressed,
        # we send the corresponding action to the joystick.
        joystick.button[key_event.key_number + 9].source_value = 0 if key_event.pressed else 1
    
    # Now we can continue
    joystick.update()