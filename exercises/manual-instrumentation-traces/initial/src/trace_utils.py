from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

# OTel API
from opentelemetry import trace as trace_api

# OTel SDK
from opentelemetry.sdk.trace import TracerProvider


def create_tracing_pipeline() -> BatchSpanProcessor:

    console_exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(console_exporter)
    return span_processor


def create_tracer(name: str, version: str) -> trace_api.Tracer:

    provider = TracerProvider()
    provider.add_span_processor(create_tracing_pipeline())
    trace_api.set_tracer_provider(provider)
    tracer = trace_api.get_tracer(name, version)
    return tracer
