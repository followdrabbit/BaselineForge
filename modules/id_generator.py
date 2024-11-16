import uuid

class IDGenerator:
    """Generates unique IDs for security baselines."""

    @staticmethod
    def generate_id(vendor: str, category: str, technology: str, version: str, year: int, revision: int) -> str:
        """
        Generates a unique ID based on the provided parameters.

        Args:
            vendor (str): Name of the vendor (e.g., AWS, Azure).
            category (str): Category of the baseline (e.g., Security, Performance).
            technology (str): Technology name (e.g., EC2, Lambda).
            version (str): Version of the technology.
            year (int): Current year.
            revision (int): Revision number.

        Returns:
            str: A unique ID in the format 'vendor.category.technology.version.year.r{revision}'.
        """
        # Handle missing or empty values gracefully
        if not all([vendor, category, technology, version]):
            raise ValueError("All fields (vendor, category, technology, version) must be provided.")
        
        # Generate ID in the expected format
        id_string = f"{vendor}.{category}.{technology}.{version}.{year}.r{revision}"
        
        # Ensure no double dots and return the result
        return id_string.replace("..", ".")

    @staticmethod
    def generate_uuid() -> str:
        """
        Generates a UUID for tracking purposes.

        Returns:
            str: A unique UUID string.
        """
        return str(uuid.uuid4())
