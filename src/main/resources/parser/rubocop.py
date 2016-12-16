import json
from parser.xunit import throw_if_some_failed, parse_last_modified, parse_junit_test_results, open_file


def rubocop_validate_files(files):
    filtered = []
    for file in files:
        if str(file).endswith("json"):
            filtered.append(file)
    throw_if_some_failed(files, filtered)


def rubocop_iterate_test_cases(file):
    """
    Iterate all test cases found in `file`.
    :param file:
    :return: a list/iterator of tuples (test case node, test hierarchy path)
    """
    with open_file(file) as data_file:
        features = json.load(data_file)
        for rubytest in features["files"]:
            yield (rubytest, (rubytest['path'], rubytest['path'], '0'))


def rubocop_duration(splitResult):
    return 0


def rubocop_result(scenario):
    offenses = scenario["offenses"]
    for offense in offenses:
        severity = offense["severity"]

        if severity in ("refactor","convention","warning"):
            continue
        elif severity in ("error", "fatal"):
            return "FAILED"
        else:
            return "OTHER"

    return "PASSED"


def rubocop_failure_reason(scenario):
    offenses = scenario["offenses"]
    for offense in offenses:
        severity = offense["severity"]

        if severity not in ("refactor","convention","warning"):
            error_message = offense["message"]
            unicode_error_message = unicode(error_message, "utf-8")
            return unicode_error_message.encode("ascii", "xmlcharrefreplace")

    return None


def rubocop_custom_properties(scenario, file):
    return {
        "path": scenario["path"]
    }


def rubocop_last_modified(file):
    return file.lastModified()


rubocop_validate_files(files)

last_modified = parse_last_modified(files, extract_last_modified=rubocop_last_modified)

print 'LAST MOD', last_modified, test_run_historian.isKnownKey(str(last_modified))
if not test_run_historian.isKnownKey(str(last_modified)):
    events = parse_junit_test_results(files, last_modified,
                                      iterate_test_cases=rubocop_iterate_test_cases,
                                      extract_duration=rubocop_duration,
                                      extract_result=rubocop_result,
                                      extract_failure_reason=rubocop_failure_reason,
                                      extract_custom_properties=rubocop_custom_properties)
    print 'built run with events', events
else:
    events = []

# Result holder should contain a list of test runs. A test run is a list of events

result_holder.result = [events] if events else []
