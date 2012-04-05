import os

import pygments.lexers
from pygments import highlight
from pygments.formatters import HtmlFormatter

from flask import Flask, request, make_response
from db import insert, find
from bson.errors import InvalidId
from settings import *

app = Flask(__name__)


HOME = """
<style> a { text-decoration: none } </style>
<pre>
sprunge(1)                          SPRUNGE                          sprunge(1)

NAME
    sprunge: command line pastebin:

SYNOPSIS
    &lt;command&gt; | curl -F '%s=&lt;-' %s

DESCRIPTION
    add <a href='http://pygments.org/docs/lexers/'>?&lt;lang&gt;</a> to resulting url for line numbers and syntax highlighting

EXAMPLES
    ~$ cat bin/ching | curl -F '%s=&lt;-' %s
       %s/VZiY
    ~$ firefox %s/VZiY?py#n-7

SEE ALSO
    http://github.com/rupa/sprunge

</pre>"""


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return HOME % (NAME, HOST, NAME, HOST, HOST, HOST)

    data = request.form.get('sprunge', None)

    if not data:
        return 'fail'

    uid = insert(data)
    return '%s/%s\n' % (HOST, uid)


@app.route('/<uid>')
def snip(uid):
    try:
        data = find(uid)
    except InvalidId:
        return '404'

    if not data:
        return '404'

    try:
        syntax = request.args.keys()[0]
    except IndexError:
        syntax = None

    if syntax:
        try:
            lexer = pygments.lexers.get_lexer_by_name(syntax)
        except:
            lexer = pygments.lexers.TextLexer()
        formatter = HtmlFormatter(full=True,
                style=STYLE, linenos='inline',
                encoding='utf-8')
        return highlight(data['content'], lexer, formatter)
    else:
        response = make_response(data['content'])
        response.headers['Content-Type'] = 'text/plain';
        return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
