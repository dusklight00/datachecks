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

import pytest

from datachecks.core.common.errors import DataChecksDataSourcesConnectionError
from datachecks.integrations.databases.opensearch import OpenSearchDataSource


@pytest.mark.skip(reason="problem with opensearch docker container")
def test_should_throw_exception_when_opensearch_connect_fail():
    datasource = OpenSearchDataSource(
        data_source_name="test_os_data_source",
        data_connection={
            "username": "admin",
            "password": "admin",
            "host": "localhost",
            "port": 2000,
        },
    )

    with pytest.raises(DataChecksDataSourcesConnectionError):
        datasource.connect()
