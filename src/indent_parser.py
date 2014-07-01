#!/usr/bin/env python

import re


class IndentParser(object):
    def __init__(self, content, ignore_characters=[]):
        """
        >>> f=open('../resources/test_file.txt')
        >>> content=f.read()
        >>> parser=IndentParser(content)
        >>> len(parser.configs)
        4
        >>> parser.configs[0]['line']
        'indent1'
        >>> parser.configs[1]['line']
        'indent2'
        >>> parser.configs[2]['line']
        'indent3'
        >>> parser.configs[3]['line']
        'indent4'
        >>> len(parser.configs[0]['children'])
        0
        >>> len(parser.configs[1]['children'])
        0
        >>> len(parser.configs[2]['children'])
        3
        >>> len(parser.configs[3]['children'])
        2
        >>> parser.configs[2]['children'][0]['line']
        'indent31'
        >>> parser.configs[2]['children'][1]['line']
        'indent32'
        >>> parser.configs[2]['children'][2]['line']
        'indent33'
        >>> parser.configs[3]['children'][0]['line']
        'indent41'
        >>> parser.configs[3]['children'][1]['line']
        'indent42'
        >>> len(parser.configs[2]['children'][0]['children'])
        0
        >>> len(parser.configs[2]['children'][1]['children'])
        0
        >>> len(parser.configs[2]['children'][2]['children'])
        0
        >>> len(parser.configs[3]['children'][0]['children'])
        0
        >>> len(parser.configs[3]['children'][1]['children'])
        3
        >>> parser.configs[3]['children'][1]['children'][0]['line']
        'indent421'
        >>> parser.configs[3]['children'][1]['children'][1]['line']
        'indent422'
        >>> parser.configs[3]['children'][1]['children'][2]['line']
        'indent423'
        """
        self.configs = self.parse_lines(content, ignore_characters=ignore_characters)


    def parse_lines(self, content, indent_count=0, ignore_characters=[]):


        configs = []
        line_content_pattern = re.compile('^\s{%(indent_count)s}[^%(ignore_characters)s\s][\S\s]+?(?=\Z|^\s{0,%(indent_count)s}[^%(ignore_characters)s\s])' % {'indent_count': indent_count,
                                                                                                                                                               'ignore_characters': ''.join(
                                                                                                                                                                   ignore_characters)},
                                          re.M | re.DOTALL)
        line_pattern = re.compile('^\s{%(indent_count)s}(?P<line>[^\n]+)' % {'indent_count': indent_count}, re.M)
        indent_count += 1
        for grp in line_content_pattern.findall(content, re.M):
            match = line_pattern.search(grp)
            config = {'line': match.group('line'), 'children': self.parse_lines(grp, indent_count=indent_count)}
            configs.append(config)
        return configs


    def find_line(self, nested_lines, exactmatch=False, configs=None, ):
        configs = configs is not None and configs or self.configs
        if not nested_lines:
            return None
        results = []
        nested_line = nested_lines[0]
        for config in configs:
            if (exactmatch and config['line'] == nested_line) or (not exactmatch and nested_line in config['line']):
                if len(nested_lines) == 1:
                    results.append(config['line'])
                else:
                    result = self.find_line(nested_lines[1:], exactmatch=exactmatch, configs=config['children'])
                    if result:
                        results.extend(result)
            else:
                if config['children']:
                    result = self.find_line(nested_lines, exactmatch=exactmatch, configs=config['children'])
                    if result:
                        results.extend(result)
        return results

    def find_children(self, nested_lines, exactmatch=False, configs=None, ):
        configs = configs is not None and configs or self.configs
        if not nested_lines:
            return None

        nested_line = nested_lines[0]
        for config in configs:
            if (exactmatch and config['line'] == nested_line) or (not exactmatch and nested_line in config['line']):
                if len(nested_lines) == 1:
                    return config['children']
                else:
                    result = self.find_children(nested_lines[1:], exactmatch=exactmatch, configs=config['children'])
                    if result:
                        return result
            else:
                if config['children']:
                    result = self.find_children(nested_lines, exactmatch=exactmatch, configs=config['children'])
                    if result:
                        return result







