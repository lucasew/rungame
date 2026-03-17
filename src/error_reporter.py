import sys
import logging
from typing import Optional

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def report_error(error: Exception, context_info: Optional[dict] = None) -> None:
    """
    Centralized error-reporting function for the project.
    If Sentry or another backend were configured, this function would send the error there.
    Currently, it logs to the console with context.
    """
    error_message = f"{type(error).__name__}: {str(error)}"
    if context_info:
        error_message += f" | Context: {context_info}"

    logger.error(error_message, exc_info=True)
    # NOTE: If we add Sentry later, the integration goes here (e.g. Sentry.captureException)
