# -*- coding: utf-8 -*-

# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import abc
from google.aiplatform.compat.types import model_monitoring as gca_model_monitoring

class _AlertConfig(abc.ABC):
    """An abstract class for setting model monitoring alert config"""
    def __init__(
        self, 
        enable_logging: Optional[bool] = None
    ):
        self.enable_logging = enable_logging

    @abstractmethod
    def as_proto(self) -> gca_model_monitoring.ModelMonitoringAlertConfig:
        pass
        

class EmailAlertConfig(_AlertConfig):
    def __init__(
        self, 
        user_emails: List[str], 
        enable_logging: Optional[bool] = None
    ):
        """Initializer for EmailAlertConfig

        Args:
            user_emails (List[str]):
                The email addresses to send the alert to.
            enable_logging (bool):
                Optional. Streams detected anomalies to Cloud Logging. The anomalies will be
                put into json payload encoded from proto
                [google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry][].
                This can be further sync'd to Pub/Sub or any other services
                supported by Cloud Logging.

        Returns:
            An instance of EmailAlertConfig
        """
        super().__init__(
            enable_logging = self.enable_logging
        )
        self.user_emails = user_emails
    
    def as_proto(self) -> gca_model_monitoring.ModelMonitoringAlertConfig:
        user_email_alert_config = gca_model_monitoring.ModelMonitoringAlertConfig.EmailAlertConfig(
            user_emails = self.user_emails
        )
        return gca_model_monitoring.ModelMonitoringAlertConfig(
            email_alert_config = user_email_alert_config,
            enable_logging = self.enable_logging
        )
