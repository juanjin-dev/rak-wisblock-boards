New Boards
**********

* Shenzhen RAKwireless Technology Co., Ltd.

   * :zephyr:board:`rak3312` (``rak3312/esp32s3/procpu``, ``rak3312/esp32s3/appcpu``)
   * :zephyr:board:`rak3372` (``rak3372/stm32wle5ccux``)
   * :zephyr:board:`rak3401` (``rak3401/nrf52840``)
   * :zephyr:board:`rak4631re` (``rak4631re/nrf52840``)
   * :zephyr:board:`rak11310` (``rak11310``)
   * :zephyr:board:`rak11722` (``rak11722``)
   * :zephyr:board:`rak19026` (``rak19026``)

New Shields
===========

* :ref:`RAKwireless RAK19001 WisBlock Dual IO Base Board <rakwireless_rak19001>`
* :ref:`RAKwireless RAK19003 WisBlock Mini Base Board <rakwireless_rak19003>`
* :ref:`RAKwireless RAK19007 WisBlock Base Board 2nd Gen <rakwireless_rak19007>`
* :ref:`RAKwireless RAK19009 WisBlock Mini Base Board with Power Slot <rakwireless_rak19009>`
* :ref:`RAKwireless RAK19010 WisBlock Base Board with Power Slot <rakwireless_rak19010>`
* :ref:`RAKwireless RAK19011 WisBlock Dual IO Base Board with Power Slot <rakwireless_rak19011>`
* :ref:`RAKwireless RAK19012 WisBlock USB LiPo Solar Power Slot Module <rakwireless_rak19012>`
* :ref:`RAKwireless RAK19013 WisBlock LiPo Solar Power Slot Module <rakwireless_rak19013>`
* :ref:`RAKwireless RAK19014 WisBlock Battery USB Power Slot Module <rakwireless_rak19014>`
* :ref:`RAKwireless RAK19015 WisBlock Battery Power Slot Module <rakwireless_rak19015>`
* :ref:`RAKwireless RAK19016 WisBlock 5-24V Power Slot Module <rakwireless_rak19016>`
* :ref:`RAKwireless RAK19017 WisBlock POE Slot Module <rakwireless_rak19017>`

Other notable changes
*********************

* WisBlock Platform Interface

  Support for the RAKwireless WisBlock modular platform has been introduced.
  WisBlock Core modules expose a standardized ``wisblock_io`` connector node
  defined in ``dts/common/wisblock/``, which maps SoC-specific pins to a
  vendor-neutral interface. This is modelled after the ``arduino_uno`` header
  pattern and allows Base board shields to remain fully agnostic to the
  underlying Core SoC. Per-slot DTSI files (``wisblock_slota.dtsi`` through
  ``wisblock_slotf.dtsi``) are provided for Base board shield authors.

  A ``wisblock_spi_cs.dtsi`` preprocessor-based accumulator is introduced to
  correctly construct multi-entry ``cs-gpios`` arrays when multiple SPI
  peripheral shields are stacked on the same Base board. This works around the
  DTS last-writer-wins limitation for array properties across multiple overlay
  files. The accumulator is part of the Base board shield layer, as the slot
  topology and GPIO assignments are a property of the carrier board, not of the
  individual peripheral shields placed on it.

  A ``wisblock-console`` snippet is provided to redirect the Zephyr console to
  the WisBlock UART interface when building applications that do not use a Base
  board shield with USB CDC ACM console routing.

* WisBlock DT Bindings and Pin Headers

  New devicetree bindings are added under ``dts/bindings/`` for the WisBlock IO
  connector (``wisblock-io-connector``), slot connector
  (``wisblock-slot-connector``), ADC nexus (``wisblock-adc``), and PWM nexus
  (``wisblock-pwm``). Corresponding pin-index header files are added under
  ``include/zephyr/dt-bindings/`` for GPIO, ADC, and PWM nexus consumers.
