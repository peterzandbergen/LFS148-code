from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import ConsoleLogExporter, SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource
import logging

# Create logger provider with the resource
logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "example-app",
        }
    ),
)

# Add a log record processor that sends the log records to the console on standard out
logger_provider.add_log_record_processor(SimpleLogRecordProcessor(ConsoleLogExporter()))

# Create a handler
handler = LoggingHandler(logger_provider=logger_provider)

# Configure the system wide logger to use our handler
logger = logging.getLogger()
logger.addHandler(handler)