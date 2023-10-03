#  Copyright 2022-present, the Waterdip Labs Pvt. Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union


class MetricsType(str, Enum):
    """
    MetricsType is an enum that represents the type of metric that is generated by a data source.
    """

    ROW_COUNT = "row_count"
    DOCUMENT_COUNT = "document_count"
    MIN = "min"
    MAX = "max"
    AVG = "avg"
    SUM = "sum"
    STDDEV = "stddev"
    VARIANCE = "variance"
    DISTINCT_COUNT = "distinct_count"
    MISSING_COUNT = "missing_count"
    DUPLICATE_COUNT = "duplicate_count"
    NULL_COUNT = "null_count"
    NULL_PERCENTAGE = "null_percentage"
    EMPTY_STRING_COUNT = "empty_string_count"
    EMPTY_STRING_PERCENTAGE = "empty_string_percentage"
    SKEWNESS = "skewness"
    KURTOSIS = "kurtosis"
    FRESHNESS = "freshness"
    MAX_LENGTH = "max_length"
    MIN_LENGTH = "min_length"
    AVG_LENGTH = "avg_length"
    COMBINED = "combined"


@dataclass
class MetricValue:
    """
    MetricValue is a class that represents a metric value that is generated by a data source.

    """

    identity: str
    value: Union[int, float]
    metric_type: MetricsType
    timestamp: str
    data_source: Optional[str] = None
    expression: Optional[str] = None
    table_name: Optional[str] = None
    index_name: Optional[str] = None
    field_name: Optional[str] = None
    is_valid: Optional[bool] = None
    reason: Optional[str] = None
    tags: Dict[str, str] = None


@dataclass
class TableMetrics:
    """
    TableMetrics is a class that represents a list of metric values that is generated by a data source.
    """

    data_source: str
    table_name: str
    """
    metrics is a dictionary of metric identifier and metric value
    """
    metrics: Dict[str, MetricValue]


@dataclass
class IndexMetrics:
    """
    IndexMetrics is a class that represents a list of metric values that is generated by a data source.
    """

    data_source: str
    index_name: str
    """
    metrics is a dictionary of metric identifier and metric value
    """
    metrics: Dict[str, MetricValue]


@dataclass
class DataSourceMetrics:
    """
    DataSourceMetrics is a class that represents a list of metric values that is generated by a data source.
    """

    data_source: str
    table_metrics: Optional[Dict[str, TableMetrics]] = None
    index_metrics: Optional[Dict[str, IndexMetrics]] = None


@dataclass
class CombinedMetrics:
    """
    CombinedMetrics is a class that represents a list of metric values that is generated by a data source.
    """

    expression: str
    """
    metrics is a dictionary of metric identifier and metric value
    """
    metrics: Dict[str, MetricValue]
