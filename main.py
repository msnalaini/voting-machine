def on_button_pressed_a():
    radio.send_number(0)
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(255)
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(4)
radio.set_transmit_serial_number(True)
basic.show_icon(IconNames.GHOST)