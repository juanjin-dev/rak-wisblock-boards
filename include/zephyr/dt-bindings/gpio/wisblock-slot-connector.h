/*
 * Copyright (c) 2026 Shenzhen RAKwireless Technology Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * @file
 * @brief WisBlock slot connector pin constants
 * @ingroup wisblock-slot-connector
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_

/**
 * @defgroup wisblock-slot-connector WisBlock Slot Connector
 * @brief Constants for pins exposed on RAKwireless WisBlock Slots
 * @ingroup devicetree-gpio-pin-headers
 * @{
 */

#define WISBLOCK_SLOT_TXD	0 /**< UART TX */
#define WISBLOCK_SLOT_SPI_CS	1 /**< SPI chip select */
#define WISBLOCK_SLOT_SPI_CLK	2 /**< SPI clock */
#define WISBLOCK_SLOT_SPI_MISO	3 /**< SPI MISO */
#define WISBLOCK_SLOT_SPI_MOSI	4 /**< SPI MOSI */
#define WISBLOCK_SLOT_I2C_SCL	5 /**< I2C SCL */
#define WISBLOCK_SLOT_I2C_SDA	6 /**< I2C SDA */
#define WISBLOCK_SLOT_GPIO1	7 /**< General-purpose GPIO1 */
#define WISBLOCK_SLOT_GPIO2	8 /**< General-purpose GPIO2 */
#define WISBLOCK_SLOT_RXD	9 /**< UART RX */

/** @} */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_WISBLOCK_SLOT_CONNECTOR_H_ */
