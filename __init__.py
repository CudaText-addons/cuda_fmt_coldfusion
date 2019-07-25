import re
import json
from .coldfusionbeautifier import Beautifier, default_options
from cuda_fmt import get_config_filename

def do_format(text):

    fn = get_config_filename('ColdFusion Beautify')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    d = json.loads(s)

    opts = default_options()

    opts.tab_size = d.get('tab_size', 4)
    opts.indent_size = d.get('indent_size', 4)
    opts.indent_char = d.get('indent_char', ' ')
    opts.indent_with_tabs = d.get('indent_with_tabs', False)
    opts.expand_tags = d.get('expand_tags', False)
    opts.minimum_attribute_count = d.get('minimum_attribute_count', 2)
    opts.first_attribute_on_new_line = d.get('first_attribute_on_new_line', False)
    opts.reduce_empty_tags = d.get('reduce_empty_tags', False)
    opts.reduce_whole_word_tags = d.get('reduce_whole_word_tags', False)
    opts.exception_on_tag_mismatch = d.get('exception_on_tag_mismatch', False)
    opts.custom_singletons = d.get('custom_singletons', '')
        
    fmt = Beautifier(text, opts)
    return fmt.beautify()
