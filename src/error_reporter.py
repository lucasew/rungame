import sys
import traceback

def report_error(error):
    """
    Centralized error-reporting function.
    Currently logs to stderr with stack trace.
    If Sentry is added later, it should be integrated here.
    """
    sys.stderr.write(f"ERROR: {str(error)}\n")
    traceback.print_exc(file=sys.stderr)
