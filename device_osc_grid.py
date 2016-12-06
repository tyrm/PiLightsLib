#!/usr/bin/env python3

from pythonosc import osc_bundle_builder
from pythonosc import osc_message_builder
from pythonosc import udp_client

from lights import DeviceObj, rgba32


# OSC Grid Object
class OSCGrid(DeviceObj):
    def __init__(self, name, width, height, ip, port, bri=1):
        DeviceObj.__init__(self, name, "osc_grid", width, height)

        self.buffer = []
        self.brightness = bri

        self.osc = udp_client.SimpleUDPClient(ip, port)

    def set(self, r, g, b, x=0, y=0):
        DeviceObj.set(self, r, g, b, x, y)

        # Set Pixel
        builder = osc_message_builder.OscMessageBuilder(address="/light/{0}/{1}/color".format(x, y))

        scaled_r = int(r*self.brightness)
        scaled_g = int(g*self.brightness)
        scaled_b = int(b*self.brightness)

        builder.add_arg(rgba32(scaled_r, scaled_g, scaled_b))

        self.buffer.append(builder.build())

    def show(self):
        DeviceObj.show(self)

        # Update Display
        bundle = osc_bundle_builder.OscBundleBuilder(0)

        for m in self.buffer:
            bundle.add_content(m)

        self.osc.send(bundle.build())

        self.buffer.clear()
