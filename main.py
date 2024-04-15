from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest,
)


def run_sample():
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_report(property_id)


def run_report(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report of active users grouped by country."""
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="year")],
        metrics=[Metric(name="active1DayUsers")],
        date_ranges=[DateRange(start_date="today", end_date="today")],
    )
    response = client.run_report(request)
    print_run_report_response(response)


def print_run_report_response(response):
    """Prints results of a runReport call."""
    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name} ({metric_type})")

    print("Report result:")
    for rowIdx, row in enumerate(response.rows):
        print(f"\nRow {rowIdx}")
        for i, dimension_value in enumerate(row.dimension_values):
            dimension_name = response.dimension_headers[i].name
            print(f"{dimension_name}: {dimension_value.value}")

        for i, metric_value in enumerate(row.metric_values):
            metric_name = response.metric_headers[i].name
            print(f"{metric_name}: {metric_value.value}")


if __name__ == "__main__":
    run_sample()