# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class ExternalTracker(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_tracker_format': 'str',
        'external_tracker_style': 'str',
        'external_tracker_url': 'str'
    }

    attribute_map = {
        'external_tracker_format': 'external_tracker_format',
        'external_tracker_style': 'external_tracker_style',
        'external_tracker_url': 'external_tracker_url'
    }

    def __init__(self, external_tracker_format=None, external_tracker_style=None, external_tracker_url=None, _configuration=None):  # noqa: E501
        """ExternalTracker - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_tracker_format = None
        self._external_tracker_style = None
        self._external_tracker_url = None
        self.discriminator = None

        if external_tracker_format is not None:
            self.external_tracker_format = external_tracker_format
        if external_tracker_style is not None:
            self.external_tracker_style = external_tracker_style
        if external_tracker_url is not None:
            self.external_tracker_url = external_tracker_url

    @property
    def external_tracker_format(self):
        """Gets the external_tracker_format of this ExternalTracker.  # noqa: E501

        External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index.  # noqa: E501

        :return: The external_tracker_format of this ExternalTracker.  # noqa: E501
        :rtype: str
        """
        return self._external_tracker_format

    @external_tracker_format.setter
    def external_tracker_format(self, external_tracker_format):
        """Sets the external_tracker_format of this ExternalTracker.

        External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index.  # noqa: E501

        :param external_tracker_format: The external_tracker_format of this ExternalTracker.  # noqa: E501
        :type: str
        """

        self._external_tracker_format = external_tracker_format

    @property
    def external_tracker_style(self):
        """Gets the external_tracker_style of this ExternalTracker.  # noqa: E501

        External Issue Tracker Number Format, either `numeric` or `alphanumeric`  # noqa: E501

        :return: The external_tracker_style of this ExternalTracker.  # noqa: E501
        :rtype: str
        """
        return self._external_tracker_style

    @external_tracker_style.setter
    def external_tracker_style(self, external_tracker_style):
        """Sets the external_tracker_style of this ExternalTracker.

        External Issue Tracker Number Format, either `numeric` or `alphanumeric`  # noqa: E501

        :param external_tracker_style: The external_tracker_style of this ExternalTracker.  # noqa: E501
        :type: str
        """

        self._external_tracker_style = external_tracker_style

    @property
    def external_tracker_url(self):
        """Gets the external_tracker_url of this ExternalTracker.  # noqa: E501

        URL of external issue tracker.  # noqa: E501

        :return: The external_tracker_url of this ExternalTracker.  # noqa: E501
        :rtype: str
        """
        return self._external_tracker_url

    @external_tracker_url.setter
    def external_tracker_url(self, external_tracker_url):
        """Sets the external_tracker_url of this ExternalTracker.

        URL of external issue tracker.  # noqa: E501

        :param external_tracker_url: The external_tracker_url of this ExternalTracker.  # noqa: E501
        :type: str
        """

        self._external_tracker_url = external_tracker_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ExternalTracker, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalTracker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalTracker):
            return True

        return self.to_dict() != other.to_dict()
