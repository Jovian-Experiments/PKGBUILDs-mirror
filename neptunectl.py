#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
import sys
import click
import serial
import serial.tools.list_ports
import time
import pylink
import subprocess
from hexdump import hexdump
from textwrap import dedent


VALVE_USB_VID   = 0x28de
NEPTUNE_USB_PID = 0x1205

KNOWN_COMPORTS = [
    p for p in serial.tools.list_ports.comports() if \
        p.vid == VALVE_USB_VID and p.pid == NEPTUNE_USB_PID
]

KNOWN_SERIALS = [
    p.device for p in KNOWN_COMPORTS
]

try:
    KNOWN_JLINKS = [
        f"JLINK-{i.SerialNumber}" for i in pylink.JLink().connected_emulators()
    ]
except TypeError as e:

    if "Expected to be given a valid DLL" in str(e):
        #
        # Looks like our host doesn't have valid SEGGER DLL
        # installed. Report no known JLinks and proceed as usual.
        #
        KNOWN_JLINKS = []
    else:
        raise

KNOWN_ADAPTERS = KNOWN_SERIALS + KNOWN_JLINKS

@click.group()
def cli():
    pass

@cli.command()
def list():
    print("Found the following CDC-ACM sources of telemetry:\n")
    for i, p in enumerate(KNOWN_COMPORTS):
        print(f"{p.usb_info()} : {p.device}")
    print("")
    print("Found the following CDC-ACM sources of telemetry:\n")
    for i, j in enumerate(KNOWN_JLINKS):
        print(f"{j}")


class JLinkRTTSource:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.jlink = pylink.JLink()
        self.io = io.StringIO()

    def readline(self):
        line = self.io.readline()
        if not line:
            try:
                data = bytes(self.jlink.rtt_read(buffer_index=0,
                                                 num_bytes=4096))
                self.io = io.StringIO(data.decode())
            except ValueError:
                pass
        return line

    def __enter__(self):
        self.jlink.open(self.serial_number)
        # self.jlink.set_log_file("foo.txt")
        self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        #
        # AFAICT passing "wrong" chip ID doesn't really affect our
        # ability to read RTT.
        #
        self.jlink.connect("ATSAMD21J18", speed="auto", verbose=True)

        if self.jlink.core_name() == "Cortex-M33":
            block_address = 0x2001f000
        else:
            block_address = 0x20007000
        self.jlink.rtt_start(block_address=block_address)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.jlink.rtt_stop()


class SerialRTTSource:
    def __open(self):
        tty = serial.Serial(self.device, timeout = 0.5)
        tty.baudrate = 0x0EADBEEF  # Magic baudrate that starts streaming
        return tty

    def __init__(self, device):
        self.device = device
        self.tty = None

    def readline(self):
       # assert self.tty, "readline() called outside with statement"125ms

        line = None
        try:
            if not self.tty:
                self.tty = self.__open()

            line = self.tty.readline().decode()
        except serial.serialutil.SerialException:
            if self.tty:
                sys.stderr.write(dedent("""
                    =====================================================

                    Caught SerialException. Serial got disconnected? Will
                    continue trying to connect. Press Ctrl-C to exit.

                    =====================================================
                    """))

            self.tty = None

        return line

    def __enter__(self):
        self.tty = self.__open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tty:
            self.tty.close()

def make_rtt_source(source):
    if source.startswith("JLINK-"):
        return JLinkRTTSource(int(source[6:]))
    else:
        return SerialRTTSource(source)

@cli.command()
@click.option("--source", type=click.Choice(KNOWN_ADAPTERS),
              default=KNOWN_ADAPTERS[0] if KNOWN_ADAPTERS else None)
def log(source):
    with make_rtt_source(source) as s:
        while True:
            line = s.readline()
            if line:
                sys.stdout.write(line)
                sys.stdout.flush()

@cli.command()
def launch_jlink():
    mcu = os.environ.get("MCU")
    if not mcu:
        print("No MCU specified via the environment")
        return

    server = os.environ.get("JLINK_GDB_SERVER")
    args   = os.environ.get("JLINK_GDB_SERVER_ARGS")

    if not server or not args:
        print("JLINK_GDB_SERVER or JLINK_GDB_SERVER_ARGS missing")

    emulators = pylink.JLink().connected_emulators()
    for serial in [i.SerialNumber for i in emulators]:
        try:
            with pylink.JLink(serial_no=serial) as jlink:
                jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
                jlink.connect("ATSAMD20J18", speed="auto", verbose=True)

                core_name = jlink.core_name()
                if core_name == "Cortex-M33" and mcu == "ra4":
                    break

                if core_name == "Cortex-M0":
                    DSU_BASE    = 0x41002000
                    DSU_REG_DID = 0x0018

                    did = jlink.memory_read32(DSU_BASE + DSU_REG_DID, 1)[0]

                    if did == 0x10010300 and mcu == "d21":
                        break

                    if did == 0x10001400 and mcu == "d20":
                        break
        except pylink.errors.JLinkException as e:
            if 'J-Link is already open.' in str(e):
                pass
            else:
                raise
    else:
        print("Couldn't find the right adapter to use")
        return

    args = args.replace("USB", f"USB={serial}")

    print(f"Running: {server} {args} ")

    subprocess.run([server] + args.split())

if __name__ == '__main__':
    cli()
