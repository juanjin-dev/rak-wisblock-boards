/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright (c) 2026 RAKwireless Technology Co., Ltd.
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_

/**
 * @defgroup wisblock-io-connector WisBlock Slot Connector
 * @brief Constants for pins exposed on RAKwireless WisBlock Slots
 * @ingroup devicetree-gpio-pin-headers
 */
#define WISBLOCK_SLOT_TXD		0
#define WISBLOCK_SLOT_SPI_CS		1
#define WISBLOCK_SLOT_SPI_CLK		2
#define WISBLOCK_SLOT_SPI_MISO		3
#define WISBLOCK_SLOT_SPI_MOSI		4
#define WISBLOCK_SLOT_I2C_SCL		5
#define WISBLOCK_SLOT_I2C_SDA		6
#define WISBLOCK_SLOT_GPIO1		7
#define WISBLOCK_SLOT_GPIO2		8
#define WISBLOCK_SLOT_RXD		9

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_ */