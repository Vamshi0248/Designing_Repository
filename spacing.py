"""
Spacing utilities for design systems.
This module provides functions to handle consistent spacing
across UI components and layouts.
"""


class SpacingSystem:
    """
    A spacing system for maintaining consistent spacing throughout the design.
    """

    # Define spacing scale (in pixels)
    SPACING_SCALE = {
        "xs": 4,      # Extra small spacing
        "sm": 8,      # Small spacing
        "md": 16,     # Medium spacing (base unit)
        "lg": 24,     # Large spacing
        "xl": 32,     # Extra large spacing
        "2xl": 48,    # 2x extra large spacing
        "3xl": 64,    # 3x extra large spacing
    }

    @staticmethod
    def get_spacing(size):
        """
        Get spacing value by size key.

        Args:
            size (str): The size key (xs, sm, md, lg, xl, 2xl, 3xl)

        Returns:
            int: The spacing value in pixels
        """
        return SpacingSystem.SPACING_SCALE.get(size, 16)

    @staticmethod
    def get_padding(size):
        """
        Calculate padding value.

        Args:
            size (str): The size key for padding

        Returns:
            str: Padding CSS value
        """
        value = SpacingSystem.get_spacing(size)
        return f"{value}px"

    @staticmethod
    def get_margin(size):
        """
        Calculate margin value.

        Args:
            size (str): The size key for margin

        Returns:
            str: Margin CSS value
        """
        value = SpacingSystem.get_spacing(size)
        return f"{value}px"

    @staticmethod
    def get_gap(size):
        """
        Calculate gap value for flex/grid layouts.

        Args:
            size (str): The size key for gap

        Returns:
            str: Gap CSS value
        """
        value = SpacingSystem.get_spacing(size)
        return f"{value}px"


# Example usage
if __name__ == "__main__":
    spacing = SpacingSystem()

    print("Spacing System Examples:")
    print("-" * 40)

    for size_key in ["xs", "sm", "md", "lg", "xl", "2xl", "3xl"]:
        padding = spacing.get_padding(size_key)
        margin = spacing.get_margin(size_key)
        gap = spacing.get_gap(size_key)

        print(f"\nSize: {size_key}")
        print(f"  Padding: {padding}")
        print(f"  Margin: {margin}")
        print(f"  Gap: {gap}")
