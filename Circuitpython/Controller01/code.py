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
)

# Set up the rotary encoder inputs
ENC_A = board.A5
ENC_B = board.SCK

encoder = rotaryio.IncrementalEncoder(ENC_A, ENC_B)
encoder_pos = encoder.position
last_encoder_pos = encoder.position
encoder_value = 0

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
    
    # Now we can continue
    joystick.update()