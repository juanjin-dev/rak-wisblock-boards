## boards: rakwireless: add WisBlock Core and Base board support

This pull request introduces upstream support for the RAKwireless WisBlock
modular hardware platform. WisBlock is an open, certified ecosystem where any
WisBlock Certified manufacturer can produce compatible Core and peripheral
modules. Zephyr support for the platform foundation enables the broader
ecosystem to build on a common, upstream-maintained base.

### Scope of Upstreaming

This PR covers the platform foundation only:

**Core modules** (7): RAK3312, RAK3372, RAK3401, RAK4631, RAK11310, RAK11722,
RAK19026

**Base board shields** (12): RAK19001, RAK19003, RAK19007, RAK19009, RAK19010,
RAK19011, RAK19012, RAK19013, RAK19014, RAK19015, RAK19016, RAK19017

In addition to board and shield definitions, this PR includes:

- `dts/bindings/` — WisBlock IO connector, slot connector, ADC, and PWM nexus
  bindings
- `include/zephyr/dt-bindings/` — pin index constants for the above bindings
- `dts/common/wisblock/` — shared slot DTSI files and the SPI CS accumulator
- `dts/vendor/rakwireless/` — RAKwireless SoM DTSI files
- `snippets/wisblock-console` — console redirection snippet

Functional peripheral shields (sensors, communication modules) are maintained
out-of-tree in a companion repository and are not part of this submission.

### Console Routing & Twister Compatibility

WisBlock Core modules have no physical USB or UART bridge of their own — those
are a property of the Base board. Core module definitions therefore intentionally
omit the `zephyr,console` chosen node and the `serial` hardware feature.
Console routing is delegated to the Base board shield: the shield's
`Kconfig.defconfig` inspects the `zephyr,console` compatible string at build
time and injects either the USB CDC ACM stack (for boards with a Type-C
connector) or a plain UART console (for boards with a USB-to-UART bridge). In
CI, standalone core module builds lacking `serial` are correctly filtered by
Twister; combined builds (`twister -p <core> --shield <base>`) acquire the
feature via `shield.yml` and execute normally.

### Testing


Signed-off-by: JaeHwan Jin <jaehwan.jin@rakwireless.com>
