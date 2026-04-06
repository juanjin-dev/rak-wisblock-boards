.. _snippet-wisblock-console-uart0:

WisBlock Console on UART0 Snippet (wisblock-console-uart0)
##########################################################

.. code-block:: console

   west build -S wisblock-console-uart0 [...]

Overview
********

This snippet redirects the Zephyr console-related chosen UARTs to
``&wisblock_uart0``.

It is intended for WisBlock systems where the hardware composition is modeled
with Zephyr boards and shields, while the console routing policy is selected
independently at build time. In other words, this snippet does not describe a
new hardware module. Instead, it overrides the console path on top of an
existing WisBlock board and shield configuration.

The snippet updates the following chosen nodes:

- ``zephyr,console``
- ``zephyr,shell-uart``
- ``zephyr,uart-mcumgr``
- ``zephyr,bt-mon-uart``
- ``zephyr,bt-c2h-uart``

All of them are redirected to ``&wisblock_uart0``.

This is useful when the default console selected by the board or shield should
be replaced with the UART0 path exposed by the WisBlock connector abstraction.

Requirements
************

This snippet requires a WisBlock board definition that provides the
``wisblock_uart0`` devicetree node label.

The snippet only changes ``/chosen``. It does not:

- create a UART device,
- enable a disabled UART controller,
- add pins or pin control configuration,
- provide connector hardware by itself.

Any required UART controller enablement and board-specific routing must already
be provided by the selected board, shield stack, or application configuration.

Usage
*****

This snippet is typically combined with a WisBlock board and one or more
WisBlock shields.

.. code-block:: console

   west build -b <board> -S wisblock-console-uart0 --shield <shield> <app>

For example:

.. code-block:: console

   west build -b rak4631re/nrf52840 -S wisblock-console-uart0 --shield rakwireless_rak19007 samples/hello_world

When to use this snippet
************************

Use this snippet when:

- the selected WisBlock board/shield combination already models the hardware
  correctly,
- the default console route is not the desired one for the build,
- the application should use the UART0 path exported through the WisBlock
  abstraction layer.

Do not use this snippet as a replacement for a board or shield definition.
Physical WisBlock modules and stack composition should continue to be modeled
with Zephyr boards and shields.

See also
********

- :ref:`snippet-wisblock-console-uart1`