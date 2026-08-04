class ETLError(Exception):
    """Base exception for ETL operations."""


class ETLValidationError(ETLError):
    """Raised when uploaded data fails validation."""


class ETLReaderError(ETLError):
    """Raised when uploaded file cannot be read."""


class ETLTransformationError(ETLError):
    """Raised when data transformation fails."""


class ETLLoadError(ETLError):
    """Raised when data loading fails."""
