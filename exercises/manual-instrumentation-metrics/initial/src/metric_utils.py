# OTel SDK
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
    MetricReader,
)

# OTel API
from opentelemetry import metrics as metric_api

# OTel SDK
from opentelemetry.sdk.metrics import MeterProvider



def create_metrics_pipeline(export_interval: int) -> MetricReader:
    console_exporter = ConsoleMetricExporter()
    reader = PeriodicExportingMetricReader(
        exporter=console_exporter,
        export_interval_millis=export_interval
    )
    return reader


def create_meter(name: str, version: str) -> metric_api.Meter:
    # configure provider
    metric_reader = create_metrics_pipeline(5000)
    provider = MeterProvider(
        metric_readers=[metric_reader],
    )

    # obtain meter
    metric_api.set_meter_provider(provider)
    meter = metric_api.get_meter(name, version)
    return meter


def create_request_instruments(meter: metric_api.Meter) -> dict:
    traffic_volume = meter.create_counter(
        name="traffic_volume",
        unit="request",
        description="total volume of requests to an endpoint",
    )
    
    error_rate = meter.create_counter(
        name="error_rate",
        unit="request",
        description="rate of failed requests",
    )
    
    
    instruments = {
        "traffic_volume": traffic_volume,
        "error_rate": error_rate,
    }
    return instruments