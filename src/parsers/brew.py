"""Parsers for transforming Homebrew JSON output into BrewPackage models."""

from typing import Any

from models.brew import BrewBottle, BrewBottleFile, BrewFormula, BrewPackage


def parse_brew_output(output: dict[str, Any]) -> BrewPackage:
    """Parse Homebrew JSON output into a BrewPackage model.

    Args:
        output (dict): Dictionary from `brew info --json=v2`.

    Returns:
        BrewPackage: Fully constructed BrewPackage with nested models.

    """
    formulae = []

    for formula_data in output.get("formulae", []):
        bottle_data = formula_data.get("bottle")
        bottle_model = None

        if bottle_data and "stable" in bottle_data:
            stable = bottle_data["stable"]
            files_dict = {
                platform: BrewBottleFile(**file_data)
                for platform, file_data in stable.get("files", {}).items()
            }
            bottle_model = BrewBottle(stable=files_dict)

        formula_model = BrewFormula(
            **{k: v for k, v in formula_data.items() if k != "bottle"},
            bottle=bottle_model,
        )

        formulae.append(formula_model)

    return BrewPackage(
        formulae=formulae,
        casks=output.get("casks", []),
    )
