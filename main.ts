input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(0)
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(255)
    basic.showIcon(IconNames.Yes)
})
radio.setGroup(4)
radio.setTransmitSerialNumber(true)
basic.showIcon(IconNames.Ghost)
