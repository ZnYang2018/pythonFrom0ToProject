import json
import os
import re
import subprocess

os.system(r'cd D:\github\ZnYang2018\hello-world')
os.chdir(r'D:\github\ZnYang2018\hello-world')
print(os.getcwd())
# cmd = 'git diff d32fc616624337552328007ab25057cc078c7bb4 1cba22a81497a7212808df7f48d6740c193a6c94'
# cmd = 'git diff f86334eb157bb7a12ea8954db680f8dc013fabdf 1cba22a81497a7212808df7f48d6740c193a6c94'
cmd = 'git diff d76d7ebe5fb93e718221627fa7885a07f530f4fd b8ed9117742ff8fde795e3e6af4b0112aeacf4ff'
cmd = 'git diff 17779a7dc4523196439a79d92ff4180b2f34c10d 23dc62b77681ffe2c5787d3de2ffd3ba80b12668'


# {"diffs": [{"path": "/OpenCoverXmlProcessor/CoverXmlProcessor.cs", "lines": [[1, 7], [10, 12], [31, 7], [97, 12]]}]}
def execute_cmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = []
    while True:
        result = process.stdout.readline()
        print(result)
        if result:
            try:
                lines.append(result.decode('gbk').strip('\r\n'))
            except UnicodeDecodeError:
                lines.append(result.decode('utf-8').strip('\r\n'))
            except Exception as e:
                print(e)
        else:
            break
    return lines


class FileDiff(object):
    def __init__(self, lines):
        self.lines = lines

    def __repr__(self):
        return f'ChangedLines:{self.get_changed_lines()}, IsSource:{self.is_source_code()}, Path:{self.get_file_path()}'

    def get_file_path(self):
        """Get the changed file's path

        :return:
        """
        first_line = self.lines[0]
        path = re.search('diff --git a(/.*) b(/.*)', first_line, re.RegexFlag.I).groups()[1]
        return path

    def is_source_code(self):
        """Get if the changed file is source code file

        :return:
        """
        path = self.get_file_path()
        is_cs = os.path.splitext(os.path.basename(path))[1].lower() in ['.cs', '.py']
        return is_cs

    def get_changed_lines(self):
        changed_lines = []
        for line in self.lines:
            if line.startswith('@@'):
                changed_line = re.search('@@ -\d+,\d+ \+(\d+,\d+) @@', line, re.RegexFlag.I).groups()[0]
                changed_lines.append(tuple([int(item) for item in changed_line.split(',')]))
        return changed_lines

    def to_json_data_obj(self):
        return {'path': self.get_file_path(), 'lines': self.get_new_changed_lines()}

    def get_new_changed_lines(self):
        new_changed_lines = []
        block_diffs = self._get_block_diffs()
        for b in block_diffs:
            new_changed_lines.extend(b.get_new_changed_lines())
        return new_changed_lines

    def _get_block_diffs(self):
        block_diff_list = []
        block_lines = []
        for line in self.lines:
            if line.startswith('@@'):
                if block_lines:
                    block_diff_list.append(BlockDiff(block_lines))
                    block_lines = []
                block_lines.append(line)
            elif block_lines:
                block_lines.append(line)
        else:
            if block_lines:
                block_diff_list.append(BlockDiff(block_lines))
        return block_diff_list


class BlockDiff(object):
    """
    The changed lines message contains the updated lines and its detail info
    """

    def __init__(self, lines):
        self.lines = lines

    def get_raw_changed_line(self):
        """Get the changed line in the raw message

        :return: tuple contains the start line and offset
        """
        line_numbers = re.search('@@ -\d+,\d+ \+(\d+,\d+) @@', self.lines[0], re.RegexFlag.I).groups()[0].split(',')
        return tuple((int(i) for i in line_numbers))

    def get_new_changed_lines(self):
        start, offset = self.get_raw_changed_line()
        message_lines = []

        for i, line in enumerate(self.lines):
            if i == 0:
                # # not end with @@ indicates that the first code line append to @@
                # message = line[line.rindex('@@') + 2:].lstrip()
                continue
            elif i != 0:
                message = line

            if not message.startswith('-'):
                message_lines.append(message)

        changed_line_numbers = []
        for i, line in enumerate(message_lines):
            if line.startswith('+'):
                changed_line_number = start + i
                changed_line_numbers.append(changed_line_number)

        changed_line_spans = []
        changed_line_span = []

        for number in changed_line_numbers:
            if len(changed_line_span) == 0:
                changed_line_span = [number, 1]
            elif len(changed_line_span) == 2:
                if number - changed_line_span[0] == changed_line_span[1]:
                    # continuous end number
                    changed_line_span[1] += 1
                else:
                    changed_line_spans.append(tuple(changed_line_span))
                    changed_line_span = [number, 1]
        else:
            if changed_line_span:
                changed_line_spans.append(tuple(changed_line_span))
        return changed_line_spans


def generate_file_diffs(lines):
    file_diffs = []
    file_lines = []
    for line in lines:
        if line.startswith('diff --git'):
            if file_lines:
                file_diffs.append(FileDiff(file_lines))
            file_lines = []
        file_lines.append(line)
    else:
        if file_lines:
            file_diffs.append(FileDiff(file_lines))
            file_lines = []
    return file_diffs


result_lines = execute_cmd(cmd)
file_diff_list = generate_file_diffs(result_lines)

data = {'diffs': [item.to_json_data_obj() for item in file_diff_list if item.is_source_code()]}
json_data = json.dumps(data)
print(json_data, file=open('data.json', 'w'))
# https://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-diff
