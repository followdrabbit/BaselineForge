import uuid

class IDGenerator:
    """Generates unique IDs for security baselines."""

    @staticmethod
    def generate_control_id(vendor: str, technology: str, year: int, counter: int) -> str:
        """
        Generates a simplified control ID in the format: VENDOR-TECHNOLOGY-YEAR-COUNTER.
        Any spaces in the vendor or technology names are replaced with '-' for consistency.
        
        Example:
            AWS-AMAZON-S3-2025-0001

        Args:
            vendor (str): Name of the vendor.
            technology (str): Name of the technology.
            year (int): Current year.
            counter (int): Sequential counter with 4 digits.

        Returns:
            str: The generated control ID.
        """
        vendor_normalized = vendor.upper().replace(" ", "-")
        technology_normalized = technology.upper().replace(" ", "-")
        return f"{vendor_normalized}-{technology_normalized}-{year}-{counter:04d}"

    @staticmethod
    def generate_uuid() -> str:
        """
        Generates a UUID for tracking purposes.

        Returns:
            str: A unique UUID string.
        """
        return str(uuid.uuid4())
