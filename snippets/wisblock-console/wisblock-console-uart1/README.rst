.. _snippet-wisblock-console-uart1:

WisBlock Console on UART1 Snippet (wisblock-console-uart1)
##########################################################

.. code-block:: console

   west build -S wisblock-console-uart1 [...]

Overview
********

This snippet redirects the Zephyr console-related chosen UARTs to
``&wisblock_uart1``.

It is intended for WisBlock systems where hardware assembly is expressed using
Zephyr boards and shields, while console selection is treated as a reusable
build-time policy. This keeps the physical WisBlock composition separate from
the console routing choice.

The snippet updates the following chosen nodes:

- ``zephyr,console``
- ``zephyr,shell-uart``
- ``zephyr,uart-mcumgr``
- ``zephyr,bt-mon-uart``
- ``zephyr,bt-c2h-uart``

All of them are redirected to ``&wisblock_uart1``.

This is useful for WisBlock builds that need shell, mcumgr UART transport, and
other console-related traffic to use the UART1 path exposed through the common
WisBlock connector abstraction.

Requirements
************

This snippet requires a WisBlock board definition that provides the
``wisblock_uart1`` devicetree node label.

The snippet only changes ``/chosen``. It does not:

- create a UART device,
- enable a disabled UART controller,
- add pins or pin control configuration,
- model any WisBlock Base board or expansion module.

Any required UART enablement and board-specific routing must already be
provided by the selected board, shield stack, or application configuration.

Usage
*****

This snippet is typically used together with a WisBlock board and one or more
WisBlock shields.

.. code-block:: console

   west build -b <board> -S wisblock-console-uart1 --shield <shield> <app>

For example, this fits naturally with WisBlock shield-based hardware
compositions such as:

.. code-block:: console

   west build -b rak4631re/nrf52840 -S wisblock-console-uart1 --shield rakwireless_rak19010 --shield rakwireless_rak19013 samples/drivers/fuel_gauge

When to use this snippet
************************

Use this snippet when:

- the hardware is already described correctly by the selected WisBlock board and
  shield combination,
- the build should override the default console route,
- UART1 is the preferred external console path for the target setup.

This snippet is especially useful when the same application and hardware stack
may need different console routes in different builds without duplicating board,
shield, or application configuration.

Do not use this snippet to model physical WisBlock hardware. Boards and shields
remain the correct place to describe the Core module, Base board, and attached
WisBlock modules.

See also
********

- :ref:`snippet-wisblock-console-uart0`