/*
 * Copyright (c) 2026 RAKwireless Technology Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/devicetree/gpio.h>

BUILD_ASSERT(
	DT_NODE_EXISTS(DT_NODELABEL(wisblock_console)),
	"wisblock_console missing"
);
BUILD_ASSERT(
	DT_NODE_EXISTS(DT_NODELABEL(wisblock_uart1)),
	"wisblock_uart1 missing"
);
BUILD_ASSERT(
	DT_NODE_EXISTS(DT_NODELABEL(wisblock_spi)),
	"wisblock_spi missing"
);
BUILD_ASSERT(
	DT_NODE_EXISTS(DT_NODELABEL(wisblock_i2c1)),
	"wisblock_i2c1 missing"
);

#define ZU DT_PATH(zephyr_user)

/* LEDs */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, led1_gpios),     okay),
	"IO LED1 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, led2_gpios),     okay),
	"IO LED2 ctrl disabled"
);
/* I2C1 */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, i2c1_sda_gpios), okay),
	"IO I2C1_SDA ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, i2c1_scl_gpios), okay),
	"IO I2C1_SCL ctrl disabled"
);
/* ADC inputs */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, ain0_gpios),     okay),
	"IO AIN0 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, ain1_gpios),     okay),
	"IO AIN1 ctrl disabled"
);
/* SPI */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, spi_cs_gpios),   okay),
	"IO SPI_CS ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, spi_clk_gpios),  okay),
	"IO SPI_CLK ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, spi_miso_gpios), okay),
	"IO SPI_MISO ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, spi_mosi_gpios), okay),
	"IO SPI_MOSI ctrl disabled"
);
/* General-purpose IOs */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io1_gpios),      okay),
	"IO IO1 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io2_gpios),      okay),
	"IO IO2 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io3_gpios),      okay),
	"IO IO3 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io4_gpios),      okay),
	"IO IO4 ctrl disabled"
);
/* UART1 */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, txd1_gpios),     okay),
	"IO TXD1 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, rxd1_gpios),     okay),
	"IO RXD1 ctrl disabled"
);
/* General-purpose IOs (cont.) */
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io5_gpios),      okay),
	"IO IO5 ctrl disabled"
);
BUILD_ASSERT(
	DT_NODE_HAS_STATUS(DT_GPIO_CTLR(ZU, io6_gpios),      okay),
	"IO IO6 ctrl disabled"
);

int main(void) {
	return 0;
}
