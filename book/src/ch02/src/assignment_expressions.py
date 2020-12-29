"""Clean Code in Python - Second edition
Chapter 02: Assignment expressions
"""

import re
from typing import Iterable, Set

ARN_REGEX = re.compile(r"arn:aws:[a-z0-9\-]*:[a-z0-9\-]*:(?P<account_id>\d+):.*")


def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """Given several ARNs in the form

        arn:partition:service:region:account-id:resource-id

    Collect the unique account IDs found on those strings, and return them.
    """
    collected_account_ids = set()
    for arn in arns:
        matched = re.match(ARN_REGEX, arn)
        if matched is not None:
            account_id = matched.groupdict()["account_id"]
            collected_account_ids.add(account_id)
    return collected_account_ids


def collect_account_ids_from_arns2(arns: Iterable[str]) -> Set[str]:
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}


def collect_account_ids_from_arns3(arns: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["account_id"]
        for arn in arns
        if (matched := re.match(ARN_REGEX, arn)) is not None
    }
