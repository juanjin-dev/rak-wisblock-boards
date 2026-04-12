# Pre-upstream Testbed for WisBlock Zephyr Support

> **⚠️ DO NOT submit changes from this repository to Zephyr upstream without
> explicit sign-off from the maintainer.**
> The hardware interface contracts are not yet finalized and the software has
> not been fully validated. Premature upstream submission will be rejected and
> may harm the platform's upstream track record.

> **Intellectual Property Notice**
> All interface designs, DTS structures, and binding definitions in this
> repository represent original work authored by and copyright
> © Shenzhen RAKwireless Technology Co., Ltd. Unauthorized submission of
> this work to any upstream project without proper attribution constitutes
> copyright infringement. RAKwireless Technology Co., Ltd. reserves the
> right to pursue legal action for unauthorized use or misattribution.

Out-of-tree Zephyr module providing board and shield definitions for the
RAKwireless WisBlock ecosystem. Code here is being validated before submission
to Zephyr upstream.

> **This repository is a staging testbed. APIs, DTS node names, and board
> identifiers may change without notice.**

## Contents

- `boards/rakwireless/` — WisBlock Core boards: RAK3312, RAK3372, RAK3401,
  RAK4631 (upstream name pending), RAK11310, RAK11722, RAK19026
- `boards/shields/` — WisBlock Base board shields: RAK19001, RAK19003,
  RAK19007, RAK19009–RAK19017
- `dts/bindings/` — WisBlock IO slot connector bindings
- `snippets/` — `wisblock-console` snippet

## Usage

Add this module to your `west.yml`:

```yaml
manifest:
  projects:
    - name: rak-wisblock-boards
      url: https://github.com/juanjin-dev/rak-wisblock-boards
      revision: main
      path: modules/rak-wisblock-boards
```

The module registers `board_root`, `dts_root`, and `snippet_root` automatically
via `zephyr/module.yml`.

## Relationship to wisblock-for-zephyr

[wisblock-for-zephyr](https://github.com/RAKwireless/wisblock-for-zephyr)
provides sensor and communication shield definitions together with sample
applications. It depends on this repository for Core and Base board support.

## License

Apache-2.0 — see [LICENSE](LICENSE).
