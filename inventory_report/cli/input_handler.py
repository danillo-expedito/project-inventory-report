from typing import List
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    if not report_type == "simple" and not report_type == "complete":
        raise ValueError("Report type is invalid.")

    report = CompleteReport() if report_type == "complete" else SimpleReport()

    for path in file_paths:
        file_extension = path.split(".")[-1]
        if file_extension == "json":
            report.add_inventory(Inventory(JsonImporter(path).import_data()))
        elif file_extension == "csv":
            report.add_inventory(Inventory(CsvImporter(path).import_data()))

    return report.generate()
