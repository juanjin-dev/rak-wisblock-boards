## boards: rakwireless: add WisBlock Core and Base board support

This pull request introduces upstream support for the RAKwireless WisBlock
modular hardware platform. WisBlock is an open, certified ecosystem where any
WisBlock Certified manufacturer can produce compatible Core and peripheral
modules. Zephyr support for the platform foundation enables the broader
ecosystem to build on a common, upstream-maintained base.

Due to the highly modular nature of the platform, this implementation heavily
utilizes Zephyr's Hardware Model v2 to explicitly separate compute identities
from physical interconnects, preventing devicetree overlay duplication across
multiple core and carrier combinations.

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

### Naming Considerations

RAK4631 is submitted as ``rak4631re`` to avoid conflicting with the existing
``rak4631`` board already present in the Zephyr tree (a HW Model v1 legacy
implementation). Coordination with the existing board's maintainer regarding
deprecation or coexistence is ongoing and will be resolved before this PR is
merged.

### Hardware Semantic Mapping

The hardware is abstracted into four structural layers:

1. **SoC Layer**: Standard Zephyr silicon definitions (e.g., nRF52840,
   STM32WLE5).
2. **SoM Layer**: Vendor-specific IP encapsulation (e.g., `rak4630.dtsi`).
   Complex clock trees, power management, and RF PHY configurations are isolated
   within `dts/vendor/rakwireless/` for reuse.
3. **Common Interface Layer**: Core modules map their SoC-specific pins to a
   standardized connector node (`wisblock_io`). This binding is placed in
   `dts/common/wisblock/` to establish a vendor-neutral bridge — vendor-neutral
   because any WisBlock Certified manufacturer can produce modules that consume
   this interface, similar to the `arduino_uno` header implementation.
4. **Base Board Layer**: Carrier boards (e.g., `rakwireless_rak19007`) are
   implemented as shields. They instantiate per-slot nodes (`wisblock_slota`
   through `wisblock_slotf`) using the `wisblock-slot-connector` binding, which
   maps the 10-pin slot pinout to SoC GPIOs via `wisblock_io`. This keeps Base
   board definitions completely agnostic to the underlying Core SoC.

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

### Devicetree Limitations Workaround

WisBlock Base boards expose multiple SPI module slots, each requiring a
dedicated chip-select GPIO. The native DTS overlay mechanism uses last-writer-
wins semantics for array properties, so naively appending `cs-gpios` entries
across multiple shield overlays silently discards earlier values.

`wisblock_spi_cs.dtsi` resolves this with a preprocessor-based accumulator
pattern. Each slot overlay appends to a macro that grows the `cs-gpios` array
incrementally. The final array is emitted once after all slot overlays are
processed, producing a correct multi-entry `cs-gpios` property regardless of
how many peripheral shields are stacked.

This approach is acknowledged as non-standard. A DTS-level solution using
fixed-size `cs-gpios` arrays was considered, but requires Base board shields to
reserve entries for all possible slot positions upfront, producing sparse arrays
with placeholder `<&gpio0 0 0>` entries that do not correspond to real hardware.
The preprocessor accumulator was preferred as it emits only the entries that are
actually wired on the carrier board.

This file is part of the Base board foundation rather than the peripheral
shields because the slot topology and GPIO assignments are a property of the
carrier board, not of the individual peripheral modules placed on it.

### Testing

- Built and verified `hello_world` and `blinky` on rak4631re, RAK11310, and
  RAK3372.
- Verified dynamic console routing on RAK19007.
- RAK3312, RAK3401, RAK11722, and RAK19026 are defined but not yet verified
  on hardware; build-only validation has been performed.
- TODO: Run `scripts/checkpatch.pl --git HEAD` before submission.
- TODO: Run combined twister builds (`twister -p <core> --shield
  rakwireless_rak19007`) before submission.

Signed-off-by: JaeHwan Jin <jaehwan.jin@rakwireless.com>
