import re
from datetime import datetime
from typing import Any

# This module supports various conditions for advanced searches, outlined below as global constants.
OR: str = 'OR'  # Represents the "or" condition
AND: str = 'AND'  # Represents the "and" condition

LESS_THAN: str = 'lt'  # Represents the less than ("<") value
LESS_THAN_OR_EQUAL_TO: str = 'lte'  # Represents the less than or equal to ("<=") value
GREATER_THAN: str = 'gt'  # Represents the greater than (">") value
GREATER_THAN_OR_EQUAL_TO: str = 'gte'  # Represents the greater than or equal to (">=") value
EQUAL_TO: str = 'eq'  # Represents the equal to ("=") value
NOT_EQUAL_TO: str = 'ne'  # Represents the not equal to ("!=") value
BETWEEN: str = 'between'  # Represents the between range ("< x <") value


def _match_condition(value: str, role_field: str | list, condition: str, matched: bool) -> bool:
    """
    Matches the condition based on the specified parameters.
    :param value: The value to be evaluated.
    :type value: str
    :param role_field: The value or list of values to compare against.
    :type role_field: str | list
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    if not value or not role_field:
        return False

    if isinstance(role_field, str):
        role_field = [role_field]

    found_match = any(re.search(value, field, re.IGNORECASE) for field in role_field)

    if condition == OR:
        return matched or found_match
    elif condition == AND:
        return matched and found_match if matched else found_match

    return matched


def _match_compare_condition(value: dict, role_field: Any, condition: str, matched: bool) -> bool:
    """
    Matches the condition by comparing based on the specified parameters.
    :param value: The value to be evaluated.
    :type value: dict
    :param role_field: The value to compare against.
    :type role_field: Any
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    match = True
    if isinstance(value, dict):
        for operator, compare_value in value.items():
            if isinstance(role_field, datetime) and isinstance(compare_value, str):
                compare_value = datetime.fromisoformat(compare_value).replace(tzinfo=None)

            if operator == LESS_THAN and not role_field < compare_value:
                match = False
            elif operator == LESS_THAN_OR_EQUAL_TO and not role_field <= compare_value:
                match = False
            elif operator == EQUAL_TO and not role_field == compare_value:
                match = False
            elif operator == NOT_EQUAL_TO and not role_field != compare_value:
                match = False
            elif operator == GREATER_THAN and not role_field > compare_value:
                match = False
            elif operator == GREATER_THAN_OR_EQUAL_TO and not role_field >= compare_value:
                match = False
            elif operator == BETWEEN:
                if not isinstance(compare_value, list) or len(compare_value) != 2:
                    raise ValueError('The "between" operator requires a list of two values.')
                if isinstance(role_field, datetime):
                    compare_value[0] = datetime.fromisoformat(compare_value[0]).replace(tzinfo=None)
                    compare_value[1] = datetime.fromisoformat(compare_value[1]).replace(tzinfo=None)
                if not (compare_value[0] <= role_field <= compare_value[1]):
                    match = False
    else:
        raise ValueError('Conditions should be specified as a dictionary with operators.')

    if condition == OR and match:
        return True
    elif condition == AND and not match:
        return False

    return matched


def _match_tag_condition(value, tags, condition: str, matched: bool, key_only: bool) -> bool:
    """
    Matches the condition based on the specified tags.
    :param value: The value to be evaluated.
    :type value: Any
    :param tags: The value to compare against.
    :type tags: Any
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :param key_only: Flag to indicate to match just key or both key and value.
    :type key_only: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    match = False
    if key_only:
        if value in tags:
            match = True
    else:
        match = True
        for key, val in value.items():
            if tags.get(key) != val:
                match = False
                break

    if not matched:
        return False

    if condition == "OR":
        return match
    elif condition == "AND":
        return match
    else:
        return matched
